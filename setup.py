from setuptools import setup, find_packages

setup(
    name='pynqo',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pydantic',
        'aiohttp',
    ],
    author='Pynqo Labs',
    description='Official Python SDK for pynqo',
    python_requires='>=3.8',
    url='https://github.com/pynqo/pynqo_py',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
