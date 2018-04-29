***************
 Documentation
***************

.. automodule:: binary_tree

======
 Node
======

.. autoclass:: binary_tree.Node

Comparing the value of a Node instance
--------------------------------------
.. automethod:: binary_tree.Node.__eq__

Getting the binary tree structure of a Node instance
----------------------------------------------------
.. automethod:: binary_tree.Node.__repr__

Iterating over the binary tree structure of a Node instance
-----------------------------------------------------------
.. automethod:: binary_tree.Node.__iter__

======
 node
======

.. automodule:: binary_tree.node

Checking for a Node instance
----------------------------
.. autofunction:: binary_tree.node.is_node

Checking for a child Node instance
----------------------------------
.. autofunction:: binary_tree.node.is_left

.. autofunction:: binary_tree.node.is_right

Checking for a Node instance in a binary tree structure
-------------------------------------------------------
.. autofunction:: binary_tree.node.is_leaf

.. autofunction:: binary_tree.node.is_root

.. autofunction:: binary_tree.node.is_orphan

======
 tree
======

.. automodule:: binary_tree.tree

Setting up a Node instance with a binary tree structure 
-------------------------------------------------------
.. autofunction:: binary_tree.tree.from_string

.. autofunction:: binary_tree.tree.from_orders

.. autofunction:: binary_tree.tree.connect_nodes

.. autofunction:: binary_tree.tree.to_string

Traversing a Node instance with a binary tree structure
-------------------------------------------------------
.. autofunction:: binary_tree.tree.traverse_pre_order

.. autofunction:: binary_tree.tree.traverse_in_order

.. autofunction:: binary_tree.tree.traverse_post_order

.. autofunction:: binary_tree.tree.traverse_level_order

.. autofunction:: binary_tree.tree.traverse

Analyzing a Node instance with a binary tree structure
------------------------------------------------------
.. autofunction:: binary_tree.tree.is_symmetrical

.. autofunction:: binary_tree.tree.max_depth

.. autofunction:: binary_tree.tree.get_path

.. autofunction:: binary_tree.tree.all_paths

.. autofunction:: binary_tree.tree.has_sum

.. autofunction:: binary_tree.tree.find_path

.. autofunction:: binary_tree.tree.get_lca

