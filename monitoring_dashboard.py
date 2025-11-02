#!/usr/bin/env python3
"""
📊 Real-time Monitoring Dashboard - ParallelMind Engine
======================================================
Real-time monitoring and visualization dashboard
"""

import asyncio
import aiohttp
from aiohttp import web, web_ws
import json
import time
from datetime import datetime, timedelta
from typing import Dict, List, Any
import psutil
import logging
import weakref

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MonitoringDashboard:
    """Real-time monitoring dashboard for ParallelMind Engine"""
    
    def __init__(self, port: int = 8590):
        self.port = port
        self.app = web.Application()
        self.websockets = weakref.WeakSet()
        
        # Monitoring data
        self.metrics_history = {
            "timestamps": [],
            "requests_per_second": [],
            "response_times": [],
            "memory_usage": [],
            "cpu_usage": [],
            "active_connections": [],
            "error_rates": []
        }
        
        # Current metrics
        self.current_metrics = {
            "total_requests": 0,
            "successful_requests": 0,
            "failed_requests": 0,
            "active_connections": 0,
            "average_response_time": 0.0,
            "requests_per_second": 0.0,
            "memory_usage_mb": 0.0,
            "cpu_usage_percent": 0.0,
            "uptime_seconds": 0,
            "last_updated": datetime.now().isoformat()
        }
        
        # System info
        self.system_info = {
            "python_version": f"{psutil.sys.version_info.major}.{psutil.sys.version_info.minor}",
            "cpu_count": psutil.cpu_count(),
            "memory_total_gb": psutil.virtual_memory().total / (1024**3),
            "platform": psutil.sys.platform,
            "hostname": psutil.sys.platform
        }
        
        self.start_time = time.time()
        self.setup_routes()
    
    def setup_routes(self):
        """Setup web routes"""
        # Static files and dashboard
        self.app.router.add_get('/', self.dashboard_handler)
        self.app.router.add_get('/api/metrics', self.metrics_handler)
        self.app.router.add_get('/api/system', self.system_handler)
        self.app.router.add_get('/api/history', self.history_handler)
        self.app.router.add_get('/ws', self.websocket_handler)
        
        # Health check
        self.app.router.add_get('/health', self.health_handler)
    
    async def dashboard_handler(self, request):
        """Serve dashboard HTML"""
        html_content = self.get_dashboard_html()
        return web.Response(text=html_content, content_type='text/html')
    
    async def metrics_handler(self, request):
        """API endpoint for current metrics"""
        return web.json_response(self.current_metrics)
    
    async def system_handler(self, request):
        """API endpoint for system information"""
        return web.json_response(self.system_info)
    
    async def history_handler(self, request):
        """API endpoint for metrics history"""
        return web.json_response(self.metrics_history)
    
    async def health_handler(self, request):
        """Health check endpoint"""
        return web.json_response({"status": "healthy", "timestamp": datetime.now().isoformat()})
    
    async def websocket_handler(self, request):
        """WebSocket handler for real-time updates"""
        ws = web.WebSocketResponse()
        await ws.prepare(request)
        
        self.websockets.add(ws)
        logger.info("New WebSocket connection established")
        
        try:
            async for msg in ws:
                if msg.type == web_ws.WSMsgType.TEXT:
                    data = json.loads(msg.data)
                    if data.get('type') == 'ping':
                        await ws.send_str(json.dumps({'type': 'pong'}))
                elif msg.type == web_ws.WSMsgType.ERROR:
                    logger.error(f'WebSocket error: {ws.exception()}')
        except Exception as e:
            logger.error(f"WebSocket error: {str(e)}")
        finally:
            logger.info("WebSocket connection closed")
        
        return ws
    
    async def broadcast_metrics(self):
        """Broadcast current metrics to all connected WebSockets"""
        if not self.websockets:
            return
        
        message = json.dumps({
            'type': 'metrics_update',
            'data': self.current_metrics,
            'history': {
                'timestamps': self.metrics_history['timestamps'][-20:],  # Last 20 points
                'requests_per_second': self.metrics_history['requests_per_second'][-20:],
                'response_times': self.metrics_history['response_times'][-20:],
                'memory_usage': self.metrics_history['memory_usage'][-20:],
                'cpu_usage': self.metrics_history['cpu_usage'][-20:]
            }
        })
        
        # Send to all connected WebSockets
        disconnected = []
        for ws in self.websockets:
            try:
                await ws.send_str(message)
            except Exception as e:
                logger.warning(f"Failed to send to WebSocket: {str(e)}")
                disconnected.append(ws)
        
        # Remove disconnected WebSockets
        for ws in disconnected:
            self.websockets.discard(ws)
    
    def update_metrics(self, metrics: Dict[str, Any]):
        """Update current metrics and history"""
        current_time = datetime.now()
        
        # Update current metrics
        self.current_metrics.update(metrics)
        self.current_metrics["uptime_seconds"] = int(time.time() - self.start_time)
        self.current_metrics["last_updated"] = current_time.isoformat()
        
        # Update history
        self.metrics_history["timestamps"].append(current_time.isoformat())
        self.metrics_history["requests_per_second"].append(metrics.get("requests_per_second", 0))
        self.metrics_history["response_times"].append(metrics.get("average_response_time", 0))
        self.metrics_history["memory_usage"].append(metrics.get("memory_usage_mb", 0))
        self.metrics_history["cpu_usage"].append(metrics.get("cpu_usage_percent", 0))
        self.metrics_history["active_connections"].append(metrics.get("active_connections", 0))
        
        # Calculate error rate
        total = metrics.get("total_requests", 1)
        failed = metrics.get("failed_requests", 0)
        error_rate = (failed / total) * 100 if total > 0 else 0
        self.metrics_history["error_rates"].append(error_rate)
        
        # Keep only last 100 data points
        max_history = 100
        for key in self.metrics_history:
            if len(self.metrics_history[key]) > max_history:
                self.metrics_history[key] = self.metrics_history[key][-max_history:]
    
    def get_dashboard_html(self) -> str:
        """Generate dashboard HTML"""
        return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ParallelMind Engine - Monitoring Dashboard</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #333;
            min-height: 100vh;
        }
        
        .header {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            padding: 1rem 2rem;
            box-shadow: 0 2px 20px rgba(0,0,0,0.1);
            position: sticky;
            top: 0;
            z-index: 100;
        }
        
        .header h1 {
            color: #4a5568;
            font-size: 2rem;
            font-weight: 700;
        }
        
        .header .subtitle {
            color: #718096;
            font-size: 1rem;
            margin-top: 0.25rem;
        }
        
        .status-indicator {
            display: inline-block;
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: #48bb78;
            margin-right: 8px;
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0% { opacity: 1; }
            50% { opacity: 0.5; }
            100% { opacity: 1; }
        }
        
        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 2rem;
        }
        
        .metrics-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
            margin-bottom: 2rem;
        }
        
        .metric-card {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            transition: transform 0.2s ease;
        }
        
        .metric-card:hover {
            transform: translateY(-2px);
        }
        
        .metric-title {
            font-size: 0.875rem;
            font-weight: 600;
            color: #718096;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 0.5rem;
        }
        
        .metric-value {
            font-size: 2rem;
            font-weight: 700;
            color: #2d3748;
            margin-bottom: 0.25rem;
        }
        
        .metric-unit {
            font-size: 0.875rem;
            color: #a0aec0;
        }
        
        .charts-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 2rem;
        }
        
        .chart-card {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        }
        
        .chart-title {
            font-size: 1.125rem;
            font-weight: 600;
            color: #2d3748;
            margin-bottom: 1rem;
        }
        
        .chart-container {
            position: relative;
            height: 300px;
        }
        
        .connection-status {
            position: fixed;
            top: 20px;
            right: 20px;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-size: 0.875rem;
            font-weight: 600;
            z-index: 1000;
        }
        
        .connected {
            background: #48bb78;
            color: white;
        }
        
        .disconnected {
            background: #f56565;
            color: white;
        }
        
        .footer {
            text-align: center;
            padding: 2rem;
            color: rgba(255, 255, 255, 0.8);
            font-size: 0.875rem;
        }
    </style>
