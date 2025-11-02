#!/usr/bin/env python3
"""
⚡ Performance Optimizer - Enhanced ParallelMind Performance
===========================================================
Memory management, caching, and performance optimizations
"""

import asyncio
import aiohttp
import time
import json
import hashlib
import psutil
import gc
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
from collections import defaultdict, deque
import weakref
import threading
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class CacheEntry:
    """Cache entry with metadata"""
    data: Any
    created_at: datetime
    last_accessed: datetime
    access_count: int = 0
    size_bytes: int = 0
    ttl_seconds: int = 3600  # 1 hour default
    
    def is_expired(self) -> bool:
        """Check if cache entry is expired"""
        return datetime.now() > self.created_at + timedelta(seconds=self.ttl_seconds)
    
    def touch(self):
        """Update last accessed time and increment count"""
        self.last_accessed = datetime.now()
        self.access_count += 1

@dataclass
class PerformanceMetrics:
    """Performance tracking metrics"""
    requests_per_second: float = 0.0
    average_response_time: float = 0.0
    memory_usage_mb: float = 0.0
    cpu_usage_percent: float = 0.0
    cache_hit_rate: float = 0.0
    concurrent_requests: int = 0
    total_requests: int = 0
    error_rate: float = 0.0
    
    # Advanced metrics
    p95_response_time: float = 0.0
    p99_response_time: float = 0.0
    throughput_trend: List[float] = field(default_factory=list)
    memory_trend: List[float] = field(default_factory=list)

class SmartCache:
    """Intelligent caching system with LRU and TTL"""
    
    def __init__(self, max_size: int = 1000, default_ttl: int = 3600):
        self.max_size = max_size
        self.default_ttl = default_ttl
        self.cache: Dict[str, CacheEntry] = {}
        self.access_order = deque()
        self.lock = threading.RLock()
        self.stats = {
            "hits": 0,
            "misses": 0,
            "evictions": 0,
            "size_bytes": 0
        }
    
    def _generate_key(self, request: str, context: Dict = None) -> str:
        """Generate cache key from request and context"""
        content = f"{request}:{json.dumps(context or {}, sort_keys=True)}"
        return hashlib.sha256(content.encode()).hexdigest()[:16]
    
    def get(self, request: str, context: Dict = None) -> Optional[Any]:
        """Get cached result"""
        key = self._generate_key(request, context)
        
        with self.lock:
            if key in self.cache:
                entry = self.cache[key]
                
                # Check if expired
                if entry.is_expired():
                    self._remove_entry(key)
                    self.stats["misses"] += 1
                    return None
                
                # Update access info
                entry.touch()
                
                # Move to end of access order
                if key in self.access_order:
                    self.access_order.remove(key)
                self.access_order.append(key)
                
                self.stats["hits"] += 1
                return entry.data
            
            self.stats["misses"] += 1
            return None
    
    def put(self, request: str, data: Any, context: Dict = None, ttl: int = None) -> None:
        """Store result in cache"""
        key = self._generate_key(request, context)
        ttl = ttl or self.default_ttl
        
        # Calculate data size
        size_bytes = len(json.dumps(data).encode()) if data else 0
        
        with self.lock:
            # Remove if already exists
            if key in self.cache:
                self._remove_entry(key)
            
            # Check if we need to evict
            while len(self.cache) >= self.max_size:
                self._evict_lru()
            
            # Create new entry
            entry = CacheEntry(
                data=data,
                created_at=datetime.now(),
                last_accessed=datetime.now(),
                size_bytes=size_bytes,
                ttl_seconds=ttl
            )
            
            self.cache[key] = entry
            self.access_order.append(key)
            self.stats["size_bytes"] += size_bytes
    
    def _remove_entry(self, key: str) -> None:
        """Remove entry from cache"""
        if key in self.cache:
            entry = self.cache[key]
            self.stats["size_bytes"] -= entry.size_bytes
            del self.cache[key]
            
            if key in self.access_order:
                self.access_order.remove(key)
    
    def _evict_lru(self) -> None:
        """Evict least recently used entry"""
        if self.access_order:
            lru_key = self.access_order.popleft()
            self._remove_entry(lru_key)
            self.stats["evictions"] += 1
    
    def cleanup_expired(self) -> int:
        """Remove expired entries"""
        expired_keys = []
        
        with self.lock:
            for key, entry in self.cache.items():
                if entry.is_expired():
                    expired_keys.append(key)
            
            for key in expired_keys:
                self._remove_entry(key)
        
        return len(expired_keys)
    
    def get_stats(self) -> Dict[str, Any]:
        """Get cache statistics"""
        total_requests = self.stats["hits"] + self.stats["misses"]
        hit_rate = self.stats["hits"] / total_requests if total_requests > 0 else 0
        
        return {
            "size": len(self.cache),
            "max_size": self.max_size,
            "hit_rate": hit_rate,
            "hits": self.stats["hits"],
            "misses": self.stats["misses"],
            "evictions": self.stats["evictions"],
            "size_mb": self.stats["size_bytes"] / (1024 * 1024)
        }

