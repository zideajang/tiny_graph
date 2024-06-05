from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here,"README.md"),encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='tinygraph',
    version='1.0.0',
    author='zidea',
    author_email='zidea2015@163.com',
    description='tiny graph for controlling workflow',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="agent operation os llos agentos",
    url="https://github.com/zideajang/tiny_graph",
    # install_requires=requirements,
    packages=find_packages(exclude=["examples","docs"]),
    python_requires=">=3.9"
)