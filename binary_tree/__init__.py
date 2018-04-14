"""This package provides a Node object and useful tools for processing a binary tree data structure. 

For example::

    from binary_tree import Node, traverse

    node = Node.from_string("1,2,,3,4,,5")
    
    in_order = [node.value for node in traverse("in", node)]
    pre_order = [node.value for node in traverse("pre", node)]
    node2 = Node.from_orders("in-pre", in_order, pre_order)

>>> node == node2
True

For a more detailed demonstration of the Node class, you can run this in your terminal::

    $ binary_tree/node.py

Also, to see another demonstration of the tree functions provided in this module, run::

    $ binary_tree/tree.py
"""

__author__ = 'Han Keong'
__email__ = 'hk997@live.com'
__version__ = '0.0.4'

from .node import *
del node

from .tree import *
del tree

__all__ = [
    "Node",
    "is_node",
    "has_path_sum",
    "is_symmetrical",
    "traverse_pre_order",
    "traverse_in_order",
    "traverse_post_order",
    "traverse_level_order",
    "traverse",
    "get_all_paths",
    "get_max_depth",
    ]