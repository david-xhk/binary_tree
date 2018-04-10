#!/usr/bin/env python3
"""
Demonstration of binary tree.

Done by Han Keong
Created on 10/04/2018 2251 +0800
Last updated on 11/04/2018 0050 +0800
"""

from node import Node
from traversals import traverse_pre_order, traverse_in_order, traverse_post_order, traverse_level_order
from helpers import get_max_depth, get_all_paths
from misc import is_symmetric, has_path_sum


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


def listen_lines():
    while True:
        line = input("Enter a binary tree:\n")
        if line:
            yield line
        else:
            print("Goodbye!")
            return


given_lines = (
    "1, 2, 3, 4, 5, 6, 7, 8",
    "1, null, 2, 3",
    "3, 9, 20, null, null, 15, 7",
    "1, 2, 2, 3, 4, 4, 3",
    "1, 2, 2, null, 3, null, 3",
    "5, 4, 8, 11, 13, 4, 7, 2, null, 1",
    )

lines_slice = slice(None)


commands = (
    "treestring",
    "repr(Node.from_string(treestring))",
    "list(traverse_pre_order(root))",
    "list(traverse_in_order(root))",
    "list(traverse_post_order(root))",
    "list(traverse_level_order(root))",
    "get_max_depth(root)",
    "is_symmetric(root)",
    "list(get_all_paths(root))",
    "has_path_sum(root, 22)",
    "repr(Node.from_in_pre_orders(inorder, preorder))",
    "repr(Node.from_in_post_orders(inorder, postorder))",
    )

commands_slice = slice(None)


show = True

if __name__ == '__main__' and show:
    # for tree in listenLines():
    for treestring in given_lines[lines_slice]:
        root = Node.from_string(treestring)
        preorder = list(traverse_pre_order(root))
        inorder = list(traverse_in_order(root))
        postorder = list(traverse_post_order(root))
        for command in commands[commands_slice]:
            print_in(command)
            exec(f"print_out({command})")
        print()
            
