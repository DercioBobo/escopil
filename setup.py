from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in esco/__init__.py
from esco import __version__ as version

setup(
	name="esco",
	version=version,
	description="esco",
	author="esco",
	author_email="esco@duys.co.mz",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
