from tree_sitter import Language, Parser

from tree_sitter_rst._rst import language as _language

RST_LANGUAGE = Language(_language())
_parser = Parser(RST_LANGUAGE)
parse = _parser.parse
