#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This module contains a demonstration for binary tree functions."""

from tools import insert_parent_dir, Demo
insert_parent_dir(2)

from binary_tree.tree import *

class TreeDemo(Demo):
    help_text = """\
A binary tree string should:
    Consist of numbers.
    Be separated by commas.
* The tree will be constructed in level order.

Indicate absent nodes with "null" or an immediate comma.
    "1,2,,3,4" is equivalent to "1,2,null,3,4".

The root node (i.e. first number) should not be empty.
    ",1,2,3,4" will not work as its root is empty."""

    setup_prompt = "Select an option, or enter a binary tree string:\n"

    setup_code = """\
root = from_string(response)
if root is None:
    demo.restart("Missing root value. Please try again.")"""

    commands = [
        "in_order = list(traverse_in_order(root))",
        "pre_order = list(traverse_pre_order(root))",
        "post_order = list(traverse_post_order(root))",
        "root2 = from_orders(\"in-pre\", in_order, pre_order)",
        "root3 = from_orders(\"in-post\", in_order, post_order)",
        "for tree in (root, root2, root3):\n"
        "    print(repr(tree))",
        "list(traverse_level_order(root))",
        "list(traverse(root, \"level\"))",
        "get_max_depth(root)",
        "is_symmetrical(root)",
        "list(get_all_paths(root))",
        "has_path_sum(root, 12)",
        ]


if __name__ == "__main__":
    demo = TreeDemo()
    demo.run()

