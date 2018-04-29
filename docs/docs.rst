***************
 Documentation
***************

.. automodule:: binary_tree

======
 Node
======

.. autoclass:: binary_tree.Node
    :members:
    :member-order: bysource
    :special-members: __repr__, __iter__, __eq__

======
 node
======

.. automodule:: binary_tree.node
    :members:
    :member-order: bysource
    :exclude-members: Node

======
 tree
======

.. automodule:: binary_tree.tree

Setting up a Node tree 
----------------------
.. autofunction:: binary_tree.tree.from_string

.. autofunction:: binary_tree.tree.from_orders

.. autofunction:: binary_tree.tree.connect_nodes

.. autofunction:: binary_tree.tree.to_string

Traversing a Node tree 
----------------------
.. autofunction:: binary_tree.tree.traverse_pre_order

.. autofunction:: binary_tree.tree.traverse_in_order

.. autofunction:: binary_tree.tree.traverse_post_order

.. autofunction:: binary_tree.tree.traverse_level_order

.. autofunction:: binary_tree.tree.traverse

Analyzing a Node tree
---------------------
.. autofunction:: binary_tree.tree.is_symmetrical

.. autofunction:: binary_tree.tree.max_depth

.. autofunction:: binary_tree.tree.get_path

.. autofunction:: binary_tree.tree.all_paths

.. autofunction:: binary_tree.tree.has_sum

.. autofunction:: binary_tree.tree.find_path

.. autofunction:: binary_tree.tree.get_lca