class ConnectionPool:
    """Optimized connection pool for HTTP requests"""
    
    def __init__(self, max_connections: int = 100, max_connections_per_host: int = 30):
        self.connector = aiohttp.TCPConnector(
            limit=max_connections,
            limit_per_host=max_connections_per_host,
            keepalive_timeout=30,
            enable_cleanup_closed=True
        )
        self.session = None
        self.active_connections = 0
        self.max_connections = max_connections
    
    async def get_session(self) -> aiohttp.ClientSession:
        """Get or create session"""
        if self.session is None or self.session.closed:
            timeout = aiohttp.ClientTimeout(total=30, connect=10)
            self.session = aiohttp.ClientSession(
                connector=self.connector,
                timeout=timeout
            )
        return self.session
    
    async def close(self):
        """Close connection pool"""
        if self.session and not self.session.closed:
            await self.session.close()
        if self.connector:
            await self.connector.close()

class MemoryManager:
    """Memory usage monitoring and optimization"""
    
    def __init__(self):
        self.memory_threshold_mb = 1000  # 1GB threshold
        self.gc_frequency = 100  # Run GC every 100 requests
        self.request_count = 0
        self.memory_history = deque(maxlen=100)
    
    def check_memory_usage(self) -> Dict[str, float]:
        """Check current memory usage"""
        process = psutil.Process()
        memory_info = process.memory_info()
        
        usage = {
            "rss_mb": memory_info.rss / (1024 * 1024),
            "vms_mb": memory_info.vms / (1024 * 1024),
            "percent": process.memory_percent()
        }
        
        self.memory_history.append(usage["rss_mb"])
        return usage
    
    def should_run_gc(self) -> bool:
        """Determine if garbage collection should run"""
        self.request_count += 1
        
        # Run GC periodically
        if self.request_count % self.gc_frequency == 0:
            return True
        
        # Run GC if memory usage is high
        memory_usage = self.check_memory_usage()
        if memory_usage["rss_mb"] > self.memory_threshold_mb:
            return True
        
        return False
    
    def run_gc(self) -> Dict[str, Any]:
        """Run garbage collection and return stats"""
        before_memory = self.check_memory_usage()
        
        # Run garbage collection
        collected = gc.collect()
        
        after_memory = self.check_memory_usage()
        
        return {
            "objects_collected": collected,
            "memory_before_mb": before_memory["rss_mb"],
            "memory_after_mb": after_memory["rss_mb"],
            "memory_freed_mb": before_memory["rss_mb"] - after_memory["rss_mb"]
        }

