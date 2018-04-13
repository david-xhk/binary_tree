"""Tools for a binary tree data structure.

Node:
    You can run "binary_tree/node.py" in your terminal or "binary_tree/tree.py"
    to look at a demonstration of the Node class or the tree functions provided
    in this module.
"""

__author__ = 'Han Keong'
__email__ = 'hk997@live.com'
__version__ = '0.0.4'

from .node import *
del node

from .tree import *
del tree

# __all__ = [
#     "Node",
#     "is_node", 
#     "is_leaf_node", 
#     "traverse_pre_order", 
#     "traverse_in_order", 
#     "traverse_post_order", 
#     "traverse_level_order", 
#     "traverse"
#     "get_max_depth", 
#     "get_all_paths",
#     "is_symmetrical", 
#     "has_path_sum",
#     ]

