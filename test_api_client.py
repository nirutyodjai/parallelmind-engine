#!/usr/bin/env python3
"""
🧪 API Client Test - ทดสอบ ParallelMind Engine APIs
==================================================
"""

import asyncio
import aiohttp
import json
import time

async def test_parallelmind_apis():
    """ทดสอบ ParallelMind Engine APIs ทั้งหมด"""
    print("🧪 Testing ParallelMind Engine v2.1.0 APIs")
    print("=" * 60)
    
    base_url = "http://localhost:8591"
    
    async with aiohttp.ClientSession() as session:
        
        # Test 1: Health Check
        print("\n🏥 Testing Health Check...")
        try:
            async with session.get(f"{base_url}/health") as response:
                health_data = await response.json()
                print(f"   ✅ Status: {health_data['status']}")
                print(f"   ✅ Version: {health_data.get('version', 'N/A')}")
                print(f"   ✅ Uptime: {health_data.get('uptime_seconds', 0)}s")
        except Exception as e:
            print(f"   ❌ Health check failed: {str(e)}")
        
        # Test 2: API Info
        print("\n📋 Testing API Info...")
        try:
            async with session.get(f"{base_url}/info") as response:
                info_data = await response.json()
                print(f"   ✅ Name: {info_data['name']}")
                print(f"   ✅ Version: {info_data['version']}")
                print(f"   ✅ Supported versions: {', '.join(info_data['supported_versions'])}")
                print(f"   ✅ Processing modes: {len(info_data['processing_modes'])} modes")
        except Exception as e:
            print(f"   ❌ API info failed: {str(e)}")
        
        # Test 3: Metrics
        print("\n📊 Testing Metrics...")
        try:
            async with session.get(f"{base_url}/metrics") as response:
                metrics_data = await response.json()
                print(f"   ✅ Total requests: {metrics_data['total_requests']}")
                print(f"   ✅ Memory usage: {metrics_data['memory_usage_mb']:.1f} MB")
                print(f"   ✅ CPU usage: {metrics_data['cpu_usage_percent']:.1f}%")
        except Exception as e:
            print(f"   ❌ Metrics failed: {str(e)}")
        
        # Test 4: V1 API (Legacy)
        print("\n🔄 Testing V1 API (Legacy)...")
        try:
            payload = {
                "request": "Test V1 legacy API",
                "ai_user": "API Tester"
            }
            
            start_time = time.time()
            async with session.post(f"{base_url}/api/v1/process", json=payload) as response:
                v1_data = await response.json()
                processing_time = time.time() - start_time
                
                print(f"   ✅ Status: Success")
                print(f"   ✅ Processing time: {processing_time:.3f}s")
                print(f"   ✅ Version: {v1_data.get('version', 'N/A')}")
                print(f"   ✅ Request ID: {v1_data.get('request_id', 'N/A')[:8]}...")
        except Exception as e:
            print(f"   ❌ V1 API failed: {str(e)}")
        
        # Test 5: V2 API (Enhanced) - without auth for testing
        print("\n🚀 Testing V2 API (Enhanced)...")
        try:
            payload = {
                "request": "Test V2 enhanced API with parallel reasoning",
                "ai_user": "API Tester V2",
                "mode": "parallel",
                "priority": "high"
            }
            
            # Use demo API key
            headers = {"Authorization": "Bearer pm_demo_key_2025"}
            
            start_time = time.time()
            async with session.post(f"{base_url}/api/v2/process", json=payload, headers=headers) as response:
                if response.status == 200:
                    v2_data = await response.json()
                    processing_time = time.time() - start_time
                    
                    print(f"   ✅ Status: {v2_data['status']}")
                    print(f"   ✅ Processing time: {processing_time:.3f}s")
                    print(f"   ✅ Mode: {v2_data['mode']}")
                    print(f"   ✅ Priority: {v2_data['priority']}")
                    print(f"   ✅ Request ID: {v2_data['request_id'][:8]}...")
                else:
                    error_data = await response.json()
                    print(f"   ⚠️ Status {response.status}: {error_data.get('detail', 'Unknown error')}")
        except Exception as e:
            print(f"   ❌ V2 API failed: {str(e)}")
        
        # Test 6: Batch Processing
        print("\n📦 Testing Batch Processing...")
        try:
            batch_payload = {
                "requests": [
                    {
                        "request": f"Batch test request {i}",
                        "ai_user": "Batch Tester",
                        "mode": "parallel",
                        "priority": "medium"
                    }
                    for i in range(3)
                ],
                "parallel_execution": True,
                "max_concurrent": 3
            }
            
            headers = {"Authorization": "Bearer pm_demo_key_2025"}
            
            start_time = time.time()
            async with session.post(f"{base_url}/api/v2/batch", json=batch_payload, headers=headers) as response:
                if response.status == 200:
                    batch_data = await response.json()
                    processing_time = time.time() - start_time
                    
                    print(f"   ✅ Batch ID: {batch_data['batch_id'][:8]}...")
                    print(f"   ✅ Total requests: {batch_data['total_requests']}")
                    print(f"   ✅ Successful: {batch_data['successful']}")
                    print(f"   ✅ Failed: {batch_data['failed']}")
                    print(f"   ✅ Total time: {processing_time:.3f}s")
                else:
                    error_data = await response.json()
                    print(f"   ⚠️ Status {response.status}: {error_data.get('detail', 'Unknown error')}")
        except Exception as e:
            print(f"   ❌ Batch processing failed: {str(e)}")
        
        # Test 7: Different Processing Modes
        print("\n🧠 Testing Different Processing Modes...")
        modes = ["parallel", "sequential", "hybrid", "adaptive", "chain", "ensemble"]
        
        for mode in modes:
            try:
                payload = {
                    "request": f"Test {mode} reasoning mode",
                    "ai_user": "Mode Tester",
                    "mode": mode,
                    "priority": "medium"
                }
                
                headers = {"Authorization": "Bearer pm_demo_key_2025"}
                
                start_time = time.time()
                async with session.post(f"{base_url}/api/v2/process", json=payload, headers=headers) as response:
                    if response.status == 200:
                        mode_data = await response.json()
                        processing_time = time.time() - start_time
                        print(f"   ✅ {mode.capitalize()}: {processing_time:.3f}s - {mode_data['status']}")
                    else:
                        print(f"   ⚠️ {mode.capitalize()}: Status {response.status}")
                        
                # Small delay between requests
                await asyncio.sleep(0.1)
                
            except Exception as e:
                print(f"   ❌ {mode.capitalize()}: {str(e)}")
        
        # Test 8: Final Metrics Check
        print("\n📈 Final Metrics Check...")
        try:
            async with session.get(f"{base_url}/metrics") as response:
                final_metrics = await response.json()
                print(f"   ✅ Total requests processed: {final_metrics['total_requests']}")
                print(f"   ✅ Successful requests: {final_metrics['successful_requests']}")
                print(f"   ✅ Failed requests: {final_metrics['failed_requests']}")
                
                if final_metrics['total_requests'] > 0:
                    success_rate = (final_metrics['successful_requests'] / final_metrics['total_requests']) * 100
                    print(f"   ✅ Success rate: {success_rate:.1f}%")
                    print(f"   ✅ Average response time: {final_metrics['average_response_time']:.3f}s")
        except Exception as e:
            print(f"   ❌ Final metrics failed: {str(e)}")

    print(f"\n🎉 API Testing Complete!")
    print(f"🌐 Monitoring Dashboard: http://localhost:8590")
    print(f"📖 API Documentation: http://localhost:8591/docs")

if __name__ == "__main__":
    asyncio.run(test_parallelmind_apis())
