#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests binary_tree module."""

import pytest
from binary_tree import *

tree_string = "1,2,3,4,,5,6"
repr_string = "Node(1, Node(2, Node(4)), Node(3, Node(5), Node(6)))"
in_order = [4,2,1,5,3,6]
pre_order = [1,2,4,3,5,6]
post_order = [4,2,5,6,3,1]

def is_correct(node):
    assert repr(node) == repr_string
    assert node.value == 1
    assert node.left.value == 2
    assert node.right.value == 3
    assert node.left.left.value == 4
    assert node.left.right is None
    assert node.right.left.value == 5
    assert node.right.right.value == 6
    return True

@pytest.fixture
def node_from_string():
    """Test Node.from_string constructor."""
    return Node.from_string(tree_string)

def test_node_from_string(node_from_string):
    """Check the tree structure."""
    assert is_correct(node_from_string)
    
@pytest.fixture
def node_from_in_pre_orders():
    """Test Node.from_orders (in-pre) constructor."""
    return Node.from_orders("in-pre", in_order, pre_order)

def test_node_from_in_pre_orders(node_from_in_pre_orders):
    """Check the tree structure."""
    assert is_correct(node_from_in_pre_orders)

@pytest.fixture
def node_from_in_post_orders():
    """Test Node.from_orders (in-post) constructor."""    
    return Node.from_orders("in-post", in_order, post_order)

def test_node_from_in_post_orders(node_from_in_post_orders):
    """Check the tree structure."""
    assert is_correct(node_from_in_post_orders)
        
