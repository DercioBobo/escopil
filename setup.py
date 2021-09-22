from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in escopil/__init__.py
from escopil import __version__ as version

setup(
	name="escopil",
	version=version,
	description="Escopil Apps",
	author="Duys",
	author_email="dercio.bobo@escopil.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
