#!/usr/bin/env python3
"""
Setup script for ParallelMind Engine
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="parallelmind-engine",
    version="2.0.0",
    author="ParallelMind Engine Team",
    author_email="team@parallelmind.ai",
    description="Revolutionary Parallel Logical Reasoning System - 202 problems/second",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/parallelmind-ai/parallelmind-engine",
    project_urls={
        "Bug Tracker": "https://github.com/parallelmind-ai/parallelmind-engine/issues",
        "Documentation": "https://github.com/parallelmind-ai/parallelmind-engine/wiki",
        "Source Code": "https://github.com/parallelmind-ai/parallelmind-engine",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Distributed Computing",
    ],
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-asyncio>=0.21.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
            "coverage>=7.0.0",
        ],
        "performance": [
            "psutil>=5.9.0",
            "memory-profiler>=0.61.0",
            "line-profiler>=4.0.0",
        ],
        "research": [
            "numpy>=1.24.0",
            "pandas>=2.0.0",
            "matplotlib>=3.7.0",
            "jupyter>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "parallelmind=parallelmind_engine:main",
            "parallelmind-test=tests.test_basic:main",
            "parallelmind-benchmark=benchmarks.performance:main",
        ],
    },
    include_package_data=True,
    package_data={
        "parallelmind": [
            "config/*.json",
            "templates/*.html",
            "static/*",
        ],
    },
    keywords=[
        "artificial intelligence",
        "parallel processing",
        "logical reasoning",
        "concurrent computing",
        "AI reasoning",
        "parallel thinking",
        "cognitive computing",
        "high performance AI",
    ],
    zip_safe=False,
)
