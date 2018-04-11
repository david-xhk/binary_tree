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
    assert node.left.value == 2
    assert node.right.value == 3
    assert node.left.left is None
    assert node.left.right.value == 4
