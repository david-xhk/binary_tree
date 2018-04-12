*************
Documentation
*************

==============
Node interface
==============

----------
Attributes
----------

.. currentmodule:: binary_tree

.. autoclass:: Node

------------
Constructors
------------

.. class:: Node

    .. automethod:: from_string

    .. automethod:: from_in_pre_orders

    .. automethod:: from_in_post_orders

    .. note::

        There cannot be any duplicates in `in_order` and `pre_order` or `post_order`.

-------
Testing
-------

.. autofunction:: is_node

.. autofunction:: is_leaf_node

==============
Tree processes
==============

----------
Traversals
----------

.. autofunction:: traverse_pre_order

.. autofunction:: traverse_in_order

.. autofunction:: traverse_post_order

.. autofunction:: traverse_level_order

.. autofunction:: traverse

-------------
Getting paths
-------------

.. autofunction:: get_all_paths

-------------
Finding depth
-------------

.. autofunction:: get_max_depth

-------
Testing
-------

.. autofunction:: is_symmetrical

.. autofunction:: has_path_sum

---------------------------------------------------------------------------------

.. note::

    For a demonstration of binary_tree, run "binary_tree/tree.py".