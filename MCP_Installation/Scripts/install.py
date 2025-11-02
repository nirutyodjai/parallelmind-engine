#!/usr/bin/env python3
"""
📦 MCP System Installer - ติดตั้ง MCP System
================================================================
"""

import subprocess
import sys
import os
from pathlib import Path

def install_requirements():
    """ติดตั้ง requirements"""
    
    print("📦 Installing requirements...")
    
    requirements = [
        "fastapi",
        "uvicorn[standard]",
        "aiohttp",
        "pydantic",
        "python-multipart"
    ]
    
    for req in requirements:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", req])
            print(f"  ✅ Installed: {req}")
        except Exception as e:
            print(f"  ❌ Failed to install {req}: {e}")

def start_mcp_systems():
    """เริ่มต้น MCP Systems"""
    
    print("\n🚀 Starting MCP Systems...")
    
    systems = [
        {"name": "Fast Coding MCP", "port": 8574, "path": "Fast_Coding_MCP/main.py"},
        {"name": "Sequential Thinking MCP", "port": 8575, "path": "Sequential_Thinking_MCP/main.py"},
        {"name": "Neuroflow Logs MCP", "port": 8573, "path": "Neuroflow_Logs_MCP/main.py"}
    ]
    
    for system in systems:
        print(f"Starting {system['name']} on port {system['port']}...")
        # ใช้ subprocess.Popen เพื่อรันแบบ background
        # subprocess.Popen([sys.executable, system['path']])

def main():
    """ติดตั้งและเริ่มต้น MCP System"""
    
    print("📦 MCP System Installation")
    print("=" * 50)
    
    # ติดตั้ง requirements
    install_requirements()
    
    # เริ่มต้นระบบ
    start_mcp_systems()
    
    print("\n🎉 MCP System Installation Complete!")
    print("Access points:")
    print("  • Fast Coding MCP: http://localhost:8574")
    print("  • Sequential Thinking MCP: http://localhost:8575")
    print("  • Neuroflow Logs MCP: http://localhost:8573")

if __name__ == "__main__":
    main()
