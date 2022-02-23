from distutils.command.config import config


try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension

with open("README.md", "r", encoding="utf-8") as f:
    README = f.read()

config = {
    "name": "textfsm_aos",
    "version": "1.1.2",
    "description": "Alcatel-Lucent Enterprise AOS CLI parsing (TextFSM) ",
    "long_description": README,
    "long_description_content_type": "text/markdown",
    "author": "Jef Vantongerloo",
    "url": "https://github.com/jefvantongerloo/textfsm-aos",
    "download_url": "",
    "license": "Apache-2.0",
    "author_email": "jefvantongerloo@gmail.com",
    "include_package_data": True,
    "install_requires": ["scrapli", "textfsm"],
    "packages": ["textfsm_aos"],
    "scripts": "",
    "zip_safe": True,
}

setup(**config)
