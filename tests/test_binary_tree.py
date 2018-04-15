#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests binary_tree module."""

import pytest
from binary_tree import *

@pytest.fixture
def node_from_string():
    """Test Node.from_string constructor."""
    tree_string = "1,2,3,4,,5,6"
    return Node.from_string(tree_string)

def test_node_from_string(node_from_string):
    """Check the tree structure."""
    assert node_from_string.value == 1
    assert node_from_string.left.value == 2
    assert node_from_string.right.value == 3
    assert node_from_string.left.left.value == 4
    assert node_from_string.left.right is None
    assert node_from_string.right.left.value == 5
    assert node_from_string.right.right.value == 6

@pytest.fixture
def node_from_in_pre_orders():
    """Test Node.from_orders (in-pre) constructor."""
    in_order = [4,2,1,5,3,6]
    pre_order = [1,2,4,3,5,6]
    return Node.from_orders("in-pre", in_order, pre_order)

def test_node_from_in_pre_orders(node_from_in_pre_orders):
    """Check the tree structure."""
    assert node_from_in_pre_orders.value == 1
    assert node_from_in_pre_orders.left.value == 2
    assert node_from_in_pre_orders.right.value == 3
    assert node_from_in_pre_orders.left.left.value == 4
    assert node_from_in_pre_orders.left.right is None
    assert node_from_in_pre_orders.right.left.value == 5
    assert node_from_in_pre_orders.right.right.value == 6

@pytest.fixture
def node_from_in_post_orders():
    """Test Node.from_orders (in-post) constructor."""
    in_order = [4,2,1,5,3,6]
    post_order = [4,2,5,6,3,1]
    return Node.from_orders("in-post", in_order, post_order)

def test_node_from_in_post_orders(node_from_in_post_orders):
    """Check the tree structure."""
    assert node_from_in_post_orders.value == 1
    assert node_from_in_post_orders.left.value == 2
    assert node_from_in_post_orders.right.value == 3
    assert node_from_in_post_orders.left.left.value == 4
    assert node_from_in_post_orders.left.right is None
    assert node_from_in_post_orders.right.left.value == 5
    assert node_from_in_post_orders.right.right.value == 6

