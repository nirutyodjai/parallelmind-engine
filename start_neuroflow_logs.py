#!/usr/bin/env python3
"""
Neuroflow Log Tools Launcher for Ultimate IDE
ระบบจัดการและวิเคราะห์ Application Logs สำหรับ Neuroflow AI
"""

import sys
import os
from pathlib import Path

# Add current directory to path
sys.path.append(str(Path(__file__).parent))

from neuroflow_log_ui import NeuroflowLogUI

def main():
    """เริ่ม Neuroflow Log Tools"""
    print("🧠 Starting Neuroflow Log Tools...")
    print("📊 ระบบจัดการและวิเคราะห์ Application Logs สำหรับ Neuroflow AI")
    print("=" * 60)
    
    # Create Neuroflow Log Tools instance
    neuroflow_logs = NeuroflowLogUI()
    
    print("🧠 Neuroflow Log Tools Features:")
    print("   • 📁 Log File Management - จัดการ log files ทั้งหมด")
    print("   • 📖 Log Viewer - ดูข้อมูล logs แบบ real-time")
    print("   • 🔍 Advanced Search - ค้นหาใน logs ด้วย patterns")
    print("   • 📊 Log Analysis - วิเคราะห์ errors, warnings, performance")
    print("   • 📡 Real-time Monitor - ติดตาม logs แบบ live")
    print("   • 🚨 Error Detection - ตรวจจับ error patterns")
    print("   • ⚡ Performance Analysis - วิเคราะห์ปัญหา performance")
    print("   • 🔒 Security Monitoring - ติดตาม security events")
    print("   • 📈 Statistics & Reports - สถิติและรายงาน")
    print("   • 💾 Export & Backup - ส่งออกและสำรองข้อมูล")
    print()
    
    print("📂 Log Directory: D:/Central MCP/data/Application logs/neuroflow-ai/api/mcpx2")
    print("🌐 Neuroflow Log Tools will be available at: http://localhost:8573")
    print()
    print("🎯 Access from Ultimate IDE: http://localhost:8568")
    print("🎯 Direct access: http://localhost:8573")
    print()
    print("Press Ctrl+C to stop...")
    
    try:
        neuroflow_logs.run(host="0.0.0.0", port=8573)
    except KeyboardInterrupt:
        print("\n👋 Neuroflow Log Tools stopped")
    except Exception as e:
        print(f"❌ Error starting Neuroflow Log Tools: {e}")

if __name__ == "__main__":
    main()
