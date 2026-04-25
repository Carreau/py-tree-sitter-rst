import os
import sys

from setuptools import Extension, setup

sources = ["src/binding.c", "tree-sitter-rst/src/parser.c"]
scanner = "tree-sitter-rst/src/scanner.c"
if os.path.exists(scanner):
    sources.append(scanner)

extra_compile_args = [] if sys.platform == "win32" else ["-std=c11"]

setup(
    ext_modules=[
        Extension(
            name="tree_sitter_rst._rst",
            sources=sources,
            include_dirs=["tree-sitter-rst/src"],
            extra_compile_args=extra_compile_args,
        )
    ]
)
