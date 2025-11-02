#!/usr/bin/env python3
"""
🧠 Advanced Reasoning Engine - Enhanced ParallelMind Features
============================================================
New reasoning modes and advanced capabilities
"""

import asyncio
import aiohttp
import time
import json
from datetime import datetime
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from enum import Enum
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ReasoningMode(Enum):
    """Advanced reasoning modes"""
    PARALLEL = "parallel"           # Original parallel reasoning
    SEQUENTIAL = "sequential"       # Traditional sequential
    HYBRID = "hybrid"              # Mix of parallel and sequential
    ADAPTIVE = "adaptive"          # AI decides best approach
    CHAIN_OF_THOUGHT = "chain"     # Step-by-step reasoning
    TREE_SEARCH = "tree"           # Tree-based exploration
    ENSEMBLE = "ensemble"          # Multiple approaches combined

class PriorityLevel(Enum):
    """Task priority levels"""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    BACKGROUND = "background"

@dataclass
class ReasoningTask:
    """Enhanced task structure"""
    id: str
    request: str
    mode: ReasoningMode
    priority: PriorityLevel
    ai_user: str
    context: Dict[str, Any] = None
    dependencies: List[str] = None
    timeout: int = 30
    retry_count: int = 0
    max_retries: int = 3
    created_at: datetime = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()
        if self.context is None:
            self.context = {}
        if self.dependencies is None:
            self.dependencies = []

