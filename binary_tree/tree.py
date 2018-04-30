# -*- coding: utf-8 -*-

"""This module contains functions for binary trees."""

from .node import Node, is_node, is_leaf
import functools

def connect_nodes(root):
    """Connect the :class:`~binary_tree.Node` instances in each level of `root`.
    
    Args:
        root: A root :class:`~binary_tree.Node` instance.
    """
    for level in traverse_level_order(root):
        prev_node, next_node = None, None
        for i in range(len(level)):
            prev_node, level[i].prev, next_node, level[-i-1].next = (
                level[i], prev_node, level[-i-1], next_node)

def from_string(tree_string, cls=Node):
    """Construct a :class:`~binary_tree.Node` instance with the binary tree structure represented by `tree_string`.

    Initializes the root :class:`~binary_tree.Node` instance (the first level), followed by :attr:`~binary_tree.Node.left` and then :attr:`~binary_tree.Node.right` for every :class:`~binary_tree.Node` instance per level (level-order).
    
    Args:
        tree_string (str): A level-order binary tree traversal, separated by commas.
        cls (type): The class constructor to use. Defaults to :class:`~binary_tree.Node`.
    
    Returns:
        A newly initialized `cls` instance with the binary tree structure that represents `tree_string`. If `tree_string` has no root value, returns ``None``.

    Note:
        Empty spaces can be represented by an immediate comma or ``"null"`` for explicitness.
    """
    for char in " []\n'\"":
        tree_string = tree_string.replace(char, "")
    values = iter(tree_string.split(","))
    value = next(values)
    if value == "":  # Empty root value.
        return None
    try:
        value = int(value)
    except ValueError:  # value is not a number.
        pass
    root = cls(value)
    level = [root]
    while level:
        next_level = []
        for node in level:
            for side in ["left", "right"]:
                try:
                    value = next(values)
                except StopIteration:  # values has been exhausted.
                    break  # break out of all loops
                if value in ["", "null"]:  # Not a node.
                    continue
                try:
                    value = int(value)
                except ValueError:  # value is not a number.
                    pass
                child = cls(value)
                setattr(node, side, child)
                next_level.append(child)
            else:
                continue
            break
        else:
            level = next_level
            continue
        break
    connect_nodes(root)
    return root

def from_orders(kind, in_order, other_order, cls=Node):
    """Construct a :class:`~binary_tree.Node` instance with the binary tree structure that entails `in-order` and `other_order`.

    Recursively initializes :attr:`~binary_tree.Node.parent`, :attr:`~binary_tree.Node.left`, and then :attr:`~binary_tree.Node.right`. (pre-order).
    
    Args:
        kind (str): Either "in-pre" or "in-post".
        in_order (list[int, ...]): The in-order traversal of a binary tree.
        other_order (list[int, ...]): Either the tree's pre-order or 
            post-order traversal.
        cls (type): The class constructor to use. Defaults to :class:`~binary_tree.Node`.

    Returns:
        A newly initialized `cls` instance with the binary tree structure that entails `in_order` and `other_order`. If either arguments are empty, returns ``None``.

    Raises:
        ValueError: If `in_order` and `other_order` do not correspond to a binary tree structure or contain duplicates.
        KeyError: If `kind` is not one of the accepted keys.

    Note:
        There cannot be any duplicates in `in_order` and `other_order`.
    """
    if kind == "in-pre":
        def make_node(in_order, other_order):
            if not in_order or not other_order:
                return None
            node = cls(other_order[0])
            in_slice = in_order[:in_order.index(other_order[0])]
            other_slice = other_order[1:len(in_slice)+1]
            node.left = make_node(in_slice, other_slice)
            in_slice = in_order[in_order.index(other_order[0])+1:]
            other_slice = other_order[-len(in_slice):]
            node.right = make_node(in_slice, other_slice)
            return node
    elif kind == "in-post":
        def make_node(in_order, other_order):
            if not in_order or not other_order:
                return None
            node = cls(other_order[-1])
            in_slice = in_order[:in_order.index(other_order[-1])]
            other_slice = other_order[:len(in_slice)]
            node.left = make_node(in_slice, other_slice)
            in_slice = in_order[in_order.index(other_order[-1])+1:]
            other_slice = other_order[-len(in_slice)-1:-1]
            node.right = make_node(in_slice, other_slice)
            return node    
    else:
        raise KeyError("Invalid argument for kind. "
                       "Expected \"in-pre\" or \"in-post\"")
    root = make_node(in_order, other_order)
    connect_nodes(root)
    return root

def to_string(root):
    """Deconstruct `root` into a string.
    
    Args:
        root: A root :class:`~binary_tree.Node` instance.
    
    Returns:
        str: A level-order binary tree traversal, separated
        by commas.

    Note:
        Empty spaces in the tree string are indicated with ``"null"``.
    """
    tree_values = []
    level = [root]
    while any(level):
        level_values = []
        next_level = []
        for node in level:
            level_values.append(getattr(node, "value", None))
            for side in ["left", "right"]:
                next_level.append(getattr(node, side, None))
        for value in level_values:
            if value:
                tree_values.append(str(value))
            else:
                tree_values.append("null")
        level = next_level
    else:
        return ",".join(tree_values)

def traverse_pre_order(root):
    """Traverse `root` in pre-order.

    Visit :attr:`~binary_tree.Node.parent`, :attr:`~binary_tree.Node.left`, and then :attr:`~binary_tree.Node.right`.
    
    Args:
        root: A root :class:`~binary_tree.Node` instance.

    Yields:
        A :class:`~binary_tree.Node` instance in the binary tree structure of `root`.
    """
    queue = [root]
    while queue:
        node = queue.pop()
        if is_node(node):
            yield node
        if is_node(node.right):
            queue.append(node.right)
        if is_node(node.left):
            queue.append(node.left)

