"""
Node class.

Reference: https://leetcode.com/explore/learn/card/data-structure-tree/

Done by Han Keong
Created on 10/04/2018 2220 +0800
Last updated on 11/04/2018 1343 +0800
"""

from constructors import from_string as _make_node_from_string, from_orders as _make_node_from_orders

class Node:
    def __init__(self, value, left=None, right=None):
        """Initialize self.

        Args:
            value (int): The node value.
            left (:obj:`Node`, optional): The left child. Defaults to None.
            right (:obj:`Node`, optional): The right child. Defaults to None.

        Raises:
            ValueError: If `value` cannot be typecasted to an int.
        """
        self.value = int(value)
        self.left = left
        self.right = right

    def __str__(self):
        """Get str(self).
        
        Returns:
            str: A short representation of `self`.
        """
        return f"Node({self.value})"

    def __repr__(self):
        """Get repr(str).
        
        Returns:
            str: An executable representation of `self`.
        """
        args = [str(self.value)]
        if None not in (self.left, self.right):
            args.append(repr(self.left))
            if self.right is not None:
                args.append(repr(self.right))
        return f"Node({', '.join(args)})"
    
    @classmethod
    def from_string(cls, tree_string):
        """Instantiate and return a new :class:`Node` from a string.
        
        Args:
            tree_string (str): A flattened, level-order binary tree traversal.
                The node values should be separated by commas.
        
        Returns:
            :class:`Node`: A newly instantiated :class:`Node` representing `tree_string`.
            None: If `tree_string` has an invalid root value or does not contain any node values.
        """
        return _make_node_from_string(cls, tree_string)

    @classmethod
    def from_in_pre_orders(cls, in_order, pre_order):
        """Instantiate and return a new :class:`Node` from an in-order and a pre-order traversal.
        
        Note:
            There cannot be any duplicates in `in_order` and `pre_order`.

        Args:
            in_order (:obj:`list` of :obj:`int`): An in-order binary tree traversal.
            pre_order (:obj:`list` of :obj:`int`): A pre-order binary tree traversal.
        
        Returns:
            :class:`Node`: A newly instantiated :class:`Node` entailing `in_order` and `pre_order`.
            None: If `in_order` or `pre_order` is empty.

        Raises:
            IndexError: If `in_order` and `pre_order` do not constitute a binary tree,
                or if they contain any duplicates.
        """
        return _make_node_from_orders(cls, "in-pre", in_order, pre_order)

    @classmethod
    def from_in_post_orders(cls, in_order, post_order):
        """Instantiate and return a new :class:`Node` from an in-order and a post-order traversal.
        
        Note:
            There cannot be any duplicates in `in_order` and `post_order`.
        
        Args:
            in_order (:obj:`list` of :obj:`int`): An in-order binary tree traversal.
            post_order (:obj:`list` of :obj:`int`): A post-order binary tree traversal.
        
        Returns:
            :class:`Node`: A newly instantiated :class:`Node` entailing `in_order` and `post_order`.
            None: If `in_order` or `post_order` is empty.

        Raises:
            IndexError: If `in_order` and `post_order` do not constitute a binary tree,
                or if they contain any duplicates.
        """
        return _make_node_from_orders(cls, "in-post", in_order, post_order)

