#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This module contains a demonstration for the Node interface."""

from tools import Demo
from node import *

class NodeDemo(Demo):
    help_text = """\
Node has the following attributes:
    'value', the inherent value.
    'left' and 'right', the children nodes.
    'prev' and 'next', the neighbour nodes.
    'parent', the parent node.

To create a Node, pass a value into its constructor.
The other attributes can be set on initialization using keyword arguments.
* Keyword values should only be instances of Node.

Reciprocative pointers will be set automatically. For example:
    foo.left = bar will also set bar.parent to foo.
    spam.prev = eggs will also set eggs.next to spam."""

    setup_prompt = "Select an option, or press 'enter' to continue.\n"

    setup_code = """\
left_branch = Node(2, left=Node(4))
right_branch = Node(3, left=Node(5), right=Node(6))
node = Node(1, left=left_branch, right=right_branch)"""

    commands = [
        "str(node)",
        "repr(node)",
        "node.value, type(node.value)",
        "node is node.left.parent",
        "node == Node(1), node == 1",
        "is_node(node), is_node(1)",
        "is_left(node.left), is_right(node.right)",
        "is_root(node), is_root(node.left)",
        "is_leaf(node.left), is_leaf(node.right.left)",
        "is_orphan(node), is_orphan(Node(4))",
        ]


if __name__ == "__main__":
    demo = NodeDemo()
    demo.run()

