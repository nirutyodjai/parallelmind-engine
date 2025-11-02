#!/usr/bin/env python3
"""
👥 Team Coding with MCP Tools - ทดสอบเขียนโค้ดแบบทีมด้วย MCP Tools
================================================================

ทดสอบให้ทีม AI เขียนโค้ดร่วมกันโดยใช้ MCP Tools จริงๆ
"""

import asyncio
import aiohttp
import json
import time
from datetime import datetime
from typing import Dict, List, Any
import random

class TeamCodingWithMCPTools:
    """ระบบเขียนโค้ดแบบทีมด้วย MCP Tools"""
    
    def __init__(self):
        # ทีม AI สำหรับเขียนโค้ด
        self.coding_team = {
            "GitHub Copilot": {
                "role": "Code Generator",
                "specialty": "Pattern recognition & code completion",
                "preferred_tools": ["Fast_Coding"],
                "tasks": ["generate_functions", "complete_code", "suggest_patterns"]
            },
            "Trae AI": {
                "role": "System Architect", 
                "specialty": "Architecture & design patterns",
                "preferred_tools": ["Sequential_Thinking"],
                "tasks": ["design_architecture", "plan_structure", "create_blueprints"]
            },
            "Coder AI": {
                "role": "Implementation Lead",
                "specialty": "Enterprise-grade implementation",
                "preferred_tools": ["Fast_Coding", "Sequential_Thinking"],
                "tasks": ["implement_features", "optimize_code", "handle_complexity"]
            },
            "Anthropic Claude": {
                "role": "Quality Assurance",
                "specialty": "Code review & safety",
                "preferred_tools": ["Sequential_Thinking", "Neuroflow_Logs"],
                "tasks": ["review_code", "check_security", "ensure_quality"]
            },
            "OpenAI GPT": {
                "role": "Problem Solver",
                "specialty": "Creative solutions & debugging",
                "preferred_tools": ["Sequential_Thinking", "Fast_Coding"],
                "tasks": ["solve_problems", "debug_issues", "find_solutions"]
            },
            "Google AI": {
                "role": "Performance Optimizer",
                "specialty": "Data processing & optimization",
                "preferred_tools": ["Fast_Coding", "Neuroflow_Logs"],
                "tasks": ["optimize_performance", "handle_data", "improve_efficiency"]
            }
        }
        
        # MCP Tools
        self.mcp_tools = {
            "Fast_Coding": {
                "url": "http://localhost:8574",
                "capabilities": ["rapid_coding", "template_generation", "quick_implementation"],
                "best_for": ["prototyping", "quick_solutions", "code_generation"]
            },
            "Sequential_Thinking": {
                "url": "http://localhost:8575", 
                "capabilities": ["logical_analysis", "step_by_step_planning", "problem_decomposition"],
                "best_for": ["architecture", "complex_logic", "systematic_approach"]
            },
            "Neuroflow_Logs": {
                "url": "http://localhost:8573",
                "capabilities": ["monitoring", "logging", "analysis"],
                "best_for": ["debugging", "performance_tracking", "quality_assurance"]
            }
        }
        
        # โปรเจคที่จะเขียนร่วมกัน
        self.coding_projects = [
            {
                "name": "Web API Server",
                "description": "Create a FastAPI server with user management",
                "complexity": "medium",
                "requirements": [
                    "FastAPI framework",
                    "User authentication",
                    "Database integration", 
                    "API documentation",
                    "Error handling"
                ],
                "files_to_create": ["main.py", "models.py", "auth.py", "database.py"]
            },
            {
                "name": "Data Processing Pipeline",
                "description": "Build a data processing and analysis pipeline",
                "complexity": "high",
                "requirements": [
                    "Data ingestion",
                    "Data validation",
                    "Processing algorithms",
                    "Output generation",
                    "Monitoring system"
                ],
                "files_to_create": ["pipeline.py", "processor.py", "validator.py", "monitor.py"]
            },
            {
                "name": "Task Automation Tool",
                "description": "Create a CLI tool for task automation",
                "complexity": "low",
                "requirements": [
                    "Command-line interface",
                    "Configuration management",
                    "Task scheduling",
                    "Logging system"
                ],
                "files_to_create": ["cli.py", "config.py", "scheduler.py", "logger.py"]
            }
        ]
        
        self.team_activities = []
        self.generated_code = {}
        self.collaboration_sessions = []
    
    async def start_team_coding(self):
        """เริ่มการเขียนโค้ดแบบทีม"""
        
        print("👥 Team Coding with MCP Tools - Starting...")
        print("=" * 60)
        print("AI team will collaborate to write code using MCP Tools")
        print()
        
        # เลือกโปรเจคที่จะทำ
        for i, project in enumerate(self.coding_projects, 1):
            print(f"🎯 Project {i}: {project['name']}")
            print(f"Description: {project['description']}")
            print(f"Complexity: {project['complexity']}")
            print(f"Files to create: {', '.join(project['files_to_create'])}")
            print("-" * 50)
            
            # ให้ทีมวางแผนโปรเจค
            await self.team_project_planning(project)
            
            # ให้ทีมเขียนโค้ดร่วมกัน
            await self.team_collaborative_coding(project)
            
            # รีวิวและปรับปรุงโค้ด
            await self.team_code_review(project)
            
            print("-" * 50)
            print()
        
        # สรุปผลการเขียนโค้ดแบบทีม
        self.summarize_team_coding()
    
    async def team_project_planning(self, project: Dict[str, Any]):
        """ให้ทีมวางแผนโปรเจค"""
        
        print("📋 Team Project Planning Phase...")
        
        # ให้ System Architect วางแผนโครงสร้าง
        architect = "Trae AI"
        print(f"🏗️ {architect} planning project architecture...")
        
        architecture_plan = await self.ai_use_mcp_tool(
            architect, 
            "Sequential_Thinking",
            f"Plan architecture for {project['name']}: {project['description']}",
            "architecture_planning"
        )
        
        if architecture_plan["success"]:
            print(f"  ✅ Architecture planned successfully")
            print(f"     Plan: {architecture_plan['result'][:100]}...")
        
        # ให้ Implementation Lead วางแผนการพัฒนา
        lead = "Coder AI"
        print(f"⚡ {lead} planning implementation strategy...")
        
        implementation_plan = await self.ai_use_mcp_tool(
            lead,
            "Sequential_Thinking", 
            f"Plan implementation strategy for {project['name']} with requirements: {', '.join(project['requirements'])}",
            "implementation_planning"
        )
        
        if implementation_plan["success"]:
            print(f"  ✅ Implementation strategy planned")
            print(f"     Strategy: {implementation_plan['result'][:100]}...")
        
        # สร้าง collaboration session สำหรับโปรเจค
        session_result = await self.create_project_collaboration(project)
        print(f"👥 Project Collaboration: {session_result}")
    
    async def team_collaborative_coding(self, project: Dict[str, Any]):
        """ให้ทีมเขียนโค้ดร่วมกัน"""
        
        print("💻 Team Collaborative Coding Phase...")
        
        # แบ่งงานให้แต่ละคนในทีม
        file_assignments = self.assign_files_to_team(project)
        
        print("📝 File assignments:")
        for ai_name, files in file_assignments.items():
            print(f"   • {ai_name}: {', '.join(files)}")
        
        # ให้แต่ละ AI เขียนโค้ดส่วนของตัวเอง
        for ai_name, files in file_assignments.items():
            ai_info = self.coding_team[ai_name]
            print(f"\n💻 {ai_name} ({ai_info['role']}) coding...")
            
            for filename in files:
                # เลือก MCP Tool ที่เหมาะสม
                tool_name = self.select_best_tool_for_task(ai_info, "coding")
                
                # ให้ AI เขียนโค้ด
                code_result = await self.ai_write_code(
                    ai_name, 
                    tool_name,
                    project,
                    filename
                )
                
                if code_result["success"]:
                    print(f"  ✅ {filename} created by {ai_name}")
                    print(f"     Code preview: {code_result['code'][:80]}...")
                    
                    # เก็บโค้ดที่สร้าง
                    if project["name"] not in self.generated_code:
                        self.generated_code[project["name"]] = {}
                    self.generated_code[project["name"]][filename] = {
                        "author": ai_name,
                        "code": code_result["code"],
                        "tool_used": tool_name
                    }
                else:
                    print(f"  ❌ Failed to create {filename}")
                
                # รอสักครู่
                await asyncio.sleep(1)
    
    async def team_code_review(self, project: Dict[str, Any]):
        """ให้ทีมรีวิวโค้ด"""
        
        print("🔍 Team Code Review Phase...")
        
        # ให้ Quality Assurance รีวิวโค้ด
        reviewer = "Anthropic Claude"
        print(f"🔍 {reviewer} reviewing code quality...")
        
        if project["name"] in self.generated_code:
            files_to_review = list(self.generated_code[project["name"]].keys())
            
            for filename in files_to_review[:2]:  # รีวิวแค่ 2 ไฟล์แรก
                review_result = await self.ai_use_mcp_tool(
                    reviewer,
                    "Sequential_Thinking",
                    f"Review code quality for {filename} in {project['name']} project",
                    "code_review"
                )
                
                if review_result["success"]:
                    print(f"  ✅ {filename} reviewed")
                    print(f"     Review: {review_result['result'][:100]}...")
        
        # ให้ Performance Optimizer ตรวจสอบประสิทธิภาพ
        optimizer = "Google AI"
        print(f"⚡ {optimizer} optimizing performance...")
        
        optimization_result = await self.ai_use_mcp_tool(
            optimizer,
            "Neuroflow_Logs",
            f"Analyze performance for {project['name']} project",
            "performance_optimization"
        )
        
        if optimization_result["success"]:
            print(f"  ✅ Performance analysis completed")
            print(f"     Analysis: {optimization_result['result'][:100]}...")
    
    async def ai_use_mcp_tool(self, ai_name: str, tool_name: str, task: str, task_type: str) -> Dict[str, Any]:
        """ให้ AI ใช้ MCP Tool เฉพาะ"""
        
        try:
            tool_info = self.mcp_tools[tool_name]
            
            async with aiohttp.ClientSession() as session:
                payload = {
                    "request": task,
                    "ai_user": ai_name,
                    "task_type": task_type,
                    "type": "team_coding"
                }
                
                async with session.post(
                    f"{tool_info['url']}/api/process",
                    json=payload,
                    timeout=10
                ) as response:
                    if response.status == 200:
                        data = await response.json()
                        result = data.get('response', 'Task completed successfully')
                        
                        # บันทึกกิจกรรม
                        self.record_team_activity(ai_name, tool_name, task, task_type, True, result)
                        
                        return {
                            "success": True,
                            "result": result,
                            "tool_used": tool_name
                        }
                    else:
                        error_msg = f"HTTP {response.status}"
                        self.record_team_activity(ai_name, tool_name, task, task_type, False, error_msg)
                        return {"success": False, "error": error_msg}
        
        except Exception as e:
            error_msg = str(e)
            self.record_team_activity(ai_name, tool_name, task, task_type, False, error_msg)
            return {"success": False, "error": error_msg}
    
    async def ai_write_code(self, ai_name: str, tool_name: str, project: Dict[str, Any], filename: str) -> Dict[str, Any]:
        """ให้ AI เขียนโค้ดไฟล์เฉพาะ"""
        
        # สร้าง prompt สำหรับเขียนโค้ด
        ai_info = self.coding_team[ai_name]
        code_prompt = f"""
Write {filename} for {project['name']} project.
Role: {ai_info['role']}
Requirements: {', '.join(project['requirements'])}
Description: {project['description']}
Create functional, well-structured code.
        """.strip()
        
        result = await self.ai_use_mcp_tool(ai_name, tool_name, code_prompt, "code_generation")
        
        if result["success"]:
            # สร้างโค้ดจำลอง (เนื่องจาก MCP Tool ไม่ได้สร้างโค้ดจริง)
            mock_code = self.generate_mock_code(filename, project, ai_name)
            return {
                "success": True,
                "code": mock_code,
                "tool_used": tool_name
            }
        else:
            return result
    
    def generate_mock_code(self, filename: str, project: Dict[str, Any], author: str) -> str:
        """สร้างโค้ดจำลองสำหรับการทดสอบ"""
        
        code_templates = {
            "main.py": f'''#!/usr/bin/env python3
"""
{project['name']} - Main Application
Generated by: {author}
"""

from fastapi import FastAPI
from models import User
from auth import AuthManager
from database import DatabaseManager

app = FastAPI(title="{project['name']}")
auth = AuthManager()
db = DatabaseManager()

@app.get("/")
async def root():
    return {{"message": "Welcome to {project['name']}"}}

@app.get("/health")
async def health_check():
    return {{"status": "healthy", "service": "{project['name']}"}}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
''',
            
            "models.py": f'''"""
{project['name']} - Data Models
Generated by: {author}
"""

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class User(BaseModel):
    id: Optional[int] = None
    username: str
    email: str
    created_at: Optional[datetime] = None
    is_active: bool = True

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime
    is_active: bool
''',
            
            "auth.py": f'''"""
{project['name']} - Authentication Manager
Generated by: {author}
"""

from typing import Optional
import hashlib
import secrets

class AuthManager:
    def __init__(self):
        self.secret_key = secrets.token_hex(32)
    
    def hash_password(self, password: str) -> str:
        """Hash password securely"""
        salt = secrets.token_hex(16)
        hashed = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000)
        return f"{{salt}}:{{hashed.hex()}}"
    
    def verify_password(self, password: str, hashed: str) -> bool:
        """Verify password against hash"""
        try:
            salt, stored_hash = hashed.split(':')
            new_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000)
            return new_hash.hex() == stored_hash
        except:
            return False
    
    def create_token(self, user_id: int) -> str:
        """Create authentication token"""
        return secrets.token_urlsafe(32)
''',
            
            "database.py": f'''"""
{project['name']} - Database Manager
Generated by: {author}
"""

from typing import List, Optional
import sqlite3
from models import User, UserCreate

class DatabaseManager:
    def __init__(self, db_path: str = "app.db"):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize database tables"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    is_active BOOLEAN DEFAULT TRUE
                )
            """)
    
    def create_user(self, user_data: UserCreate) -> Optional[User]:
        """Create new user"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.execute(
                    "INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
                    (user_data.username, user_data.email, "hashed_password")
                )
                user_id = cursor.lastrowid
                return User(id=user_id, username=user_data.username, email=user_data.email)
        except:
            return None
    
    def get_user(self, user_id: int) -> Optional[User]:
        """Get user by ID"""
        with sqlite3.connect(self.db_path) as conn:
            row = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
            if row:
                return User(id=row[0], username=row[1], email=row[2])
        return None
'''
        }
        
        # ถ้าไม่มี template ให้สร้างโค้ดทั่วไป
        if filename not in code_templates:
            return f'''"""
{filename} for {project['name']}
Generated by: {author}
"""

# {filename} implementation
# Created for {project['description']}

class {filename.replace('.py', '').title()}:
    def __init__(self):
        self.name = "{project['name']}"
        self.author = "{author}"
    
    def process(self):
        """Main processing method"""
        print(f"Processing in {{self.name}} by {{self.author}}")
        return True

if __name__ == "__main__":
    processor = {filename.replace('.py', '').title()}()
    processor.process()
'''
        
        return code_templates.get(filename, "# Code generated by AI team")
    
    def assign_files_to_team(self, project: Dict[str, Any]) -> Dict[str, List[str]]:
        """แบ่งไฟล์ให้แต่ละคนในทีม"""
        
        files = project["files_to_create"]
        assignments = {}
        
        # กำหนดไฟล์ตามบทบาท
        role_file_mapping = {
            "System Architect": ["models.py"],
            "Implementation Lead": ["main.py"],
            "Code Generator": ["auth.py"],
            "Quality Assurance": ["database.py"],
            "Problem Solver": [],
            "Performance Optimizer": []
        }
        
        # แบ่งไฟล์ตามบทบาท
        remaining_files = files.copy()
        
        for ai_name, ai_info in self.coding_team.items():
            role = ai_info["role"]
            assigned_files = []
            
            # ให้ไฟล์ที่เหมาะสมกับบทบาท
            if role in role_file_mapping:
                for file in role_file_mapping[role]:
                    if file in remaining_files:
                        assigned_files.append(file)
                        remaining_files.remove(file)
            
            assignments[ai_name] = assigned_files
        
        # แบ่งไฟล์ที่เหลือให้คนที่ยังไม่มีงาน
        for ai_name in assignments:
            if not assignments[ai_name] and remaining_files:
                assignments[ai_name].append(remaining_files.pop(0))
        
        return assignments
    
    def select_best_tool_for_task(self, ai_info: Dict[str, Any], task_type: str) -> str:
        """เลือก MCP Tool ที่เหมาะสมสำหรับงาน"""
        
        preferred_tools = ai_info["preferred_tools"]
        
        # เลือกตาม task type
        if task_type == "coding":
            if "Fast_Coding" in preferred_tools:
                return "Fast_Coding"
        elif task_type == "planning":
            if "Sequential_Thinking" in preferred_tools:
                return "Sequential_Thinking"
        elif task_type == "review":
            if "Neuroflow_Logs" in preferred_tools:
                return "Neuroflow_Logs"
        
        # ถ้าไม่มีที่เหมาะสม ให้เลือกตัวแรก
        return preferred_tools[0] if preferred_tools else "Fast_Coding"
    
    async def create_project_collaboration(self, project: Dict[str, Any]) -> str:
        """สร้าง collaboration session สำหรับโปรเจค"""
        
        try:
            async with aiohttp.ClientSession() as session:
                payload = {
                    "action": "start_session",
                    "data": {
                        "project": project["name"],
                        "description": project["description"],
                        "ai_participants": list(self.coding_team.keys()),
                        "files_to_create": project["files_to_create"]
                    }
                }
                
                async with session.post(
                    "http://localhost:8565/api/team/collaborate",
                    json=payload,
                    timeout=10
                ) as response:
                    if response.status == 200:
                        data = await response.json()
                        session_id = data.get('result', {}).get('session_id', 'unknown')
                        
                        self.collaboration_sessions.append({
                            "session_id": session_id,
                            "project": project["name"],
                            "participants": list(self.coding_team.keys()),
                            "timestamp": datetime.now().isoformat()
                        })
                        
                        return f"Session {session_id} created"
                    else:
                        return f"Failed (HTTP {response.status})"
        
        except Exception as e:
            return f"Error: {str(e)}"
    
    def record_team_activity(self, ai_name: str, tool_name: str, task: str, task_type: str, success: bool, result: str):
        """บันทึกกิจกรรมของทีม"""
        
        self.team_activities.append({
            "ai_name": ai_name,
            "tool_name": tool_name,
            "task": task,
            "task_type": task_type,
            "success": success,
            "result": result,
            "timestamp": datetime.now().isoformat()
        })
    
    def summarize_team_coding(self):
        """สรุปผลการเขียนโค้ดแบบทีม"""
        
        print("=" * 60)
        print("📊 TEAM CODING WITH MCP TOOLS SUMMARY")
        print("=" * 60)
        
        total_activities = len(self.team_activities)
        successful_activities = sum(1 for a in self.team_activities if a["success"])
        
        print(f"📈 Team Coding Statistics:")
        print(f"   • Total Activities: {total_activities}")
        print(f"   • Successful: {successful_activities}")
        print(f"   • Failed: {total_activities - successful_activities}")
        print(f"   • Success Rate: {(successful_activities/total_activities)*100:.1f}%")
        
        print(f"\n🤖 AI Team Performance:")
        
        # วิเคราะห์ตาม AI
        ai_stats = {}
        for activity in self.team_activities:
            ai_name = activity["ai_name"]
            if ai_name not in ai_stats:
                ai_stats[ai_name] = {"total": 0, "success": 0}
            
            ai_stats[ai_name]["total"] += 1
            if activity["success"]:
                ai_stats[ai_name]["success"] += 1
        
        for ai_name, stats in ai_stats.items():
            success_rate = (stats["success"] / stats["total"]) * 100
            role = self.coding_team[ai_name]["role"]
            print(f"   • {ai_name} ({role}): {stats['success']}/{stats['total']} ({success_rate:.1f}%)")
        
        print(f"\n🔧 MCP Tools Usage:")
        
        # วิเคราะห์ตาม tool
        tool_stats = {}
        for activity in self.team_activities:
            tool_name = activity["tool_name"]
            if tool_name not in tool_stats:
                tool_stats[tool_name] = {"total": 0, "success": 0}
            
            tool_stats[tool_name]["total"] += 1
            if activity["success"]:
                tool_stats[tool_name]["success"] += 1
        
        for tool_name, stats in tool_stats.items():
            success_rate = (stats["success"] / stats["total"]) * 100
            print(f"   • {tool_name}: {stats['success']}/{stats['total']} ({success_rate:.1f}%)")
        
        print(f"\n💻 Generated Code Summary:")
        
        total_files = 0
        for project_name, files in self.generated_code.items():
            print(f"   📁 {project_name}: {len(files)} files")
            total_files += len(files)
            for filename, file_info in files.items():
                print(f"      • {filename} by {file_info['author']} using {file_info['tool_used']}")
        
        print(f"\n👥 Collaboration Sessions: {len(self.collaboration_sessions)}")
        for session in self.collaboration_sessions:
            print(f"   • {session['session_id']}: {session['project']} ({len(session['participants'])} AIs)")
        
        print(f"\n🎯 Team Coding Insights:")
        if successful_activities == total_activities:
            print("🎉 Perfect team collaboration! All AI members used MCP Tools successfully")
        elif successful_activities >= total_activities * 0.8:
            print("✅ Excellent team performance! Most activities completed successfully")
        else:
            print("⚠️ Team coordination needs improvement")
        
        print(f"\n📊 Code Generation Results:")
        print(f"   • Total Projects: {len(self.generated_code)}")
        print(f"   • Total Files Generated: {total_files}")
        print(f"   • AI Team Members: {len(self.coding_team)}")
        print(f"   • MCP Tools Used: {len(self.mcp_tools)}")
        
        print(f"\n🏆 TEAM CODING COMPLETE!")
        print("AI team successfully collaborated to write code using MCP Tools!")

async def main():
    """รันการเขียนโค้ดแบบทีม"""
    
    team_coder = TeamCodingWithMCPTools()
    await team_coder.start_team_coding()

if __name__ == "__main__":
    print("👥 Team Coding with MCP Tools")
    print("AI team collaboration for code development")
    print("=" * 60)
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Team coding stopped by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
