#!/usr/bin/env python3
"""
🚀 Test Fast_Coding 10x - ทดสอบใช้ Fast_Coding 10 ครั้งในไฟล์เดียว
================================================================

ทดสอบการใช้ Fast_Coding MCP Tool 10 ครั้งพร้อมกันและแยกกัน
"""

import asyncio
import aiohttp
import time
from datetime import datetime
from typing import List, Dict, Any

class FastCoding10xTester:
    """ระบบทดสอบ Fast_Coding 10 ครั้ง"""
    
    def __init__(self):
        self.fast_coding_url = "http://localhost:8574"
        self.test_results = []
        
        # 10 งานที่จะให้ Fast_Coding ทำ
        self.coding_tasks = [
            {
                "id": 1,
                "task": "Create a Python function to calculate fibonacci numbers",
                "ai_user": "GitHub Copilot",
                "expected": "fibonacci function"
            },
            {
                "id": 2,
                "task": "Generate a FastAPI endpoint for user registration",
                "ai_user": "Coder AI",
                "expected": "FastAPI endpoint"
            },
            {
                "id": 3,
                "task": "Write a React component for login form",
                "ai_user": "v0 AI",
                "expected": "React component"
            },
            {
                "id": 4,
                "task": "Create a database connection class in Python",
                "ai_user": "Windsurf AI",
                "expected": "database class"
            },
            {
                "id": 5,
                "task": "Generate a REST API client in JavaScript",
                "ai_user": "Bolt AI",
                "expected": "API client"
            },
            {
                "id": 6,
                "task": "Write a data validation function",
                "ai_user": "Replit AI",
                "expected": "validation function"
            },
            {
                "id": 7,
                "task": "Create a file upload handler",
                "ai_user": "Fast Coding AI",
                "expected": "upload handler"
            },
            {
                "id": 8,
                "task": "Generate a password hashing utility",
                "ai_user": "MIX IDE AI",
                "expected": "password utility"
            },
            {
                "id": 9,
                "task": "Write a JSON response formatter",
                "ai_user": "Lovable AI",
                "expected": "JSON formatter"
            },
            {
                "id": 10,
                "task": "Create an error handling middleware",
                "ai_user": "AI-IDE-Agent",
                "expected": "error middleware"
            }
        ]
    
    async def run_fast_coding_10x_test(self):
        """รันการทดสอบ Fast_Coding 10 ครั้ง"""
        
        print("🚀 Fast_Coding 10x Test - Starting...")
        print("=" * 60)
        print("Testing Fast_Coding MCP Tool with 10 different tasks")
        print()
        
        # ทดสอบแบบ Sequential (ทีละครั้ง)
        await self.test_sequential_requests()
        
        # ทดสอบแบบ Concurrent (พร้อมกัน)
        await self.test_concurrent_requests()
        
        # ทดสอบแบบ Batch (แบ่งเป็นกลุม)
        await self.test_batch_requests()
        
        # สรุปผลการทดสอบ
        self.summarize_results()
    
    async def test_sequential_requests(self):
        """ทดสอบแบบ Sequential - ทีละครั้ง"""
        
        print("🔄 Sequential Test - One by One")
        print("-" * 40)
        
        start_time = time.time()
        
        for i, task in enumerate(self.coding_tasks, 1):
            print(f"🚀 Task {i}: {task['task'][:50]}...")
            
            result = await self.call_fast_coding(task, f"sequential_{i}")
            
            if result["success"]:
                print(f"  ✅ Completed in {result['duration']:.3f}s")
            else:
                print(f"  ❌ Failed: {result['error']}")
            
            # รอสักครู่ระหว่างการเรียก
            await asyncio.sleep(0.5)
        
        end_time = time.time()
        total_duration = end_time - start_time
        
        print(f"\n📊 Sequential Results:")
        print(f"   • Total Time: {total_duration:.2f}s")
        print(f"   • Average per Task: {total_duration/10:.3f}s")
        
        successful_sequential = [r for r in self.test_results if r["test_type"] == "sequential" and r["success"]]
        print(f"   • Success Rate: {len(successful_sequential)}/10 ({len(successful_sequential)*10}%)")
    
    async def test_concurrent_requests(self):
        """ทดสอบแบบ Concurrent - พร้อมกัน 10 ครั้ง"""
        
        print(f"\n⚡ Concurrent Test - All 10 Together")
        print("-" * 40)
        
        print("🚀 Starting 10 Fast_Coding requests simultaneously...")
        
        start_time = time.time()
        
        # สร้าง tasks ทั้งหมด
        tasks = []
        for i, task in enumerate(self.coding_tasks, 1):
            tasks.append(self.call_fast_coding(task, f"concurrent_{i}"))
        
        # รันทั้งหมดพร้อมกัน
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        end_time = time.time()
        total_duration = end_time - start_time
        
        # นับผลลัพธ์
        successful_concurrent = 0
        for i, result in enumerate(results, 1):
            if isinstance(result, dict) and result.get("success"):
                successful_concurrent += 1
                print(f"  ✅ Task {i}: {result['duration']:.3f}s")
            else:
                print(f"  ❌ Task {i}: Failed")
        
        print(f"\n📊 Concurrent Results:")
        print(f"   • Total Time: {total_duration:.2f}s")
        print(f"   • Success Rate: {successful_concurrent}/10 ({successful_concurrent*10}%)")
        print(f"   • Requests/Second: {successful_concurrent/total_duration:.2f}")
    
    async def test_batch_requests(self):
        """ทดสอบแบบ Batch - แบ่งเป็น 2 กลุม ๆ ละ 5"""
        
        print(f"\n📦 Batch Test - 2 Batches of 5 Tasks")
        print("-" * 40)
        
        batch_size = 5
        batches = [
            self.coding_tasks[:batch_size],
            self.coding_tasks[batch_size:]
        ]
        
        total_start_time = time.time()
        
        for batch_num, batch_tasks in enumerate(batches, 1):
            print(f"🚀 Batch {batch_num}: Starting {len(batch_tasks)} tasks...")
            
            batch_start_time = time.time()
            
            # รัน batch พร้อมกัน
            tasks = []
            for i, task in enumerate(batch_tasks, 1):
                task_id = f"batch{batch_num}_{i}"
                tasks.append(self.call_fast_coding(task, task_id))
            
            batch_results = await asyncio.gather(*tasks, return_exceptions=True)
            
            batch_end_time = time.time()
            batch_duration = batch_end_time - batch_start_time
            
            # นับผลลัพธ์ batch
            successful_batch = 0
            for i, result in enumerate(batch_results, 1):
                if isinstance(result, dict) and result.get("success"):
                    successful_batch += 1
                    print(f"  ✅ Task {i}: {result['duration']:.3f}s")
                else:
                    print(f"  ❌ Task {i}: Failed")
            
            print(f"  📊 Batch {batch_num}: {successful_batch}/{len(batch_tasks)} in {batch_duration:.2f}s")
            
            # รอระหว่าง batch
            if batch_num < len(batches):
                await asyncio.sleep(1)
        
        total_end_time = time.time()
        total_duration = total_end_time - total_start_time
        
        successful_batch_total = [r for r in self.test_results if r["test_type"].startswith("batch") and r["success"]]
        
        print(f"\n📊 Batch Results:")
        print(f"   • Total Time: {total_duration:.2f}s")
        print(f"   • Success Rate: {len(successful_batch_total)}/10 ({len(successful_batch_total)*10}%)")
    
    async def call_fast_coding(self, task: Dict[str, Any], test_id: str) -> Dict[str, Any]:
        """เรียกใช้ Fast_Coding MCP Tool"""
        
        start_time = time.time()
        
        try:
            async with aiohttp.ClientSession() as session:
                payload = {
                    "request": task["task"],
                    "ai_user": task["ai_user"],
                    "task_id": task["id"],
                    "test_id": test_id,
                    "type": "fast_coding_10x_test"
                }
                
                async with session.post(
                    f"{self.fast_coding_url}/api/process",
                    json=payload,
                    timeout=15
                ) as response:
                    end_time = time.time()
                    duration = end_time - start_time
                    
                    if response.status == 200:
                        data = await response.json()
                        
                        result = {
                            "task_id": task["id"],
                            "test_id": test_id,
                            "test_type": test_id.split("_")[0],
                            "success": True,
                            "duration": duration,
                            "response": data.get("response", "Success"),
                            "ai_user": task["ai_user"],
                            "task": task["task"]
                        }
                        
                        self.test_results.append(result)
                        return result
                    else:
                        result = {
                            "task_id": task["id"],
                            "test_id": test_id,
                            "test_type": test_id.split("_")[0],
                            "success": False,
                            "duration": duration,
                            "error": f"HTTP {response.status}",
                            "ai_user": task["ai_user"],
                            "task": task["task"]
                        }
                        
                        self.test_results.append(result)
                        return result
        
        except asyncio.TimeoutError:
            end_time = time.time()
            duration = end_time - start_time
            
            result = {
                "task_id": task["id"],
                "test_id": test_id,
                "test_type": test_id.split("_")[0],
                "success": False,
                "duration": duration,
                "error": "Timeout",
                "ai_user": task["ai_user"],
                "task": task["task"]
            }
            
            self.test_results.append(result)
            return result
        
        except Exception as e:
            end_time = time.time()
            duration = end_time - start_time
            
            result = {
                "task_id": task["id"],
                "test_id": test_id,
                "test_type": test_id.split("_")[0],
                "success": False,
                "duration": duration,
                "error": str(e),
                "ai_user": task["ai_user"],
                "task": task["task"]
            }
            
            self.test_results.append(result)
            return result
    
    def summarize_results(self):
        """สรุปผลการทดสอบทั้งหมด"""
        
        print("\n" + "=" * 60)
        print("📊 FAST_CODING 10x TEST SUMMARY")
        print("=" * 60)
        
        # สถิติรวม
        total_requests = len(self.test_results)
        successful_requests = len([r for r in self.test_results if r["success"]])
        failed_requests = total_requests - successful_requests
        
        print(f"📈 Overall Statistics:")
        print(f"   • Total Requests: {total_requests}")
        print(f"   • Successful: {successful_requests}")
        print(f"   • Failed: {failed_requests}")
        print(f"   • Success Rate: {(successful_requests/total_requests)*100:.1f}%")
        
        # วิเคราะห์ตาม test type
        test_types = ["sequential", "concurrent", "batch1", "batch2"]
        
        print(f"\n🎯 Performance by Test Type:")
        for test_type in test_types:
            type_results = [r for r in self.test_results if r["test_type"] == test_type]
            if type_results:
                successful = len([r for r in type_results if r["success"]])
                avg_duration = sum(r["duration"] for r in type_results if r["success"]) / max(successful, 1)
                
                print(f"   • {test_type.title()}: {successful}/{len(type_results)} ({successful/len(type_results)*100:.1f}%)")
                print(f"     Avg Duration: {avg_duration:.3f}s")
        
        # วิเคราะห์เวลาตอบสนอง
        successful_durations = [r["duration"] for r in self.test_results if r["success"]]
        if successful_durations:
            avg_duration = sum(successful_durations) / len(successful_durations)
            min_duration = min(successful_durations)
            max_duration = max(successful_durations)
            
            print(f"\n⏱️ Response Time Analysis:")
            print(f"   • Average: {avg_duration:.3f}s")
            print(f"   • Fastest: {min_duration:.3f}s")
            print(f"   • Slowest: {max_duration:.3f}s")
        
        # วิเคราะห์ตาม AI User
        ai_users = {}
        for result in self.test_results:
            ai_user = result["ai_user"]
            if ai_user not in ai_users:
                ai_users[ai_user] = {"total": 0, "success": 0}
            
            ai_users[ai_user]["total"] += 1
            if result["success"]:
                ai_users[ai_user]["success"] += 1
        
        print(f"\n🤖 Performance by AI User:")
        for ai_user, stats in ai_users.items():
            success_rate = (stats["success"] / stats["total"]) * 100
            print(f"   • {ai_user}: {stats['success']}/{stats['total']} ({success_rate:.1f}%)")
        
        # รายละเอียดงานที่ทำ
        print(f"\n📋 Task Details:")
        for i, task in enumerate(self.coding_tasks, 1):
            task_results = [r for r in self.test_results if r["task_id"] == task["id"]]
            successful_task = len([r for r in task_results if r["success"]])
            
            print(f"   {i}. {task['task'][:50]}...")
            print(f"      Success: {successful_task}/{len(task_results)} times")
        
        print(f"\n🎯 Key Insights:")
        if successful_requests == total_requests:
            print("🎉 Perfect performance! Fast_Coding handled all 10x requests successfully!")
        elif successful_requests >= total_requests * 0.9:
            print("✅ Excellent performance! Fast_Coding handled most requests well!")
        elif successful_requests >= total_requests * 0.7:
            print("👍 Good performance! Fast_Coding showed decent reliability!")
        else:
            print("⚠️ Performance needs improvement!")
        
        print(f"\n🚀 Fast_Coding 10x Test Complete!")
        print("Fast_Coding MCP Tool demonstrated its capabilities across multiple scenarios!")

async def main():
    """รันการทดสอบ Fast_Coding 10x"""
    
    tester = FastCoding10xTester()
    await tester.run_fast_coding_10x_test()

if __name__ == "__main__":
    print("🚀 Fast_Coding 10x Test")
    print("Testing Fast_Coding MCP Tool with 10 different tasks")
    print("=" * 60)
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Test stopped by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
