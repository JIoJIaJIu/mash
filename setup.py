from setuptools import setup, find_packages

__version__ = '0.0.1'

setup(
    name='mash-meal',
    license='MIT',
    long_description=open('README.rst').read(),
    packages=find_packages(),
    version=__version__,
    url='https://github.com/JIoJIaJIu/mash-meal.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Topic :: Utilities'
    ]
)
