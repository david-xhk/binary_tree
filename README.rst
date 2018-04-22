*****
About
*****

binary_tree provides a Node object and some useful tools for a binary tree data structure.

========
Features
========

.. toctree::
    :maxdepth: 2

=====
Usage
=====

---------
Importing
---------

To use the functions provided by :mod:`binary_tree`, you can do the following import::

    import binary_tree as tree

If you would like to use :class:`~binary_tree.Node` on its own, you may also write::
    
    from binary_tree import Node

-------------
Making a node 
-------------

To create an instance, pass a value into :class:`~binary_tree.Node`.

>>> left_node = Node(1)

Nodes have the following attributes:

* Children nodes
  
  * :attr:`~binary_tree.Node.left`
  * :attr:`~binary_tree.Node.right`

* Neighbour nodes
  
  * :attr:`~binary_tree.Node.prev`
  * :attr:`~binary_tree.Node.next`

* Parent node

  * :attr:`~binary_tree.Node.parent`

These attributes are supposed to be instances of :class:`~binary_tree.Node` themselves if they are present. They can be set on initialization using keyword arguments.

>>> parent_node = Node(3, left=left_node)

Reciprocative relationships will be set automatically. For example, when you set a child node, its parent is automatically set for you.

>>> right_node = Node(2)
>>> parent_node.right = right_node
>>> right_node.parent is parent_node
True

Likewise, setting a neighbour node will affect the corresponding neighbour node.

>>> right_node.prev = left_node
>>> left_node.next is right_node
True

---------------
Checking a node
---------------

The following functions can be used to check if a node has certain properties.

* :func:`~binary_tree.is_node`

>>> tree.is_node(parent_node)
True

* :func:`~binary_tree.is_left`

>>> tree.is_left(parent_node.left)
True

* :func:`~binary_tree.is_right`

>>> tree.is_right(parent_node.right)
True

* :func:`~binary_tree.is_leaf`

>>> tree.is_leaf(parent_node.right)
True

* :func:`~binary_tree.is_root`

>>> tree.is_root(parent_node):
True

* :func:`~binary_tree.is_orphan`

>>> lonely_node = Node(1)
>>> tree.is_orphan(lonely_node)
True

Nodes have a special way of testing equality, which is to tentatively compare its own value with the other object's value. 

If the other object does not have a `value` attribute, the object itself is taken as the basis of comparison. 

This allows the following comparisons to work:

>>> root = Node(1)
True

>>> root = 1
True

------------------------
Setting up a binary tree 
------------------------

To generate a binary tree, you can pass in a string of values into :func:`~binary_tree.from_string`.

>>> tree_string = "1,2,3,4,,5,6"
>>> root = tree.from_string(tree_string)
>>> repr(root)
"Node(1, left=Node(2, left=Node(4)), right=Node(3, left=Node(5), right=Node(6)))"

.. note::
    
    from_string() will grow the tree structure in **level-order**.

Another way is with an in-order and pre-order traversal using :func:`~binary_tree.from_orders`, which reconstructs the original tree structure.

>>> in_order = [4,2,1,5,3,6]
>>> pre_order = [1,2,4,3,5,6]
>>> root = tree.from_orders("in-pre", in_order, pre_order)
>>> repr(root)
"Node(1, left=Node(2, left=Node(4)), right=Node(3, left=Node(5), right=Node(6)))"

Alternatively, you can use an in-order and post-order traversal.

>>> post_order = [4,2,5,6,3,1]
>>> repr(root)
"Node(1, left=Node(2, left=Node(4)), right=Node(3, left=Node(5), right=Node(6)))"

.. note::
    
    There should not be duplicates present in `in_order` and `pre_order` or `post_order`.

When using the above methods to construct a binary tree, the neighbour nodes in each level will be automatically connected for you using :func:`~binary_tree.connect_nodes`.

You may use this function again to reconfigure a tree after it is modified. 

>>> root.right.right = None  # Prune the right branch of the right node
>>> tree.connect_nodes(root)

Just as a tree can be constructed from string, it can be deconstructed back into one too, using :func:`~binary_tree.to_string`.

>>> tree.to_string(root)
"1,2,3,4,,5"

------------------------
Traversing a binary tree
------------------------

With a tree set up, there are several functions you can use to traverse down the tree.

* :func:`pre-order <binary_tree.traverse_pre_order>`

>>> for node in tree.traverse_pre_order(root):
>>>     print(node)
Node(1)
Node(2)
Node(4)
Node(3)
Node(5)

* :func:`in-order <binary_tree.traverse_in_order>`

>>> for node in tree.traverse_in_order(root):
>>>     print(node)
Node(4)
Node(2)
Node(1)
Node(5)
Node(3)

* :func:`post-order <binary_tree.traverse_post_order>`

>>> for node in tree.traverse_post_order(root):
>>>     print(node)
Node(4)
Node(2)
Node(5)
Node(3)
Node(1)

* :func:`level-order <binary_tree.traverse_level_order>`

>>> for level in tree.traverse_level_order(root):
>>>     for node in level:
>>>           print(node)
Node(1)
Node(2)
Node(3)
Node(4)
Node(5)

.. note::
    
    traverse_level_order() will output a list of lists, each representing a level in the tree.

Level-order is also the default mode of traversal when iterating over a root node.

>>> for node in root:
>>>     print(node)
Node(1)
Node(2)
Node(3)
Node(4)
Node(5)

A single dispatch function, :func:`~binary_tree.traverse`, is available for your convenience.

>>> for node in tree.traverse(root, "pre"):
>>>     print(node)
Node(1)
Node(2)
Node(4)
Node(3)
Node(5)

>>> for node in tree.traverse(root, "in"):
>>>     print(node)
Node(4)
Node(2)
Node(1)
Node(5)
Node(3)

>>> for node in tree.traverse(root, "post"):
>>>     print(node)
Node(4)
Node(2)
Node(5)
Node(3)
Node(1)

>>> for level in tree.traverse(root, "level"):
>>>     print(level)
[Node(1)]
[Node(2), Node(3)]
[Node(4), Node(5)]

-----------------------
Analyzing a binary tree
-----------------------

The following functions are available to find certain properties of a binary tree.

* :func:`~binary_tree.is_symmetrical`

>>> tree.is_symmetrical(root)
False

* :func:`~binary_tree.get_max_depth`
    
>>> tree.get_max_depth(root)
3

* :func:`~binary_tree.get_path`

>>> tree.get_path(root.right.left)
[Node(1), Node(3), Node(5)]

* :func:`~binary_tree.get_all_paths`

>>> for path in tree.get_all_paths(root):
>>>     print(path)
[Node(1), Node(2), Node(4)]
[Node(1), Node(3), Node(5)]

.. note::

    get_all_paths() will search for paths using post-order traversal.

* :func:`~binary_tree.has_path_sum`

>>> tree.has_path_sum(root, 7)
True

* :func:`~binary_tree.find_path`

>>> tree.find_path(5)
[Node(1), Node(3), Node(5)]

>>> tree.find_path(2)
[Node(1), Node(2)]

* :func:`~binary_tree.get_lca`

>>> tree.get_lca(root, 2, 4)
Node(2)

>>> tree.get_lca(root, 1, 3, 5)
Node(1)

.. note::

    Since Node compares for equality tentatively, it is possible to exploit this by simply passing in the value of the Node you wish to refer to, *provided that the value is unique within the tree*.

=======
Credits
=======

binary_tree was written by Han Keong <hk997@live.com>.

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

