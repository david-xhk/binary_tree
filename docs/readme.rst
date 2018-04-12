*****
About
*****

binary_tree.py provides a ``Node`` object and some useful tools like constructors and tree traversals for a binary tree data structure.


========
Features
========

* Construct a binary tree using 

  * String
  * In-order and pre-order traversal
  * In-order and post-order traversal

* Traverse a binary tree by 
    
  * Pre-order
  * In-order
  * Post-order
  * Level-order

* Get from a binary tree

  * All root-to-leaf paths
  * The maximum depth

* Check if a binary tree
   
  * Is symmetrical
  * Has a certain path sum


=====
Usage
=====

-------
Imports
-------

To use the functions provided by :mod:`binary_tree`, you can do the following import::

    import binary_tree as tree


If you would like to use :class:`~binary_tree.Node` on its own, you may also do this::
    
    from binary_tree import Node

-------------
Node creation
-------------

Pass a value into :class:`~binary_tree.Node` to create an instance. ::
    
    node = Node(1)

Nodes have a :attr:`~binary_tree.Node.left` and a :attr:`~binary_tree.Node.right` attribute which are expected to be instances of :class:`~binary_tree.Node`. They can be set on initialization. ::

    another_node = Node(2)
    parent_node = Node(3, node, another_node)

However, manually setting up a binary tree structure is tedious. A more preferable way of generating one is to pass in a string of values to the :func:`~binary_tree.Node.from_string` constructor. ::

    tree_string = "1,2,3,4,,5,6"
    root = Node.from_string(tree_string)

Take note that this method will generate a binary tree structure in `level-order`.

Another way to construct a binary tree is from its in-order and pre-order traversals. You can regenerate the original tree structure using :func:`~binary_tree.Node.from_in_pre_orders`. ::

    inorder = "4,2,1,5,3,6"
    preorder = "1,2,4,3,5,6"
    root = Node.from_in_pre_orders(inorder, preorder)

Alternatively, you can use in-order and post-order traversals with :func:`~binary_tree.Node.from_in_post_orders`. ::

    inorder = "4,2,1,5,3,6"
    postorder = "4,2,5,6,3,1"
    root = Node.from_in_post_orders(inorder, postorder)

---------------
Tree processing
---------------

With a tree set up, there are several functions you can use such as :func:`~binary_tree.has_path_sum` or :func:`~binary_tree.is_symmetrical` to analyse the nature of the tree. ::

    if tree.has_path_sum(root, 10):
        print(str(root) + "has path with sum 10!")

    if tree.is_symmetrical(root):
        print(str(root) + "is symmetrical!")

You can also traverse down the tree, yielding each node along the way. There are four different methods to do so::

    for node in tree.traverse_pre_order(root):
        print(node, "(pre-order traversal)")

    for node in tree.traverse_in_order(root):
        print(node, "(in-order traversal)")

    for node in tree.traverse_post_order(root):
        print(node, "(post-order traversal)")

    for level in tree.traverse_level_order(root):
        for node in level:
            print(node, "(level-order traversal)")

A single dispatch function, :func:`~binary_tree.traverse`, is available for these traversals. ::
    
    traversals = []
    for kind in ("pre", "in", "post", "level"):
        traversal = list(tree.traverse(root, kind))
        traversals.append(traversal)

On top of traversals, you can get the paths between the root node and all the leaf nodes of the binary tree using :func:`~binary_tree.get_all_paths`. This can be useful for functions like :func:`~binary_tree.has_path_sum`::
    
    def has_path_sum(node, value):
        for path in tree.get_all_paths(node):
            total = 0
            for node in path:
                total += node.value
            if total == value:
                return True
        else:
            return False

Also, you can use :func:`~binary_tree.get_max_depth` to get the total number of levels in the tree. ::
    
    depth = tree.get_max_depth(root)

Finally, there is :func:`~binary_tree.is_node` and :func:`~binary_tree.is_leaf_node`, which might be useful when writing your own tree functions. ::

    if tree.is_leaf_node(node):
        print(str(node) + "is a leaf node!")

    if tree.is_node(node.left):
        print(str(node) + "has left child!")


=======
Credits
=======

binary_tree was written by Han Keong <hk997@live.com>.

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
