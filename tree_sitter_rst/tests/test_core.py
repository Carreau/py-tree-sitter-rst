from tree_sitter_rst import parse


def test_parse():
    tree = parse(b".. this::\n   is a directive")
    assert (
        tree.root_node.sexp()
        == "(document (directive name: (type) body: (body (content))))"
    )
