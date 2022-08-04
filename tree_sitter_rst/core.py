import pathlib

from tree_sitter import Language, Parser

_binary_path = str(pathlib.Path(__file__).parent / "rst.so")
rst = Language(binary_path, language)
