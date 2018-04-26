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
        """Return a full representation of self.

        The repr string is composed of :attr:`~binary_tree.node.Node.value`, the repr string of :attr:`~binary_tree.node.Node.left`, and the repr string of :attr:`~binary_tree.node.Node.right`.

        Returns:
            str: The repr string of self.
        """
        args = [str(self.value)]
        if not is_leaf(self):
            args.append("left=" + repr(self.left))
            if is_node(self.right):
                args.append("right=" + repr(self.right))
        return "Node(" + ", ".join(args) + ")"

    def __eq__(self, other):
        """Tentatively compare the :attr:`~binary_tree.node.Node.value` of self and `other`.

        If `other` does not have a :attr:`~binary_tree.node.Node.value`, use `other` itself as a basis of comparison.

        Args:
            other: Any object.

        Returns:
            ``True`` if the :attr:`~binary_tree.node.Node.value` of self is equal to the :attr:`~binary_tree.node.Node.value` of `other`, or `other` itself- and ``False`` otherwise.
        """
        return self.value == getattr(other, "value", other)

    def __ne__(self, other):
        return self.value != getattr(other, "value", other)

    def __iter__(self):
        """Traverse the tree structure of self in level-order.

        Yields:
            A :class:`~binary_tree.node.Node` in the tree structure of self.
        """
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
    """Check if `obj` is an instance of :class:`~binary_tree.node.Node`.

    Args:
        obj: Any object.

    Returns:
        ``True`` if `obj` is an instance of :class:`~binary_tree.node.Node`, ``False`` otherwise.
    """
    return isinstance(obj, Node)

def is_left(node):
    """Check if `node` is a :attr:`~binary_tree.node.Node.left` child.

    Return:
        ``True`` if `node` is the :attr:`~binary_tree.node.Node.left` node of its :attr:`~binary_tree.node.Node.parent`, ``False`` otherwise, or if its :attr:`~binary_tree.node.Node.parent` is not set.
    """
    return (is_node(node.parent)
            and node.parent.left is node)

def is_right(node):
    """Check if `node` is a :attr:`~binary_tree.node.Node.right` child.

    Return:
        ``True`` if `node` is the :attr:`~binary_tree.node.Node.right` node of its :attr:`~binary_tree.node.Node.parent`, ``False`` otherwise, or if its :attr:`~binary_tree.node.Node.parent` is not set.
    """
    return (is_node(node.parent)
            and node.parent.right is node)

def is_leaf(node):
    """Check if `node` is a leaf node.

    Returns:
        ``True`` if `node` has a :attr:`~binary_tree.node.Node.parent` but no :attr:`~binary_tree.node.Node.left` or :attr:`~binary_tree.node.Node.right` node, ``False`` otherwise.
    """
    return (node.parent is not None
            and node.left is None
            and node.right is None)

def is_root(node):
    """Check if `node` is a root node.

    Return:
        ``True`` if `node` has a :attr:`~binary_tree.node.Node.left` or :attr:`~binary_tree.node.Node.right` node but no :attr:`~binary_tree.node.Node.parent` node, ``False`` otherwise.
    """
    return ((node.left is not None or node.right is not None) 
            and node.parent is None)

def is_orphan(node):
    """Check if `node` is an orphan node.

    Return:
        ``True`` if `node` has no parent or children nodes, ``False`` otherwise.
    """
    return (node.parent is None
            and node.left is None
            and node.right is None)

