# -*- coding: utf-8 -*-

"""This module contains the interface for the Node class."""

class Node(object):
    """The basic unit of a binary tree structure.

    Attributes:
        value: The node value.
        left (Node, optional): The left child node, if present.
        right (Node, optional): The right child node, if present.
    """
    __slots__ = ["value", "left", "right"]

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return "Node(" + str(self.value) + ")"

    def __repr__(self):
        args = [str(self.value)]
        if not is_leaf(self):
            args.append(repr(self.left))
            if is_node(self.right):
                args.append(repr(self.right))
        return "Node(" + ", ".join(args) + ")"

    def __eq__(self, other):
        try:
            for attr in self.__slots__:
                if getattr(self, attr) != getattr(other, attr):
                    return False
            else:
                return True
        except AttributeError:
            return NotImplemented

    def __ne__(self, other):
        try:
            for attr in self.__slots__:
                if getattr(self, attr) != getattr(other, attr):
                    return True
            else:
                return False
        except AttributeError:
            return NotImplemented

    @classmethod
    def from_string(cls, tree_string):
        """Generate a binary tree from a string.

        Instantiates the left child, and then the right child for every node 
        in each level (level-order).
        
        Args:
            tree_string (str): A level-order binary tree traversal, separated
            by commas.
        
        Returns:
            A newly instantiated Node representing `tree_string`.
            If `tree_string` has no root value, returns ``None``.
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
                        return root
                    else:
                        if value in ["", "null"]:  # Not a node.
                            continue
                        try:
                            value = int(value)
                        except ValueError:  # value is not a number.
                            pass
                        child = cls(value)
                        setattr(node, side, child)
                        next_level.append(child)
            level = next_level
        else:  
            # next_level is an empty list, so subsequent node values are lost.
            return root

    @classmethod
    def from_orders(cls, kind, in_order, other_order):
        """Generate a binary tree from in-order and pre/post-order traversal.

        Recursively instantiates the parent, its left child, and then its 
        right child (pre-order).
        
        Args:
            kind (str): Either "in-pre" or "in-post".
            in_order (list[int, ...]): The in-order traversal of a binary tree
            other_order (list[int, ...]): Either the tree's pre-order or 
                post-order traversal

        Returns:
            A newly instantiated Node entailing `in_order` and `other_order`.
            If either arguments are empty, returns ``None``.

        Raises:
            ValueError: If `in_order` and `other_order` do not correspond or 
                contain duplicates.
            KeyError: If `kind` is not one of the accepted keys.

        Warning:
            There cannot be any duplicates in `in_order` and `other_order`.
        """
        if kind == "in-pre":
            def make_node(in_order, other_order):
                if not in_order or not other_order:
                    return None
                node = cls(other_order[-1])
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
        return make_node(in_order, other_order)

def is_node(obj):
    """Check if `obj` is an instance of Node.

    Look for the attributes that Node needs to function properly.

    Args:
        obj: Any object.

    Return:
        ``True`` if `obj` is an instance of Node, ``False`` otherwise.
    """
    for attr in Node.__slots__:
        if not hasattr(obj, attr):
            return False
    else:
        return True

def is_leaf(node):
    """Check if `node` is a leaf node.

    Return:
        ``True`` if `node` has no children nodes, ``False`` otherwise, or
        if `node` is not an instance of Node.
    """
    for side in Node.__slots__[1:]:
        if getattr(node, side, 1):
            return False
    else:
        return True


