from setuptools import setup, find_packages

setup(
    name="a2a-commons",
    version="0.1.0",
    description="Common utilities for A2A (Agent-to-Agent) communication",
    author="gakwayaremy",
    author_email="d4remy@gmail.com",
    package_dir={"a2a_common": "common"},
    packages=["a2a_common"] + [
        "a2a_common." + pkg for pkg in find_packages(where="common")
    ],
    install_requires=[
        "starlette",
        "pydantic",
        "sse-starlette",
        "uvicorn",
    ],
    license="Apache License 2.0",
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