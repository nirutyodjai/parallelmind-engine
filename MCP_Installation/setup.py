#!/usr/bin/env python3
"""
📦 MCP System Setup - ติดตั้งและตั้งค่า MCP System
================================================================
"""

from setuptools import setup, find_packages

setup(
    name="mcp-system",
    version="1.0.0",
    description="Complete MCP (Model Context Protocol) System",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="MCP Development Team",
    author_email="dev@mcp-system.com",
    url="https://github.com/mcp-system/mcp-system",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "fastapi>=0.104.1",
        "uvicorn[standard]>=0.24.0",
        "aiohttp>=3.9.1",
        "pydantic>=2.5.0",
        "python-multipart>=0.0.6",
        "psutil>=5.9.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-asyncio>=0.21.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "mcp-manager=Tools.mcp_manager:main",
            "mcp-install=Scripts.install:main",
            "mcp-start=Scripts.start_all:start_all_mcp_systems",
            "mcp-test=Scripts.test_systems:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.md", "*.txt", "*.json", "*.yaml", "*.yml"],
    },
    zip_safe=False,
)
