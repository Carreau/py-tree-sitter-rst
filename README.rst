==========================================
py-tree-sitter-rst
==========================================

Binary Python wheels for the `tree-sitter-rst`_ reStructuredText parser.

`py-tree-sitter`_ is a Python binding for the `tree-sitter`_ parsing library.
This package distributes pre-compiled binary wheels for the RST grammar,
so you do not need a C compiler or build tools at install time.

.. _`tree-sitter-rst`: https://github.com/stsewd/tree-sitter-rst
.. _`py-tree-sitter`: https://github.com/tree-sitter/py-tree-sitter
.. _`tree-sitter`: https://tree-sitter.github.io/


Install
=======

::

   pip install tree_sitter_rst


Usage
=====

::

   from tree_sitter_rst import parse

   tree = parse(b".. note::\n   Hello world")
   print(tree.root_node.sexp())

Refer to `py-tree-sitter`_ for the full parser and node API.


Development
===========

The RST grammar lives in the ``tree-sitter-rst`` git submodule (tracking
`stsewd/tree-sitter-rst <https://github.com/stsewd/tree-sitter-rst>`_).

Updating the grammar
--------------------

To pull in the latest upstream grammar commit::

   git submodule update --remote tree-sitter-rst
   git add tree-sitter-rst
   git commit -m "chore: update tree-sitter-rst submodule"

To pin to a specific tag or commit::

   cd tree-sitter-rst
   git fetch
   git checkout <tag-or-sha>
   cd ..
   git add tree-sitter-rst
   git commit -m "chore: pin tree-sitter-rst to <tag-or-sha>"

Using a fork
------------

If you need to test against a fork of ``tree-sitter-rst`` (e.g. a branch with
an unreleased fix), edit ``.gitmodules`` to point at the fork::

   [submodule "tree-sitter-rst"]
       path = tree-sitter-rst
       url = https://github.com/<your-username>/tree-sitter-rst

Then re-initialise the submodule::

   git submodule sync
   git submodule update --init --remote tree-sitter-rst

Optionally check out a specific branch in the fork::

   cd tree-sitter-rst
   git checkout <branch-name>
   cd ..
   git add .gitmodules tree-sitter-rst
   git commit -m "chore: point submodule at fork branch <branch-name>"

Remember to revert ``.gitmodules`` before merging back to main.


Building wheels locally
=======================

Wheels are built with `cibuildwheel`_::

   pip install cibuildwheel
   git submodule update --init
   cibuildwheel --output-dir wheelhouse

.. _`cibuildwheel`: https://github.com/pypa/cibuildwheel


License
=======

Copyright Matthias Bussonnier and contributors.

Licensed under the Apache License, Version 2.0.
See ``LICENSE`` for the full text.

The bundled binary includes code from `tree-sitter-rst`_ by Santos Gallegos,
licensed under the MIT License.
