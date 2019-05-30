import multiprocessing
from setuptools import setup

with open ('README.md', 'r') as File:
    Description = File.read ()

setup (
    name = 'GGLogger',
    version = '1.0.0',
    packages = ['GG'],
    author = 'Munchii',
    author_email = 'contact@munchii.me',
    license = 'MIT',
    description = 'A simple function logger for Python',
    long_description = Description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/Dmunch04/GGLogger',
    install_requires = [
        'DavesLogger'
    ],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
    ],
    keywords = 'simple function logger for python'
)
