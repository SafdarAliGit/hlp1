from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in hlp1/__init__.py
from hlp1 import __version__ as version

setup(
	name="hlp1",
	version=version,
	description="This is HLP1 site",
	author="Tech Ventrues",
	author_email="safdar211@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
