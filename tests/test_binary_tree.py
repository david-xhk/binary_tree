#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for the binary_tree module."""

import pytest
from binary_tree import *

tree_string = "1,2,3,4,,5,6"
repr_string = "Node(1, Node(2, Node(4)), Node(3, Node(5), Node(6)))"
in_order = [4,2,1,5,3,6]
pre_order = [1,2,4,3,5,6]
post_order = [4,2,5,6,3,1]

def is_correct(root):
    assert repr(root) == repr_string
    assert root.value == 1
    assert root.left.value == 2
    assert root.right.value == 3
    assert root.left.left.value == 4
    assert root.left.right is None
    assert root.right.left.value == 5
    assert root.right.right.value == 6
    return True

@pytest.fixture
def tree_from_Node():
    """Test Node constructor."""
    left_branch = Node(2, left=Node(4))
    right_branch = Node(3, left=Node(5), right=Node(6))
    root = Node(1, left=left_branch, right=right_branch)
    return root

def test_tree_from_Node(tree_from_Node):
    """Check the tree structure."""
    assert is_correct(tree_from_Node)

@pytest.fixture
def tree_from_string():
    """Test tree_from_string constructor."""
    return from_string(tree_string)

def test_tree_from_string(tree_from_string):
    """Check the tree structure."""
    assert is_correct(tree_from_string)
    
@pytest.fixture
def tree_from_in_pre_orders():
    """Test tree_from_orders (in-pre) constructor."""
    return from_orders("in-pre", in_order, pre_order)

def test_tree_from_in_pre_orders(tree_from_in_pre_orders):
    """Check the tree structure."""
    assert is_correct(tree_from_in_pre_orders)

@pytest.fixture
def tree_from_in_post_orders():
    """Test tree_from_orders (in-post) constructor."""    
    return from_orders("in-post", in_order, post_order)

def test_tree_from_in_post_orders(tree_from_in_post_orders):
    """Check the tree structure."""
    assert is_correct(tree_from_in_post_orders)
        
