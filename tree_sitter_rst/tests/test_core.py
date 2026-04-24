from tree_sitter_rst import parse


def test_parse():
    tree = parse(b".. this::\n   is a directive")
    assert (
        str(tree.root_node)
        == "(document (directive name: (type) body: (body (content))))"
    )
