=====
Usage
=====

-------
Imports
-------

^^^^^^^^^^^^^^^^^^
binary_tree module
^^^^^^^^^^^^^^^^^^

.. code-block:: python

    import binary_tree as tree

^^^^^^^^^^
Node class
^^^^^^^^^^

.. code-block:: python
    
    from binary_tree import Node


---------------------------------------------------------------------

-------------
Node creation
-------------

^^^^^^^^^^^
Using string
^^^^^^^^^^^

.. code-block:: python

    tree_string = "1,2,3,4,,5,6"
    root = Node.from_string(tree_string)

^^^^^^^^^^^^^^^^^^^^^^^^^^^
From in-order and pre-order
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    inorder = "4,2,1,5,3,6"
    preorder = "1,2,4,3,5,6"
    root = Node.from_in_pre_orders(inorder, preorder)

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
From in-order and post-order
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    inorder = "4,2,1,5,3,6"
    postorder = "4,2,5,6,3,1"
    root = Node.from_in_post_orders(inorder, postorder)


---------------------------------------------------------------------

---------------
Tree processing
---------------

^^^^^^^^^^^^^^^
Checking a tree
^^^^^^^^^^^^^^^

.. code-block:: python

    if tree.has_path_sum(root, 10):
        print(str(root) + "has path with sum 10!")

    if tree.is_symmetric(root):
        print(str(root) + "is symmetrical!")

^^^^^^^^^^^^^^^^^
Traversing a tree
^^^^^^^^^^^^^^^^^

.. code-block:: python

    for node in tree.traverse_pre_order(root):
        if tree.is_leaf_node(node):  # Checking for leaf nodes
            print(str(node) + "is a leaf node!")

^^^^^^^^^^^^^^^^^^^^^^^
Getting paths in a tree
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    for path in tree.get_all_paths(root):
        for node in path:
            if tree.is_node(node.left):  # Checking for child nodes
                print(str(node) + "has left child!")
            if tree.is_node(node.right):
                print(str(node) + "has right child!")            

