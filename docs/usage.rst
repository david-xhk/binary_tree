=====
Usage
=====
-------
Imports
-------

To use the functions provided by binary_tree, you can do the following import::

    import binary_tree as tree

If you would like to use the Node object on its own, you may also do this::
    
    from binary_tree import Node

-------------
Node creation
-------------

To create a Node object, you can simply do::
    
    node = Node(1)

Nodes have a ``left`` and a ``right`` attribute which are expected to also be instances of Node. They can be set on initialization like so::

    another_node = Node(2)
    parent_node = Node(3, node, another_node)

However, manually setting up a binary tree structure may get very tedious. The preferrable way of initiating a binary tree structure is to pass in a string of values to the Node.from_string constructor::

    tree_string = "1,2,3,4,,5,6"
    root = Node.from_string(tree_string)

Take note that this method will generate a binary tree structure in level-order.

Another way to construct a binary tree is through retrosynthesis from its in-order and pre-order traversals. If you happen to have only this information, you can regenerate the original tree structure as follows::

    inorder = "4,2,1,5,3,6"
    preorder = "1,2,4,3,5,6"
    root = Node.from_in_pre_orders(inorder, preorder)

You can also do the same thing with in-order and post-order traversals::

    inorder = "4,2,1,5,3,6"
    postorder = "4,2,5,6,3,1"
    root = Node.from_in_post_orders(inorder, postorder)

---------------
Tree processing
---------------

With a tree set up, there are several functions available to analyse the nature of the tree. For instance::

    if tree.has_path_sum(root, 10):
        print(str(root) + "has path with sum 10!")

    if tree.is_symmetric(root):
        print(str(root) + "is symmetrical!")

You can also traverse down a tree, yielding the respective node with each step of the way. There are four different ways to do so::

    for node in tree.traverse_pre_order(root):
        print(node, "(pre-order traversal)")

    for node in tree.traverse_in_order(root):
        print(node, "(in-order traversal)")

    for node in tree.traverse_post_order(root):
        print(node, "(post-order traversal)")

    for level in tree.traverse_in_order(root):
        for node in level:
            print(node, "(level-order traversal)")

On top of doing tree traversals, you can also get all the paths between the root node and all the leaf nodes of the binary tree structure. This might be useful for doing membership tests. ::
    
    def has_path_sum(node, value):
        for path in tree.get_all_paths(node):
            total = 0
            for node in path:
                total += node.value
            if total == value:
                return True
        else:
            return False

Finally, there are tests for nodes too, which might come in handy for the above-mentioned processes:

        if tree.is_leaf_node(node):
            print(str(node) + "is a leaf node!")

        if tree.is_node(node.left):
            print(str(node) + "has left child!")

        if tree.is_node(node.right):
            print(str(node) + "has right child!")            

