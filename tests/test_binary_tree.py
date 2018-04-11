#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests the `from_string` method of `Node`."""

import pytest

from binary_tree import Node

@pytest.fixture
def response():
    """Test from_string constructor."""
    treestring = "1, 2, 3, 4, 5, null, 6, 7"
    return Node.from_string(treestring)

def test_content(response):
    """Check the tree structure."""
    assert response.value == 1
    assert (response.left).value == 2
    assert (response.right).value == 3
    assert ((response.left).left).value == 4
    assert ((response.left).right).value == 5
    assert ((response.right).right).value == 6
    assert (((response.left).left).left).value == 7

