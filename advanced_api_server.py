#!/usr/bin/env python3
"""
🚀 Advanced API Server - Enhanced ParallelMind Engine APIs
==========================================================
Advanced API endpoints with versioning, authentication, and enhanced features
"""

from fastapi import FastAPI, HTTPException, Depends, BackgroundTasks, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
import asyncio
import aiohttp
import time
import json
import uuid
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Union
from pydantic import BaseModel, Field
from enum import Enum
import logging
import jwt
import hashlib

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# API Models
class APIVersion(str, Enum):
    V1 = "v1"
    V2 = "v2"
    V3 = "v3"

class ProcessingMode(str, Enum):
    PARALLEL = "parallel"
    SEQUENTIAL = "sequential"
    HYBRID = "hybrid"
    ADAPTIVE = "adaptive"
    CHAIN = "chain_of_thought"
    TREE = "tree_search"
    ENSEMBLE = "ensemble"

class PriorityLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class RequestModel(BaseModel):
    request: str = Field(..., description="The reasoning request")
    ai_user: str = Field(..., description="AI user identifier")
    mode: ProcessingMode = Field(ProcessingMode.PARALLEL, description="Processing mode")
    priority: PriorityLevel = Field(PriorityLevel.MEDIUM, description="Request priority")
    context: Optional[Dict[str, Any]] = Field(None, description="Additional context")
    timeout: Optional[int] = Field(30, description="Timeout in seconds")
    stream: Optional[bool] = Field(False, description="Enable streaming response")

class BatchRequestModel(BaseModel):
    requests: List[RequestModel] = Field(..., description="List of requests to process")
    parallel_execution: bool = Field(True, description="Execute requests in parallel")
    max_concurrent: int = Field(10, description="Maximum concurrent requests")

class ResponseModel(BaseModel):
    request_id: str
    status: str
    result: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
    processing_time: float
    mode: str
    priority: str
    timestamp: str

class BatchResponseModel(BaseModel):
    batch_id: str
    total_requests: int
    successful: int
    failed: int
    total_processing_time: float
    results: List[ResponseModel]

class MetricsModel(BaseModel):
    total_requests: int
    successful_requests: int
    failed_requests: int
    average_response_time: float
    requests_per_second: float
    active_connections: int
    uptime_seconds: int
    memory_usage_mb: float
    cpu_usage_percent: float

class UserModel(BaseModel):
    username: str
    email: str
    tier: str = "free"  # free, pro, enterprise
    api_key: str
    rate_limit: int = 100  # requests per hour
    created_at: datetime

# Security
security = HTTPBearer()
SECRET_KEY = "parallelmind-engine-secret-key-2025"

