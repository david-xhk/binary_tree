#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests the `from_string` method of `Node`."""

import pytest

@pytest.fixture
def node():
    """Test from_string constructor."""
    from binary_tree import Node
    tree_string = "1,2,3,null,4"
    return Node.from_string(tree_string)

def test_content(node):
    """Check the tree structure."""
    assert node.value == 1

    left_node = node.left
    assert left_node.value == 2
    assert left_node.left is None
    assert left_node.right.value == 4

    assert node.right.value == 3

