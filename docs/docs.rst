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
.. automethod:: binary_tree.tree.from_string

.. automethod:: binary_tree.tree.from_orders

.. automethod:: binary_tree.tree.connect_nodes

.. automethod:: binary_tree.tree.to_string

Traversing a Node tree 
----------------------
.. automethod:: binary_tree.tree.traverse_pre_order

.. automethod:: binary_tree.tree.traverse_in_order

.. automethod:: binary_tree.tree.traverse_post_order

.. automethod:: binary_tree.tree.traverse_level_order

.. automethod:: binary_tree.tree.traverse

Analyzing a Node tree
---------------------
.. automethod:: binary_tree.tree.is_symmetrical

.. automethod:: binary_tree.tree.max_depth

.. automethod:: binary_tree.tree.get_path

.. automethod:: binary_tree.tree.all_paths

.. automethod:: binary_tree.tree.has_sum

.. automethod:: binary_tree.tree.find_path

.. automethod:: binary_tree.tree.get_lca

