#!/usr/bin/env python3
"""
🚀 Start All MCP Systems - เริ่มต้น MCP Systems ทั้งหมด
================================================================
"""

import subprocess
import sys
import time
import os
from pathlib import Path

def start_all_mcp_systems():
    """เริ่มต้น MCP Systems ทั้งหมด"""
    
    print("🚀 Starting All MCP Systems")
    print("=" * 50)
    
    # เปลี่ยนไปยัง directory ของ MCP_Installation
    base_path = Path(__file__).parent.parent
    os.chdir(base_path)
    
    systems = [
        {
            "name": "Fast Coding MCP",
            "port": 8574,
            "script": "Fast_Coding_MCP/main.py",
            "url": "http://localhost:8574"
        },
        {
            "name": "Sequential Thinking MCP", 
            "port": 8575,
            "script": "Sequential_Thinking_MCP/main.py",
            "url": "http://localhost:8575"
        },
        {
            "name": "Neuroflow Logs MCP",
            "port": 8573,
            "script": "Neuroflow_Logs_MCP/main.py",
            "url": "http://localhost:8573"
        }
    ]
    
    processes = []
    
    for system in systems:
        print(f"🚀 Starting {system['name']} on port {system['port']}...")
        
        try:
            # เริ่มต้นระบบแบบ background
            process = subprocess.Popen(
                [sys.executable, system['script']],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            processes.append({
                "name": system['name'],
                "process": process,
                "url": system['url']
            })
            print(f"  ✅ {system['name']} started (PID: {process.pid})")
            
            # รอสักครู่เพื่อให้ระบบเริ่มต้น
            time.sleep(2)
            
        except Exception as e:
            print(f"  ❌ Failed to start {system['name']}: {e}")
    
    print(f"\n🎉 All MCP Systems Started!")
    print("=" * 50)
    print("🌐 Access Points:")
    
    for proc_info in processes:
        print(f"  • {proc_info['name']}: {proc_info['url']}")
    
    print(f"\n📊 System Status:")
    for proc_info in processes:
        if proc_info['process'].poll() is None:
            print(f"  🟢 {proc_info['name']}: Running")
        else:
            print(f"  🔴 {proc_info['name']}: Stopped")
    
    print(f"\n⚠️ Note: Systems are running in background")
    print("To stop all systems, use Ctrl+C or close terminal")
    
    # รอให้ user กด Ctrl+C
    try:
        print(f"\nPress Ctrl+C to stop all systems...")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n🛑 Stopping all MCP systems...")
        
        for proc_info in processes:
            try:
                proc_info['process'].terminate()
                print(f"  ✅ Stopped {proc_info['name']}")
            except:
                print(f"  ⚠️ Could not stop {proc_info['name']}")
        
        print("👋 All systems stopped!")

if __name__ == "__main__":
    start_all_mcp_systems()
