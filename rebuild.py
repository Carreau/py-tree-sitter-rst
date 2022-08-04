from tree_sitter import Language, Parser
from pathlib import Path

pth = Path("tree_sitter_rst/rst.so")
if pth.exists():
    print("parser exists, erasing to rebuild")
    pth.unlink()

spth = str(pth)

Language.build_library(
    # Store the library in the `build` directory
    spth,
    # Include one or more languages
    [
        "tree-sitter-rst",
    ],
)