class AdvancedReasoningEngine:
    """Enhanced ParallelMind Engine with advanced features"""
    
    def __init__(self):
        self.base_url = "http://localhost:8575"
        self.session = None
        self.task_queue = asyncio.Queue()
        self.active_tasks = {}
        self.completed_tasks = {}
        self.performance_metrics = {
            "total_processed": 0,
            "success_rate": 0.0,
            "average_response_time": 0.0,
            "mode_performance": {},
            "priority_stats": {}
        }
        self.reasoning_strategies = {
            ReasoningMode.PARALLEL: self._parallel_reasoning,
            ReasoningMode.SEQUENTIAL: self._sequential_reasoning,
            ReasoningMode.HYBRID: self._hybrid_reasoning,
            ReasoningMode.ADAPTIVE: self._adaptive_reasoning,
            ReasoningMode.CHAIN_OF_THOUGHT: self._chain_reasoning,
            ReasoningMode.TREE_SEARCH: self._tree_reasoning,
            ReasoningMode.ENSEMBLE: self._ensemble_reasoning
        }
        
    async def __aenter__(self):
        """Async context manager entry"""
        self.session = aiohttp.ClientSession()
        return self
        
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit"""
        if self.session:
            await self.session.close()
    
    async def process_advanced_task(self, task: ReasoningTask) -> Dict[str, Any]:
        """Process task with advanced reasoning modes"""
        start_time = time.time()
        
        try:
            # Select reasoning strategy
            strategy = self.reasoning_strategies.get(task.mode, self._parallel_reasoning)
            
            # Execute reasoning
            result = await strategy(task)
            
            # Calculate metrics
            processing_time = time.time() - start_time
            
            # Update performance metrics
            self._update_metrics(task, processing_time, True)
            
            # Store completed task
            self.completed_tasks[task.id] = {
                "task": task,
                "result": result,
                "processing_time": processing_time,
                "completed_at": datetime.now()
            }
            
            return {
                "task_id": task.id,
                "status": "success",
                "result": result,
                "processing_time": processing_time,
                "mode": task.mode.value,
                "priority": task.priority.value
            }
            
        except Exception as e:
            processing_time = time.time() - start_time
            self._update_metrics(task, processing_time, False)
            
            logger.error(f"Task {task.id} failed: {str(e)}")
            
            return {
                "task_id": task.id,
                "status": "error",
                "error": str(e),
                "processing_time": processing_time,
                "mode": task.mode.value,
                "priority": task.priority.value
            }
    
    async def _parallel_reasoning(self, task: ReasoningTask) -> Dict[str, Any]:
        """Original parallel reasoning mode"""
        payload = {
            "request": task.request,
            "ai_user": task.ai_user,
            "type": "parallel_reasoning",
            "context": task.context
        }
        
        async with self.session.post(f"{self.base_url}/api/process", json=payload) as response:
            return await response.json()
    
    async def _sequential_reasoning(self, task: ReasoningTask) -> Dict[str, Any]:
        """Sequential reasoning mode"""
        payload = {
            "request": task.request,
            "ai_user": task.ai_user,
            "type": "sequential_reasoning",
            "context": task.context
        }
        
        async with self.session.post(f"{self.base_url}/api/process", json=payload) as response:
            return await response.json()
    
    async def _hybrid_reasoning(self, task: ReasoningTask) -> Dict[str, Any]:
        """Hybrid reasoning - combines parallel and sequential"""
        # First phase: Parallel exploration
        parallel_task = ReasoningTask(
            id=f"{task.id}_parallel",
            request=f"Explore multiple approaches: {task.request}",
            mode=ReasoningMode.PARALLEL,
            priority=task.priority,
            ai_user=task.ai_user,
            context=task.context
        )
        
        parallel_result = await self._parallel_reasoning(parallel_task)
        
        # Second phase: Sequential refinement
        sequential_task = ReasoningTask(
            id=f"{task.id}_sequential",
            request=f"Refine and synthesize: {task.request}",
            mode=ReasoningMode.SEQUENTIAL,
            priority=task.priority,
            ai_user=task.ai_user,
            context={**task.context, "parallel_insights": parallel_result}
        )
        
        sequential_result = await self._sequential_reasoning(sequential_task)
        
        return {
            "hybrid_result": sequential_result,
            "parallel_exploration": parallel_result,
            "approach": "hybrid_reasoning"
        }
    
    async def _adaptive_reasoning(self, task: ReasoningTask) -> Dict[str, Any]:
        """Adaptive reasoning - AI chooses best approach"""
        # Analyze task complexity to choose mode
        complexity_score = await self._analyze_task_complexity(task)
        
        if complexity_score > 0.8:
            chosen_mode = ReasoningMode.HYBRID
        elif complexity_score > 0.6:
            chosen_mode = ReasoningMode.PARALLEL
        elif complexity_score > 0.4:
            chosen_mode = ReasoningMode.CHAIN_OF_THOUGHT
        else:
            chosen_mode = ReasoningMode.SEQUENTIAL
        
        # Execute with chosen mode
        adapted_task = ReasoningTask(
            id=task.id,
            request=task.request,
            mode=chosen_mode,
            priority=task.priority,
            ai_user=task.ai_user,
            context=task.context
        )
        
        result = await self.reasoning_strategies[chosen_mode](adapted_task)
        
        return {
            "adaptive_result": result,
            "chosen_mode": chosen_mode.value,
            "complexity_score": complexity_score,
            "approach": "adaptive_reasoning"
        }
    
    async def _chain_reasoning(self, task: ReasoningTask) -> Dict[str, Any]:
        """Chain of thought reasoning"""
        steps = await self._break_into_steps(task.request)
        results = []
        
        for i, step in enumerate(steps):
            step_task = ReasoningTask(
                id=f"{task.id}_step_{i}",
                request=step,
                mode=ReasoningMode.SEQUENTIAL,
                priority=task.priority,
                ai_user=task.ai_user,
                context={**task.context, "previous_steps": results}
            )
            
            step_result = await self._sequential_reasoning(step_task)
            results.append({
                "step": i + 1,
                "question": step,
                "result": step_result
            })
        
        return {
            "chain_result": results[-1]["result"] if results else None,
            "reasoning_chain": results,
            "approach": "chain_of_thought"
        }
    
    async def _tree_reasoning(self, task: ReasoningTask) -> Dict[str, Any]:
        """Tree search reasoning"""
        # Generate multiple approaches
        approaches = await self._generate_approaches(task.request)
        
        # Explore each approach in parallel
        exploration_tasks = []
        for i, approach in enumerate(approaches):
            explore_task = ReasoningTask(
                id=f"{task.id}_branch_{i}",
                request=f"Explore approach: {approach} for {task.request}",
                mode=ReasoningMode.PARALLEL,
                priority=task.priority,
                ai_user=task.ai_user,
                context=task.context
            )
            exploration_tasks.append(self._parallel_reasoning(explore_task))
        
        # Execute all explorations
        exploration_results = await asyncio.gather(*exploration_tasks, return_exceptions=True)
        
        # Select best result
        best_result = await self._select_best_result(exploration_results)
        
        return {
            "tree_result": best_result,
            "explored_branches": exploration_results,
            "approach": "tree_search"
        }
    
    async def _ensemble_reasoning(self, task: ReasoningTask) -> Dict[str, Any]:
        """Ensemble reasoning - multiple modes combined"""
        modes = [ReasoningMode.PARALLEL, ReasoningMode.SEQUENTIAL, ReasoningMode.CHAIN_OF_THOUGHT]
        
        ensemble_tasks = []
        for mode in modes:
            ensemble_task = ReasoningTask(
                id=f"{task.id}_{mode.value}",
                request=task.request,
                mode=mode,
                priority=task.priority,
                ai_user=task.ai_user,
                context=task.context
            )
            ensemble_tasks.append(self.reasoning_strategies[mode](ensemble_task))
        
        # Execute all modes
        ensemble_results = await asyncio.gather(*ensemble_tasks, return_exceptions=True)
        
        # Combine results
        combined_result = await self._combine_ensemble_results(ensemble_results)
        
        return {
            "ensemble_result": combined_result,
            "individual_results": ensemble_results,
            "approach": "ensemble_reasoning"
        }
    
    async def _analyze_task_complexity(self, task: ReasoningTask) -> float:
        """Analyze task complexity to choose reasoning mode"""
        # Simple heuristics for complexity analysis
        complexity_indicators = [
            len(task.request.split()) > 50,  # Long request
            "analyze" in task.request.lower(),
            "compare" in task.request.lower(),
            "multiple" in task.request.lower(),
            "complex" in task.request.lower(),
            "step" in task.request.lower(),
            len(task.context) > 5,  # Rich context
        ]
        
        return sum(complexity_indicators) / len(complexity_indicators)
    
    async def _break_into_steps(self, request: str) -> List[str]:
        """Break complex request into reasoning steps"""
        # Simple step breakdown (could be enhanced with AI)
        if "analyze" in request.lower():
            return [
                f"Understand the problem: {request}",
                f"Identify key components in: {request}",
                f"Analyze relationships in: {request}",
                f"Draw conclusions for: {request}"
            ]
        elif "compare" in request.lower():
            return [
                f"Identify items to compare in: {request}",
                f"List similarities for: {request}",
                f"List differences for: {request}",
                f"Make comparison conclusion: {request}"
            ]
        else:
            return [
                f"Break down the problem: {request}",
                f"Solve step by step: {request}",
                f"Verify the solution: {request}"
            ]
    
    async def _generate_approaches(self, request: str) -> List[str]:
        """Generate different approaches for tree search"""
        return [
            f"Analytical approach: {request}",
            f"Creative approach: {request}",
            f"Systematic approach: {request}",
            f"Intuitive approach: {request}"
        ]
    
    async def _select_best_result(self, results: List[Any]) -> Any:
        """Select best result from multiple options"""
        # Simple selection (could be enhanced with AI evaluation)
        valid_results = [r for r in results if not isinstance(r, Exception)]
        return valid_results[0] if valid_results else None
    
    async def _combine_ensemble_results(self, results: List[Any]) -> Dict[str, Any]:
        """Combine results from ensemble reasoning"""
        valid_results = [r for r in results if not isinstance(r, Exception)]
        
        return {
            "consensus": "Combined insights from multiple reasoning approaches",
            "confidence": len(valid_results) / len(results),
            "primary_result": valid_results[0] if valid_results else None,
            "supporting_evidence": valid_results[1:] if len(valid_results) > 1 else []
        }
    
    def _update_metrics(self, task: ReasoningTask, processing_time: float, success: bool):
        """Update performance metrics"""
        self.performance_metrics["total_processed"] += 1
        
        # Update success rate
        if success:
            current_success = self.performance_metrics["success_rate"] * (self.performance_metrics["total_processed"] - 1)
            self.performance_metrics["success_rate"] = (current_success + 1) / self.performance_metrics["total_processed"]
        else:
            current_success = self.performance_metrics["success_rate"] * (self.performance_metrics["total_processed"] - 1)
            self.performance_metrics["success_rate"] = current_success / self.performance_metrics["total_processed"]
        
        # Update average response time
        current_avg = self.performance_metrics["average_response_time"] * (self.performance_metrics["total_processed"] - 1)
        self.performance_metrics["average_response_time"] = (current_avg + processing_time) / self.performance_metrics["total_processed"]
        
        # Update mode performance
        mode_key = task.mode.value
        if mode_key not in self.performance_metrics["mode_performance"]:
            self.performance_metrics["mode_performance"][mode_key] = {"count": 0, "avg_time": 0.0, "success_rate": 0.0}
        
        mode_stats = self.performance_metrics["mode_performance"][mode_key]
        mode_stats["count"] += 1
        mode_stats["avg_time"] = ((mode_stats["avg_time"] * (mode_stats["count"] - 1)) + processing_time) / mode_stats["count"]
        
        if success:
            current_mode_success = mode_stats["success_rate"] * (mode_stats["count"] - 1)
            mode_stats["success_rate"] = (current_mode_success + 1) / mode_stats["count"]
        else:
            current_mode_success = mode_stats["success_rate"] * (mode_stats["count"] - 1)
            mode_stats["success_rate"] = current_mode_success / mode_stats["count"]
    
    def get_performance_report(self) -> Dict[str, Any]:
        """Get comprehensive performance report"""
        return {
            "timestamp": datetime.now().isoformat(),
            "overall_metrics": self.performance_metrics,
            "active_tasks": len(self.active_tasks),
            "completed_tasks": len(self.completed_tasks),
            "queue_size": self.task_queue.qsize(),
            "reasoning_modes_available": [mode.value for mode in ReasoningMode],
            "priority_levels_available": [priority.value for priority in PriorityLevel]
        }

# Example usage and testing
async def test_advanced_reasoning():
    """Test advanced reasoning capabilities"""
    print("🧠 Testing Advanced Reasoning Engine")
    print("=" * 50)
    
    async with AdvancedReasoningEngine() as engine:
        # Test different reasoning modes
        test_tasks = [
            ReasoningTask(
                id="test_parallel",
                request="Analyze the benefits of parallel processing in AI systems",
                mode=ReasoningMode.PARALLEL,
                priority=PriorityLevel.HIGH,
                ai_user="Advanced Tester"
            ),
            ReasoningTask(
                id="test_adaptive",
                request="Compare different machine learning algorithms for natural language processing",
                mode=ReasoningMode.ADAPTIVE,
                priority=PriorityLevel.MEDIUM,
                ai_user="Advanced Tester"
            ),
            ReasoningTask(
                id="test_chain",
                request="Solve this step by step: How to optimize database performance?",
                mode=ReasoningMode.CHAIN_OF_THOUGHT,
                priority=PriorityLevel.HIGH,
                ai_user="Advanced Tester"
            ),
            ReasoningTask(
                id="test_ensemble",
                request="Design a scalable microservices architecture",
                mode=ReasoningMode.ENSEMBLE,
                priority=PriorityLevel.CRITICAL,
                ai_user="Advanced Tester"
            )
        ]
        
        # Process tasks
        results = []
        for task in test_tasks:
            print(f"\n🚀 Processing {task.mode.value} reasoning...")
            result = await engine.process_advanced_task(task)
            results.append(result)
            print(f"   ✅ Completed in {result['processing_time']:.2f}s")
        
        # Show performance report
        print(f"\n📊 Performance Report:")
        report = engine.get_performance_report()
        print(f"   • Total processed: {report['overall_metrics']['total_processed']}")
        print(f"   • Success rate: {report['overall_metrics']['success_rate']:.1%}")
        print(f"   • Average time: {report['overall_metrics']['average_response_time']:.2f}s")
        
        print(f"\n🎯 Mode Performance:")
        for mode, stats in report['overall_metrics']['mode_performance'].items():
            print(f"   • {mode}: {stats['count']} tasks, {stats['avg_time']:.2f}s avg, {stats['success_rate']:.1%} success")

if __name__ == "__main__":
    asyncio.run(test_advanced_reasoning())
