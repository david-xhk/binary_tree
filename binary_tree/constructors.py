"""
Node constructors.

Done by Han Keong
Created on 10/04/2018 2204 +0800
Last updated on 11/04/2018 1334 +0800
"""

def from_string(cls, tree_string):
    """Instantiate each parent in the level, and then each of their left and right children.

    See :ref:`Node.from_string` for more documentation.
    """
    values = iter(tree_string.replace(' []\n\'"', '').split(','))
    try:
        value = next(values)
    except StopIteration:  # tree_string has no values
        return None
    try:
        root = cls(value)
    except ValueError:  # root value is invalid
        return None
    level = [root]
    while True:
        next_level = []
        for node in level:
            for side in _sides:
                try:
                    value = next(values)
                except StopIteration:  # values has been exhausted
                    return root
                try:
                    child = cls(value)
                except ValueError:  # null value
                    pass
                else:
                    setattr(node, side, child)
                    next_level.append(child)
        level = next_level

def from_orders(cls, kind, *orders):
    """Instantiate the parent, the left child, and then the right child.

    See :ref:`Node.from_in_pre_orders` and :ref:`Node.from_in_post_orders` for more documentation.
    """
    if not all(orders):
        return None
    node = cls(orders[1][-_kinds[kind]])
    for side in _sides:
        child = from_orders(
            cls, kind, *_slice_orders(kind, side, *orders))
        setattr(node, side, child)
    return node

# Helper objects

_slices = (
    ":orders[0].index(orders[1][0])", 
    "1:len(orders[0])+1", 
    "orders[0].index(orders[1][0])+1:", 
    "-len(orders[0]):", 
    ":orders[0].index(orders[1][-1])", 
    ":len(orders[0])", 
    "orders[0].index(orders[1][-1])+1:", 
    "-len(orders[0])-1:-1",
    )

_kinds = {
    "in-pre": 0,
    "in-post": 1
}

_sides = {
    "left": 0,
    "right": 1
}

def _slice_orders(kind, side, *orders):
    """Slice orders based on which order and what side is provided.
    
    Note:
        There cannot be any duplicates in the orders provided.

    Args:
        kind (str): Either "in-pre" or "in-post".
        side (str): Either "left" or "right".
        *orders (:obj:`list` of :obj:`int`): Either (`in_order`, `pre_order`) or (`in_order`, `post_order`),
            where `in_order` and `pre_order` or `post_order` are lists of ints.
    
    Returns:
        :obj:`list` of :obj:`list`: Sliced copies of the orders provided.
    
    Raises:
        KeyError: If `kind` or `side` is invalid.
        IndexError: If the orders provided do not constitute a binary tree,
            or if they contain any duplicates.
    """
    orders = list(orders)
    for index in (0, 1):
        slice_index = _get_binary_index(_kinds[kind], _sides[side], index)
        exec(f"orders[index] = orders[index][{_slices[slice_index]}]")
    return orders

def _get_binary_index(*bools):
    """Transform a succession of boolean numbers into a decimal integer.

    Args:
        *bools (int): A succession of boolean numbers.
    
    Returns:
        int: A decimal integer.

    Raises:
        ValueError: If any argument in `bools` is not a boolean number.
    """
    return int("".join(str(int(num)) for num in bools), 2)

