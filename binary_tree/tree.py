#!/usr/bin/env python3
"""
Binary tree implementation.
For a demonstration, run "./tree treestring".

Done by Han Keong
Created on 10/04/2018 2251 +0800
Last updated on 11/04/2018 1402 +0800
"""

from . import *

if __name__ == "__main__":
  def listen_lines():
        while True:
            line = input("Enter a binary tree:\n")
            if line:
                yield line
            else:
                print("Goodbye!")
                return
    
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

    commands = [
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
    ]
    
    for treestring in listenLines():
        root = Node.from_string(treestring)
        if not root:
            print("Invalid treestring.")
            continue
        preorder = list(traverse_pre_order(root))
        inorder = list(traverse_in_order(root))
        postorder = list(traverse_post_order(root))
        for command in commands:
            print_in(command)
            exec(f"print_out({command})")
        print()

