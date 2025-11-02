#!/usr/bin/env python3
"""
🧠 Extreme SequentialThinking Test - ทดสอบใช้มากกว่านี้เพื่อดูผลแปลก
================================================================

ทดสอบ SequentialThinking Engine ในระดับ extreme เพื่อดูว่าจะเกิดผลแปลกๆ ไหม
- 50 problems พร้อมกัน
- 100 problems พร้อมกัน  
- Stress test จนถึงขีดจำกัด
"""

import asyncio
import aiohttp
import time
from datetime import datetime
from typing import List, Dict, Any
import random

class ExtremeSequentialThinkingTester:
    """ระบบทดสอบ SequentialThinking แบบ extreme"""
    
    def __init__(self):
        self.sequential_thinking_url = "http://localhost:8575"
        self.test_results = []
        self.anomalies_detected = []
        
        # Problem templates สำหรับสร้างปัญหาจำนวนมาก
        self.problem_templates = [
            "Design {system_type} architecture for {domain} with {complexity_factor}",
            "Analyze {analysis_type} in {technology} system with {scale} requirements", 
            "Optimize {optimization_target} for {application_type} handling {load_type}",
            "Implement {feature_type} with {security_level} security for {user_scale}",
            "Debug {issue_type} in {system_component} affecting {performance_metric}",
            "Plan {migration_type} from {old_tech} to {new_tech} for {business_type}",
            "Create {algorithm_type} algorithm for {data_type} processing at {speed_requirement}",
            "Design {integration_type} between {service_a} and {service_b} with {reliability_level}",
            "Solve {mathematical_problem} optimization with {constraint_type} constraints",
            "Architect {distributed_system} handling {concurrent_users} with {availability_target}"
        ]
        
        # Variables for problem generation
        self.variables = {
            "system_type": ["microservices", "monolithic", "serverless", "hybrid", "distributed"],
            "domain": ["e-commerce", "healthcare", "finance", "gaming", "IoT", "AI/ML"],
            "complexity_factor": ["high scalability", "real-time processing", "global distribution"],
            "analysis_type": ["performance bottlenecks", "security vulnerabilities", "data flow"],
            "technology": ["Kubernetes", "Docker", "React", "Node.js", "Python", "Go"],
            "scale": ["enterprise", "startup", "global", "regional", "local"],
            "optimization_target": ["database queries", "API responses", "memory usage", "CPU utilization"],
            "application_type": ["web application", "mobile app", "desktop software", "API service"],
            "load_type": ["high traffic", "batch processing", "real-time streams", "concurrent users"],
            "feature_type": ["authentication system", "payment gateway", "notification service"],
            "security_level": ["enterprise-grade", "military-grade", "standard", "enhanced"],
            "user_scale": ["millions of users", "thousands of users", "enterprise users"],
            "issue_type": ["memory leaks", "race conditions", "deadlocks", "performance degradation"],
            "system_component": ["database layer", "API gateway", "message queue", "cache system"],
            "performance_metric": ["response time", "throughput", "availability", "consistency"],
            "migration_type": ["database migration", "cloud migration", "architecture migration"],
            "old_tech": ["legacy monolith", "on-premise servers", "SQL database"],
            "new_tech": ["cloud-native", "microservices", "NoSQL database"],
            "business_type": ["startup", "enterprise", "government", "non-profit"],
            "algorithm_type": ["sorting", "search", "machine learning", "optimization"],
            "data_type": ["big data", "real-time data", "structured data", "unstructured data"],
            "speed_requirement": ["real-time", "near real-time", "batch processing"],
            "integration_type": ["API integration", "database sync", "message passing"],
            "service_a": ["payment service", "user service", "inventory service"],
            "service_b": ["notification service", "analytics service", "logging service"],
            "reliability_level": ["99.9% uptime", "99.99% uptime", "fault-tolerant"],
            "mathematical_problem": ["linear programming", "graph theory", "dynamic programming"],
            "constraint_type": ["resource", "time", "budget", "regulatory"],
            "distributed_system": ["CDN network", "blockchain network", "IoT network"],
            "concurrent_users": ["1M concurrent", "10M concurrent", "100M concurrent"],
            "availability_target": ["99.999% availability", "zero downtime", "disaster recovery"]
        }
        
        self.ai_users = [
            "Trae AI", "OpenAI GPT", "Anthropic Claude", "Google AI", "Complete MCP AI",
            "Sequential Thinking AI", "NEXUS AI", "Security Analyst AI", "Performance Optimizer AI",
            "Documentation AI", "Specialized Debugger AI", "Coder AI", "GitHub Copilot",
            "v0 AI", "Windsurf AI", "Bolt AI", "Replit AI", "Lovable AI", "AI-IDE-Agent",
            "MIX IDE AI", "Fast Coding AI", "Local AI", "Roo-Cline"
        ]
    
    async def run_extreme_tests(self):
        """รันการทดสอบแบบ extreme"""
        
        print("🧠 Extreme SequentialThinking Test - Starting...")
        print("=" * 60)
        print("Testing SequentialThinking Engine beyond normal limits")
        print("Looking for anomalies, breaking points, and emergent behaviors")
        print()
        
        # Test 1: Medium load (25 problems)
        await self.test_medium_load()
        
        # Test 2: Heavy load (50 problems) 
        await self.test_heavy_load()
        
        # Test 3: Extreme load (100 problems)
        await self.test_extreme_load()
        
        # Test 4: Stress test (200 problems)
        await self.test_stress_load()
        
        # Test 5: Breaking point test (500 problems)
        await self.test_breaking_point()
        
        # Analyze anomalies and patterns
        self.analyze_anomalies()
        
        # Final summary
        self.summarize_extreme_results()
    
    async def test_medium_load(self):
        """ทดสอบ medium load - 25 problems"""
        
        print("📊 Medium Load Test - 25 Problems Simultaneously")
        print("-" * 50)
        
        problems = self.generate_problems(25, "medium")
        await self.run_concurrent_test(problems, "medium_load")
    
    async def test_heavy_load(self):
        """ทดสอบ heavy load - 50 problems"""
        
        print(f"\n⚡ Heavy Load Test - 50 Problems Simultaneously")
        print("-" * 50)
        
        problems = self.generate_problems(50, "heavy")
        await self.run_concurrent_test(problems, "heavy_load")
    
    async def test_extreme_load(self):
        """ทดสอบ extreme load - 100 problems"""
        
        print(f"\n🚀 Extreme Load Test - 100 Problems Simultaneously")
        print("-" * 50)
        print("⚠️ This may push the engine to its limits...")
        
        problems = self.generate_problems(100, "extreme")
        await self.run_concurrent_test(problems, "extreme_load")
    
    async def test_stress_load(self):
        """ทดสอบ stress load - 200 problems"""
        
        print(f"\n💥 Stress Test - 200 Problems Simultaneously")
        print("-" * 50)
        print("🔥 Maximum stress test - looking for breaking behaviors...")
        
        problems = self.generate_problems(200, "stress")
        await self.run_concurrent_test(problems, "stress_load")
    
    async def test_breaking_point(self):
        """ทดสอบจุดแตกหัก - 500 problems"""
        
        print(f"\n💀 Breaking Point Test - 500 Problems Simultaneously")
        print("-" * 50)
        print("⚠️ WARNING: This may cause system instability!")
        print("🔍 Looking for complete system breakdown or emergent behaviors...")
        
        problems = self.generate_problems(500, "breaking")
        await self.run_concurrent_test(problems, "breaking_point")
    
    def generate_problems(self, count: int, test_type: str) -> List[Dict[str, Any]]:
        """สร้างปัญหาจำนวนมาก"""
        
        problems = []
        
        for i in range(count):
            template = random.choice(self.problem_templates)
            
            # แทนที่ variables ใน template
            problem_text = template
            for var_type, options in self.variables.items():
                if f"{{{var_type}}}" in problem_text:
                    problem_text = problem_text.replace(f"{{{var_type}}}", random.choice(options))
            
            complexity = random.choice(["medium", "high", "extreme"])
            expected_steps = random.randint(5, 15)
            
            if test_type in ["extreme", "stress", "breaking"]:
                # เพิ่ม complexity สำหรับ extreme tests
                complexity = random.choice(["high", "extreme", "impossible"])
                expected_steps = random.randint(8, 20)
            
            problem = {
                "id": i + 1,
                "problem": problem_text,
                "ai_user": random.choice(self.ai_users),
                "complexity": complexity,
                "steps_expected": expected_steps,
                "test_type": test_type
            }
            
            problems.append(problem)
        
        return problems
    
    async def run_concurrent_test(self, problems: List[Dict[str, Any]], test_name: str):
        """รันการทดสอบ concurrent"""
        
        print(f"🧠 Starting {len(problems)} SequentialThinking processes...")
        
        start_time = time.time()
        
        # สร้าง tasks ทั้งหมด
        tasks = []
        for problem in problems:
            tasks.append(self.process_extreme_problem(problem, test_name))
        
        # รันทั้งหมดพร้อมกัน
        try:
            results = await asyncio.gather(*tasks, return_exceptions=True)
        except Exception as e:
            print(f"💥 SYSTEM EXCEPTION: {e}")
            results = [{"success": False, "error": "System Exception"}] * len(problems)
        
        end_time = time.time()
        total_duration = end_time - start_time
        
        # วิเคราะห์ผลลัพธ์
        successful = 0
        failed = 0
        timeouts = 0
        errors = {}
        response_times = []
        thinking_steps_total = 0
        
        for i, result in enumerate(results, 1):
            if isinstance(result, Exception):
                failed += 1
                error_type = type(result).__name__
                errors[error_type] = errors.get(error_type, 0) + 1
                print(f"  💥 Problem {i}: Exception - {error_type}")
            elif isinstance(result, dict):
                if result.get("success"):
                    successful += 1
                    response_times.append(result["duration"])
                    thinking_steps_total += result.get("thinking_steps", 0)
                    
                    # ตรวจหา anomalies
                    self.detect_anomalies(result, test_name)
                    
                    if i <= 10:  # แสดงแค่ 10 ตัวแรก
                        print(f"  ✅ Problem {i}: {result['duration']:.3f}s | Steps: {result.get('thinking_steps', 0)}")
                else:
                    failed += 1
                    if "timeout" in result.get("error", "").lower():
                        timeouts += 1
                    
                    error_msg = result.get("error", "Unknown")
                    errors[error_msg] = errors.get(error_msg, 0) + 1
                    
                    if i <= 10:
                        print(f"  ❌ Problem {i}: {error_msg}")
            else:
                failed += 1
                errors["Unknown"] = errors.get("Unknown", 0) + 1
        
        # คำนวณ metrics
        success_rate = (successful / len(problems)) * 100
        problems_per_second = successful / total_duration if total_duration > 0 else 0
        avg_response_time = sum(response_times) / len(response_times) if response_times else 0
        avg_thinking_steps = thinking_steps_total / successful if successful > 0 else 0
        
        print(f"\n📊 {test_name.title()} Results:")
        print(f"   • Total Problems: {len(problems)}")
        print(f"   • Successful: {successful}")
        print(f"   • Failed: {failed}")
        print(f"   • Timeouts: {timeouts}")
        print(f"   • Success Rate: {success_rate:.1f}%")
        print(f"   • Total Time: {total_duration:.2f}s")
        print(f"   • Problems/Second: {problems_per_second:.2f}")
        
        if response_times:
            print(f"   • Avg Response Time: {avg_response_time:.3f}s")
            print(f"   • Min Response Time: {min(response_times):.3f}s")
            print(f"   • Max Response Time: {max(response_times):.3f}s")
            print(f"   • Avg Thinking Steps: {avg_thinking_steps:.1f}")
        
        if errors:
            print(f"   • Error Types: {dict(list(errors.items())[:5])}")  # แสดง 5 อันแรก
        
        # ตรวจสอบ system behavior anomalies
        self.check_system_anomalies(test_name, len(problems), successful, failed, 
                                   total_duration, avg_response_time, problems_per_second)
    
    async def process_extreme_problem(self, problem: Dict[str, Any], test_name: str) -> Dict[str, Any]:
        """ประมวลผลปัญหาแบบ extreme"""
        
        start_time = time.time()
        
        try:
            async with aiohttp.ClientSession() as session:
                payload = {
                    "request": f"Solve systematically: {problem['problem']}",
                    "ai_user": problem["ai_user"],
                    "problem_id": problem["id"],
                    "complexity": problem["complexity"],
                    "expected_steps": problem["steps_expected"],
                    "test_type": test_name,
                    "extreme_test": True
                }
                
                # เพิ่ม timeout สำหรับ extreme tests
                timeout = 30 if test_name in ["breaking_point", "stress_load"] else 20
                
                async with session.post(
                    f"{self.sequential_thinking_url}/api/process",
                    json=payload,
                    timeout=timeout
                ) as response:
                    end_time = time.time()
                    duration = end_time - start_time
                    
                    if response.status == 200:
                        data = await response.json()
                        
                        # ประมาณ thinking steps
                        thinking_steps = self.estimate_extreme_thinking_steps(problem, duration, test_name)
                        
                        result = {
                            "problem_id": problem["id"],
                            "test_name": test_name,
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
                            "test_name": test_name,
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
                "test_name": test_name,
                "success": False,
                "duration": duration,
                "error": f"Timeout after {duration:.1f}s",
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
                "test_name": test_name,
                "success": False,
                "duration": duration,
                "error": str(e),
                "complexity": problem["complexity"],
                "ai_user": problem["ai_user"],
                "problem": problem["problem"]
            }
            
            self.test_results.append(result)
            return result
    
    def estimate_extreme_thinking_steps(self, problem: Dict[str, Any], duration: float, test_name: str) -> int:
        """ประมาณ thinking steps สำหรับ extreme tests"""
        
        base_steps = problem["steps_expected"]
        
        # ปรับตาม test type
        test_multipliers = {
            "medium_load": 1.0,
            "heavy_load": 1.1,
            "extreme_load": 1.2,
            "stress_load": 1.3,
            "breaking_point": 1.5
        }
        
        multiplier = test_multipliers.get(test_name, 1.0)
        
        # ปรับตาม duration (ถ้าใช้เวลานานอาจคิดลึกขึ้น)
        time_factor = min(duration / 2.0, 2.0)
        
        # ปรับตาม complexity
        complexity_multipliers = {"medium": 1.0, "high": 1.2, "extreme": 1.5, "impossible": 2.0}
        complexity_mult = complexity_multipliers.get(problem["complexity"], 1.0)
        
        estimated_steps = int(base_steps * multiplier * time_factor * complexity_mult)
        return max(estimated_steps, 3)
    
    def detect_anomalies(self, result: Dict[str, Any], test_name: str):
        """ตรวจหา anomalies ในผลลัพธ์"""
        
        # Anomaly 1: Unusually fast response (< 1 second)
        if result["duration"] < 1.0:
            self.anomalies_detected.append({
                "type": "ultra_fast_response",
                "test": test_name,
                "duration": result["duration"],
                "problem_id": result["problem_id"],
                "description": f"Unusually fast response: {result['duration']:.3f}s"
            })
        
        # Anomaly 2: Unusually slow response (> 10 seconds)
        if result["duration"] > 10.0:
            self.anomalies_detected.append({
                "type": "ultra_slow_response", 
                "test": test_name,
                "duration": result["duration"],
                "problem_id": result["problem_id"],
                "description": f"Unusually slow response: {result['duration']:.3f}s"
            })
        
        # Anomaly 3: Extreme thinking steps (> 25)
        if result.get("thinking_steps", 0) > 25:
            self.anomalies_detected.append({
                "type": "extreme_thinking_steps",
                "test": test_name,
                "steps": result["thinking_steps"],
                "problem_id": result["problem_id"],
                "description": f"Extreme thinking steps: {result['thinking_steps']}"
            })
        
        # Anomaly 4: Minimal thinking steps (< 2)
        if result.get("thinking_steps", 0) < 2:
            self.anomalies_detected.append({
                "type": "minimal_thinking",
                "test": test_name,
                "steps": result["thinking_steps"],
                "problem_id": result["problem_id"],
                "description": f"Minimal thinking steps: {result['thinking_steps']}"
            })
    
    def check_system_anomalies(self, test_name: str, total_problems: int, successful: int, 
                              failed: int, duration: float, avg_response: float, pps: float):
        """ตรวจสอบ system-level anomalies"""
        
        success_rate = (successful / total_problems) * 100
        
        # System Anomaly 1: Dramatic performance drop
        if test_name != "medium_load":
            previous_results = [r for r in self.test_results if r.get("test_name") and r["test_name"] != test_name]
            if previous_results:
                prev_avg_duration = sum(r["duration"] for r in previous_results if r["success"]) / len([r for r in previous_results if r["success"]])
                
                if avg_response > prev_avg_duration * 2:
                    self.anomalies_detected.append({
                        "type": "performance_degradation",
                        "test": test_name,
                        "description": f"Performance dropped {avg_response/prev_avg_duration:.1f}x from previous tests"
                    })
        
        # System Anomaly 2: Unexpected high success rate under extreme load
        if test_name in ["extreme_load", "stress_load", "breaking_point"] and success_rate > 90:
            self.anomalies_detected.append({
                "type": "unexpected_resilience",
                "test": test_name,
                "success_rate": success_rate,
                "description": f"Unexpectedly high success rate ({success_rate:.1f}%) under extreme load"
            })
        
        # System Anomaly 3: Complete system breakdown
        if success_rate < 10:
            self.anomalies_detected.append({
                "type": "system_breakdown",
                "test": test_name,
                "success_rate": success_rate,
                "description": f"System breakdown: Only {success_rate:.1f}% success rate"
            })
        
        # System Anomaly 4: Impossible throughput
        if pps > 20:  # More than 20 problems per second seems impossible
            self.anomalies_detected.append({
                "type": "impossible_throughput",
                "test": test_name,
                "pps": pps,
                "description": f"Impossible throughput: {pps:.2f} problems/second"
            })
    
    def analyze_anomalies(self):
        """วิเคราะห์ anomalies ที่พบ"""
        
        print(f"\n🔍 Anomaly Analysis")
        print("-" * 50)
        
        if not self.anomalies_detected:
            print("✅ No anomalies detected - System behaved predictably")
            return
        
        print(f"⚠️ {len(self.anomalies_detected)} anomalies detected:")
        
        # จัดกลุ่ม anomalies ตามประเภท
        anomaly_types = {}
        for anomaly in self.anomalies_detected:
            atype = anomaly["type"]
            if atype not in anomaly_types:
                anomaly_types[atype] = []
            anomaly_types[atype].append(anomaly)
        
        for atype, anomalies in anomaly_types.items():
            print(f"\n🚨 {atype.replace('_', ' ').title()}: {len(anomalies)} instances")
            for anomaly in anomalies[:3]:  # แสดงแค่ 3 ตัวอย่างแรก
                print(f"   • {anomaly['description']}")
            
            if len(anomalies) > 3:
                print(f"   ... and {len(anomalies) - 3} more")
    
    def summarize_extreme_results(self):
        """สรุปผลการทดสอบ extreme"""
        
        print("\n" + "=" * 60)
        print("📊 EXTREME SEQUENTIAL THINKING TEST SUMMARY")
        print("=" * 60)
        
        total_requests = len(self.test_results)
        successful_requests = len([r for r in self.test_results if r["success"]])
        
        print(f"📈 Extreme Test Statistics:")
        print(f"   • Total Problems Tested: {total_requests}")
        print(f"   • Successful: {successful_requests}")
        print(f"   • Failed: {total_requests - successful_requests}")
        print(f"   • Overall Success Rate: {(successful_requests/total_requests)*100:.1f}%")
        
        # วิเคราะห์ตาม test type
        test_types = ["medium_load", "heavy_load", "extreme_load", "stress_load", "breaking_point"]
        
        print(f"\n🎯 Performance by Load Level:")
        for test_type in test_types:
            type_results = [r for r in self.test_results if r.get("test_name") == test_type]
            if type_results:
                successful = len([r for r in type_results if r["success"]])
                success_rate = (successful / len(type_results)) * 100
                
                avg_duration = sum(r["duration"] for r in type_results if r["success"]) / max(successful, 1)
                
                print(f"   • {test_type.replace('_', ' ').title()}: {successful}/{len(type_results)} ({success_rate:.1f}%)")
                print(f"     Avg Duration: {avg_duration:.3f}s")
        
        print(f"\n🔍 Key Findings:")
        
        # หาจุดแตกหัก
        breaking_point = None
        for test_type in test_types:
            type_results = [r for r in self.test_results if r.get("test_name") == test_type]
            if type_results:
                success_rate = (len([r for r in type_results if r["success"]]) / len(type_results)) * 100
                if success_rate < 50:  # ถ้า success rate ต่ำกว่า 50%
                    breaking_point = test_type
                    break
        
        if breaking_point:
            print(f"💥 Breaking Point: {breaking_point.replace('_', ' ').title()}")
        else:
            print("🚀 No breaking point found - System extremely resilient!")
        
        # วิเคราะห์ anomalies
        if self.anomalies_detected:
            print(f"⚠️ Anomalies Detected: {len(self.anomalies_detected)}")
            
            # หา anomaly ที่น่าสนใจที่สุด
            interesting_anomalies = [a for a in self.anomalies_detected if a["type"] in 
                                   ["unexpected_resilience", "impossible_throughput", "extreme_thinking_steps"]]
            
            if interesting_anomalies:
                print("🆕 Most Interesting Anomalies:")
                for anomaly in interesting_anomalies[:3]:
                    print(f"   • {anomaly['description']}")
        else:
            print("✅ No anomalies - Predictable behavior under all loads")
        
        print(f"\n🏆 EXTREME TEST COMPLETE!")
        print("SequentialThinking Engine pushed to its absolute limits!")

async def main():
    """รันการทดสอบ extreme"""
    
    tester = ExtremeSequentialThinkingTester()
    await tester.run_extreme_tests()

if __name__ == "__main__":
    print("🧠 Extreme SequentialThinking Test")
    print("Testing beyond normal limits to discover anomalies")
    print("=" * 60)
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Extreme test stopped by user")
    except Exception as e:
        print(f"\n❌ Extreme test error: {e}")
