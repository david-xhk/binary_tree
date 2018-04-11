=====
Usage
=====

Importing from binary_tree
--------------------------

.. code-block:: python

    import binary_tree as tree

Importing Node
--------------

.. code-block:: python
    
    from binary_tree import Node

Instantiating Node
------------------

.. code-block:: python

    tree_string = "1,2,3,4,,5,6,"
    root = Node.from_string(tree_string)

Checking a tree
---------------

.. code-block:: python

    if tree.has_path_sum(root, 10):
        print("Has path with sum 10!")

    if tree.is_symmetric(root):
        print("Is symmetrical!")

Traversing a tree
-----------------

.. code-block:: python

    for node in tree.traverse_pre_order(root):
        if tree.is_leaf_node(node):  # Checking for leaf nodes
            print(str(node) + "is a leaf node!")

Getting paths in a tree
-----------------------

.. code-block:: python

    for path in tree.get_all_paths(root):
        for node in path:
            if tree.is_node(node.left):  # Checking for child nodes
                print(str(node) + "has left child!")
            if tree.is_node(node.right):
                print(str(node) + "has right child!")            

