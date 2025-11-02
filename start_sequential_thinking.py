#!/usr/bin/env python3
"""
Sequential Thinking MCP Tools Launcher for Ultimate IDE
ระบบคิดเชิงลำดับและการแก้ปัญหาแบบ step-by-step
"""

import sys
import os
from pathlib import Path

# Add current directory to path
sys.path.append(str(Path(__file__).parent))

from sequential_thinking_ui import SequentialThinkingUI

def main():
    """เริ่ม Sequential Thinking MCP Tools"""
    print("🧠 Starting Sequential Thinking MCP Tools...")
    print("🎯 ระบบคิดเชิงลำดับและการแก้ปัญหาแบบ step-by-step สำหรับ Ultimate IDE")
    print("=" * 60)
    
    # Create Sequential Thinking MCP instance
    sequential_thinking = SequentialThinkingUI()
    
    print("🧠 Sequential Thinking MCP Features:")
    print("   • 📋 Thinking Strategies - กลยุทธ์การคิด 8 แบบ")
    print("   • 🧠 Step-by-Step Analysis - วิเคราะห์ปัญหาแบบลำดับขั้น")
    print("   • 💡 Insight Generation - สร้างข้อมูลเชิงลึก")
    print("   • 📝 Note Taking - จดบันทึกความคิด")
    print("   • 📊 Progress Tracking - ติดตามความคืบหน้า")
    print("   • 🎯 Session Management - จัดการ session การคิด")
    print("   • 📄 Summary Generation - สร้างสรุปอัตโนมัติ")
    print("   • 💾 Export & Backup - ส่งออกข้อมูล (Markdown, JSON)")
    print("   • 🎨 Modern UI - หน้าตาที่ทันสมัย")
    print("   • 📈 Analytics - วิเคราะห์การคิดและข้อมูลเชิงลึก")
    print()
    
    print("🎯 กลยุทธ์การคิดที่รองรับ:")
    print("   • 🔍 Problem Decomposition - แยกปัญหาเป็นส่วนย่อย")
    print("   • 🎯 Root Cause Analysis - หาสาเหตุของปัญหา")
    print("   • 🎨 Design Thinking - กระบวนการคิดเชิงออกแบบ")
    print("   • 🔬 Scientific Method - กระบวนการทางวิทยาศาสตร์")
    print("   • 🌐 Systems Thinking - มองภาพรวมและความสัมพันธ์")
    print("   • 🧠 Critical Thinking - การคิดอย่างมีวิจารณญาณ")
    print("   • 💡 Creative Problem Solving - การแก้ปัญหาสร้างสรรค์")
    print("   • ⚖️ Decision Making Framework - กรอบการตัดสินใจ")
    print()
    
    print("📂 Directories:")
    print("   🧠 Sessions: D:/MCP_System/sequential_thinking_sessions")
    print("   📋 Templates: D:/MCP_System/thinking_templates")
    print("   🎯 Strategies: D:/MCP_System/thinking_strategies")
    print()
    print("🌐 Sequential Thinking MCP will be available at: http://localhost:8575")
    print()
    print("🎯 Access from Ultimate IDE: http://localhost:8569")
    print("🎯 Direct access: http://localhost:8575")
    print()
    print("Press Ctrl+C to stop...")
    
    try:
        sequential_thinking.run(host="0.0.0.0", port=8575)
    except KeyboardInterrupt:
        print("\n👋 Sequential Thinking MCP Tools stopped")
    except Exception as e:
        print(f"❌ Error starting Sequential Thinking MCP Tools: {e}")

if __name__ == "__main__":
    main()
