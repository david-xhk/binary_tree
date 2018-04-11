#!/usr/bin/env python3
"""
Binary tree implementation.
For a demonstration, run "./tree.py".

Done by Han Keong
Created on 10/04/2018 2251 +0800
Last updated on 11/04/2018 2258 +0800
"""

from __future__ import print_function

class Node:
    def __init__(self, value, left=None, right=None):
        """Initialize self.

        Args:
            value: The node value.
            left (:obj:`Node`, optional): The left child node.
            right (:obj:`Node`, optional): The right child node.
        """
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        """Get str(self).
        
        Returns:
            str: A short representation of `self`.
        """
        return "Node(" + str(self.value) + ")"

    def __repr__(self):
        """Get repr(str).
        
        Returns:
            str: An executable representation of `self`.
        """
        args = [str(self.value)]
        if not is_leaf_node(self):
            args.append(repr(self.left))
            if is_node(self.right):
                args.append(repr(self.right))
        return "Node(" + ", ".join(args) + ")"
    
    @classmethod
    def from_string(cls, tree_string):
        """Instantiate and return a new :class:`Node` from a string.
        
        Args:
            tree_string (str): A flattened, level-order binary tree traversal.
                The node values should be separated by commas.
        
        Returns:
            :class:`Node`: A newly instantiated :class:`Node` representing `tree_string`.
            None: If `tree_string` does not contain any node values.
        """
        return _from_string(cls, tree_string)

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
            
        Returns:
            None: If `in_order` or `pre_order` is empty.

        Raises:
            ValueError: If `in_order` and `pre_order` do not constitute a binary tree,
                or if they contain any duplicates.
        """
        return _from_orders(cls, "in-pre", in_order, pre_order)

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
        
        Returns:
            None: If `in_order` or `post_order` is empty.

        Raises:
            ValueError: If `in_order` and `post_order` do not constitute a binary tree,
                or if they contain any duplicates.
        """
        return _from_orders(cls, "in-post", in_order, post_order)

# Node constructors.

def _from_string(cls, tree_string):
    """Instantiate each parent in the level, and then each of their left and right children.

    See :ref:`Node.from_string` for more documentation.
    """
    values = iter(tree_string.replace(" []\n'\"", "").split(","))
    try:
        value = next(values)
    except StopIteration:  # tree_string has no values.
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
            for side in _sides:
                try:
                    value = next(values)
                except StopIteration:  # values has been exhausted.
                    return root
                else:
                    if value in ("", "null"):  # Not a node.
                        continue
                    try:
                        value = int(value)
                    except ValueError:  # value is not a number.
                        pass
                    child = cls(value)
                    setattr(node, side, child)
                    next_level.append(child)
        level = next_level
    else:  # next_level is an empty list, so subsequent node values are lost.
        return root

def _from_orders(cls, kind, *orders):
    """Instantiate the parent, the left child, and then the right child.

    See :ref:`Node.from_in_pre_orders` and :ref:`Node.from_in_post_orders` for more documentation.
    """
    if not all(orders):
        return None
    node = cls(orders[1][-1*_kinds[kind]])
    for side in _sides:
        child = _from_orders(cls, kind, *_slice_orders(kind, side, *orders))
        setattr(node, side, child)
    return node

# Constructor helper objects

_slices = (
    ":orders[0].index(orders[1][0])",     #  in-pre,  left, 0
    "1:len(orders[0])+1",                 #  in-pre,  left, 1
    "orders[0].index(orders[1][0])+1:",   #  in-pre, right, 0
    "-len(orders[0]):",                   #  in-pre, right, 1
    ":orders[0].index(orders[1][-1])",    # in-post,  left, 0
    ":len(orders[0])",                    # in-post,  left, 1
    "orders[0].index(orders[1][-1])+1:",  # in-post, right, 0
    "-len(orders[0])-1:-1",               # in-post, right, 1
    )

_kinds = {
    "in-pre": 0,
    "in-post": 1
}

_sides = {
    "left": 0,
    "right": 1
}

def _slice_orders(kind, side, *orders):
    """Slice orders based on which order and what side is provided.
    
    Note:
        There cannot be any duplicates in the orders provided.

    Args:
        kind (str): Either "in-pre" or "in-post".
        side (str): Either "left" or "right".
        *orders (:obj:`list` of :obj:`int`): Either (`in_order`, `pre_order`) or (`in_order`, `post_order`),
            where `in_order` and `pre_order` or `post_order` are lists of ints.
    
    Returns:
        :obj:`list` of :obj:`list`: Sliced copies of the orders provided.
    
    Raises:
        KeyError: If `kind` or `side` is invalid.
        IndexError: If the orders provided do not constitute a binary tree,
            or if they contain any duplicates.
    """
    orders = list(orders)
    for index in (0, 1):
        slice_index = _get_binary_index(_kinds[kind], _sides[side], index)
        exec("orders[index] = orders[index][" + _slices[slice_index] + "]")
    return orders

def _get_binary_index(*bools):
    """Transform a succession of boolean numbers into a decimal integer.

    Args:
        *bools (int): A succession of boolean numbers.
    
    Returns:
        int: A decimal integer.

    Raises:
        ValueError: If any argument in `bools` is not a boolean number.
    """
    return int("".join(str(int(num)) for num in bools), 2)

# Tree traversal generators.