class PerformanceOptimizer:
    """Main performance optimization engine"""
    
    def __init__(self):
        self.cache = SmartCache(max_size=2000, default_ttl=1800)  # 30 minutes
        self.connection_pool = ConnectionPool()
        self.memory_manager = MemoryManager()
        self.metrics = PerformanceMetrics()
        
        # Performance tracking
        self.response_times = deque(maxlen=1000)
        self.request_timestamps = deque(maxlen=1000)
        self.error_count = 0
        self.total_requests = 0
        
        # Background tasks
        self.cleanup_task = None
        self.metrics_task = None
        
    async def start_background_tasks(self):
        """Start background optimization tasks"""
        self.cleanup_task = asyncio.create_task(self._cleanup_loop())
        self.metrics_task = asyncio.create_task(self._metrics_loop())
    
    async def stop_background_tasks(self):
        """Stop background tasks"""
        if self.cleanup_task:
            self.cleanup_task.cancel()
        if self.metrics_task:
            self.metrics_task.cancel()
        await self.connection_pool.close()
    
    async def optimized_request(self, url: str, payload: Dict, use_cache: bool = True) -> Tuple[Dict, Dict]:
        """Make optimized HTTP request with caching and performance tracking"""
        start_time = time.time()
        cache_key = f"{url}:{json.dumps(payload, sort_keys=True)}"
        
        try:
            # Check cache first
            if use_cache:
                cached_result = self.cache.get(cache_key)
                if cached_result is not None:
                    processing_time = time.time() - start_time
                    return cached_result, {"cached": True, "processing_time": processing_time}
            
            # Make HTTP request
            session = await self.connection_pool.get_session()
            
            async with session.post(url, json=payload) as response:
                result = await response.json()
                
                # Cache successful results
                if use_cache and response.status == 200:
                    self.cache.put(cache_key, result)
                
                processing_time = time.time() - start_time
                
                # Update metrics
                self._update_metrics(processing_time, True)
                
                return result, {
                    "cached": False,
                    "processing_time": processing_time,
                    "status_code": response.status
                }
        
        except Exception as e:
            processing_time = time.time() - start_time
            self._update_metrics(processing_time, False)
            
            logger.error(f"Request failed: {str(e)}")
            raise
    
    async def batch_optimized_requests(self, requests: List[Tuple[str, Dict]], use_cache: bool = True) -> List[Tuple[Dict, Dict]]:
        """Process multiple requests with optimization"""
        # Check memory before batch processing
        if self.memory_manager.should_run_gc():
            gc_stats = self.memory_manager.run_gc()
            logger.info(f"GC freed {gc_stats['memory_freed_mb']:.1f}MB")
        
        # Process requests concurrently
        tasks = []
        for url, payload in requests:
            task = self.optimized_request(url, payload, use_cache)
            tasks.append(task)
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Handle exceptions
        processed_results = []
        for i, result in enumerate(results):
            if isinstance(result, Exception):
                processed_results.append((
                    {"error": str(result)},
                    {"cached": False, "processing_time": 0, "error": True}
                ))
            else:
                processed_results.append(result)
        
        return processed_results
    
    def _update_metrics(self, processing_time: float, success: bool):
        """Update performance metrics"""
        current_time = time.time()
        
        # Update counters
        self.total_requests += 1
        if not success:
            self.error_count += 1
        
        # Track response times
        self.response_times.append(processing_time)
        self.request_timestamps.append(current_time)
        
        # Calculate metrics
        self.metrics.total_requests = self.total_requests
        self.metrics.error_rate = self.error_count / self.total_requests
        self.metrics.average_response_time = sum(self.response_times) / len(self.response_times)
        
        # Calculate percentiles
        if len(self.response_times) >= 20:
            sorted_times = sorted(self.response_times)
            self.metrics.p95_response_time = sorted_times[int(len(sorted_times) * 0.95)]
            self.metrics.p99_response_time = sorted_times[int(len(sorted_times) * 0.99)]
        
        # Calculate requests per second
        recent_timestamps = [t for t in self.request_timestamps if current_time - t <= 60]  # Last minute
        self.metrics.requests_per_second = len(recent_timestamps) / 60
        
        # Update cache hit rate
        cache_stats = self.cache.get_stats()
        self.metrics.cache_hit_rate = cache_stats["hit_rate"]
        
        # Update system metrics
        memory_usage = self.memory_manager.check_memory_usage()
        self.metrics.memory_usage_mb = memory_usage["rss_mb"]
        self.metrics.cpu_usage_percent = psutil.cpu_percent()
    
    async def _cleanup_loop(self):
        """Background cleanup task"""
        while True:
            try:
                # Clean expired cache entries
                expired_count = self.cache.cleanup_expired()
                if expired_count > 0:
                    logger.info(f"Cleaned up {expired_count} expired cache entries")
                
                # Sleep for 5 minutes
                await asyncio.sleep(300)
                
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"Cleanup loop error: {str(e)}")
                await asyncio.sleep(60)
    
    async def _metrics_loop(self):
        """Background metrics collection task"""
        while True:
            try:
                # Update trends
                self.metrics.throughput_trend.append(self.metrics.requests_per_second)
                self.metrics.memory_trend.append(self.metrics.memory_usage_mb)
                
                # Keep only last 100 data points
                if len(self.metrics.throughput_trend) > 100:
                    self.metrics.throughput_trend.pop(0)
                if len(self.metrics.memory_trend) > 100:
                    self.metrics.memory_trend.pop(0)
                
                # Sleep for 30 seconds
                await asyncio.sleep(30)
                
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"Metrics loop error: {str(e)}")
                await asyncio.sleep(60)
    
    def get_performance_report(self) -> Dict[str, Any]:
        """Get comprehensive performance report"""
        cache_stats = self.cache.get_stats()
        memory_usage = self.memory_manager.check_memory_usage()
        
        return {
            "timestamp": datetime.now().isoformat(),
            "performance_metrics": {
                "requests_per_second": self.metrics.requests_per_second,
                "average_response_time": self.metrics.average_response_time,
                "p95_response_time": self.metrics.p95_response_time,
                "p99_response_time": self.metrics.p99_response_time,
                "error_rate": self.metrics.error_rate,
                "total_requests": self.metrics.total_requests
            },
            "cache_metrics": cache_stats,
            "memory_metrics": memory_usage,
            "system_metrics": {
                "cpu_usage_percent": psutil.cpu_percent(),
                "memory_available_mb": psutil.virtual_memory().available / (1024 * 1024),
                "disk_usage_percent": psutil.disk_usage('/').percent
            },
            "trends": {
                "throughput_trend": self.metrics.throughput_trend[-10:],  # Last 10 data points
                "memory_trend": self.metrics.memory_trend[-10:]
            }
        }

