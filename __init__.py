from setuptools import setup, find_packages

setup(
    name="a2a-commons",
    version="0.1.0",
    description="Common utilities for A2A (Agent-to-Agent) communication",
    author="gakwayaremy",
    author_email="d4remy@gmail.com",
    packages=find_packages(),
    install_requires=[
        "starlette",
        "pydantic",
        "sse-starlette",
        "uvicorn",
    ],
    extras_require={
        "dev": [
            "pytest",
            "pytest-asyncio",
            "black",
            "isort",
            "mypy",
            "flake8",
        ],
        "docs": [
            "sphinx",
            "sphinx-rtd-theme",
        ],
    },
    license="Apache-2.0",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
)
