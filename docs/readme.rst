===========
Binary Tree
===========

binary_tree provides a Node object and some useful functions like constructors and tree traversals for a binary tree data structure.

--------
Features
--------

1. Construct a binary tree using 
 * String
 * In-order and pre-order traversal
 * In-order and post-order traversal

2. Traverse a binary tree by 
 * Pre-order
 * In-order
 * Post-order
 * Level-order.

3. Get from a binary tree
 * All root-to-leaf paths
 * The maximum depth

4. Check if a binary tree
 * Is symmetrical
 * Has a certain path sum.

-----
Usage
-----

^^^^^^^
Imports
^^^^^^^

To use the functions provided by :mod:`binary_tree`, you can do the following import::

    import binary_tree as tree

If you would like to use :class:`~binary_tree.Node` on its own, you may also do this::
    
    from binary_tree import Node

^^^^^^^^^^^^^
Node creation
^^^^^^^^^^^^^

To create a :class:`~binary_tree.Node` object, you can simply do::
    
    node = Node(1)

Nodes have a :attr:`~binary_tree.Node.left` and a :attr:`~binary_tree.Node.right` attribute which are expected to also be instances of :class:`~binary_tree.Node`. They can be set on initialization like so::

    another_node = Node(2)
    parent_node = Node(3, node, another_node)

However, manually setting up a binary tree structure may get very tedious. The preferrable way of initiating a binary tree structure is to pass in a string of values to the :func:`~binary_tree.Node.from_string` constructor. ::

    tree_string = "1,2,3,4,,5,6"
    root = Node.from_string(tree_string)

Take note that this method will generate a binary tree structure in level-order.

Another way to construct a binary tree is through retrosynthesis from its in-order and pre-order traversals. If you happen to have only this information, you can regenerate the original tree structure using :func:`~binary_tree.Node.from_in_pre_orders`. ::

    inorder = "4,2,1,5,3,6"
    preorder = "1,2,4,3,5,6"
    root = Node.from_in_pre_orders(inorder, preorder)

Similarly, you can use in-order and post-order traversals with :func:`~binary_tree.Node.from_in_post_orders`. ::

    inorder = "4,2,1,5,3,6"
    postorder = "4,2,5,6,3,1"
    root = Node.from_in_post_orders(inorder, postorder)

^^^^^^^^^^^^^^^
Tree processing
^^^^^^^^^^^^^^^

With a tree set up, there are several functions available such as :func:`~binary_tree.has_path_sum` or :func:`~binary_tree.is_symmetric` to analyse the nature of the tree. ::

    if tree.has_path_sum(root, 10):
        print(str(root) + "has path with sum 10!")

    if tree.is_symmetric(root):
        print(str(root) + "is symmetrical!")

You can also :func:`traverse <binary_tree.traverse_pre_order>` down the tree, yielding the respective node with each step of the way. There are four different methods to do so::

    for node in tree.traverse_pre_order(root):
        print(node, "(pre-order traversal)")

    for node in tree.traverse_in_order(root):
        print(node, "(in-order traversal)")

    for node in tree.traverse_post_order(root):
        print(node, "(post-order traversal)")

    for level in tree.traverse_in_order(root):
        for node in level:
            print(node, "(level-order traversal)")

On top of doing tree traversals, you can get the paths between the root node and all the leaf nodes of the binary tree structure using :func:`~binary_tree.get_all_paths`. This might be useful for doing membership tests such as::
    
    def has_path_sum(node, value):
        for path in tree.get_all_paths(node):
            total = 0
            for node in path:
                total += node.value
            if total == value:
                return True
        else:
            return False

You can also call :func:`~binary_tree.get_max_depth` to get the total number of levels in the tree. ::
    
    depth = tree.get_max_depth(root)

Finally, there are :func:`tests <binary_tree.is_node>` for nodes too, which might come in handy for the above-mentioned processes. ::

    if tree.is_leaf_node(node):
        print(str(node) + "is a leaf node!")

    if tree.is_node(node.left):
        print(str(node) + "has left child!")

-------
Credits
-------

binary_tree was written by Han Keong <hk997@live.com>.

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage



