# -*- coding: utf-8 -*-

"""This module provides a Node class, node functions, and tree functions for a binary tree data structure.

Example:
    ::

      from binary_tree import from_string, from_orders, traverse

      node = from_string("1,2,,3,4,,5")
      
      in_order = list(traverse(node, "in"))
      pre_order = list(traverse(node, "pre"))
      node2 = from_orders("in-pre", in_order, pre_order)

>>> repr(node) == repr(node2)
True
"""

__author__ = 'Han Keong'
__email__ = 'hk997@live.com'
__version__ = '0.1.0'

from .node import *
from .tree import *

__all__ = ["Node", "is_node", "is_left", "is_right", "is_leaf", "is_root", 
           "is_orphan", "from_string", "from_orders", "connect_nodes",
           "to_string", "traverse_pre_order", "traverse_in_order",
           "traverse_post_order", "traverse_level_order", "traverse",
           "is_symmetrical", "max_depth", "get_path", "all_paths", "has_sum",
           "find_path", "get_lca"]

