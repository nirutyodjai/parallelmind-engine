#!/usr/bin/env python3
"""
Fast Coding MCP Tools Launcher for Ultimate IDE
ระบบเขียนโค้ดแบบรวดเร็วและอัตโนมัติ
"""

import sys
import os
from pathlib import Path

# Add current directory to path
sys.path.append(str(Path(__file__).parent))

from fast_coding_ui import FastCodingUI

def main():
    """เริ่ม Fast Coding MCP Tools"""
    print("⚡ Starting Fast Coding MCP Tools...")
    print("🔧 ระบบเขียนโค้ดแบบรวดเร็วและอัตโนมัติสำหรับ Ultimate IDE")
    print("=" * 60)
    
    # Create Fast Coding MCP instance
    fast_coding = FastCodingUI()
    
    print("⚡ Fast Coding MCP Features:")
    print("   • 📁 Project Templates - เทมเพลตโปรเจคพร้อมใช้งาน")
    print("   • 🔧 Code Generator - สร้างโค้ดจาก patterns")
    print("   • 📝 Code Snippets - ชุดโค้ดสำเร็จ")
    print("   • 🚀 Quick Project Setup - สร้างโปรเจคใน 1 คลิก")
    print("   • 🎯 Multi-Language Support - รองรับหลายภาษา")
    print("   • 📊 Project Management - จัดการโปรเจคง่ายๆ")
    print("   • 🔨 Build & Run - Build และ run โปรเจคอัตโนมัติ")
    print("   • 💾 Auto-Configuration - ตั้งค่าโปรเจคอัตโนมัติ")
    print("   • 🎨 Modern UI - หน้าตาที่ทันสมัย")
    print("   • 📈 Smart Templates - เทมเพลตอัจฉริยะ")
    print()
    
    print("🎯 รองรับภาษาและเฟรมเวิร์ค:")
    print("   • 🐍 Python - FastAPI, Flask, Django")
    print("   • ⚛️ JavaScript - React, Vue, Express")
    print("   • 🔷 TypeScript - React, Vue, Node.js")
    print("   • 🐳 Docker - Containerized apps")
    print("   • 🌐 Web Applications - Full-stack")
    print("   • 📱 Mobile Apps - React Native")
    print("   • 🤖 AI/ML Projects - TensorFlow, PyTorch")
    print()
    
    print("📂 Templates Directory: D:/MCP_System/fast_coding_templates")
    print("📝 Snippets Directory: D:/MCP_System/code_snippets")
    print("📁 Projects Directory: D:/MCP_System/fast_projects")
    print()
    print("🌐 Fast Coding MCP will be available at: http://localhost:8574")
    print()
    print("🎯 Access from Ultimate IDE: http://localhost:8568")
    print("🎯 Direct access: http://localhost:8574")
    print()
    print("Press Ctrl+C to stop...")
    
    try:
        fast_coding.run(host="0.0.0.0", port=8574)
    except KeyboardInterrupt:
        print("\n👋 Fast Coding MCP Tools stopped")
    except Exception as e:
        print(f"❌ Error starting Fast Coding MCP Tools: {e}")

if __name__ == "__main__":
    main()
