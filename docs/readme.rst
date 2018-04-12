*****
About
*****

binary_tree.py provides a :class:`~binary_tree.Node` object and some useful tools like constructors and tree traversals for a binary tree data structure.

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

To create an instance, pass a value into :class:`~binary_tree.Node`. ::
    
    node = Node(1)

Nodes have a :attr:`~binary_tree.Node.left` and a :attr:`~binary_tree.Node.right` attribute, which are expected to be instances of :class:`~binary_tree.Node`. They can also be set on initialization. ::

    another_node = Node(2)
    parent_node = Node(3, node, another_node)

However, manually setting up a binary tree structure may be tedious. A more preferable way of creating one is to pass in a string of values to the :func:`~binary_tree.Node.from_string` constructor. ::

    tree_string = "1,2,3,4,,5,6"
    root = Node.from_string(tree_string)

.. note::
    
    Node.from_string() will generate the tree structure in *level-order*.

Another way to construct a binary tree is from its in-order and pre-order traversals. You can regenerate the original tree structure using :func:`~binary_tree.Node.from_in_pre_orders`. ::

    in_order = "4,2,1,5,3,6"
    pre_order = "1,2,4,3,5,6"
    root = Node.from_in_pre_orders(in_order, pre_order)

Alternatively, you can use in-order and post-order traversals with :func:`~binary_tree.Node.from_in_post_orders`. ::

    in_order = "4,2,1,5,3,6"
    post_order = "4,2,5,6,3,1"
    root = Node.from_in_post_orders(in_order, post_order)

.. note::
    
    There should not be duplicates present in `in_order` and `pre_order` or `post_order`.

---------------
Tree processing
---------------

With a tree set up, there are several functions you can use such as :func:`~binary_tree.has_path_sum` or :func:`~binary_tree.is_symmetrical` to analyse the nature of the tree. ::

    if tree.has_path_sum(root, 10):
        print(str(root) + "has path with sum 10!")

    if tree.is_symmetrical(root):
        print(str(root) + "is symmetrical!")

You can also traverse down the tree, yielding each node along the way. Four different kinds of traversals are provided. ::
    
    print("This is a pre-order traversal.")
    for node in tree.traverse_pre_order(root):
        print(node)

    print("This is an in-order traversal.")
    for node in tree.traverse_in_order(root):
        print(node)

    print("This is a post-order traversal.")
    for node in tree.traverse_post_order(root):
        print(node)

    print("This is a level-order traversal")
    for level in tree.traverse_level_order(root):
        for node in level:
            print(node)

A single dispatch function, :func:`~binary_tree.traverse`, is available for them. ::
    
    traversals = []
    for kind in ("pre", "in", "post", "level"):
        traversal = list(tree.traverse(root, kind))
        traversals.append(traversal)

On top of traversals, you can get the paths between the root node and each leaf node using :func:`~binary_tree.get_all_paths`. This can be useful for functions like :func:`~binary_tree.has_path_sum`. ::
    
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

