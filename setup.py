from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Stats Package created for common data anaysis tasks in Rescues research division'

# Setting up
setup(
    name="stats_package_TEST",
    version=VERSION,
    author="Elisabeth Jones",
    author_email="<ejones@rescueagency.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['pandas', 'numpy', 'matplotlib', 'researchpy', 'scipy'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
