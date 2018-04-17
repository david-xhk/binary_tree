# -*- coding: utf-8 -*-

"""This module contains ensure_type, a decorator class for checking specific arguments after function runtime.

To look at an implementation of ensure_type, you may refer to 'binary_tree/__init__.py'.
"""

import functools
import inspect

class ensure_type:
    will_check = True
    error_text = "`{}` should be <class '{}'>, not <class '{}'>"
    error_type = ValueError

    def __init__(self, **arg_types):
        self.arg_types = arg_types
    
    def __call__(self, func):
        if inspect.isclass(func):
            methods = inspect.getmembers(func, predicate=inspect.ismethod)
            for name, method in methods:
                setattr(func, name, self(method))
        elif self.has_arg(func):
            @functools.wraps(func)
            def inner(*args, **kwargs):
                if self.will_check:
                    self.check_args(func, *args, **kwargs)
                return func(*args, **kwargs)
            return inner
        return func
    
    def has_arg(self, func):
        try:
            arg_spec = inspect.getargspec(func)
        except TypeError:
            pass
        else:
            for arg_name in arg_spec[0]:
                if arg_name in self.arg_types:
                    return True
            if arg_spec[1] in self.arg_types:
                return True
            if arg_spec[2] in self.arg_types:
                return True
            if arg_spec[3]:
                for arg_name in arg_spec[3]:
                    if arg_name in self.arg_types:
                        return True
        return False

    def check_args(self, func, *args, **kwargs):
        for arg_name, value in self.get_args(func, *args, **kwargs):
            arg_type = self.arg_types[arg_name.lstrip("*")]
            if not isinstance(value, arg_type):
                error = self.error_text.format(
                    arg_name, arg_type.__name__, type(value).__name__)
                raise self.error_type(error)

    def get_args(self, func, *args, **kwargs):
        arg_spec = inspect.getargspec(func)
        for arg_index, arg_name in enumerate(arg_spec[0]):
            if arg_name in self.arg_types:
                yield arg_name, args[arg_index]
        if arg_spec[1] in self.arg_types:
            for value in args[len(arg_spec[0]):]:
                yield "*" + arg_spec[1], value
        if arg_spec[2] in self.arg_types:
            for arg_name, value in kwargs.items():
                yield arg_name, value
        if arg_spec[3]:
            for arg_name in arg_spec[3]:
                if arg_name in self.arg_types:
                    yield arg_name, kwargs[arg_name]

