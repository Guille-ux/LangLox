# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
# 
# Copyright (c) 2025 Guillermo Leira Temes

from setuptools import setup, find_packages

setup(
	name="ZynkPy",
	version="0.1.0",
	description="A semi-interpreted programming language",
	long_description=open("README.md").read(),
	long_description_content_type="text/markdown",
	package_dir={"":"src"},
	packages=find_packages(where="src"),
	install_requires=[],
	entry_points={
		"console_scripts":["zynk=cli:main"]
	},
	# metadata
	author="Guillermo Leira Temes",
	author_email="guilleleiratemes@gmail.com,guillermoleiratemes@gmail.com",
	license="GPLv3",
	url="https://github.com/Guille-ux/LangLox",
	classifiers=[
		"Development Status :: 3 - Alpha",
		"Intended Audience :: Developers",
		"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
		"Programming Language :: Python :: 3"
	],
	python_requires=">=3.6",
	include_package_data=True
)
