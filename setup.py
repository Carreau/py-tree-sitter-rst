import pathlib
import re
import setuptools


setuptools.setup(
    name="tree_sitter_rst",
    version="0.0.1",
    description="Binary Python wheels for tree_sitter_rst parser.",
    long_description="",
    author="Matthias Bussonnier",
    author_email="bussonniermatthias@gmail.com",
    url="",
    license="BSD",
    packages=["tree_sitter_rst"],
    package_data={"tree_sitter_rst": ["rst.so"]},
    install_requires=["tree-sitter"],
)
