#!/usr/bin/env python3
"""
🤖 AI Team Using MCP Tools - ให้ทีม AI เป็นคนใช้ MCP Tools
================================================================

ระบบให้ทีม AI ใช้ MCP Tools เพื่อทำงานร่วมกันแบบอัตโนมัติ
"""

import asyncio
import aiohttp
import json
import random
import time
from datetime import datetime
from typing import Dict, List, Any

class AITeamMCPUser:
    """ระบบให้ทีม AI ใช้ MCP Tools"""
    
    def __init__(self):
        # ทีม AI ที่จะใช้ MCP Tools
        self.ai_team = {
            "GitHub Copilot": {
                "specialty": "Code completion & patterns",
                "preferred_tools": ["Fast_Coding", "Sequential_Thinking"],
                "personality": "efficient",
                "tasks": ["code_generation", "pattern_recognition", "quick_fixes"]
            },
            "Trae AI": {
                "specialty": "Architecture & design",
                "preferred_tools": ["Sequential_Thinking", "Neuroflow_Logs"],
                "personality": "systematic",
                "tasks": ["architecture_design", "system_analysis", "planning"]
            },
            "Coder AI": {
                "specialty": "Enterprise solutions",
                "preferred_tools": ["Fast_Coding", "Neuroflow_Logs"],
                "personality": "professional",
                "tasks": ["enterprise_coding", "security_review", "optimization"]
            },
            "OpenAI GPT": {
                "specialty": "General problem solving",
                "preferred_tools": ["Sequential_Thinking", "Fast_Coding"],
                "personality": "analytical",
                "tasks": ["problem_solving", "logic_analysis", "creative_solutions"]
            },
            "Anthropic Claude": {
                "specialty": "Code quality & safety",
                "preferred_tools": ["Sequential_Thinking", "Neuroflow_Logs"],
                "personality": "careful",
                "tasks": ["code_review", "safety_analysis", "documentation"]
            },
            "Google AI": {
                "specialty": "Data & ML integration",
                "preferred_tools": ["Fast_Coding", "Sequential_Thinking"],
                "personality": "data_driven",
                "tasks": ["data_processing", "ml_integration", "performance_analysis"]
            }
        }
        
        # MCP Tools ที่มีให้ใช้
        self.mcp_tools = {
            "Fast_Coding": {
                "url": "http://localhost:8574",
                "capabilities": ["speed_coding", "template_generation", "quick_fixes"],
                "best_for": ["rapid_development", "prototyping", "quick_solutions"]
            },
            "Sequential_Thinking": {
                "url": "http://localhost:8575",
                "capabilities": ["step_by_step_coding", "logic_analysis", "problem_decomposition"],
                "best_for": ["complex_problems", "logical_analysis", "systematic_approach"]
            },
            "Neuroflow_Logs": {
                "url": "http://localhost:8573",
                "capabilities": ["advanced_logging", "log_analysis", "monitoring"],
                "best_for": ["debugging", "monitoring", "system_analysis"]
            }
        }
        
        self.ai_activities = []
        self.collaboration_sessions = []
    
    async def start_ai_team_work(self):
        """เริ่มให้ทีม AI ทำงานด้วย MCP Tools"""
        
        print("🤖 AI Team Using MCP Tools - Starting...")
        print("=" * 60)
        print("Letting AI team members use MCP Tools autonomously")
        print()
        
        # สร้าง work scenarios สำหรับ AI team
        work_scenarios = [
            {
                "name": "Build Web Application",
                "description": "Create a full-stack web application",
                "complexity": "high",
                "required_skills": ["architecture", "coding", "testing"]
            },
            {
                "name": "Optimize Performance",
                "description": "Analyze and optimize system performance",
                "complexity": "medium",
                "required_skills": ["analysis", "optimization", "monitoring"]
            },
            {
                "name": "Debug System Issues",
                "description": "Find and fix system bugs",
                "complexity": "medium",
                "required_skills": ["debugging", "analysis", "problem_solving"]
            },
            {
                "name": "Create API Documentation",
                "description": "Generate comprehensive API documentation",
                "complexity": "low",
                "required_skills": ["documentation", "analysis", "writing"]
            }
        ]
        
        # ให้ AI team เลือกงานและใช้ MCP Tools
        for i, scenario in enumerate(work_scenarios, 1):
            print(f"🎯 Scenario {i}: {scenario['name']}")
            print(f"Description: {scenario['description']}")
            print(f"Complexity: {scenario['complexity']}")
            print("-" * 40)
            
            # ให้ AI team วิเคราะห์และแบ่งงาน
            await self.ai_team_analyze_work(scenario)
            
            # ให้ AI team ใช้ MCP Tools ทำงาน
            await self.ai_team_execute_work(scenario)
            
            print("-" * 40)
            print()
        
        # สรุปการทำงานของ AI team
        self.summarize_ai_team_work()
    
    async def ai_team_analyze_work(self, scenario: Dict[str, Any]):
        """ให้ AI team วิเคราะห์งาน"""
        
        print("🧠 AI Team Analysis Phase...")
        
        # เลือก AI ที่เหมาะสมกับงาน
        suitable_ais = self.select_suitable_ais(scenario)
        
        print(f"Selected AI Team Members: {len(suitable_ais)}")
        for ai_name in suitable_ais:
            ai_info = self.ai_team[ai_name]
            print(f"  • {ai_name} - {ai_info['specialty']}")
        
        # ให้ AI team วางแผนการใช้ MCP Tools
        tool_plan = await self.ai_team_plan_tools(suitable_ais, scenario)
        
        print(f"Tool Usage Plan:")
        for ai_name, tools in tool_plan.items():
            print(f"  • {ai_name}: {', '.join(tools)}")
        
        return suitable_ais, tool_plan
    
    async def ai_team_execute_work(self, scenario: Dict[str, Any]):
        """ให้ AI team ใช้ MCP Tools ทำงาน"""
        
        print("⚡ AI Team Execution Phase...")
        
        suitable_ais, tool_plan = await self.ai_team_analyze_work(scenario)
        
        # ให้แต่ละ AI ใช้ MCP Tools ตามแผน
        for ai_name in suitable_ais:
            ai_info = self.ai_team[ai_name]
            tools_to_use = tool_plan.get(ai_name, [])
            
            print(f"\n🤖 {ai_name} is working...")
            
            for tool_name in tools_to_use:
                await self.ai_use_mcp_tool(ai_name, tool_name, scenario)
                
                # รอสักครู่เพื่อจำลองการทำงาน
                await asyncio.sleep(1)
        
        # สร้าง collaboration session
        session_result = await self.create_ai_collaboration_session(suitable_ais, scenario)
        print(f"\n👥 Collaboration Result: {session_result}")
    
    async def ai_use_mcp_tool(self, ai_name: str, tool_name: str, scenario: Dict[str, Any]):
        """ให้ AI ใช้ MCP Tool เฉพาะ"""
        
        ai_info = self.ai_team[ai_name]
        tool_info = self.mcp_tools[tool_name]
        
        # สร้างคำขอที่เหมาะสมกับ AI และ scenario
        request = self.generate_ai_request(ai_name, tool_name, scenario)
        
        try:
            async with aiohttp.ClientSession() as session:
                payload = {
                    "request": request,
                    "ai_user": ai_name,
                    "scenario": scenario["name"],
                    "type": "ai_team_work"
                }
                
                async with session.post(
                    f"{tool_info['url']}/api/process",
                    json=payload,
                    timeout=10
                ) as response:
                    if response.status == 200:
                        data = await response.json()
                        print(f"  ✅ {ai_name} used {tool_name}: Success")
                        print(f"     Task: {request[:50]}...")
                        print(f"     Result: {data.get('response', 'Completed')[:50]}...")
                        
                        # บันทึกกิจกรรม
                        self.record_ai_activity(ai_name, tool_name, request, True, data.get('response', ''))
                    else:
                        print(f"  ❌ {ai_name} used {tool_name}: HTTP {response.status}")
                        self.record_ai_activity(ai_name, tool_name, request, False, f"HTTP {response.status}")
        
        except Exception as e:
            print(f"  ❌ {ai_name} used {tool_name}: Error - {str(e)}")
            self.record_ai_activity(ai_name, tool_name, request, False, str(e))
    
    def select_suitable_ais(self, scenario: Dict[str, Any]) -> List[str]:
        """เลือก AI ที่เหมาะสมกับงาน"""
        
        suitable_ais = []
        
        for ai_name, ai_info in self.ai_team.items():
            # ตรวจสอบว่า AI มีความเชี่ยวชาญที่เกี่ยวข้องไหม
            ai_skills = ai_info["tasks"]
            scenario_skills = scenario["required_skills"]
            
            # ถ้ามีความเชี่ยวชาญที่ตรงกัน
            if any(skill in " ".join(ai_skills) for skill in scenario_skills):
                suitable_ais.append(ai_name)
        
        # ถ้าไม่มี AI ที่เหมาะสม ให้เลือกแบบสุ่ม
        if not suitable_ais:
            suitable_ais = random.sample(list(self.ai_team.keys()), min(3, len(self.ai_team)))
        
        return suitable_ais[:4]  # จำกัดไม่เกิน 4 AI
    
    async def ai_team_plan_tools(self, ai_list: List[str], scenario: Dict[str, Any]) -> Dict[str, List[str]]:
        """ให้ AI team วางแผนการใช้ MCP Tools"""
        
        tool_plan = {}
        
        for ai_name in ai_list:
            ai_info = self.ai_team[ai_name]
            preferred_tools = ai_info["preferred_tools"]
            
            # เลือก tools ตาม preference และความซับซ้อนของงาน
            if scenario["complexity"] == "high":
                # งานซับซ้อน ใช้หลาย tools
                selected_tools = preferred_tools[:2] if len(preferred_tools) >= 2 else preferred_tools
            elif scenario["complexity"] == "medium":
                # งานปานกลาง ใช้ 1-2 tools
                selected_tools = preferred_tools[:1] + [random.choice(list(self.mcp_tools.keys()))]
            else:
                # งานง่าย ใช้ 1 tool
                selected_tools = [preferred_tools[0]] if preferred_tools else [random.choice(list(self.mcp_tools.keys()))]
            
            tool_plan[ai_name] = list(set(selected_tools))  # ลบ duplicate
        
        return tool_plan
    
    def generate_ai_request(self, ai_name: str, tool_name: str, scenario: Dict[str, Any]) -> str:
        """สร้างคำขอที่เหมาะสมกับ AI และ tool"""
        
        ai_info = self.ai_team[ai_name]
        tool_info = self.mcp_tools[tool_name]
        
        # สร้างคำขอตาม specialty ของ AI และ capability ของ tool
        request_templates = {
            ("GitHub Copilot", "Fast_Coding"): f"Generate code patterns for {scenario['name']}",
            ("GitHub Copilot", "Sequential_Thinking"): f"Analyze code structure for {scenario['name']}",
            ("Trae AI", "Sequential_Thinking"): f"Design system architecture for {scenario['name']}",
            ("Trae AI", "Neuroflow_Logs"): f"Plan logging strategy for {scenario['name']}",
            ("Coder AI", "Fast_Coding"): f"Implement enterprise solution for {scenario['name']}",
            ("Coder AI", "Neuroflow_Logs"): f"Set up monitoring for {scenario['name']}",
            ("OpenAI GPT", "Sequential_Thinking"): f"Solve complex problems in {scenario['name']}",
            ("OpenAI GPT", "Fast_Coding"): f"Create innovative solution for {scenario['name']}",
            ("Anthropic Claude", "Sequential_Thinking"): f"Review code safety for {scenario['name']}",
            ("Anthropic Claude", "Neuroflow_Logs"): f"Analyze system logs for {scenario['name']}",
            ("Google AI", "Fast_Coding"): f"Optimize data processing for {scenario['name']}",
            ("Google AI", "Sequential_Thinking"): f"Analyze performance metrics for {scenario['name']}"
        }
        
        # ใช้ template ที่เหมาะสม หรือสร้างแบบทั่วไป
        key = (ai_name, tool_name)
        if key in request_templates:
            return request_templates[key]
        else:
            return f"{ai_name} working on {scenario['name']} using {tool_name}"
    
    async def create_ai_collaboration_session(self, ai_list: List[str], scenario: Dict[str, Any]) -> str:
        """สร้าง collaboration session สำหรับ AI team"""
        
        try:
            async with aiohttp.ClientSession() as session:
                payload = {
                    "action": "start_session",
                    "data": {
                        "project": scenario["name"],
                        "ai_participants": ai_list,
                        "scenario": scenario
                    }
                }
                
                async with session.post(
                    "http://localhost:8565/api/team/collaborate",
                    json=payload,
                    timeout=10
                ) as response:
                    if response.status == 200:
                        data = await response.json()
                        result = data.get('result', {})
                        session_id = result.get('session_id', 'unknown')
                        
                        self.collaboration_sessions.append({
                            "session_id": session_id,
                            "scenario": scenario["name"],
                            "participants": ai_list,
                            "timestamp": datetime.now().isoformat()
                        })
                        
                        return f"Session {session_id} created with {len(ai_list)} AI participants"
                    else:
                        return f"Failed to create session: HTTP {response.status}"
        
        except Exception as e:
            return f"Error creating session: {str(e)}"
    
    def record_ai_activity(self, ai_name: str, tool_name: str, request: str, success: bool, response: str):
        """บันทึกกิจกรรมของ AI"""
        
        self.ai_activities.append({
            "ai_name": ai_name,
            "tool_name": tool_name,
            "request": request,
            "success": success,
            "response": response,
            "timestamp": datetime.now().isoformat()
        })
    
    def summarize_ai_team_work(self):
        """สรุปการทำงานของ AI team"""
        
        print("=" * 60)
        print("📊 AI TEAM MCP TOOLS USAGE SUMMARY")
        print("=" * 60)
        
        total_activities = len(self.ai_activities)
        successful_activities = sum(1 for a in self.ai_activities if a["success"])
        
        print(f"📈 Total AI Activities: {total_activities}")
        print(f"✅ Successful: {successful_activities}")
        print(f"❌ Failed: {total_activities - successful_activities}")
        print(f"📊 Success Rate: {(successful_activities/total_activities)*100:.1f}%")
        
        print(f"\n🤖 AI Team Performance:")
        
        # วิเคราะห์ตาม AI
        ai_stats = {}
        for activity in self.ai_activities:
            ai_name = activity["ai_name"]
            if ai_name not in ai_stats:
                ai_stats[ai_name] = {"total": 0, "success": 0}
            
            ai_stats[ai_name]["total"] += 1
            if activity["success"]:
                ai_stats[ai_name]["success"] += 1
        
        for ai_name, stats in ai_stats.items():
            success_rate = (stats["success"] / stats["total"]) * 100
            print(f"   • {ai_name}: {stats['success']}/{stats['total']} ({success_rate:.1f}%)")
        
        print(f"\n🔧 MCP Tools Usage:")
        
        # วิเคราะห์ตาม tool
        tool_stats = {}
        for activity in self.ai_activities:
            tool_name = activity["tool_name"]
            if tool_name not in tool_stats:
                tool_stats[tool_name] = {"total": 0, "success": 0}
            
            tool_stats[tool_name]["total"] += 1
            if activity["success"]:
                tool_stats[tool_name]["success"] += 1
        
        for tool_name, stats in tool_stats.items():
            success_rate = (stats["success"] / stats["total"]) * 100
            print(f"   • {tool_name}: {stats['success']}/{stats['total']} ({success_rate:.1f}%)")
        
        print(f"\n👥 Collaboration Sessions: {len(self.collaboration_sessions)}")
        for session in self.collaboration_sessions:
            print(f"   • {session['session_id']}: {session['scenario']} ({len(session['participants'])} AIs)")
        
        print(f"\n🎯 Key Insights:")
        if successful_activities == total_activities:
            print("🎉 Perfect AI team performance! All MCP Tools used successfully")
        elif successful_activities >= total_activities * 0.8:
            print("✅ Excellent AI team performance! Most MCP Tools used effectively")
        else:
            print("⚠️ AI team needs optimization in MCP Tools usage")
        
        print(f"\n🚀 AI Team MCP Tools Usage Complete!")
        print("AI team members successfully used MCP Tools autonomously!")

async def main():
    """รันระบบให้ AI team ใช้ MCP Tools"""
    
    ai_team_user = AITeamMCPUser()
    await ai_team_user.start_ai_team_work()

if __name__ == "__main__":
    print("🤖 AI Team Using MCP Tools")
    print("Letting AI team members use MCP Tools autonomously")
    print("=" * 60)
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 AI team work stopped by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
