"""
Helper functions for Node objects.

Done by Han Keong
Created on 10/04/2018 2235 +0800
Last updated on 11/04/2018 0038 +0800
"""

from node import Node
from traversals import traverse_level_order


def get_max_depth(node):
    '''Calculate the maximum depth of a binary tree.
    
    Args:
        node (:class:`Node`): A binary tree root.

    Return:
        int: The total number of levels of the binary tree.
    '''
    return sum(1 for level in traverse_level_order(node))


def get_all_paths(node):
    '''Find every unique root-to-leaf path in a binary tree.
    
    Args:
        node (:class:`Node`): A binary tree root.

    Yields:
        :obj:`tuple` of :obj:`Node`: A copy of every node from the root to a leaf.
    '''
    queue = [node]
    visited = []
    while True:
        while isinstance(queue[-1].left, Node):
            queue.append(queue[-1].left)
        while queue:
            node = queue[-1]
            if isinstance(node.right, Node):
                if node not in visited:
                    visited.append(node)
                    queue.append(node.right)
                    break
            elif not isinstance(node.left, Node):
                yield tuple(queue)
            queue.pop()
        else: 
            return
