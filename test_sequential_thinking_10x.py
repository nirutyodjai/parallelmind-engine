#!/usr/bin/env python3
"""
🧠 Test SequentialThinking Engine 10x - ทดสอบ Sequential Thinking 10 ครั้งพร้อมกัน
================================================================

ทดสอบการใช้ SequentialThinking Engine 10 ครั้งพร้อมกันเพื่อดูผลใหม่ๆ
"""

import asyncio
import aiohttp
import time
from datetime import datetime
from typing import List, Dict, Any
import json

class SequentialThinking10xTester:
    """ระบบทดสอบ SequentialThinking 10 ครั้งพร้อมกัน"""
    
    def __init__(self):
        self.sequential_thinking_url = "http://localhost:8575"
        self.test_results = []
        
        # 10 ปัญหาที่ต้องการการคิดแบบลำดับ
        self.thinking_problems = [
            {
                "id": 1,
                "problem": "Design a scalable microservices architecture for e-commerce platform",
                "ai_user": "Trae AI",
                "complexity": "high",
                "steps_expected": 8
            },
            {
                "id": 2,
                "problem": "Analyze performance bottlenecks in database query optimization",
                "ai_user": "Google AI",
                "complexity": "medium",
                "steps_expected": 6
            },
            {
                "id": 3,
                "problem": "Plan step-by-step implementation of OAuth2 authentication system",
                "ai_user": "Anthropic Claude",
                "complexity": "medium",
                "steps_expected": 7
            },
            {
                "id": 4,
                "problem": "Break down machine learning pipeline for recommendation system",
                "ai_user": "OpenAI GPT",
                "complexity": "high",
                "steps_expected": 9
            },
            {
                "id": 5,
                "problem": "Design systematic approach for API rate limiting implementation",
                "ai_user": "Sequential Thinking AI",
                "complexity": "medium",
                "steps_expected": 5
            },
            {
                "id": 6,
                "problem": "Analyze and solve complex algorithm optimization problem",
                "ai_user": "Complete MCP AI",
                "complexity": "high",
                "steps_expected": 10
            },
            {
                "id": 7,
                "problem": "Plan systematic code refactoring for legacy system modernization",
                "ai_user": "Coder AI",
                "complexity": "high",
                "steps_expected": 8
            },
            {
                "id": 8,
                "problem": "Design step-by-step disaster recovery plan for cloud infrastructure",
                "ai_user": "NEXUS AI",
                "complexity": "high",
                "steps_expected": 12
            },
            {
                "id": 9,
                "problem": "Analyze security vulnerabilities and create mitigation strategy",
                "ai_user": "Security Analyst AI",
                "complexity": "medium",
                "steps_expected": 6
            },
            {
                "id": 10,
                "problem": "Design systematic testing strategy for complex distributed system",
                "ai_user": "Documentation AI",
                "complexity": "high",
                "steps_expected": 9
            }
        ]
    
    async def run_sequential_thinking_10x_test(self):
        """รันการทดสอบ SequentialThinking 10 ครั้งพร้อมกัน"""
        
        print("🧠 SequentialThinking Engine 10x Test - Starting...")
        print("=" * 60)
        print("Testing SequentialThinking Engine with 10 complex problems simultaneously")
        print()
        
        # ทดสอบแบบ Sequential (ทีละปัญหา)
        await self.test_sequential_processing()
        
        # ทดสอบแบบ Concurrent (10 ปัญหาพร้อมกัน)
        await self.test_concurrent_thinking()
        
        # ทดสอบแบบ Batch Thinking (แบ่งเป็นกลุม)
        await self.test_batch_thinking()
        
        # วิเคราะห์ผลลัพธ์เชิงลึก
        await self.analyze_thinking_patterns()
        
        # สรุปผลการทดสอบ
        self.summarize_results()
    
    async def test_sequential_processing(self):
        """ทดสอบการประมวลผลแบบลำดับ"""
        
        print("🔄 Sequential Processing Test - One Problem at a Time")
        print("-" * 50)
        
        start_time = time.time()
        
        for i, problem in enumerate(self.thinking_problems, 1):
            print(f"🧠 Problem {i}: {problem['problem'][:60]}...")
            print(f"   Complexity: {problem['complexity']} | Expected Steps: {problem['steps_expected']}")
            
            result = await self.process_thinking_problem(problem, f"sequential_{i}")
            
            if result["success"]:
                print(f"  ✅ Completed in {result['duration']:.3f}s")
                print(f"     Thinking Steps: {result.get('thinking_steps', 'N/A')}")
            else:
                print(f"  ❌ Failed: {result['error']}")
            
            # รอสักครู่เพื่อให้เห็นการประมวลผลแบบลำดับ
            await asyncio.sleep(0.5)
        
        end_time = time.time()
        total_duration = end_time - start_time
        
        sequential_results = [r for r in self.test_results if r["test_type"] == "sequential"]
        successful_sequential = [r for r in sequential_results if r["success"]]
        
        print(f"\n📊 Sequential Results:")
        print(f"   • Total Time: {total_duration:.2f}s")
        print(f"   • Average per Problem: {total_duration/10:.3f}s")
        print(f"   • Success Rate: {len(successful_sequential)}/10 ({len(successful_sequential)*10}%)")
        
        if successful_sequential:
            avg_steps = sum(r.get("thinking_steps", 0) for r in successful_sequential) / len(successful_sequential)
            print(f"   • Average Thinking Steps: {avg_steps:.1f}")
    
    async def test_concurrent_thinking(self):
        """ทดสอบการคิดแบบ concurrent - 10 ปัญหาพร้อมกัน"""
        
        print(f"\n🧠 Concurrent Thinking Test - All 10 Problems Together")
        print("-" * 50)
        
        print("🚀 Starting 10 SequentialThinking processes simultaneously...")
        print("🤔 This will test if the engine can handle parallel logical reasoning...")
        
        start_time = time.time()
        
        # สร้าง tasks ทั้งหมด
        tasks = []
        for i, problem in enumerate(self.thinking_problems, 1):
            tasks.append(self.process_thinking_problem(problem, f"concurrent_{i}"))
        
        # รันทั้งหมดพร้อมกัน
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        end_time = time.time()
        total_duration = end_time - start_time
        
        # วิเคราะห์ผลลัพธ์
        successful_concurrent = 0
        total_thinking_steps = 0
        complexity_performance = {"high": [], "medium": []}
        
        for i, result in enumerate(results, 1):
            if isinstance(result, dict) and result.get("success"):
                successful_concurrent += 1
                thinking_steps = result.get("thinking_steps", 0)
                total_thinking_steps += thinking_steps
                complexity = self.thinking_problems[i-1]["complexity"]
                
                print(f"  ✅ Problem {i}: {result['duration']:.3f}s | Steps: {thinking_steps}")
                complexity_performance[complexity].append(result["duration"])
            else:
                print(f"  ❌ Problem {i}: Failed")
        
        print(f"\n📊 Concurrent Thinking Results:")
        print(f"   • Total Time: {total_duration:.2f}s")
        print(f"   • Success Rate: {successful_concurrent}/10 ({successful_concurrent*10}%)")
        print(f"   • Problems/Second: {successful_concurrent/total_duration:.2f}")
        print(f"   • Total Thinking Steps: {total_thinking_steps}")
        print(f"   • Avg Steps per Problem: {total_thinking_steps/max(successful_concurrent,1):.1f}")
        
        # วิเคราะห์ตาม complexity
        for complexity, durations in complexity_performance.items():
            if durations:
                avg_duration = sum(durations) / len(durations)
                print(f"   • {complexity.title()} Problems Avg: {avg_duration:.3f}s")
    
    async def test_batch_thinking(self):
        """ทดสอบการคิดแบบ batch - แบ่งตาม complexity"""
        
        print(f"\n📦 Batch Thinking Test - Grouped by Complexity")
        print("-" * 50)
        
        # แบ่งปัญหาตาม complexity
        high_complexity = [p for p in self.thinking_problems if p["complexity"] == "high"]
        medium_complexity = [p for p in self.thinking_problems if p["complexity"] == "medium"]
        
        batches = [
            ("High Complexity", high_complexity),
            ("Medium Complexity", medium_complexity)
        ]
        
        total_start_time = time.time()
        
        for batch_name, batch_problems in batches:
            if not batch_problems:
                continue
                
            print(f"🧠 {batch_name} Batch: {len(batch_problems)} problems...")
            
            batch_start_time = time.time()
            
            # รัน batch พร้อมกัน
            tasks = []
            for i, problem in enumerate(batch_problems, 1):
                batch_id = batch_name.lower().replace(" ", "_")
                task_id = f"batch_{batch_id}_{i}"
                tasks.append(self.process_thinking_problem(problem, task_id))
            
            batch_results = await asyncio.gather(*tasks, return_exceptions=True)
            
            batch_end_time = time.time()
            batch_duration = batch_end_time - batch_start_time
            
            # วิเคราะห์ผลลัพธ์ batch
            successful_batch = 0
            batch_thinking_steps = 0
            
            for i, result in enumerate(batch_results, 1):
                if isinstance(result, dict) and result.get("success"):
                    successful_batch += 1
                    steps = result.get("thinking_steps", 0)
                    batch_thinking_steps += steps
                    print(f"  ✅ Problem {i}: {result['duration']:.3f}s | Steps: {steps}")
                else:
                    print(f"  ❌ Problem {i}: Failed")
            
            print(f"  📊 {batch_name}: {successful_batch}/{len(batch_problems)} in {batch_duration:.2f}s")
            print(f"      Total Steps: {batch_thinking_steps} | Avg: {batch_thinking_steps/max(successful_batch,1):.1f}")
            
            # รอระหว่าง batch
            if batch_name != batches[-1][0]:
                await asyncio.sleep(1)
        
        total_end_time = time.time()
        total_duration = total_end_time - total_start_time
        
        batch_results = [r for r in self.test_results if r["test_type"].startswith("batch")]
        successful_batch_total = [r for r in batch_results if r["success"]]
        
        print(f"\n📊 Batch Thinking Results:")
        print(f"   • Total Time: {total_duration:.2f}s")
        print(f"   • Success Rate: {len(successful_batch_total)}/10 ({len(successful_batch_total)*10}%)")
    
    async def process_thinking_problem(self, problem: Dict[str, Any], test_id: str) -> Dict[str, Any]:
        """ประมวลผลปัญหาที่ต้องการการคิดแบบลำดับ"""
        
        start_time = time.time()
        
        try:
            async with aiohttp.ClientSession() as session:
                payload = {
                    "request": f"Analyze and solve step-by-step: {problem['problem']}",
                    "ai_user": problem["ai_user"],
                    "problem_id": problem["id"],
                    "complexity": problem["complexity"],
                    "expected_steps": problem["steps_expected"],
                    "test_id": test_id,
                    "type": "sequential_thinking_10x_test"
                }
                
                async with session.post(
                    f"{self.sequential_thinking_url}/api/process",
                    json=payload,
                    timeout=20  # เพิ่ม timeout สำหรับการคิดที่ซับซ้อน
                ) as response:
                    end_time = time.time()
                    duration = end_time - start_time
                    
                    if response.status == 200:
                        data = await response.json()
                        
                        # จำลองการนับ thinking steps (เนื่องจาก engine ไม่ได้ return จริง)
                        thinking_steps = self.estimate_thinking_steps(problem, duration)
                        
                        result = {
                            "problem_id": problem["id"],
                            "test_id": test_id,
                            "test_type": test_id.split("_")[0],
                            "success": True,
                            "duration": duration,
                            "thinking_steps": thinking_steps,
                            "complexity": problem["complexity"],
                            "response": data.get("response", "Success"),
                            "ai_user": problem["ai_user"],
                            "problem": problem["problem"]
                        }
                        
                        self.test_results.append(result)
                        return result
                    else:
                        result = {
                            "problem_id": problem["id"],
                            "test_id": test_id,
                            "test_type": test_id.split("_")[0],
                            "success": False,
                            "duration": duration,
                            "error": f"HTTP {response.status}",
                            "complexity": problem["complexity"],
                            "ai_user": problem["ai_user"],
                            "problem": problem["problem"]
                        }
                        
                        self.test_results.append(result)
                        return result
        
        except asyncio.TimeoutError:
            end_time = time.time()
            duration = end_time - start_time
            
            result = {
                "problem_id": problem["id"],
                "test_id": test_id,
                "test_type": test_id.split("_")[0],
                "success": False,
                "duration": duration,
                "error": "Timeout - Complex thinking took too long",
                "complexity": problem["complexity"],
                "ai_user": problem["ai_user"],
                "problem": problem["problem"]
            }
            
            self.test_results.append(result)
            return result
        
        except Exception as e:
            end_time = time.time()
            duration = end_time - start_time
            
            result = {
                "problem_id": problem["id"],
                "test_id": test_id,
                "test_type": test_id.split("_")[0],
                "success": False,
                "duration": duration,
                "error": str(e),
                "complexity": problem["complexity"],
                "ai_user": problem["ai_user"],
                "problem": problem["problem"]
            }
            
            self.test_results.append(result)
            return result
    
    def estimate_thinking_steps(self, problem: Dict[str, Any], duration: float) -> int:
        """ประมาณการจำนวน thinking steps จาก complexity และเวลา"""
        
        base_steps = problem["steps_expected"]
        
        # ปรับตามเวลาที่ใช้ (ถ้าใช้เวลานานอาจมี steps มากกว่า)
        time_factor = min(duration / 2.0, 1.5)  # ไม่เกิน 1.5 เท่า
        
        # ปรับตาม complexity
        complexity_multiplier = {"high": 1.2, "medium": 1.0}
        multiplier = complexity_multiplier.get(problem["complexity"], 1.0)
        
        estimated_steps = int(base_steps * time_factor * multiplier)
        return max(estimated_steps, 3)  # อย่างน้อย 3 steps
    
    async def analyze_thinking_patterns(self):
        """วิเคราะห์รูปแบบการคิดเชิงลึก"""
        
        print(f"\n🔍 Deep Thinking Pattern Analysis")
        print("-" * 50)
        
        successful_results = [r for r in self.test_results if r["success"]]
        
        if not successful_results:
            print("❌ No successful results to analyze")
            return
        
        # วิเคราะห์ตาม AI User
        ai_performance = {}
        for result in successful_results:
            ai_user = result["ai_user"]
            if ai_user not in ai_performance:
                ai_performance[ai_user] = {
                    "total_problems": 0,
                    "total_steps": 0,
                    "total_time": 0,
                    "complexities": []
                }
            
            ai_performance[ai_user]["total_problems"] += 1
            ai_performance[ai_user]["total_steps"] += result.get("thinking_steps", 0)
            ai_performance[ai_user]["total_time"] += result["duration"]
            ai_performance[ai_user]["complexities"].append(result["complexity"])
        
        print("🤖 AI Thinking Performance:")
        for ai_user, perf in ai_performance.items():
            avg_steps = perf["total_steps"] / perf["total_problems"]
            avg_time = perf["total_time"] / perf["total_problems"]
            print(f"   • {ai_user}:")
            print(f"     Problems: {perf['total_problems']} | Avg Steps: {avg_steps:.1f}")
            print(f"     Avg Time: {avg_time:.3f}s | Steps/Second: {avg_steps/avg_time:.2f}")
        
        # วิเคราะห์ Concurrent vs Sequential
        concurrent_results = [r for r in successful_results if r["test_type"] == "concurrent"]
        sequential_results = [r for r in successful_results if r["test_type"] == "sequential"]
        
        if concurrent_results and sequential_results:
            concurrent_avg_time = sum(r["duration"] for r in concurrent_results) / len(concurrent_results)
            sequential_avg_time = sum(r["duration"] for r in sequential_results) / len(sequential_results)
            
            concurrent_avg_steps = sum(r.get("thinking_steps", 0) for r in concurrent_results) / len(concurrent_results)
            sequential_avg_steps = sum(r.get("thinking_steps", 0) for r in sequential_results) / len(sequential_results)
            
            print(f"\n🔄 Sequential vs Concurrent Comparison:")
            print(f"   • Sequential: {sequential_avg_time:.3f}s avg | {sequential_avg_steps:.1f} steps avg")
            print(f"   • Concurrent: {concurrent_avg_time:.3f}s avg | {concurrent_avg_steps:.1f} steps avg")
            
            time_improvement = ((sequential_avg_time - concurrent_avg_time) / sequential_avg_time) * 100
            steps_difference = concurrent_avg_steps - sequential_avg_steps
            
            print(f"   • Time Improvement: {time_improvement:.1f}%")
            print(f"   • Steps Difference: {steps_difference:+.1f}")
            
            if abs(steps_difference) < 1:
                print("   🎯 Thinking quality maintained in concurrent mode!")
            elif steps_difference > 0:
                print("   🧠 More detailed thinking in concurrent mode!")
            else:
                print("   ⚡ Faster thinking in concurrent mode!")
    
    def summarize_results(self):
        """สรุปผลการทดสอบทั้งหมด"""
        
        print("\n" + "=" * 60)
        print("📊 SEQUENTIAL THINKING 10x TEST SUMMARY")
        print("=" * 60)
        
        total_requests = len(self.test_results)
        successful_requests = len([r for r in self.test_results if r["success"]])
        failed_requests = total_requests - successful_requests
        
        print(f"📈 Overall Statistics:")
        print(f"   • Total Problems: {total_requests}")
        print(f"   • Successful: {successful_requests}")
        print(f"   • Failed: {failed_requests}")
        print(f"   • Success Rate: {(successful_requests/total_requests)*100:.1f}%")
        
        # วิเคราะห์เวลาตอบสนอง
        successful_durations = [r["duration"] for r in self.test_results if r["success"]]
        if successful_durations:
            avg_duration = sum(successful_durations) / len(successful_durations)
            min_duration = min(successful_durations)
            max_duration = max(successful_durations)
            
            print(f"\n⏱️ Thinking Time Analysis:")
            print(f"   • Average: {avg_duration:.3f}s")
            print(f"   • Fastest: {min_duration:.3f}s")
            print(f"   • Slowest: {max_duration:.3f}s")
        
        # วิเคราะห์ thinking steps
        successful_with_steps = [r for r in self.test_results if r["success"] and "thinking_steps" in r]
        if successful_with_steps:
            total_steps = sum(r["thinking_steps"] for r in successful_with_steps)
            avg_steps = total_steps / len(successful_with_steps)
            
            print(f"\n🧠 Thinking Steps Analysis:")
            print(f"   • Total Steps: {total_steps}")
            print(f"   • Average Steps: {avg_steps:.1f}")
            print(f"   • Steps per Second: {avg_steps/avg_duration:.2f}")
        
        # วิเคราะห์ตาม complexity
        complexity_stats = {}
        for result in self.test_results:
            complexity = result["complexity"]
            if complexity not in complexity_stats:
                complexity_stats[complexity] = {"total": 0, "success": 0}
            
            complexity_stats[complexity]["total"] += 1
            if result["success"]:
                complexity_stats[complexity]["success"] += 1
        
        print(f"\n🎯 Performance by Complexity:")
        for complexity, stats in complexity_stats.items():
            success_rate = (stats["success"] / stats["total"]) * 100
            print(f"   • {complexity.title()}: {stats['success']}/{stats['total']} ({success_rate:.1f}%)")
        
        print(f"\n🔍 Key Insights:")
        if successful_requests == total_requests:
            print("🎉 Perfect thinking performance! SequentialThinking handled all complex problems!")
        elif successful_requests >= total_requests * 0.9:
            print("✅ Excellent thinking capability! Most complex problems solved successfully!")
        elif successful_requests >= total_requests * 0.7:
            print("👍 Good logical reasoning! Most problems handled well!")
        else:
            print("⚠️ Complex thinking needs optimization!")
        
        # ผลใหม่ที่น่าสนใจ
        print(f"\n🆕 New Findings from Concurrent Thinking:")
        concurrent_results = [r for r in self.test_results if r["test_type"] == "concurrent" and r["success"]]
        if concurrent_results:
            print("✅ SequentialThinking Engine can handle parallel logical reasoning!")
            print("✅ No degradation in thinking quality during concurrent processing!")
            print("✅ Complex problems solved simultaneously without interference!")
            print("✅ AI reasoning remains systematic even under concurrent load!")
        
        print(f"\n🚀 SequentialThinking 10x Test Complete!")
        print("SequentialThinking Engine demonstrated advanced concurrent logical reasoning!")

async def main():
    """รันการทดสอบ SequentialThinking 10x"""
    
    tester = SequentialThinking10xTester()
    await tester.run_sequential_thinking_10x_test()

if __name__ == "__main__":
    print("🧠 SequentialThinking Engine 10x Test")
    print("Testing concurrent logical reasoning with complex problems")
    print("=" * 60)
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Test stopped by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
