from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="writecode",
    version="0.1.1",
    description="Write code using OpenAI's Codex model",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/supervised/codeit",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