def traverse_in_order(root):
    """Traverse `root` in in-order.

    Visit :attr:`~binary_tree.Node.left`, :attr:`~binary_tree.Node.parent`, and then :attr:`~binary_tree.Node.right`.
    
    Args:
        root: A root :class:`~binary_tree.Node` instance.

    Yields:
        A :class:`~binary_tree.Node` instance in the binary tree structure of `root`.
    """
    queue = [root]
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

def traverse_post_order(root):
    """Traverse `root` in post-order.

    Visit :attr:`~binary_tree.Node.left`, :attr:`~binary_tree.Node.right`, and then :attr:`~binary_tree.Node.parent`.
    
    Args:
        root: A root :class:`~binary_tree.Node` instance.

    Yields:
        A :class:`~binary_tree.Node` instance in the binary tree structure of `root`.
    """
    queue = [root]
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
            yield node
            queue.pop()
        else:
            return

def traverse_level_order(root):
    """Traverse `root` in level-order.

    Visit `root` (the first level), followed by :attr:`~binary_tree.Node.left` and then :attr:`~binary_tree.Node.right` for every :class:`~binary_tree.Node` instance per level.
    
    Args:
        root: A root :class:`~binary_tree.Node` instance.

    Yields:
        A list of :class:`~binary_tree.Node` instances representing a level in `root`.
    """
    level = [root]
    while level:
        yield list(level)
        next_level = []
        for node in level:
            for side in ["left", "right"]:
                child = getattr(node, side)
                if is_node(child):
                    next_level.append(child)
        level = next_level

def traverse(root, kind):
    """Forward `root` to the `kind` of traversal.
    
    Args:
        root: A root :class:`~binary_tree.Node` instance.
        kind (str): "pre" or "in" or "post" or "level".

    Returns:
        The generator iterator of the `kind` of traversal (with `root` passed to it).
    
    Raises:
        KeyError: If `kind` is not one of the possible options.
    """
    traversal = globals()["traverse_{kind}_order".format(kind=kind)]
    return traversal(root)

def is_symmetrical(root):
    """Check for symmetry in `root`.
    
    Args:
        root: A root :class:`~binary_tree.Node` instance.

    Returns:
        ``True`` if the binary tree structure of `root` is symmetrical, ``False`` otherwise.
    """
    level = [root]
    while any(level):
        values = []
        next_level = []
        for node in level:
            values.append(getattr(node, "value", None))
            for side in ["left", "right"]:
                next_level.append(getattr(node, side, None))
        for i in range(len(values)):
            if values[i] != values[-i-1]:
                return False
        level = next_level
    else:
        return True

def max_depth(root):
    """Calculate the maximum depth of `root`.
    
    Args:
        root: A root :class:`~binary_tree.Node` instance.

    Returns:
        int: The total number of levels in the binary tree structure of `root`.
    """
    return sum(1 for level in traverse_level_order(root))

def get_path(node):
    """Trace the ancestry of `node`.
    
    Args:
        node: A :class:`~binary_tree.Node` instance in a binary tree.

    Returns:
        A list of :class:`~binary_tree.Node` instances from the greatest ancestor to `node`.
    """    
    path = [node]
    parent = node.parent
    while parent:
        path.append(parent)
        parent = parent.parent
    path.reverse()
    return path

def all_paths(root):
    """Find every leaf path in `root`.

    Search for leaf nodes in `root` using post-order traversal. 
    
    Args:
        root: A root :class:`~binary_tree.Node` instance.

    Yields:
        A list of :class:`~binary_tree.Node` instances from `root` to a leaf :class:`~binary_tree.Node` instance.
    """
    for node in traverse_post_order(root):
        if is_leaf(node):
            yield get_path(node)

def has_sum(root, value):
    """Determine if there is a path in `root` that adds up to `value`.
    
    Args:
        root: A root :class:`~binary_tree.Node` instance.
        value: The sum to check for.

    Returns:
        ``True`` if a path that adds up to `value` exists in `root`, ``False`` otherwise.
    """
    for path in all_paths(root):
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

def find_path(root, node):
    """Find the path of (the :class:`~binary_tree.Node` instance of) `node` in `root`.
    
    Args:
        root: A root :class:`~binary_tree.Node` instance.
        node: A :class:`~binary_tree.Node` instance or value in `root`.

    Returns:
        A list of every :class:`~binary_tree.Node` instance from `root` to (the :class:`~binary_tree.Node` instance of) `node`, or ``None`` if `node` is absent in `root`.

    Note:
        If `node` is a value, it must be unique within the binary tree structure of `root`.
    """
    for root_node in traverse_post_order(root):
        if node == root_node:
            return get_path(root_node)

def get_lca(root, *nodes):
    """Get the lowest common ancestor of two or more (:class:`~binary_tree.Node` instances of) `nodes` in `root`.
    
    Args:
        root: A root :class:`~binary_tree.Node` instance.
        *nodes (Node): :class:`~binary_tree.Node` instances or values in `root`.

    Returns:
        The :class:`~binary_tree.Node` instance that is the lowest common ancestor of (the :class:`~binary_tree.Node` instances of) `nodes` in `root`, or ``None`` if there is no common ancestor.

    Note:
        Values in `nodes` must be unique within the binary tree structure of `root`.
    """
    if len(nodes) < 2:
        return None
    paths = []
    lca_index = None
    for node in nodes:
        path = find_path(root, node)
        paths.append(path)
        max_index = len(path) - 1
        if lca_index is None or max_index < lca_index:
            lca_index = max_index
    ref_path = paths.pop()
    for path in paths:
        while path[lca_index] is not ref_path[lca_index]:
            lca_index -= 1
    return ref_path[lca_index]

