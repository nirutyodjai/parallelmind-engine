#!/usr/bin/env python3
"""
⚡ Concurrent MCP Tools Test - ทดสอบใช้ MCP Tools หลายตัวพร้อมกัน
================================================================

ทดสอบการใช้ Fast_Coding และ Sequential_Thinking หลายตัวพร้อมกันในไฟล์เดียว
พร้อมจับเวลาประสิทธิภาพ
"""

import asyncio
import aiohttp
import time
import json
from datetime import datetime
from typing import Dict, List, Any
import concurrent.futures
from dataclasses import dataclass

@dataclass
class MCPRequest:
    """คลาสสำหรับเก็บข้อมูล MCP request"""
    ai_name: str
    tool_name: str
    task: str
    request_id: str
    start_time: float = 0
    end_time: float = 0
    success: bool = False
    response: str = ""

class ConcurrentMCPTester:
    """ระบบทดสอบ MCP Tools แบบ concurrent"""
    
    def __init__(self):
        self.mcp_tools = {
            "Fast_Coding": "http://localhost:8574",
            "Sequential_Thinking": "http://localhost:8575",
            "Neuroflow_Logs": "http://localhost:8573"
        }
        
        # AI teams สำหรับการทดสอบ
        self.ai_teams = {
            "Fast_Coding_Team": [
                "GitHub Copilot", "Coder AI", "v0 AI", "Windsurf AI", 
                "Bolt AI", "Replit AI", "Fast Coding AI", "MIX IDE AI"
            ],
            "Sequential_Thinking_Team": [
                "Trae AI", "OpenAI GPT", "Anthropic Claude", "NEXUS AI",
                "Sequential Thinking AI", "Complete MCP AI", "Documentation AI", "Security Analyst AI"
            ],
            "Neuroflow_Logs_Team": [
                "Google AI", "Local AI", "Performance Optimizer AI", "Specialized Debugger AI"
            ]
        }
        
        self.test_results = []
        self.performance_metrics = {}
    
    async def run_concurrent_tests(self):
        """รันการทดสอบแบบ concurrent"""
        
        print("⚡ Concurrent MCP Tools Test - Starting...")
        print("=" * 60)
        print("Testing multiple MCP Tools simultaneously with timing")
        print()
        
        # Test scenarios
        test_scenarios = [
            {
                "name": "Small Concurrent Load",
                "description": "3 tools, 2 requests each",
                "fast_coding_requests": 2,
                "sequential_thinking_requests": 2,
                "neuroflow_logs_requests": 2
            },
            {
                "name": "Medium Concurrent Load", 
                "description": "3 tools, 4 requests each",
                "fast_coding_requests": 4,
                "sequential_thinking_requests": 4,
                "neuroflow_logs_requests": 4
            },
            {
                "name": "Heavy Concurrent Load",
                "description": "3 tools, 8 requests each",
                "fast_coding_requests": 8,
                "sequential_thinking_requests": 8,
                "neuroflow_logs_requests": 8
            },
            {
                "name": "Extreme Concurrent Load",
                "description": "3 tools, 12 requests each",
                "fast_coding_requests": 12,
                "sequential_thinking_requests": 12,
                "neuroflow_logs_requests": 12
            }
        ]
        
        # รันแต่ละ scenario
        for i, scenario in enumerate(test_scenarios, 1):
            print(f"🎯 Scenario {i}: {scenario['name']}")
            print(f"Description: {scenario['description']}")
            print("-" * 50)
            
            # รันการทดสอบ concurrent
            scenario_results = await self.run_scenario(scenario)
            
            # วิเคราะห์ผลลัพธ์
            self.analyze_scenario_results(scenario, scenario_results)
            
            print("-" * 50)
            print()
            
            # รอสักครู่ระหว่าง scenario
            await asyncio.sleep(2)
        
        # สรุปผลการทดสอบทั้งหมด
        self.summarize_all_tests()
    
    async def run_scenario(self, scenario: Dict[str, Any]) -> List[MCPRequest]:
        """รันการทดสอบ scenario เดียว"""
        
        print(f"⚡ Starting concurrent requests...")
        
        # สร้าง requests ทั้งหมด
        all_requests = []
        
        # Fast_Coding requests
        for i in range(scenario["fast_coding_requests"]):
            ai_name = self.ai_teams["Fast_Coding_Team"][i % len(self.ai_teams["Fast_Coding_Team"])]
            request = MCPRequest(
                ai_name=ai_name,
                tool_name="Fast_Coding",
                task=f"Generate code for feature {i+1} - {scenario['name']}",
                request_id=f"fc_{i+1}_{int(time.time())}"
            )
            all_requests.append(request)
        
        # Sequential_Thinking requests
        for i in range(scenario["sequential_thinking_requests"]):
            ai_name = self.ai_teams["Sequential_Thinking_Team"][i % len(self.ai_teams["Sequential_Thinking_Team"])]
            request = MCPRequest(
                ai_name=ai_name,
                tool_name="Sequential_Thinking",
                task=f"Analyze problem {i+1} step by step - {scenario['name']}",
                request_id=f"st_{i+1}_{int(time.time())}"
            )
            all_requests.append(request)
        
        # Neuroflow_Logs requests
        for i in range(scenario["neuroflow_logs_requests"]):
            ai_name = self.ai_teams["Neuroflow_Logs_Team"][i % len(self.ai_teams["Neuroflow_Logs_Team"])]
            request = MCPRequest(
                ai_name=ai_name,
                tool_name="Neuroflow_Logs",
                task=f"Monitor system {i+1} - {scenario['name']}",
                request_id=f"nl_{i+1}_{int(time.time())}"
            )
            all_requests.append(request)
        
        print(f"📊 Total requests: {len(all_requests)}")
        print(f"   • Fast_Coding: {scenario['fast_coding_requests']}")
        print(f"   • Sequential_Thinking: {scenario['sequential_thinking_requests']}")
        print(f"   • Neuroflow_Logs: {scenario['neuroflow_logs_requests']}")
        
        # เริ่มจับเวลา
        scenario_start_time = time.time()
        
        # รัน requests ทั้งหมดพร้อมกัน
        tasks = [self.execute_mcp_request(request) for request in all_requests]
        completed_requests = await asyncio.gather(*tasks, return_exceptions=True)
        
        # จบการจับเวลา
        scenario_end_time = time.time()
        scenario_duration = scenario_end_time - scenario_start_time
        
        print(f"⏱️ Scenario completed in: {scenario_duration:.2f} seconds")
        
        # ประมวลผลลัพธ์
        successful_requests = []
        for result in completed_requests:
            if isinstance(result, MCPRequest):
                successful_requests.append(result)
                self.test_results.append(result)
        
        # เก็บ metrics
        self.performance_metrics[scenario["name"]] = {
            "total_requests": len(all_requests),
            "successful_requests": len(successful_requests),
            "failed_requests": len(all_requests) - len(successful_requests),
            "duration": scenario_duration,
            "requests_per_second": len(successful_requests) / scenario_duration if scenario_duration > 0 else 0,
            "success_rate": (len(successful_requests) / len(all_requests)) * 100 if all_requests else 0
        }
        
        return successful_requests
    
    async def execute_mcp_request(self, request: MCPRequest) -> MCPRequest:
        """ดำเนินการ MCP request เดียว"""
        
        request.start_time = time.time()
        
        try:
            tool_url = self.mcp_tools[request.tool_name]
            
            async with aiohttp.ClientSession() as session:
                payload = {
                    "request": request.task,
                    "ai_user": request.ai_name,
                    "request_id": request.request_id,
                    "type": "concurrent_test"
                }
                
                async with session.post(
                    f"{tool_url}/api/process",
                    json=payload,
                    timeout=15  # เพิ่ม timeout สำหรับ concurrent requests
                ) as response:
                    request.end_time = time.time()
                    
                    if response.status == 200:
                        data = await response.json()
                        request.success = True
                        request.response = data.get('response', 'Success')
                    else:
                        request.success = False
                        request.response = f"HTTP {response.status}"
        
        except asyncio.TimeoutError:
            request.end_time = time.time()
            request.success = False
            request.response = "Timeout"
        except Exception as e:
            request.end_time = time.time()
            request.success = False
            request.response = str(e)
        
        return request
    
    def analyze_scenario_results(self, scenario: Dict[str, Any], results: List[MCPRequest]):
        """วิเคราะห์ผลลัพธ์ของ scenario"""
        
        metrics = self.performance_metrics[scenario["name"]]
        
        print(f"📈 Scenario Results:")
        print(f"   • Total Requests: {metrics['total_requests']}")
        print(f"   • Successful: {metrics['successful_requests']}")
        print(f"   • Failed: {metrics['failed_requests']}")
        print(f"   • Success Rate: {metrics['success_rate']:.1f}%")
        print(f"   • Duration: {metrics['duration']:.2f} seconds")
        print(f"   • Requests/Second: {metrics['requests_per_second']:.2f}")
        
        # วิเคราะห์ตาม tool
        tool_stats = {}
        for result in results:
            tool = result.tool_name
            if tool not in tool_stats:
                tool_stats[tool] = {"total": 0, "success": 0, "avg_time": 0, "times": []}
            
            tool_stats[tool]["total"] += 1
            if result.success:
                tool_stats[tool]["success"] += 1
            
            duration = result.end_time - result.start_time
            tool_stats[tool]["times"].append(duration)
        
        # คำนวณเวลาเฉลี่ย
        for tool, stats in tool_stats.items():
            if stats["times"]:
                stats["avg_time"] = sum(stats["times"]) / len(stats["times"])
                stats["min_time"] = min(stats["times"])
                stats["max_time"] = max(stats["times"])
        
        print(f"\n🔧 Tool Performance:")
        for tool, stats in tool_stats.items():
            success_rate = (stats["success"] / stats["total"]) * 100 if stats["total"] > 0 else 0
            print(f"   • {tool}:")
            print(f"     Success: {stats['success']}/{stats['total']} ({success_rate:.1f}%)")
            print(f"     Avg Time: {stats['avg_time']:.3f}s")
            print(f"     Min Time: {stats['min_time']:.3f}s")
            print(f"     Max Time: {stats['max_time']:.3f}s")
    
    def summarize_all_tests(self):
        """สรุปผลการทดสอบทั้งหมด"""
        
        print("=" * 60)
        print("📊 CONCURRENT MCP TOOLS TEST SUMMARY")
        print("=" * 60)
        
        total_requests = sum(len([r for r in self.test_results if r.success]) for _ in [1])
        total_successful = len([r for r in self.test_results if r.success])
        total_failed = len(self.test_results) - total_successful
        overall_success_rate = (total_successful / len(self.test_results)) * 100 if self.test_results else 0
        
        print(f"📈 Overall Statistics:")
        print(f"   • Total Requests: {len(self.test_results)}")
        print(f"   • Successful: {total_successful}")
        print(f"   • Failed: {total_failed}")
        print(f"   • Overall Success Rate: {overall_success_rate:.1f}%")
        
        print(f"\n🎯 Scenario Performance Comparison:")
        for scenario_name, metrics in self.performance_metrics.items():
            status = "🟢" if metrics["success_rate"] == 100 else "🟡" if metrics["success_rate"] >= 80 else "🔴"
            print(f"   {status} {scenario_name}:")
            print(f"      Requests: {metrics['successful_requests']}/{metrics['total_requests']}")
            print(f"      Success Rate: {metrics['success_rate']:.1f}%")
            print(f"      Duration: {metrics['duration']:.2f}s")
            print(f"      RPS: {metrics['requests_per_second']:.2f}")
        
        print(f"\n⚡ Performance Analysis:")
        
        # วิเคราะห์ประสิทธิภาพรวม
        all_durations = [r.end_time - r.start_time for r in self.test_results if r.success]
        if all_durations:
            avg_request_time = sum(all_durations) / len(all_durations)
            min_request_time = min(all_durations)
            max_request_time = max(all_durations)
            
            print(f"   • Average Request Time: {avg_request_time:.3f}s")
            print(f"   • Fastest Request: {min_request_time:.3f}s")
            print(f"   • Slowest Request: {max_request_time:.3f}s")
        
        # วิเคราะห์ตาม tool
        tool_performance = {}
        for result in self.test_results:
            tool = result.tool_name
            if tool not in tool_performance:
                tool_performance[tool] = {"requests": 0, "successes": 0, "times": []}
            
            tool_performance[tool]["requests"] += 1
            if result.success:
                tool_performance[tool]["successes"] += 1
                tool_performance[tool]["times"].append(result.end_time - result.start_time)
        
        print(f"\n🔧 Tool Performance Summary:")
        for tool, perf in tool_performance.items():
            success_rate = (perf["successes"] / perf["requests"]) * 100 if perf["requests"] > 0 else 0
            avg_time = sum(perf["times"]) / len(perf["times"]) if perf["times"] else 0
            
            print(f"   • {tool}:")
            print(f"     Total Requests: {perf['requests']}")
            print(f"     Success Rate: {success_rate:.1f}%")
            print(f"     Avg Response Time: {avg_time:.3f}s")
        
        print(f"\n🎯 Concurrency Insights:")
        
        # หา scenario ที่ดีที่สุด
        best_scenario = max(self.performance_metrics.items(), 
                           key=lambda x: x[1]["requests_per_second"])
        worst_scenario = min(self.performance_metrics.items(), 
                            key=lambda x: x[1]["requests_per_second"])
        
        print(f"   🏆 Best Performance: {best_scenario[0]}")
        print(f"      {best_scenario[1]['requests_per_second']:.2f} requests/second")
        
        print(f"   📉 Lowest Performance: {worst_scenario[0]}")
        print(f"      {worst_scenario[1]['requests_per_second']:.2f} requests/second")
        
        if overall_success_rate == 100:
            print(f"\n🎉 Perfect concurrent performance!")
            print(f"All MCP Tools handled concurrent requests successfully!")
        elif overall_success_rate >= 90:
            print(f"\n✅ Excellent concurrent performance!")
            print(f"MCP Tools handled most concurrent requests well!")
        elif overall_success_rate >= 70:
            print(f"\n👍 Good concurrent performance!")
            print(f"MCP Tools showed decent concurrent handling!")
        else:
            print(f"\n⚠️ Concurrent performance needs improvement!")
            print(f"Consider optimizing MCP Tools for better concurrency!")
        
        print(f"\n🏆 CONCURRENT TEST COMPLETE!")
        print(f"Tested {len(self.test_results)} concurrent MCP Tool requests")
        print(f"Demonstrated multi-tool concurrent capabilities")

async def main():
    """รันการทดสอบ concurrent MCP Tools"""
    
    tester = ConcurrentMCPTester()
    await tester.run_concurrent_tests()

if __name__ == "__main__":
    print("⚡ Concurrent MCP Tools Test")
    print("Testing multiple MCP Tools simultaneously with performance timing")
    print("=" * 60)
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Concurrent test stopped by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
