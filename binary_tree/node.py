# -*- coding: utf-8 -*-

"""This module contains the interface for the Node class."""

class Node(object):
    """The basic unit of a binary tree structure.

    Attributes:
        value: The node value.
        left (Node, optional): The left child node, if present.
        right (Node, optional): The right child node, if present.
        prev (Node, optional): The nearest neighbour node on the left, if present.
        next (Node, optional): The nearest neighbour node on the right, if present.
        parent (Node, optional): The parent node, if present.
    """
    __slots__ = ["value", "_left", "_right", "_prev", "_next", "parent"]

    def __init__(self, value, **nodes):
        self.value = getattr(value, "value", value)
        for attr in ["left", "right", "prev", "next", "parent"]:
            setattr(self, attr, nodes.get(attr))

    def __str__(self):
        return "Node(" + str(self.value) + ")"

    def __repr__(self):
        args = [str(self.value)]
        if not is_leaf(self):
            args.append("left=" + repr(self.left))
            if is_node(self.right):
                args.append("right=" + repr(self.right))
        return "Node(" + ", ".join(args) + ")"

    def __eq__(self, other):
        return self.value == getattr(other, "value", other)

    def __ne__(self, other):
        return self.value != getattr(other, "value", other)

    def __iter__(self):
        level = [self]
        while level:
            next_level = []
            for node in level:
                yield node
                for side in ["left", "right"]:
                    child = getattr(node, side)
                    if is_node(child):
                        next_level.append(child)
            level = next_level

    @property
    def left(self):
        return getattr(self, "_left", None)

    @left.setter
    def left(self, other):
        self._left = other
        if is_node(other):
            other.parent = self

    @property
    def right(self):
        return getattr(self, "_right", None)

    @right.setter
    def right(self, other):
        self._right = other
        if is_node(other):
            other.parent = self

    @property
    def prev(self):
        return getattr(self, "_prev", None)

    @prev.setter
    def prev(self, other):
        self._prev = other
        if is_node(other):
            other._next = self

    @property
    def next(self):
        return getattr(self, "_next", None)

    @next.setter
    def next(self, other):
        self._next = other
        if is_node(other):
            other._prev = self

def is_node(obj):
    """Check if `obj` is an instance of Node.

    Args:
        obj: Any object.

    Returns:
        ``True`` if `obj` is an instance of Node, ``False`` otherwise.
    """
    return isinstance(obj, Node)

def is_left(node):
    """Check if `node` is a left child.

    Return:
        ``True`` if `node` is the left child of its parent, ``False`` otherwise, or if parent is not set.
    """
    return (is_node(node.parent)
            and node.parent.left is node)

def is_right(node):
    """Check if `node` is a right child.

    Return:
        ``True`` if `node` is the right child of its parent, ``False`` otherwise, or if parent is not set.
    """
    return (is_node(node.parent)
            and node.parent.right is node)

def is_leaf(node):
    """Check if `node` is a leaf node.

    Returns:
        ``True`` if `node` has a parent node but no children, ``False`` otherwise.
    """
    return (node.parent is not None
            and node.left is None
            and node.right is None)

def is_root(node):
    """Check if `node` is a root node.

    Return:
        ``True`` if `node` has a child node but no parent, ``False`` otherwise.
    """
    return ((node.left is not None or node.right is not None) 
            and node.parent is None)

def is_orphan(node):
    """Check if `node` is an orphan node.

    Return:
        ``True`` if `node` has no parent or children node, ``False`` otherwise.
    """
    return (node.parent is None
            and node.left is None
            and node.right is None)