# Example usage and testing
async def test_performance_optimizer():
    """Test performance optimization features"""
    print("⚡ Testing Performance Optimizer")
    print("=" * 50)
    
    optimizer = PerformanceOptimizer()
    await optimizer.start_background_tasks()
    
    try:
        # Test single optimized request
        print("\n🚀 Testing single optimized request...")
        url = "http://localhost:8575/api/process"
        payload = {
            "request": "Test performance optimization",
            "ai_user": "Performance Tester",
            "type": "parallel_reasoning"
        }
        
        result, metadata = await optimizer.optimized_request(url, payload)
        print(f"   ✅ Completed in {metadata['processing_time']:.3f}s (cached: {metadata['cached']})")
        
        # Test cached request
        print("\n🔄 Testing cached request...")
        result2, metadata2 = await optimizer.optimized_request(url, payload)
        print(f"   ✅ Completed in {metadata2['processing_time']:.3f}s (cached: {metadata2['cached']})")
        
        # Test batch requests
        print("\n📦 Testing batch requests...")
        batch_requests = [
            (url, {"request": f"Batch test {i}", "ai_user": "Batch Tester", "type": "parallel_reasoning"})
            for i in range(5)
        ]
        
        batch_results = await optimizer.batch_optimized_requests(batch_requests)
        print(f"   ✅ Processed {len(batch_results)} requests")
        
        for i, (result, metadata) in enumerate(batch_results):
            if "error" not in result:
                print(f"      Request {i+1}: {metadata['processing_time']:.3f}s (cached: {metadata.get('cached', False)})")
        
        # Show performance report
        print(f"\n📊 Performance Report:")
        report = optimizer.get_performance_report()
        
        perf = report["performance_metrics"]
        print(f"   • Requests/sec: {perf['requests_per_second']:.1f}")
        print(f"   • Avg response time: {perf['average_response_time']:.3f}s")
        print(f"   • Error rate: {perf['error_rate']:.1%}")
        print(f"   • Total requests: {perf['total_requests']}")
        
        cache = report["cache_metrics"]
        print(f"   • Cache hit rate: {cache['hit_rate']:.1%}")
        print(f"   • Cache size: {cache['size']}/{cache['max_size']}")
        print(f"   • Cache memory: {cache['size_mb']:.1f}MB")
        
        memory = report["memory_metrics"]
        print(f"   • Memory usage: {memory['rss_mb']:.1f}MB ({memory['percent']:.1f}%)")
        
    finally:
        await optimizer.stop_background_tasks()

if __name__ == "__main__":
    asyncio.run(test_performance_optimizer())
