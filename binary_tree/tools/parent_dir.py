# -*- coding: utf-8 -*-

"""This module contains functions for getting and inserting the parent directory of __main__ into sys.path."""

import os
import sys

def get_parent_dir(level, path):
    for i in range(level):
        path = os.path.dirname(path)
    return os.path.abspath(path)

def insert_parent_dir(*args):
    """Insert parent directory into sys.path.

    Args:
        level (int, optional): The number of times to go back.
        path (str, optional): The root path. Defaults to __main__.__file__.

    Returns:
        str: The path of the parent directory
    """
    num_args = len(args)
    if num_args == 2:
        level, path = args
    else:
        path = sys.modules["__main__"].__dict__["__file__"] 
        if num_args == 1:
            level = args[0]
        else:  # Any num_args besides 1 or 2 will revert to default values
            level = 1
    dir_path = get_parent_dir(level, path)
    sys.path.insert(0, dir_path)
    return dir_path