def traverse_pre_order(node):
    """Visit the parent, the left child, and then the right child.
    
    Args:
        node (:class:`Node`): A binary tree root.

    Yields:
        int: A node value in the binary tree.
    """
    queue = [node]
    while queue:
        node = queue.pop()
        if node.value:
            yield node.value
        if is_node(node.right):
            queue.append(node.right)
        if is_node(node.left):
            queue.append(node.left)

def traverse_in_order(node):
    """Visit the left child, the parent, and then the right child.
    
    Args:
        node (:class:`Node`): A binary tree root.

    Yields:
        int: A node value in the binary tree.
    """
    queue = [node]
    while True:
        while is_node(queue[-1].left):
            queue.append(queue[-1].left)
        while queue:
            node = queue.pop()
            if node.value:
                yield node.value
            if is_node(node.right):
                queue.append(node.right)
                break
        else:
            return

def traverse_post_order(node):
    """Visit the left and right children, and then the parent.
    
    Args:
        node (:class:`Node`): A binary tree root.

    Yields:
        int: A node value in the binary tree.
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
        :obj:`tuple` of :obj:`int`: A level of nodes in the binary tree.
    """
    level = [node]
    while any(level):
        next_level = []
        values = []
        for node in level:
            if not is_node(node):
                continue
            values.append(node.value)
            for side in _sides: 
                next_level.append(getattr(node, side))
        yield tuple(values)
        level = next_level

# Helper functions for Node objects.

def get_max_depth(node):
    '''Calculate the maximum depth of a binary tree.
    
    Args:
        node (:class:`Node`): A binary tree root.

    Return:
        int: The total number of levels of the binary tree.
    '''
    return sum(1 for level in traverse_level_order(node))

def get_all_paths(node):
    '''Find every root-to-leaf path in a binary tree.
    
    Args:
        node (:class:`Node`): A binary tree root.

    Yields:
        :obj:`tuple` of :obj:`Node`: A copy of every node from the root to a leaf.
    '''
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

# Miscellaneous functions for Node objects.

def is_node(obj):
    """Check if `obj` is an instance of Node.
    Args:
        obj: Any old object.

    Return:
        bool: True if `obj` is indeed a :class:`Node`, False otherwise.
    """
    return isinstance(obj, Node)

def is_leaf_node(node):
    """Check if `node` is a leaf node.
    Args:
        node (:class:`Node`): Any node.

    Return:
        bool: True if `node` has no more children, False otherwise.
    """
    return node.left is node.right is None

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
            for side in _sides:
                next_level.append(getattr(node, side, None))
            if values != values[::-1]:
                return False
        level = next_level
    return True

def has_path_sum(node, value):
    """Determine if a binary tree contains a root-to-leaf path that sums to `value`.
    
    Args:
        node (:class:`Node`): A binary tree root.

    Returns:
        bool: True if a path that sums to `value` exists, False otherwise.
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
    from time import sleep

    def print_in(*args):
        print(">>>", *args)

    def print_out(*args, **kwargs):
        if not any(isinstance(arg, (list, tuple)) for arg in args):
            print(*args, **kwargs)
        else:
            for arg in args:
                if not any(isinstance(arg, (list, tuple)) for arg in arg):
                    print(*map(str, arg), sep=", ")
                else:
                    print_out(*arg)

    def print_dashes(width):
        print("".join("-" for i in range(width)))

    commands = [
        "tree_string",
        "repr(Node.from_string(tree_string))",
        "list(traverse_pre_order(root))",
        "list(traverse_in_order(root))",
        "list(traverse_post_order(root))",
        "list(traverse_level_order(root))",
        "get_max_depth(root)",
        "is_symmetric(root)",
        "list(get_all_paths(root))",
        "has_path_sum(root, 22)",
        "repr(Node.from_in_pre_orders(in_order, pre_order))",
        "repr(Node.from_in_post_orders(in_order, post_order))",
        ]
    
    def print_commands():
        width = max(map(len, commands)) + 4
        print_dashes(width)
        print("Methods:")
        print("\n".join("{:2}: {}".format(index, command) for index, command in enumerate(commands)))
        print_dashes(width)

    help_text = \
"""The binary tree can consist of all numbers or all alphabets.

Node values should be separated by commas.

Absent nodes can be indicated with 'null' or an immediate comma.
For example, "1,2,,3,4" is equivalent to "1,2,null,3,4".

The binary tree will be constructed in level order."""

    def print_help():
        width = max(map(len, help_text.splitlines()))
        print_dashes(width)
        print("Help:")
        print(help_text)
        print_dashes(width)

    def main():
        while True:
            tree_string = str(input("Enter a binary tree, 'h' for help, or 'q' to quit:\n"))
            if tree_string == "q":
                return
            if tree_string == "h":
                print_help()
                continue
            root = Node.from_string(tree_string)
            if root is None:
                print("Empty string. Please try again.")
                continue
            pre_order = list(traverse_pre_order(root))
            in_order = list(traverse_in_order(root))
            post_order = list(traverse_post_order(root))
            print_commands()
            while True:
                choice = slice(None)
                response = str(input(\
"""Type 'r' to reset the tree, or 'q' to quit.
To view the methods again, type 'm'.
Select a method, or 'a' for all: """))
                if response == "q":
                    return
                elif response == "r":
                    break
                elif response in map(str, range(len(commands))):
                    choice = slice(int(response), int(response)+1)
                elif response != "a":
                    if response == "m": 
                        print_commands()
                    else:
                        print("Invalid index. Please try again.")
                    continue
                for command in commands[choice]:
                    print_in(command)
                    exec("print_out(" + command + ")")
    main()
    print("Goodbye!")

