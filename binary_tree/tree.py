#!/usr/bin/env python3
"""This module contains functions for binary trees."""

from .node import is_node

def traverse_pre_order(node):
    """Visit the parent, the left child, and then the right child.
    
    Args:
        node (Node): A binary tree root.

    Yields:
        Node: A node in the binary tree.
    """
    queue = [node]
    while queue:
        node = queue.pop()
        if is_node(node):
            yield node
        if is_node(node.right):
            queue.append(node.right)
        if is_node(node.left):
            queue.append(node.left)

def traverse_in_order(node):
    """Visit the left child, the parent, and then the right child.
    
    Args:
        node (Node): A binary tree root.

    Yields:
        Node: A node in the binary tree.
    """
    queue = [node]
    while True:
        while is_node(queue[-1].left):
            queue.append(queue[-1].left)
        while queue:
            node = queue.pop()
            if is_node(node):
                yield node
            if is_node(node.right):
                queue.append(node.right)
                break
        else:
            return

def traverse_post_order(node):
    """Visit the left and right children, and then the parent.
    
    Args:
        node (Node): A binary tree root.

    Yields:
        Node: A node in the binary tree.
    """
    queue = [node]
    visited = []
    while True:
        while is_node(queue[-1].left):
            queue.append(queue[-1].left)
        while queue:
            node = queue[-1]
            if is_node(node.right) and node not in visited:
                visited.append(node)
                queue.append(node.right)
                break
            if is_node(node):
                yield node
            queue.pop()
        else:
            return

def traverse_level_order(node):
    """Visit each parent in the level, and then each of their left and right children.
    
    Args:
        node (Node): A binary tree root.

    Yields:
        tuple[Node, ...]: A level of nodes in the binary tree.
    """
    level = [node]
    while any(level):
        next_level = []
        nodes = []
        for node in level:
            if not is_node(node):
                continue
            nodes.append(node)
            for side in ["left", "right"]:
                next_level.append(getattr(node, side))
        yield tuple(nodes)
        level = next_level

def traverse(kind, node):
    """Dispatch the requested kind of traversal.
    
    Args:
        kind (str): "pre" or "in" or "post" or "level".
        node (Node): A binary tree root.

    Returns:
        The requested traversal generator iterator.
    
    Raises:
        KeyError: If `kind` is not one of the possible options.
    """
    traversal = globals()["traverse_{kind}_order".format(kind=kind)]
    return traversal(node)

def get_max_depth(node):
    """Calculate the maximum depth of a binary tree.
    
    Args:
        node (Node): A binary tree root.

    Return:
        int: The total number of levels of the binary tree.
    """
    return sum(1 for level in traverse_level_order(node))

def get_all_paths(node):
    """Find every root-to-leaf path in a binary tree.
    
    Args:
        node (Node): A binary tree root.

    Yields:
        tuple[Node, ...]: A copy of every node from the root to a leaf.
    """
    queue = [node]
    visited = []
    while True:
        while is_node(queue[-1].left):
            queue.append(queue[-1].left)
        while queue:
            node = queue[-1]
            if is_node(node.right):
                if node not in visited:
                    visited.append(node)
                    queue.append(node.right)
                    break
            elif not is_node(node.left):
                yield tuple(queue)
            queue.pop()
        else: 
            return

def is_symmetrical(node):
    """Check for symmetry in a binary tree.
    
    Args:
        node (Node): A binary tree root.

    Return:
        ``True`` if the binary tree is symmetrical, ``False`` otherwise.
    """
    level = [node]
    while any(level):
        values = []
        next_level = []
        for node in level:
            values.append(getattr(node, "value", None))
            for side in ["left", "right"]:
                next_level.append(getattr(node, side, None))
        if values != values[::-1]:
            return False
        level = next_level
    else:
        return True

def has_path_sum(node, value):
    """Determine if a binary tree contains a root-to-leaf path that adds up to `value`.
    
    Args:
        node (Node): A binary tree root.
        value: The value to check for.

    Returns:
        ``True`` if a path that adds up to `value` exists, ``False`` otherwise.
    """
    for path in get_all_paths(node):
        total = None
        for node in path:
            if total is None:
                total = node.value
            else:
                total += node.value
        if total == value:
            return True
    else:
        return False


if __name__ == "__main__":
    from .node import Node
    from .demo import BinaryTreeDemo, DemoRestart

    class TreeDemo(BinaryTreeDemo):
        commands = [
            "tree_string, repr(root)",
            "list(traverse_pre_order(root))",
            "list(traverse_in_order(root))",
            "list(traverse_post_order(root))",
            "list(traverse_level_order(root))",
            "list(traverse(\"level\", root))",
            "get_max_depth(root)",
            "is_symmetrical(root)",
            "list(get_all_paths(root))",
            "has_path_sum(root, 12)"]

        def setup_context(self, tree_string):
            root = Node.from_string(tree_string)
            if root is None:
                raise DemoRestart("Missing root value. Please try again.")
            return globals(), locals()

    demo = TreeDemo()
    demo.run()