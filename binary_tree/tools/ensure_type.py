#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This module contains ensure_type, a decorator to help check specific arguments before function runtime.

For a demonstration of ensure_type, run 'binary_tree/tools/ensure_type.py' in your terminal (for macOS).

To look at an implementation of ensure_type, you may refer to 'binary_tree/__init__.py'.
"""

# For py2.7 compatibility
from __future__ import print_function
import sys
if sys.version_info < (3,3):
    input = raw_input

import functools
import inspect

def ensure_type(**arg_types):
    def inner(func):
        if is_func(func):
            arg_spec = inspect.getargspec(func)
            if (arg_spec.varargs in arg_types
                or arg_spec.keywords in arg_types
                or any(arg_name in arg_types for arg_name in arg_spec.args)
                or arg_spec.defaults and any(arg_name in arg_types 
                    for arg_name in arg_spec.defaults)):
                # Basically, if arg_spec has any arg_name in arg_types
                func_name = func.__name__
                code_str = """\
def {func_name}(*args, **kwargs):
    if {func_name}.will_check:
        check_args(arg_spec, arg_types, *args, **kwargs)
    return {func_name}.inner(*args, **kwargs)""".format(func_name=func_name)
                func_code = compile(code_str, "<wrapper>", "exec")
                context = {"arg_spec": arg_spec, "arg_types": arg_types,
                           "check_args": check_args, "__builtins__": None}
                exec(func_code, context)
                wrapped_func = context[func_name]
                wrapped_func.will_check = True
                wrapped_func.inner = func
                wrapped_func = functools.wraps(func)(wrapped_func)
                inner.registry[func_name] = wrapped_func
                return wrapped_func
        elif inspect.isclass(func):
            methods = inspect.getmembers(func, predicate=is_func)
            for name, method in methods:
                setattr(func, name, inner(method))
        return func  # For classes, irrelevant functions, and other objects
    def stop():
        for func in inner.registry.values():
            func.will_check = False
    def check_all():
        for func in inner.registry.values():
            func.will_check = True
    inner.registry = {}
    inner.stop = stop
    inner.check_all = check_all
    inner = functools.wraps(ensure_type)(inner)
    return inner
    
def is_func(obj):
    return inspect.isfunction(obj) or inspect.ismethod(obj)

def check_args(arg_spec, arg_types, *args, **kwargs):
    for arg_name, arg_type, arg_value in get_args(
            arg_spec, arg_types, *args, **kwargs):
        if not isinstance(arg_value, arg_type):
            arg_error = ValueError(
                "{} should be <class '{}'>, not <class '{}'>".format(
                    arg_name, arg_type.__name__, type(arg_value).__name__))
            raise arg_error

def get_args(arg_spec, arg_types, *args, **kwargs):
    for arg_index, arg_value in enumerate(args):
        try:
            arg_name = arg_spec.args[arg_index]
        except IndexError:
            arg_name = arg_spec.varargs
        if arg_name in arg_types:
            yield ("[{}]".format(arg_index), arg_types[arg_name], 
                args[arg_index])
    for arg_name, arg_value in kwargs.items():
        if arg_spec.keywords in arg_types:
            arg_type = arg_types[arg_spec.keywords]
        elif (arg_spec.defaults and arg_name in arg_spec.args
                and arg_name in arg_types):
            arg_type = arg_types[arg_name]
        else:
            continue
        yield "`{}`".format(arg_name), arg_type, arg_value


if __name__ == '__main__':    
    from demo import Demo

    class EnsureTypeDemo(Demo):
        help_text = """\
To use ensure_type, pass in the argument name and the type to check for.
This creates a decorator which you can use to wrap functions or classes.

If the function has a matching argument name, it will get wrapped.
The wrapped function has the following attributes:
    `will_check`: If True, arguments will be checked.
    `inner`: The function being wrapped.
Functions without matching arguments are returned unchanged.

As for classes, their methods will be recursively wrapped, then set back.
The class will be returned after all its methods have been checked.

ensure_type has an attribute `registry` tracking the functions wrapped.
It also comes with two helper functions:
    `stop`: Set `will_check` of every wrapped function to False.
    `check_all`: Vice versa."""

        setup_prompt = "Select an option, or press 'enter' to continue.\n"

        setup_code = """\
ensure_int = ensure_type(num=int, nums=int)

@ensure_int
def func(num):
    return num + 1

@ensure_int
def func2(*nums):
    total = nums[0]
    for num in nums[1:]:
        total += num
    return total"""

        commands = [
            "func(\"not a number\")",
            "func(1)",
            "ensure_int.stop()",
            "func2(1,2,3,4,5)",
            "func2(1,2,\"bacon\",4,5)",
            "func2(\"s\", \"p\", \"a\", \"m\")",
            "ensure_int.check_all()",
            "func(\"checking?\")",
            "func(1)"
            ]

        options = Demo.options.copy()

        @options("h", "o", "q", callback="setup")
        def make_setup(self):
            return input(self.setup_prompt)

        def setup_options(self):
            return []

    demo = EnsureTypeDemo()
    demo.run()

