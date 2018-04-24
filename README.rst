*******
 About
*******

.. automodule:: binary_tree

==============
 Installation
==============

To install binary_tree, run this in your terminal::

    $ pip install git+git://github.com/han-keong/binary_tree

==========
 Features
==========

.. contents:: 
    :local:

-----------------------
 Importing binary_tree
-----------------------

The conventional way of importing from :mod:`binary_tree` is to do::

    from binary_tree import Node, node, tree

You may also want to import all functions directly::

    from binary_tree import *

---------------
 Making a Node
---------------

Node attributes
^^^^^^^^^^^^^^^
Every :class:`~binary_tree.Node` has the following attributes:

* Stored value

  * :ivar:`~binary_tree.Node.value`

* Children nodes
  
  * :ivar:`~binary_tree.Node.left`
  * :ivar:`~binary_tree.Node.right`

* Neighbour nodes
  
  * :ivar:`~binary_tree.Node.prev`
  * :ivar:`~binary_tree.Node.next`

* Parent node

  * :ivar:`~binary_tree.Node.parent`

.. note::
    The parent, children, and neighbour nodes should be instances of Node if they are present. 

Node initialization
^^^^^^^^^^^^^^^^^^^
When initializing a :class:`~binary_tree.Node`, a :ivar:`~binary_tree.Node.value` must be provided. 

>>> left_node = Node(2)

Meanwhile, the other attributes can be set using keyword arguments.

>>> parent_node = Node(1, left=left_node)

Setting Node attributes
^^^^^^^^^^^^^^^^^^^^^^^
Attributes that are reciprocative are set automatically.

For example, when you set a child node, its parent is also set behind the scenes.

>>> left_node.parent is parent_node
True

>>> right_node = Node(3)
>>> parent_node.right = right_node
>>>
>>> right_node.parent is parent_node
True

Likewise, setting a neighbour node will affect the corresponding neighbour node.

>>> right_node.prev = left_node
>>>
>>> left_node.next is right_node
True

-----------------
 Checking a Node
-----------------

The following functions can be used to check if a :class:`~binary_tree.Node` has certain properties.

is_node()
^^^^^^^^^
:func:`node.is_node() <binary_tree.node.is_node>` checks if an object is an instance of :class:`~binary_tree.Node`.

>>> node.is_node(parent_node)
True

is_left()
^^^^^^^^^
:func:`node.is_left() <binary_tree.node.is_left>` checks if an instance of :class:`~binary_tree.Node` is a left child.

>>> node.is_left(parent_node.left)
True

is_right()
^^^^^^^^^^
:func:`node.is_right() <binary_tree.node.is_right>` checks if an instance of :class:`~binary_tree.Node` is a right child.

>>> node.is_right(parent_node.right)
True

is_leaf()
^^^^^^^^^
:func:`node.is_leaf() <binary_tree.node.is_leaf>` checks if an instance of :class:`~binary_tree.Node` is a leaf node.

>>> node.is_leaf(parent_node.right)
True

is_root()
^^^^^^^^^
:func:`node.is_root() <binary_tree.node.is_root>` checks if an instance of :class:`~binary_tree.Node` is a root node.

>>> node.is_root(parent_node):
True

is_orphan()
^^^^^^^^^^^
:func:`node.is_orphan() <binary_tree.node.is_orphan>` checks if an instance of :class:`~binary_tree.Node` is an orphan node.

>>> lonely_node = Node(1)
>>> node.is_orphan(lonely_node)
True

Equality tests
^^^^^^^^^^^^^^
Nodes have a special way of testing :meth:`equality <binary_tree.Node.__eq__>`, which is to tentatively compare the :ivar:`~binary_tree.Node.value` of itself and the other object. 

If the other object does not have a :ivar:`~binary_tree.Node.value` attribute, the object itself is taken as the basis of comparison. 

This allows the following comparisons to work:

>>> parent_node == Node(1)
True

>>> parent_node == 1
True

If you would like to test if two nodes have the same tree structure, you may compare their :meth:`repr <binary_tree.Node.__repr__>` strings.

>>> parent_node2 = Node(1, left=Node(2), right=Node(3))
>>> 
>>> repr(parent_node) == repr(parent_node2)
True

------------------------
 Setting up a Node tree 
------------------------

from_string()
^^^^^^^^^^^^^
A tree string should be in level-order and separated by commas.

>>> tree_string = "1,2,3,4,5,6"

Empty spaces can be represented by an immediate comma or "null" to be explicit.

>>> tree_string = "1,2,3,4,,5,6"
>>> tree_string = "1,2,3,4,null,5,6"

Pass the string into :func:`tree.from_string() <binary_tree.tree.from_string>` to generate a binary tree.

>>> root = tree.from_string(tree_string)

You can use :meth:`repr <binary_tree.Node.__repr__>` to see a representation of the tree structure created.

>>> repr(root)
"Node(1, left=Node(2, left=Node(4)), right=Node(3, left=Node(5), right=Node(6)))"

from_orders()
^^^^^^^^^^^^^
Another way to set up a binary tree is with its in-order and pre-order traversals.

>>> in_order = [4,2,1,5,3,6]
>>> pre_order = [1,2,4,3,5,6]

Pass the appropriate key and the traversals into :func:`tree.from_orders() <binary_tree.tree.from_orders>` to reconstruct the original tree structure.

>>> root = tree.from_orders("in-pre", in_order, pre_order)
>>> repr(root)
"Node(1, left=Node(2, left=Node(4)), right=Node(3, left=Node(5), right=Node(6)))"

Alternatively, you can use the in-order and post-order traversal.

