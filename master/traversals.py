"""
Tree traversal functions.

Done by Han Keong
Created on 10/04/2018 2232 +0800
Last updated on 11/04/2018 0025 +0800
"""

from node import Node


def traverse_pre_order(node):
    """Visit the parent, the left child, and then the right child.
    
    Args:
        node (:class:`Node`): A binary tree root.

    Yields:
        int: Node values in the binary tree.
    """
    queue = [node]
    while queue:
        node = queue.pop()
        if node.value:
            yield node.value
        if isinstance(node.right, Node):
            queue.append(node.right)
        if isinstance(node.left, Node):
            queue.append(node.left)


def traverse_in_order(node):
    """Visit the left child, the parent, and then the right child.
    
    Args:
        node (:class:`Node`): A binary tree root.

    Yields:
        int: Node values in the binary tree.
    """
    queue = [node]
    while True:
        while isinstance(queue[-1].left, Node):
            queue.append(queue[-1].left)
        while queue:
            node = queue.pop()
            if node.value:
                yield node.value
            if isinstance(node.right, Node):
                queue.append(node.right)
                break
        else:
            return


def traverse_post_order(node):
    """Visit the left and right children, and then the parent.
    
    Args:
        node (:class:`Node`): A binary tree root.

    Yields:
        int: Node values in the binary tree.
    """
    queue = [node]
    visited = []
    while True:
        while isinstance(queue[-1].left, Node):
            queue.append(queue[-1].left)
        while queue:
            node = queue[-1]
            if isinstance(node.right, Node) and node not in visited:
                visited.append(node)
                queue.append(node.right)
                break
            if node.value:
                yield node.value
            queue.pop()
        else:
            return


def traverse_level_order(node):
    """Visit each parent in the level, and then each of their left and right children.
    
    Args:
        node (:class:`Node`): A binary tree root.

    Yields:
        :obj:`tuple` of :obj:`int`: Node levels in the binary tree.
    """
    level = (node,)
    while level:
        yield tuple(node.value for node in level)
        level = tuple(getattr(node, branch) for node in level 
            for branch in ("left", "right") if getattr(node, branch))

