from tree_sitter_rst import parser


def test_parse():
    tree = parser.parse(b".. this::\n   is a directive")
    assert (
        tree.root_node.sexp()
        == "(document (directive name: (type) body: (body (content))))"
    )
