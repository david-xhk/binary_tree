#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests the `from_string` method of `Node`."""

import pytest

from binary_tree import Node

@pytest.fixture
def response():
    """Test from_string constructor."""
    tree_string = "1, 2, 3, 4, 5, null, 6, 7"
    return Node.from_string(tree_string)

def test_content(response):
    """Check the tree structure."""
    assert response.value == 1
    left_node = response.left
    assert left_node.value == 2
    right_node = response.right
    assert right_node.value == 3

    leftleft_node = left_node.left
    assert leftleft_node.value == 4
    leftright_node = left_node.right
    assert leftright_node.value == 5

    rightleft_node = right_node.left
    assert rightleft_node is None
    rightright_node = right_node.right
    assert rightright_node.value == 6

    leftleftleft_node = leftleft_node.left
    assert leftleftleft_node.value == 7
