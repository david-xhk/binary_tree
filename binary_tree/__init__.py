"""binary_tree provides a Node object and useful tools for processing a binary tree data structure

Example:
    ::

        import binary_tree as tree

        node = tree.Node.from_string("1,2,,3,4,,5")
        
        in_order = [node.value for node in tree.traverse("in", node)]
        pre_order = [node.value for node in tree.traverse("pre", node)]
        node2 = Node.from_orders("in-pre", in_order, pre_order)

>>> node == node2
True
"""

__author__ = 'Han Keong'
__email__ = 'hk997@live.com'
__version__ = '0.0.4'

from .node import *
del node

from .tree import *
del tree
