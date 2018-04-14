"""This package provides a Node object and useful tools for processing a binary tree data structure. 

For example::

    from binary_tree import Node, traverse

    node = Node.from_string("1,2,,3,4,,5")
    
    in_order = [node.value for node in traverse("in", node)]
    pre_order = [node.value for node in traverse("pre", node)]
    node2 = Node.from_orders("in-pre", in_order, pre_order)

>>> node == node2
True

For a demonstration of this module, you can run this in your terminal (for macOS)::

    $ git clone https://github.com/han-keong/binary_tree.git
    $ binary_tree/demo/tree.py
"""

__author__ = 'Han Keong'
__email__ = 'hk997@live.com'
__version__ = '0.0.6'

from .node import *
del node

from .tree import *
del tree

__all__ = ["Node", "is_node", "is_leaf", "has_path_sum", 
           "is_symmetrical", "traverse_pre_order", "traverse_in_order",
           "traverse_post_order", "traverse_level_order", "traverse", 
           "get_all_paths", "get_max_depth"]