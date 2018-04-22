# -*- coding: utf-8 -*-

"""This package consists of a Node class and functions for processing a binary tree data structure. 

For example::

    from binary_tree import from_string, from_orders, traverse

    node = tree_from_string("1,2,,3,4,,5")
    
    in_order = list(traverse("in", node))
    pre_order = list(traverse("pre", node))
    node2 = from_orders("in-pre", in_order, pre_order)

>>> node == node2
True
"""

__author__ = 'Han Keong'
__email__ = 'hk997@live.com'
__version__ = '0.1.0'

from .node import *
from .tree import *

__all__ = ["Node", "is_node", "is_left", "is_right", "is_leaf", "is_root", 
           "is_orphan", "from_string", "to_string", "from_orders", 
           "traverse_pre_order", "traverse_in_order", "traverse_post_order", 
           "traverse_level_order", "traverse", "is_symmetrical",
           "connect_nodes", "get_max_depth", "get_path", "get_all_paths",
           "has_path_sum", "find_path", "get_lca"]

del node, tree

try:
    from .tools import ensure_type
except ImportError:
    pass
else:
    ensure_node = ensure_type(root=Node, node=Node, nodes=Node)
    for name in __all__:
        globals()[name] = ensure_node(globals()[name])
    del tools, ensure_type, name

