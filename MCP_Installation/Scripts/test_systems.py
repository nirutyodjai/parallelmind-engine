#!/usr/bin/env python3
"""
🧪 Test MCP Systems - ทดสอบ MCP Systems ทั้งหมด
================================================================
"""

import asyncio
import aiohttp
import time

class MCPSystemTester:
    """ระบบทดสอบ MCP Systems"""
    
    def __init__(self):
        self.systems = {
            "Fast Coding MCP": "http://localhost:8574",
            "Sequential Thinking MCP": "http://localhost:8575", 
            "Neuroflow Logs MCP": "http://localhost:8573"
        }
        
        self.test_results = []
    
    async def test_all_systems(self):
        """ทดสอบระบบทั้งหมด"""
        
        print("🧪 Testing All MCP Systems")
        print("=" * 50)
        
        # ทดสอบการเชื่อมต่อ
        await self.test_connectivity()
        
        # ทดสอบ API
        await self.test_apis()
        
        # ทดสอบประสิทธิภาพ
        await self.test_performance()
        
        # สรุปผล
        self.summarize_results()
    
    async def test_connectivity(self):
        """ทดสอบการเชื่อมต่อ"""
        
        print("🔗 Testing Connectivity...")
        
        for system_name, url in self.systems.items():
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(f"{url}/", timeout=5) as response:
                        if response.status == 200:
                            print(f"  ✅ {system_name}: Connected")
                            self.record_result(f"{system_name}_connectivity", True, "Connected")
                        else:
                            print(f"  ❌ {system_name}: HTTP {response.status}")
                            self.record_result(f"{system_name}_connectivity", False, f"HTTP {response.status}")
            except Exception as e:
                print(f"  ❌ {system_name}: {str(e)}")
                self.record_result(f"{system_name}_connectivity", False, str(e))
    
    async def test_apis(self):
        """ทดสอบ API"""
        
        print("\n🛠️ Testing APIs...")
        
        for system_name, url in self.systems.items():
            # ทดสอบ status API
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(f"{url}/api/status", timeout=5) as response:
                        if response.status == 200:
                            data = await response.json()
                            print(f"  ✅ {system_name} Status API: Working")
                            self.record_result(f"{system_name}_status_api", True, "Working")
                        else:
                            print(f"  ❌ {system_name} Status API: HTTP {response.status}")
                            self.record_result(f"{system_name}_status_api", False, f"HTTP {response.status}")
            except Exception as e:
                print(f"  ❌ {system_name} Status API: {str(e)}")
                self.record_result(f"{system_name}_status_api", False, str(e))
            
            # ทดสอบ process API
            try:
                async with aiohttp.ClientSession() as session:
                    payload = {"request": "test", "type": "installation_test"}
                    async with session.post(f"{url}/api/process", json=payload, timeout=5) as response:
                        if response.status == 200:
                            print(f"  ✅ {system_name} Process API: Working")
                            self.record_result(f"{system_name}_process_api", True, "Working")
                        else:
                            print(f"  ❌ {system_name} Process API: HTTP {response.status}")
                            self.record_result(f"{system_name}_process_api", False, f"HTTP {response.status}")
            except Exception as e:
                print(f"  ❌ {system_name} Process API: {str(e)}")
                self.record_result(f"{system_name}_process_api", False, str(e))
    
    async def test_performance(self):
        """ทดสอบประสิทธิภาพ"""
        
        print("\n⚡ Testing Performance...")
        
        for system_name, url in self.systems.items():
            try:
                # ทดสอบเวลาตอบสนอง
                start_time = time.time()
                
                async with aiohttp.ClientSession() as session:
                    payload = {"request": "performance test", "type": "speed_test"}
                    async with session.post(f"{url}/api/process", json=payload, timeout=10) as response:
                        end_time = time.time()
                        response_time = end_time - start_time
                        
                        if response.status == 200:
                            print(f"  ✅ {system_name}: {response_time:.3f}s")
                            self.record_result(f"{system_name}_performance", True, f"{response_time:.3f}s")
                        else:
                            print(f"  ❌ {system_name}: HTTP {response.status}")
                            self.record_result(f"{system_name}_performance", False, f"HTTP {response.status}")
            except Exception as e:
                print(f"  ❌ {system_name}: {str(e)}")
                self.record_result(f"{system_name}_performance", False, str(e))
    
    def record_result(self, test_name: str, success: bool, message: str):
        """บันทึกผลการทดสอบ"""
        self.test_results.append({
            "test": test_name,
            "success": success,
            "message": message
        })
    
    def summarize_results(self):
        """สรุปผลการทดสอบ"""
        
        print("\n" + "=" * 50)
        print("📊 TEST SUMMARY")
        print("=" * 50)
        
        total_tests = len(self.test_results)
        passed_tests = sum(1 for r in self.test_results if r["success"])
        failed_tests = total_tests - passed_tests
        
        print(f"📈 Total Tests: {total_tests}")
        print(f"✅ Passed: {passed_tests}")
        print(f"❌ Failed: {failed_tests}")
        print(f"📊 Success Rate: {(passed_tests/total_tests)*100:.1f}%")
        
        print(f"\n📋 Detailed Results:")
        for result in self.test_results:
            status = "✅" if result["success"] else "❌"
            print(f"   {status} {result['test']}: {result['message']}")
        
        print(f"\n🎯 System Status:")
        if failed_tests == 0:
            print("🎉 All systems are working perfectly!")
        elif failed_tests <= 2:
            print("⚠️ Most systems working, minor issues detected")
        else:
            print("❌ Multiple system issues detected")
        
        print(f"\n🌐 Access Points:")
        for system_name, url in self.systems.items():
            print(f"   • {system_name}: {url}")

async def main():
    """รันการทดสอบ"""
    
    tester = MCPSystemTester()
    await tester.test_all_systems()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Test stopped by user")
    except Exception as e:
        print(f"\n❌ Test error: {e}")