class AdvancedAPIServer:
    """Advanced API server with enhanced features"""
    
    def __init__(self, port: int = 8591):
        self.port = port
        self.app = FastAPI(
            title="ParallelMind Engine API",
            description="Revolutionary Parallel Logical Reasoning System",
            version="2.0.0",
            docs_url="/docs",
            redoc_url="/redoc"
        )
        
        # Add CORS middleware
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        
        # API state
        self.active_requests = {}
        self.request_history = []
        self.metrics = {
            "total_requests": 0,
            "successful_requests": 0,
            "failed_requests": 0,
            "average_response_time": 0.0,
            "requests_per_second": 0.0,
            "active_connections": 0,
            "uptime_seconds": 0,
            "memory_usage_mb": 0.0,
            "cpu_usage_percent": 0.0
        }
        
        # User management (simplified)
        self.users = {
            "demo_user": UserModel(
                username="demo_user",
                email="demo@parallelmind.ai",
                tier="pro",
                api_key="pm_demo_key_2025",
                rate_limit=1000,
                created_at=datetime.now()
            )
        }
        
        # Rate limiting
        self.rate_limits = {}
        
        self.start_time = time.time()
        self.setup_routes()
    
    def setup_routes(self):
        """Setup API routes"""
        
        # Health and info endpoints
        self.app.get("/health")(self.health_check)
        self.app.get("/info")(self.get_info)
        self.app.get("/metrics")(self.get_metrics)
        
        # Authentication endpoints
        self.app.post("/auth/token")(self.create_token)
        self.app.get("/auth/verify")(self.verify_token)
        
        # V1 API endpoints (legacy)
        self.app.post("/api/v1/process")(self.process_v1)
        
        # V2 API endpoints (enhanced)
        self.app.post("/api/v2/process")(self.process_v2)
        self.app.post("/api/v2/batch")(self.batch_process_v2)
        self.app.get("/api/v2/status/{request_id}")(self.get_request_status)
        self.app.delete("/api/v2/cancel/{request_id}")(self.cancel_request)
        
        # V3 API endpoints (advanced)
        self.app.post("/api/v3/process")(self.process_v3)
        self.app.post("/api/v3/stream")(self.stream_process_v3)
        self.app.get("/api/v3/history")(self.get_request_history)
        self.app.get("/api/v3/analytics")(self.get_analytics)
        
        # Admin endpoints
        self.app.get("/admin/users")(self.list_users)
        self.app.post("/admin/users")(self.create_user)
        self.app.get("/admin/system")(self.get_system_status)
    
    async def authenticate_user(self, credentials: HTTPAuthorizationCredentials = Depends(security)) -> UserModel:
        """Authenticate user by API key or JWT token"""
        token = credentials.credentials
        
        # Try JWT token first
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            username = payload.get("username")
            if username and username in self.users:
                return self.users[username]
        except jwt.InvalidTokenError:
            pass
        
        # Try API key
        for user in self.users.values():
            if user.api_key == token:
                return user
        
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    
    async def check_rate_limit(self, user: UserModel) -> bool:
        """Check if user has exceeded rate limit"""
        current_time = time.time()
        user_key = user.username
        
        if user_key not in self.rate_limits:
            self.rate_limits[user_key] = []
        
        # Remove old requests (older than 1 hour)
        self.rate_limits[user_key] = [
            req_time for req_time in self.rate_limits[user_key]
            if current_time - req_time < 3600
        ]
        
        # Check if under limit
        if len(self.rate_limits[user_key]) >= user.rate_limit:
            return False
        
        # Add current request
        self.rate_limits[user_key].append(current_time)
        return True
    
    # Health and Info Endpoints
    async def health_check(self):
        """Health check endpoint"""
        return {
            "status": "healthy",
            "timestamp": datetime.now().isoformat(),
            "version": "2.0.0",
            "uptime_seconds": int(time.time() - self.start_time)
        }
    
    async def get_info(self):
        """Get API information"""
        return {
            "name": "ParallelMind Engine API",
            "version": "2.0.0",
            "description": "Revolutionary Parallel Logical Reasoning System",
            "features": [
                "Parallel logical reasoning",
                "Multiple processing modes",
                "Real-time streaming",
                "Batch processing",
                "Advanced analytics"
            ],
            "supported_versions": ["v1", "v2", "v3"],
            "processing_modes": [mode.value for mode in ProcessingMode],
            "priority_levels": [level.value for level in PriorityLevel]
        }
    
    async def get_metrics(self) -> MetricsModel:
        """Get current metrics"""
        import psutil
        
        # Update system metrics
        self.metrics["uptime_seconds"] = int(time.time() - self.start_time)
        self.metrics["memory_usage_mb"] = psutil.virtual_memory().used / (1024 * 1024)
        self.metrics["cpu_usage_percent"] = psutil.cpu_percent()
        self.metrics["active_connections"] = len(self.active_requests)
        
        return MetricsModel(**self.metrics)
    
    # Authentication Endpoints
    async def create_token(self, username: str, password: str):
        """Create JWT token"""
        # Simplified authentication (in production, verify password hash)
        if username in self.users:
            user = self.users[username]
            payload = {
                "username": username,
                "tier": user.tier,
                "exp": datetime.utcnow() + timedelta(hours=24)
            }
            token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
            return {"access_token": token, "token_type": "bearer"}
        
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    async def verify_token(self, user: UserModel = Depends(authenticate_user)):
        """Verify token and return user info"""
        return {
            "username": user.username,
            "tier": user.tier,
            "rate_limit": user.rate_limit,
            "valid": True
        }
    
    # V1 API (Legacy)
    async def process_v1(self, request: dict):
        """Legacy V1 processing endpoint"""
        start_time = time.time()
        request_id = str(uuid.uuid4())
        
        try:
            # Simple processing (legacy format)
            result = {
                "system": "ParallelMind Engine",
                "response": f"V1 Legacy response for: {request.get('request', '')}",
                "ai_user": request.get("ai_user", "unknown"),
                "timestamp": datetime.now().isoformat()
            }
            
            processing_time = time.time() - start_time
            self._update_metrics(processing_time, True)
            
            return {
                "request_id": request_id,
                "result": result,
                "processing_time": processing_time,
                "version": "v1"
            }
            
        except Exception as e:
            processing_time = time.time() - start_time
            self._update_metrics(processing_time, False)
            raise HTTPException(status_code=500, detail=str(e))
    
    # V2 API (Enhanced)
    async def process_v2(self, request: RequestModel, user: UserModel = Depends(authenticate_user)):
        """Enhanced V2 processing endpoint"""
        
        # Check rate limit
        if not await self.check_rate_limit(user):
            raise HTTPException(status_code=429, detail="Rate limit exceeded")
        
        start_time = time.time()
        request_id = str(uuid.uuid4())
        
        # Store active request
        self.active_requests[request_id] = {
            "request": request,
            "user": user.username,
            "start_time": start_time,
            "status": "processing"
        }
        
        try:
            # Enhanced processing with mode support
            result = await self._process_with_mode(request, request_id)
            
            processing_time = time.time() - start_time
            self._update_metrics(processing_time, True)
            
            # Remove from active requests
            del self.active_requests[request_id]
            
            response = ResponseModel(
                request_id=request_id,
                status="success",
                result=result,
                processing_time=processing_time,
                mode=request.mode.value,
                priority=request.priority.value,
                timestamp=datetime.now().isoformat()
            )
            
            # Add to history
            self.request_history.append(response)
            
            return response
            
        except Exception as e:
            processing_time = time.time() - start_time
            self._update_metrics(processing_time, False)
            
            # Remove from active requests
            if request_id in self.active_requests:
                del self.active_requests[request_id]
            
            response = ResponseModel(
                request_id=request_id,
                status="error",
                error=str(e),
                processing_time=processing_time,
                mode=request.mode.value,
                priority=request.priority.value,
                timestamp=datetime.now().isoformat()
            )
            
            return response
    
    async def batch_process_v2(self, batch: BatchRequestModel, user: UserModel = Depends(authenticate_user)):
        """Batch processing endpoint"""
        
        # Check rate limit (count as number of requests)
        for _ in range(len(batch.requests)):
            if not await self.check_rate_limit(user):
                raise HTTPException(status_code=429, detail="Rate limit exceeded")
        
        batch_id = str(uuid.uuid4())
        start_time = time.time()
        
        try:
            if batch.parallel_execution:
                # Process in parallel with concurrency limit
                semaphore = asyncio.Semaphore(batch.max_concurrent)
                
                async def process_single(req):
                    async with semaphore:
                        return await self.process_v2(req, user)
                
                results = await asyncio.gather(
                    *[process_single(req) for req in batch.requests],
                    return_exceptions=True
                )
            else:
                # Process sequentially
                results = []
                for req in batch.requests:
                    result = await self.process_v2(req, user)
                    results.append(result)
            
            # Count successful and failed
            successful = sum(1 for r in results if not isinstance(r, Exception) and r.status == "success")
            failed = len(results) - successful
            
            total_time = time.time() - start_time
            
            return BatchResponseModel(
                batch_id=batch_id,
                total_requests=len(batch.requests),
                successful=successful,
                failed=failed,
                total_processing_time=total_time,
                results=[r for r in results if not isinstance(r, Exception)]
            )
            
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    async def get_request_status(self, request_id: str, user: UserModel = Depends(authenticate_user)):
        """Get status of a specific request"""
        if request_id in self.active_requests:
            req_info = self.active_requests[request_id]
            return {
                "request_id": request_id,
                "status": req_info["status"],
                "elapsed_time": time.time() - req_info["start_time"],
                "user": req_info["user"]
            }
        
        # Check history
        for response in self.request_history:
            if response.request_id == request_id:
                return response
        
        raise HTTPException(status_code=404, detail="Request not found")
    
    async def cancel_request(self, request_id: str, user: UserModel = Depends(authenticate_user)):
        """Cancel an active request"""
        if request_id in self.active_requests:
            del self.active_requests[request_id]
            return {"message": f"Request {request_id} cancelled"}
        
        raise HTTPException(status_code=404, detail="Request not found or already completed")
    
    # V3 API (Advanced)
    async def process_v3(self, request: RequestModel, background_tasks: BackgroundTasks, user: UserModel = Depends(authenticate_user)):
        """Advanced V3 processing with background tasks"""
        
        if not await self.check_rate_limit(user):
            raise HTTPException(status_code=429, detail="Rate limit exceeded")
        
        # Add background task for cleanup
        background_tasks.add_task(self._cleanup_old_requests)
        
        return await self.process_v2(request, user)
    
    async def stream_process_v3(self, request: RequestModel, user: UserModel = Depends(authenticate_user)):
        """Streaming processing endpoint"""
        
        if not await self.check_rate_limit(user):
            raise HTTPException(status_code=429, detail="Rate limit exceeded")
        
        async def generate_stream():
            request_id = str(uuid.uuid4())
            
            # Send initial response
            yield f"data: {json.dumps({'type': 'start', 'request_id': request_id})}\n\n"
            
            # Simulate processing steps
            steps = [
                "Initializing parallel reasoning...",
                "Analyzing request context...",
                "Executing reasoning algorithms...",
                "Synthesizing results...",
                "Finalizing response..."
            ]
            
            for i, step in enumerate(steps):
                await asyncio.sleep(0.5)  # Simulate processing time
                yield f"data: {json.dumps({'type': 'progress', 'step': i+1, 'total': len(steps), 'message': step})}\n\n"
            
            # Send final result
            result = await self._process_with_mode(request, request_id)
            yield f"data: {json.dumps({'type': 'complete', 'result': result})}\n\n"
        
        return StreamingResponse(generate_stream(), media_type="text/plain")
    
    async def get_request_history(self, limit: int = 100, user: UserModel = Depends(authenticate_user)):
        """Get request history"""
        return {
            "total": len(self.request_history),
            "limit": limit,
            "requests": self.request_history[-limit:]
        }
    
    async def get_analytics(self, user: UserModel = Depends(authenticate_user)):
        """Get advanced analytics"""
        if user.tier not in ["pro", "enterprise"]:
            raise HTTPException(status_code=403, detail="Analytics requires Pro or Enterprise tier")
        
        # Calculate analytics
        total_requests = len(self.request_history)
        if total_requests == 0:
            return {"message": "No data available"}
        
        # Mode distribution
        mode_counts = {}
        response_times = []
        
        for response in self.request_history:
            mode_counts[response.mode] = mode_counts.get(response.mode, 0) + 1
            response_times.append(response.processing_time)
        
        # Calculate percentiles
        response_times.sort()
        p50 = response_times[int(len(response_times) * 0.5)] if response_times else 0
        p95 = response_times[int(len(response_times) * 0.95)] if response_times else 0
        p99 = response_times[int(len(response_times) * 0.99)] if response_times else 0
        
        return {
            "total_requests": total_requests,
            "mode_distribution": mode_counts,
            "response_time_percentiles": {
                "p50": p50,
                "p95": p95,
                "p99": p99
            },
            "average_response_time": sum(response_times) / len(response_times),
            "success_rate": sum(1 for r in self.request_history if r.status == "success") / total_requests
        }
    
    # Admin Endpoints
    async def list_users(self, user: UserModel = Depends(authenticate_user)):
        """List all users (admin only)"""
        if user.tier != "enterprise":
            raise HTTPException(status_code=403, detail="Admin access required")
        
        return {"users": list(self.users.keys())}
    
    async def create_user(self, new_user: UserModel, user: UserModel = Depends(authenticate_user)):
        """Create new user (admin only)"""
        if user.tier != "enterprise":
            raise HTTPException(status_code=403, detail="Admin access required")
        
        if new_user.username in self.users:
            raise HTTPException(status_code=400, detail="User already exists")
        
        self.users[new_user.username] = new_user
        return {"message": f"User {new_user.username} created successfully"}
    
    async def get_system_status(self, user: UserModel = Depends(authenticate_user)):
        """Get system status (admin only)"""
        if user.tier != "enterprise":
            raise HTTPException(status_code=403, detail="Admin access required")
        
        import psutil
        
        return {
            "system": {
                "cpu_count": psutil.cpu_count(),
                "memory_total_gb": psutil.virtual_memory().total / (1024**3),
                "disk_usage_percent": psutil.disk_usage('/').percent
            },
            "api": {
                "active_requests": len(self.active_requests),
                "total_users": len(self.users),
                "uptime_seconds": int(time.time() - self.start_time)
            }
        }
    
    # Helper Methods
    async def _process_with_mode(self, request: RequestModel, request_id: str) -> Dict[str, Any]:
        """Process request with specified mode"""
        
        # Simulate different processing modes
        mode_responses = {
            ProcessingMode.PARALLEL: f"Parallel reasoning result for: {request.request}",
            ProcessingMode.SEQUENTIAL: f"Sequential reasoning result for: {request.request}",
            ProcessingMode.HYBRID: f"Hybrid reasoning result for: {request.request}",
            ProcessingMode.ADAPTIVE: f"Adaptive reasoning result for: {request.request}",
            ProcessingMode.CHAIN: f"Chain-of-thought result for: {request.request}",
            ProcessingMode.TREE: f"Tree search result for: {request.request}",
            ProcessingMode.ENSEMBLE: f"Ensemble reasoning result for: {request.request}"
        }
        
        # Simulate processing time based on mode
        mode_delays = {
            ProcessingMode.PARALLEL: 0.5,
            ProcessingMode.SEQUENTIAL: 1.0,
            ProcessingMode.HYBRID: 0.8,
            ProcessingMode.ADAPTIVE: 0.6,
            ProcessingMode.CHAIN: 1.2,
            ProcessingMode.TREE: 1.5,
            ProcessingMode.ENSEMBLE: 2.0
        }
        
        await asyncio.sleep(mode_delays.get(request.mode, 1.0))
        
        return {
            "system": "ParallelMind Engine v2.0",
            "response": mode_responses.get(request.mode, "Default response"),
            "mode": request.mode.value,
            "priority": request.priority.value,
            "ai_user": request.ai_user,
            "context": request.context,
            "timestamp": datetime.now().isoformat(),
            "request_id": request_id
        }
    
    def _update_metrics(self, processing_time: float, success: bool):
        """Update API metrics"""
        self.metrics["total_requests"] += 1
        
        if success:
            self.metrics["successful_requests"] += 1
        else:
            self.metrics["failed_requests"] += 1
        
        # Update average response time
        current_avg = self.metrics["average_response_time"]
        total_requests = self.metrics["total_requests"]
        self.metrics["average_response_time"] = (
            (current_avg * (total_requests - 1) + processing_time) / total_requests
        )
        
        # Calculate requests per second (last minute)
        current_time = time.time()
        recent_requests = [
            r for r in self.request_history 
            if current_time - time.mktime(datetime.fromisoformat(r.timestamp.replace('Z', '+00:00')).timetuple()) < 60
        ]
        self.metrics["requests_per_second"] = len(recent_requests) / 60
    
    async def _cleanup_old_requests(self):
        """Background task to cleanup old request history"""
        # Keep only last 1000 requests
        if len(self.request_history) > 1000:
            self.request_history = self.request_history[-1000:]
    
    async def start_server(self):
        """Start the API server"""
        import uvicorn
        
        config = uvicorn.Config(
            app=self.app,
            host="0.0.0.0",
            port=self.port,
            log_level="info"
        )
        
        server = uvicorn.Server(config)
        logger.info(f"🚀 Advanced API Server starting on http://localhost:{self.port}")
        logger.info(f"📖 API Documentation: http://localhost:{self.port}/docs")
        
        await server.serve()

# Example usage
async def main():
    """Main function to run the advanced API server"""
    api_server = AdvancedAPIServer(port=8591)
    await api_server.start_server()

if __name__ == "__main__":
    asyncio.run(main())
