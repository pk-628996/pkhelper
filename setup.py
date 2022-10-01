#!/usr/bin/python3
from setuptools import setup, find_packages
__version__=0.496

def get_long_description():
    with open("README.md") as f:
        long_description = f.read()

    try:
        import github2pypi

        return github2pypi.replace_url(
            slug="pk-628996/gdownh", content=long_description
        )
    except Exception:
        return long_description

setup(
    name="gdownh",
    version=f"{__version__}",
    packages=['gdownh'],
    py_modules=['gdownh'],
    description="Google Drive direct download of big files.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    download_url='https://github.com/pk-628996/gdownh/archive/refs/heads/main.zip',
    install_requires=['gdown','pytube','aiohttp'],
    entry_points={"console_scripts": ["gdownh=gdownh.cli:main"]},
)