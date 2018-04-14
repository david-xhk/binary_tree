#!/usr/bin/env python3
"""This module contains demos for binary_tree."""

# To allow absolute imports
import sys, os

def pardir(path, level=1):
    for i in range(level):
        path = os.path.dirname(path)
    return os.path.abspath(path)

sys.path.insert(0, pardir(__file__, 2))

from binary_tree import *
from demo import Demo, DemoRestart


class BinaryTreeDemo(Demo):
    setup_text = "Enter a binary tree:\n"

    help_text = "\n\n".join([
        "The binary tree should consist of numbers.",
        "Node values should be separated by commas.",
        "Indicate absent nodes with 'null' or an immediate comma.\n"
        "For example, \"1,2,,3,4\" is equivalent to \"1,2,null,3,4\".",
        "The binary tree will be constructed in level order."])

    def setup_context(self, tree_string):
        root = Node.from_string(tree_string)
        if root is None:
            raise DemoRestart("Missing root value. Please try again.")
        pre_order = [node.value for node in traverse_pre_order(root)]
        in_order = [node.value for node in traverse_in_order(root)]
        post_order = [node.value for node in traverse_post_order(root)]
        return globals(), locals()


class NodeDemo(BinaryTreeDemo):
    commands = [
        "tree_string",
        "Node.from_string(tree_string)",
        "str(root), repr(root)",
        "root.value, type(root.value)",
        "root.left, is_node(root.left), is_leaf(root.left)",
        "root.left == root.right",
        "in_order, pre_order",
        "repr(Node.from_orders(\"in-pre\", in_order, pre_order))",
        "in_order, post_order",
        "repr(Node.from_orders(\"in-post\", in_order, post_order))"]


class TreeDemo(BinaryTreeDemo):
    commands = [
        "tree_string, repr(root)",
        "list(traverse_pre_order(root))",
        "list(traverse_in_order(root))",
        "list(traverse_post_order(root))",
        "list(traverse_level_order(root))",
        "list(traverse(\"level\", root))",
        "get_max_depth(root)",
        "is_symmetrical(root)",
        "list(get_all_paths(root))",
        "has_path_sum(root, 12)"]


if __name__ == "__main__":
    while True:
        choice = input(
            "Enter \"1\" for a demo on the Node class,\n"
            "or \"2\" for a demo on binary tree functions: ")
        if choice == "1":
            demo = NodeDemo()
        elif choice == "2":
            demo = TreeDemo()
        else:
            print("Invalid input.")
            continue
        break
    demo.run()

