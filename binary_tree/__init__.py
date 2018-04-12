"""Tools for a binary tree data structure.

Note:
    For a demonstration, run "binary_tree/tree.py".
"""
__author__ = 'Han Keong'
__email__ = 'hk997@live.com'
__version__ = '0.0.3'

from .tree import *
del tree

__all__ = [
    "Node",
    "traverse_pre_order", 
    "traverse_in_order", 
    "traverse_post_order", 
    "traverse_level_order", 
    "traverse"
    "get_max_depth", 
    "get_all_paths",
    "is_node", 
    "is_leaf_node", 
    "is_symmetrical", 
    "has_path_sum",
    ]

