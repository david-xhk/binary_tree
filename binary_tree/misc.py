"""
Miscellaneous functions for Node objects.

Done by Han Keong
Created on 10/04/2018 2239 +0800
Last updated on 11/04/2018 1335 +0800
"""


from node import Node as _Node

def is_node(obj):
    """Check if obj is an instance of Node.
    Args:
        obj: Any old object.

    Return:
        bool: True if obj is indeed a Node, False otherwise.
    """
    return isinstance(obj, _Node)


def is_symmetric(node):
    """Check for symmetry in a binary tree.
    
    Args:
        node (:class:`Node`): A binary tree root.

    Return:
        bool: True if the binary tree is symmetrical, False otherwise.
    """
    level = [node]
    while any(level):
        values = []
        next_level = []
        for node in level:
            values.append(getattr(node, "value", None))
            for side in ("left", "right"):
                next_level.append(getattr(node, side))
            if values != values[::-1]:
                return False
        level = next_level
    return True


from helpers import get_all_paths as _get_all_paths

def has_path_sum(node, value):
    """Determine if a binary tree contains a root-to-leaf path that sums to `value`.
    
    Args:
        node (:class:`Node`): A binary tree root.

    Returns:
        bool: True if a path that sums to `value` exists, False otherwise.
    """
    return any(sum(node.value for node in path) == value 
        for path in _get_all_paths(node))
