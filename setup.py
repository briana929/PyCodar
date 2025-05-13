from setuptools import setup, find_packages

setup(
    name="codeas",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "rich>=10.0.0",
    ],
    entry_points={
        'console_scripts': [
            'codeas=cli:main',
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="Code Architecture System - A Git-like tool for auditing and understanding your codebase",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/codeas",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
) 