</head>
<body>
    <div class="connection-status" id="connectionStatus">Connecting...</div>
    
    <header class="header">
        <h1>🧠 ParallelMind Engine</h1>
        <p class="subtitle">
            <span class="status-indicator"></span>
            Real-time Monitoring Dashboard - Revolutionary AI Reasoning System
        </p>
    </header>
    
    <div class="container">
        <div class="metrics-grid">
            <div class="metric-card">
                <div class="metric-title">Requests/Second</div>
                <div class="metric-value" id="rpsValue">0</div>
                <div class="metric-unit">req/s</div>
            </div>
            
            <div class="metric-card">
                <div class="metric-title">Response Time</div>
                <div class="metric-value" id="responseTimeValue">0</div>
                <div class="metric-unit">ms</div>
            </div>
            
            <div class="metric-card">
                <div class="metric-title">Total Requests</div>
                <div class="metric-value" id="totalRequestsValue">0</div>
                <div class="metric-unit">requests</div>
            </div>
            
            <div class="metric-card">
                <div class="metric-title">Success Rate</div>
                <div class="metric-value" id="successRateValue">100</div>
                <div class="metric-unit">%</div>
            </div>
            
            <div class="metric-card">
                <div class="metric-title">Memory Usage</div>
                <div class="metric-value" id="memoryValue">0</div>
                <div class="metric-unit">MB</div>
            </div>
            
            <div class="metric-card">
                <div class="metric-title">CPU Usage</div>
                <div class="metric-value" id="cpuValue">0</div>
                <div class="metric-unit">%</div>
            </div>
        </div>
        
        <div class="charts-grid">
            <div class="chart-card">
                <div class="chart-title">📈 Requests per Second</div>
                <div class="chart-container">
                    <canvas id="rpsChart"></canvas>
                </div>
            </div>
            
            <div class="chart-card">
                <div class="chart-title">⏱️ Response Time</div>
                <div class="chart-container">
                    <canvas id="responseTimeChart"></canvas>
                </div>
            </div>
            
            <div class="chart-card">
                <div class="chart-title">💾 Memory Usage</div>
                <div class="chart-container">
                    <canvas id="memoryChart"></canvas>
                </div>
            </div>
            
            <div class="chart-card">
                <div class="chart-title">🖥️ CPU Usage</div>
                <div class="chart-container">
                    <canvas id="cpuChart"></canvas>
                </div>
            </div>
        </div>
    </div>
    
    <footer class="footer">
        <p>ParallelMind Engine v2.0.0 - Where Parallel Thinking Becomes Reality 🧠⚡</p>
    </footer>
    
    <script>
        // WebSocket connection
        let ws;
        let charts = {};
        
        function connectWebSocket() {
            const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
            ws = new WebSocket(`${protocol}//${window.location.host}/ws`);
            
            ws.onopen = function() {
                document.getElementById('connectionStatus').textContent = 'Connected';
                document.getElementById('connectionStatus').className = 'connection-status connected';
            };
            
            ws.onmessage = function(event) {
                const message = JSON.parse(event.data);
                if (message.type === 'metrics_update') {
                    updateMetrics(message.data);
                    updateCharts(message.history);
                }
            };
            
            ws.onclose = function() {
                document.getElementById('connectionStatus').textContent = 'Disconnected';
                document.getElementById('connectionStatus').className = 'connection-status disconnected';
                // Reconnect after 3 seconds
                setTimeout(connectWebSocket, 3000);
            };
            
            ws.onerror = function(error) {
                console.error('WebSocket error:', error);
            };
        }
        
        function updateMetrics(metrics) {
            document.getElementById('rpsValue').textContent = metrics.requests_per_second.toFixed(1);
            document.getElementById('responseTimeValue').textContent = (metrics.average_response_time * 1000).toFixed(0);
            document.getElementById('totalRequestsValue').textContent = metrics.total_requests.toLocaleString();
            
            const successRate = metrics.total_requests > 0 ? 
                ((metrics.successful_requests / metrics.total_requests) * 100) : 100;
            document.getElementById('successRateValue').textContent = successRate.toFixed(1);
            
            document.getElementById('memoryValue').textContent = metrics.memory_usage_mb.toFixed(0);
            document.getElementById('cpuValue').textContent = metrics.cpu_usage_percent.toFixed(1);
        }
        
        function updateCharts(history) {
            const labels = history.timestamps.map(ts => new Date(ts).toLocaleTimeString());
            
            // Update RPS chart
            charts.rps.data.labels = labels;
            charts.rps.data.datasets[0].data = history.requests_per_second;
            charts.rps.update('none');
            
            // Update Response Time chart
            charts.responseTime.data.labels = labels;
            charts.responseTime.data.datasets[0].data = history.response_times.map(t => t * 1000);
            charts.responseTime.update('none');
            
            // Update Memory chart
            charts.memory.data.labels = labels;
            charts.memory.data.datasets[0].data = history.memory_usage;
            charts.memory.update('none');
            
            // Update CPU chart
            charts.cpu.data.labels = labels;
            charts.cpu.data.datasets[0].data = history.cpu_usage;
            charts.cpu.update('none');
        }
        
        function initCharts() {
            const chartOptions = {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: {
                        beginAtZero: true,
                        grid: {
                            color: 'rgba(0,0,0,0.1)'
                        }
                    },
                    x: {
                        grid: {
                            color: 'rgba(0,0,0,0.1)'
                        }
                    }
                },
                plugins: {
                    legend: {
                        display: false
                    }
                },
                animation: {
                    duration: 0
                }
            };
            
            // RPS Chart
            charts.rps = new Chart(document.getElementById('rpsChart'), {
                type: 'line',
                data: {
                    labels: [],
                    datasets: [{
                        data: [],
                        borderColor: '#4299e1',
                        backgroundColor: 'rgba(66, 153, 225, 0.1)',
                        fill: true,
                        tension: 0.4
                    }]
                },
                options: chartOptions
            });
            
            // Response Time Chart
            charts.responseTime = new Chart(document.getElementById('responseTimeChart'), {
                type: 'line',
                data: {
                    labels: [],
                    datasets: [{
                        data: [],
                        borderColor: '#48bb78',
                        backgroundColor: 'rgba(72, 187, 120, 0.1)',
                        fill: true,
                        tension: 0.4
                    }]
                },
                options: chartOptions
            });
            
            // Memory Chart
            charts.memory = new Chart(document.getElementById('memoryChart'), {
                type: 'line',
                data: {
                    labels: [],
                    datasets: [{
                        data: [],
                        borderColor: '#ed8936',
                        backgroundColor: 'rgba(237, 137, 54, 0.1)',
                        fill: true,
                        tension: 0.4
                    }]
                },
                options: chartOptions
            });
            
            // CPU Chart
            charts.cpu = new Chart(document.getElementById('cpuChart'), {
                type: 'line',
                data: {
                    labels: [],
                    datasets: [{
                        data: [],
                        borderColor: '#9f7aea',
                        backgroundColor: 'rgba(159, 122, 234, 0.1)',
                        fill: true,
                        tension: 0.4
                    }]
                },
                options: chartOptions
            });
        }
        
        // Initialize
        document.addEventListener('DOMContentLoaded', function() {
            initCharts();
            connectWebSocket();
        });
    </script>
