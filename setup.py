import pathlib
import re
import setuptools


from wheel.bdist_wheel import bdist_wheel as _bdist_wheel
from setuptools.command.build_ext import build_ext


setuptools.setup(
    name="tree_sitter_rst",
    version="0.0.1",
    description="Binary Python wheels for tree_sitter_rst parser.",
    long_description="",
    author="Matthias Bussonnier",
    author_email="bussonniermatthias@gmail.com",
    zip_safe=False,
    url="",
    license="BSD",
    packages=["tree_sitter_rst"],
    package_data={"tree_sitter_rst": ["rst.so"]},
    install_requires=["tree-sitter"],
)