>>> post_order = [4,2,5,6,3,1]
>>> root = tree.from_orders("in-post", in_order, post_order)
>>>
>>> repr(root)
"Node(1, left=Node(2, left=Node(4)), right=Node(3, left=Node(5), right=Node(6)))"

.. note::
    There should not be duplicates present in `in_order` and `pre_order` or `post_order`.

connect_nodes()
^^^^^^^^^^^^^^^
When using the above methods to construct a binary tree, the neighbour nodes in each level are already connected using :func:`tree.connect_nodes() <binary_tree.tree.connect_nodes>`.

You may use this function again to reconfigure a tree after modifying it, or to connect one that was manually set up.

>>> root.right.right = None  # Prune the right branch of the right node
>>> tree.connect_nodes(root)

to_string()
^^^^^^^^^^^
Just as a tree can be constructed from string, it can be deconstructed back into one too, using :func:`tree.to_string() <binary_tree.tree.to_string>`.

>>> tree.to_string(root)
"1,2,3,4,,5"

------------------------
 Traversing a Node tree
------------------------

With a tree structure set up, there are several functions you can use to traverse it.

traverse_pre_order()
^^^^^^^^^^^^^^^^^^^^
:func:`tree.traverse_pre_order() <binary_tree.tree.traverse_pre_order>` traverses a binary tree in pre-order.

>>> list(tree.traverse_pre_order(root))
[Node(1), Node(2), Node(4), Node(3), Node(5)]

traverse_in_order()
^^^^^^^^^^^^^^^^^^^
:func:`tree.traverse_in_order() <binary_tree.tree.traverse_in_order>` traverses a binary tree in in-order.

>>> list(tree.traverse_in_order(root))
[Node(4), Node(2), Node(1), Node(5), Node(3)]

traverse_post_order()
^^^^^^^^^^^^^^^^^^^^^
:func:`tree.traverse_post_order() <binary_tree.tree.traverse_post_order>` traverses a binary tree in post-order.

>>> list(tree.traverse_post_order(root))
[Node(4), Node(2), Node(5), Node(3), Node(1)]

traverse_level_order()
^^^^^^^^^^^^^^^^^^^^^^
:func:`tree.traverse_level_order() <binary_tree.tree.traverse_level_order>` traverses a binary tree in level-order.

>>> list(tree.traverse_level_order(root))
[[Node(1)], [Node(2), Node(3)], [Node(4), Node(5)]]

.. note::
    traverse_level_order() will yield lists of Nodes, each representing a level in the tree.

traverse()
^^^^^^^^^^
A single dispatch function, :func:`tree.traverse() <binary_tree.tree.traverse>`, is available for convenience.

>>> list(tree.traverse(root, "pre"))
[Node(1), Node(2), Node(4), Node(3), Node(5)]

>>> list(tree.traverse(root, "in"))
[Node(4), Node(2), Node(1), Node(5), Node(3)]

>>> list(tree.traverse(root, "post"))
[Node(4), Node(2), Node(5), Node(3), Node(1)]

>>> list(tree.traverse(root, "level"))
[[Node(1)], [Node(2), Node(3)], [Node(4), Node(5)]]

Iterating over a Node
^^^^^^^^^^^^^^^^^^^^^
You can also :meth:`iterate <binary_tree.Node.__iter__>` over an instance of :class:`~binary_tree.Node` to traverse its tree structure. ::

    >>> for node in root:
    ...     print(node)
    Node(1)
    Node(2)
    Node(3)
    Node(4)
    Node(5)

.. note::
    Iterating over a Node goes by level-order traversal. 

-----------------------
 Analyzing a Node tree
-----------------------

The following functions are available to find certain properties of a binary tree.

is_symmetrical()
^^^^^^^^^^^^^^^^
:func:`tree.is_symmetrical() <binary_tree.tree.is_symmetrical>` checks for symmetry in a binary tree.

>>> tree.is_symmetrical(root)
False

max_depth()
^^^^^^^^^^^
:func:`tree.max_depth() <binary_tree.tree.max_depth>` calculates the maximum depth of a binary tree.

>>> tree.max_depth(root)
3

get_path()
^^^^^^^^^^
:func:`tree.get_path() <binary_tree.tree.get_path>` traces the ancestry of a node.

>>> tree.get_path(root.right.left)
[Node(1), Node(3), Node(5)]

all_paths()
^^^^^^^^^^^
:func:`tree.all_paths() <binary_tree.tree.all_paths>` finds every leaf path in a binary tree. ::

    >>> for path in tree.all_paths(root):
    ...     print(path)
    [Node(1), Node(2), Node(4)]
    [Node(1), Node(3), Node(5)]

.. note::
    all_paths() searches for paths using post-order traversal.

has_sum()
^^^^^^^^^
:func:`tree.has_sum() <binary_tree.tree.has_sum>` determines if there is a path that adds up to a certain value.

>>> tree.has_sum(root, 7)
True

find_path()
^^^^^^^^^^^
:func:`tree.find_path() <binary_tree.tree.find_path>` finds the path of some node in a binary tree.

>>> tree.find_path(5)
[Node(1), Node(3), Node(5)]

>>> tree.find_path(2)
[Node(1), Node(2)]

get_lca()
^^^^^^^^^
:func:`tree.get_lca() <binary_tree.tree.get_lca>` gets the lowest common ancestor of two or more nodes in a binary tree.

>>> tree.get_lca(root, 2, 4)
Node(2)

>>> tree.get_lca(root, 1, 3, 5)
Node(1)

.. note::
    Since Nodes :ref:`test for equality tentatively <Equality tests>`, it is possible to exploit this by simply passing in the value of the node you wish to refer to, provided that *the value is unique within the tree*.

=========
 Credits
=========

binary_tree was written by Han Keong <hk997@live.com>.

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

