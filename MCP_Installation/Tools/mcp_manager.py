#!/usr/bin/env python3
"""
🔧 MCP Manager - จัดการ MCP Systems
================================================================
"""

import subprocess
import sys
import json
import time
import psutil
from pathlib import Path
from typing import Dict, List, Any

class MCPManager:
    """ตัวจัดการ MCP Systems"""
    
    def __init__(self):
        self.config_path = Path(__file__).parent.parent / "Config" / "config.json"
        self.base_path = Path(__file__).parent.parent
        self.running_processes = {}
        
        # โหลด config
        self.load_config()
    
    def load_config(self):
        """โหลด configuration"""
        
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
        except Exception as e:
            print(f"❌ Failed to load config: {e}")
            self.config = {"mcp_systems": {}}
    
    def list_systems(self):
        """แสดงรายการ MCP Systems"""
        
        print("📋 Available MCP Systems:")
        print("-" * 40)
        
        for system_id, system_info in self.config["mcp_systems"].items():
            status = self.check_system_status(system_info["port"])
            status_icon = "🟢" if status else "🔴"
            
            print(f"{status_icon} {system_info['name']}")
            print(f"   Port: {system_info['port']}")
            print(f"   Description: {system_info['description']}")
            print(f"   Status: {'Running' if status else 'Stopped'}")
            print()
    
    def check_system_status(self, port: int) -> bool:
        """ตรวจสอบสถานะของระบบ"""
        
        try:
            for conn in psutil.net_connections():
                if conn.laddr.port == port and conn.status == 'LISTEN':
                    return True
            return False
        except:
            return False
    
    def start_system(self, system_id: str):
        """เริ่มต้นระบบเฉพาะ"""
        
        if system_id not in self.config["mcp_systems"]:
            print(f"❌ System '{system_id}' not found")
            return False
        
        system_info = self.config["mcp_systems"][system_id]
        
        # ตรวจสอบว่าระบบทำงานอยู่หรือไม่
        if self.check_system_status(system_info["port"]):
            print(f"⚠️ {system_info['name']} is already running on port {system_info['port']}")
            return True
        
        # หาไฟล์ script
        script_path = self.find_system_script(system_id)
        if not script_path:
            print(f"❌ Script not found for {system_id}")
            return False
        
        print(f"🚀 Starting {system_info['name']}...")
        
        try:
            # เริ่มต้นระบบ
            process = subprocess.Popen(
                [sys.executable, str(script_path)],
                cwd=self.base_path,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            
            self.running_processes[system_id] = process
            
            # รอสักครู่แล้วตรวจสอบ
            time.sleep(3)
            
            if self.check_system_status(system_info["port"]):
                print(f"✅ {system_info['name']} started successfully (PID: {process.pid})")
                print(f"   Access: http://localhost:{system_info['port']}")
                return True
            else:
                print(f"❌ Failed to start {system_info['name']}")
                return False
                
        except Exception as e:
            print(f"❌ Error starting {system_info['name']}: {e}")
            return False
    
    def stop_system(self, system_id: str):
        """หยุดระบบเฉพาะ"""
        
        if system_id not in self.config["mcp_systems"]:
            print(f"❌ System '{system_id}' not found")
            return False
        
        system_info = self.config["mcp_systems"][system_id]
        
        print(f"🛑 Stopping {system_info['name']}...")
        
        # หยุดจาก running processes
        if system_id in self.running_processes:
            try:
                self.running_processes[system_id].terminate()
                del self.running_processes[system_id]
                print(f"✅ {system_info['name']} stopped")
                return True
            except:
                pass
        
        # หยุดจาก port
        try:
            for proc in psutil.process_iter(['pid', 'name', 'connections']):
                try:
                    for conn in proc.info['connections'] or []:
                        if conn.laddr.port == system_info["port"]:
                            proc.terminate()
                            print(f"✅ {system_info['name']} stopped")
                            return True
                except:
                    continue
            
            print(f"⚠️ {system_info['name']} was not running")
            return True
            
        except Exception as e:
            print(f"❌ Error stopping {system_info['name']}: {e}")
            return False
    
    def start_all(self):
        """เริ่มต้นระบบทั้งหมด"""
        
        print("🚀 Starting All MCP Systems...")
        print("-" * 40)
        
        success_count = 0
        total_count = len(self.config["mcp_systems"])
        
        for system_id in self.config["mcp_systems"]:
            if self.start_system(system_id):
                success_count += 1
            time.sleep(2)  # รอระหว่างการเริ่มต้น
        
        print(f"\n📊 Started {success_count}/{total_count} systems")
        
        if success_count == total_count:
            print("🎉 All systems started successfully!")
        else:
            print("⚠️ Some systems failed to start")
    
    def stop_all(self):
        """หยุดระบบทั้งหมด"""
        
        print("🛑 Stopping All MCP Systems...")
        print("-" * 40)
        
        for system_id in self.config["mcp_systems"]:
            self.stop_system(system_id)
        
        print("✅ All systems stopped")
    
    def restart_system(self, system_id: str):
        """รีสตาร์ทระบบ"""
        
        print(f"🔄 Restarting {system_id}...")
        self.stop_system(system_id)
        time.sleep(2)
        return self.start_system(system_id)
    
    def find_system_script(self, system_id: str) -> Path:
        """หาไฟล์ script ของระบบ"""
        
        script_mappings = {
            "fast_coding": "Fast_Coding_MCP/main.py",
            "sequential_thinking": "Sequential_Thinking_MCP/main.py",
            "neuroflow_logs": "Neuroflow_Logs_MCP/main.py"
        }
        
        if system_id in script_mappings:
            script_path = self.base_path / script_mappings[system_id]
            if script_path.exists():
                return script_path
        
        return None
    
    def show_help(self):
        """แสดงคำแนะนำการใช้งาน"""
        
        print("🔧 MCP Manager - Help")
        print("=" * 40)
        print("Commands:")
        print("  list                 - List all systems")
        print("  start <system_id>    - Start specific system")
        print("  stop <system_id>     - Stop specific system")
        print("  restart <system_id>  - Restart specific system")
        print("  start-all           - Start all systems")
        print("  stop-all            - Stop all systems")
        print("  status              - Show system status")
        print("  help                - Show this help")
        print()
        print("System IDs:")
        for system_id, system_info in self.config["mcp_systems"].items():
            print(f"  {system_id:20} - {system_info['name']}")

def main():
    """Main function"""
    
    manager = MCPManager()
    
    if len(sys.argv) < 2:
        manager.show_help()
        return
    
    command = sys.argv[1].lower()
    
    if command == "list":
        manager.list_systems()
    elif command == "start" and len(sys.argv) > 2:
        manager.start_system(sys.argv[2])
    elif command == "stop" and len(sys.argv) > 2:
        manager.stop_system(sys.argv[2])
    elif command == "restart" and len(sys.argv) > 2:
        manager.restart_system(sys.argv[2])
    elif command == "start-all":
        manager.start_all()
    elif command == "stop-all":
        manager.stop_all()
    elif command == "status":
        manager.list_systems()
    elif command == "help":
        manager.show_help()
    else:
        print("❌ Unknown command. Use 'help' for available commands.")

if __name__ == "__main__":
    main()
