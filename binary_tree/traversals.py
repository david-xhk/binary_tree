"""
Tree traversal generators.

Done by Han Keong
Created on 10/04/2018 2232 +0800
Last updated on 11/04/2018 1344 +0800
"""

from misc import is_node as _is_node

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
        if _is_node(node.right):
            queue.append(node.right)
        if _is_node(node.left):
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
        while _is_node(queue[-1].left):
            queue.append(queue[-1].left)
        while queue:
            node = queue.pop()
            if node.value:
                yield node.value
            if _is_node(node.right):
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
        while _is_node(queue[-1].left):
            queue.append(queue[-1].left)
        while queue:
            node = queue[-1]
            if _is_node(node.right) and node not in visited:
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
    level = [node]
    while level:
        next_level = []
        values = []
        for node in level:
            if not _is_node(node):
                continue
            values.append(node.value)
            for side in ("left", "right"): 
                next_level.append(getattr(node, side))
        yield tuple(values)
        level = next_level