</body>
</html>
        """
    
    async def start_monitoring_loop(self):
        """Start the monitoring loop"""
        while True:
            try:
                # Collect system metrics
                memory = psutil.virtual_memory()
                cpu_percent = psutil.cpu_percent(interval=1)
                
                # Update metrics (these would come from the actual ParallelMind Engine)
                sample_metrics = {
                    "total_requests": self.current_metrics["total_requests"] + 1,
                    "successful_requests": self.current_metrics["successful_requests"] + 1,
                    "failed_requests": self.current_metrics["failed_requests"],
                    "active_connections": len(self.websockets),
                    "average_response_time": 2.04,  # Sample data
                    "requests_per_second": 4.8,    # Sample data
                    "memory_usage_mb": memory.used / (1024 * 1024),
                    "cpu_usage_percent": cpu_percent
                }
                
                self.update_metrics(sample_metrics)
                await self.broadcast_metrics()
                
                # Wait 2 seconds before next update
                await asyncio.sleep(2)
                
            except Exception as e:
                logger.error(f"Monitoring loop error: {str(e)}")
                await asyncio.sleep(5)
    
    async def start_server(self):
        """Start the monitoring dashboard server"""
        runner = web.AppRunner(self.app)
        await runner.setup()
        
        site = web.TCPSite(runner, '0.0.0.0', self.port)
        await site.start()
        
        logger.info(f"🚀 Monitoring Dashboard started on http://localhost:{self.port}")
        
        # Start monitoring loop
        monitoring_task = asyncio.create_task(self.start_monitoring_loop())
        
        try:
            await monitoring_task
        except KeyboardInterrupt:
            logger.info("Shutting down monitoring dashboard...")
        finally:
            await runner.cleanup()

# Example usage
async def main():
    """Main function to run the monitoring dashboard"""
    dashboard = MonitoringDashboard(port=8590)
    await dashboard.start_server()

if __name__ == "__main__":
    asyncio.run(main())
