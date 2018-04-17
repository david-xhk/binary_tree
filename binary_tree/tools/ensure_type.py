# -*- coding: utf-8 -*-

"""This module contains ensure_type, a decorator class for checking specific arguments after function runtime.

To look at an implementation of ensure_type, you may refer to 'binary_tree/__init__.py'.
"""

import functools
import inspect

def isfunc(obj):
    return (inspect.isfunction(obj) 
            or inspect.ismethod(obj))

class ensure_type:
    will_check = True
    error_text = "`{}` should be <class '{}'>, not <class '{}'>"
    error_type = ValueError

    def __init__(self, **arg_types):
        self.arg_types = arg_types
    
    def __call__(self, func):
        if inspect.isclass(func):
            methods = inspect.getmembers(func, predicate=isfunc)
            for name, method in methods:
                setattr(func, name, self(method))
        elif self.has_arg(func):
            print(func.__name__, "has arg")
            @functools.wraps(func)
            def inner(*args, **kwargs):
                if self.will_check:
                    for arg in self.get_args(func, *args, **kwargs):
                        self.check_arg(arg)
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

    def get_args(self, func, *args, **kwargs):
        arg_spec = inspect.getargspec(func)
        for arg_index, arg_name in enumerate(arg_spec[0]):
            if arg_name in self.arg_types:
                arg_type = self.arg_types[arg_name]
                arg_value = args[arg_index]
                yield arg_name, arg_type, arg_value
        if arg_spec[1] in self.arg_types:
            arg_name = "*" + arg_spec[1]
            arg_type = self.arg_types[arg_spec[1]]
            for arg_value in args[len(arg_spec[0]):]:
                yield arg_name, arg_type, arg_value
        if arg_spec[2] in self.arg_types:
            arg_type = self.arg_types[arg_spec[2]]
            for arg_name, arg_value in kwargs.items():
                yield arg_name, arg_type, arg_value
        if arg_spec[3]:
            for arg_name in arg_spec[3]:
                if arg_name in self.arg_types:
                    arg_type = self.arg_types[arg_name]
                    arg_value = kwargs[arg_name]
                    yield arg_name, arg_type, arg_value

    def check_arg(self, arg):
        arg_name, arg_type, arg_value = arg
        if not isinstance(arg_value, arg_type):
            raise self.type_error(arg)

    def type_error(self, arg):
        arg_name, arg_type, arg_value = arg
        error_text = self.error_text.format(
            arg_name, arg_type.__name__, type(arg_value).__name__)
        return self.error_type(error_text)
                
                    


