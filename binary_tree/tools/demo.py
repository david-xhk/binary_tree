#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This module contains Demo, a framework for interactive command line demonstrations.

For a demonstration of the Demo class, run 'binary_tree/tools/code_demo.py' in your terminal (for macOS).

To look at implementations of the Demo class, you may refer to 'binary_tree/tree_demo.py' and 'binary_tree/node_demo.py'.
"""

# For py2.7 compatibility
from __future__ import print_function
import sys
if sys.version_info < (3,3):
    input = raw_input

import functools
import inspect

def catch_exc(demo_exc):
    try:
        correct = issubclass(demo_exc, DemoException)
    except TypeError:
        correct = False
    if not correct:
        return catch_exc(DemoException)(demo_exc)
    def catch_exc_decorator(func):
        @functools.wraps(func)
        def inner(demo, *args, **kwargs):
            while True:
                try:
                    try:
                        return func(demo, *args, **kwargs)
                    except KeyboardInterrupt:
                        print()
                        demo.quit()
                except demo_exc as exc:
                    if exc.text:
                        print(exc.text)
                        print()
                    if isinstance(exc, DemoExit):
                        break
        return inner
    return catch_exc_decorator


class DemoException(Exception):
    text = ""
    def __init__(self, text=None):
        if text:
            self.text = text


class DemoRetry(DemoException):
    pass


class DemoRestart(DemoException):
    text = "Restarting."


class DemoExit(DemoException):
    text = "Goodbye!"


class DemoOptions(object):
    def __init__(self):
        self.callbacks = {}
        self.cache = {}

    def __call__(self, *opts, **kw_opts):
        retry = kw_opts.pop("retry", "")
        key = kw_opts.pop("callback", None)
        def options_decorator(input_getter):
            self.cache[key or input_getter.__name__] = opts, kw_opts
            @functools.wraps(input_getter)
            @catch_exc(DemoRetry)
            def input_wrapper(demo, *args, **kwargs):
                response = input_getter(demo, *args, **kwargs)
                if response in opts:
                    callback = self.callbacks[response]
                    if callback.feedback:
                        return callback(demo, *opts, key=key, **kw_opts)
                    else:
                        return callback(demo)
                if response in kw_opts:
                    return response
                if key:
                    callback = self.callbacks[key]
                    return callback(demo, response)
                demo.retry(retry)
            return input_wrapper
        return options_decorator

    def register(self, key, retry=False, feedback=False):
        def register_decorator(func):
            if not retry:
                callback = func
            else:
                @functools.wraps(func)
                def callback(demo, *args, **kwargs):
                    func(demo, *args, **kwargs)
                    demo.retry()
            callback.feedback = feedback
            self.callbacks[key] = callback
            return func
        return register_decorator

    def copy(self):
        new_options = DemoOptions()
        new_options.callbacks.update(self.callbacks)
        new_options.cache.update(self.cache)
        return new_options


class DemoBase(object):
    options = DemoOptions()

    help_text = """\
Each line is a new point.
    Indented lines are a sub point.
        Two levels of indentation are supported.

Sections can be separated with whitespace.
* Lines that start with '*' are notes."""

    @options.register("h", retry=True)
    def print_help(self):
        """Help."""
        print("Help:")
        for line in self.help_text.splitlines():
            if not line:
                print()
            elif line.startswith("        "):
                print("          * " + line.lstrip())
            elif line.startswith("    "):
                print("      - " + line.lstrip())
            elif line.startswith("*"):
                print("      Note: " + line.lstrip("* "))
            else:
                print("  • " + line)
        print()

    @options.register("o", retry=True, feedback=True)
    def print_options(self, *opts, **kw_opts):
        """View possible options."""
        key = kw_opts.pop("key", None)
        print("Options:")
        opt_list = []
        if key:
            for opt in getattr(self, key + "_options")():
                opt_list.append(opt)
            opts, kw_opts = self.options.cache[key]
        opt_list.extend(kw_opts.items())
        for opt in opts:
            desc = getattr(self.options.callbacks.get(opt), "__doc__", "")
            opt_list.append((opt, desc))
        opt_width = (max(len(opt) for opt, desc in opt_list)-3)//4*4+6
        for opt, desc in opt_list:
            print("{}: {}".format(opt.rjust(opt_width), desc))
        print()

    @options.register("r")
    def restart(self, text=None):
        """Restart."""
        raise DemoRestart(text)

    @options.register("q")
    def quit(self, text=None):
        """Quit."""
        raise DemoExit(text)

    def retry(self, text=None):
        raise DemoRetry(text)

    @catch_exc
    def run(self):
        self.print_options("h", "o", "r", "q")
        return self.options("h", "o", "r", "q")(
            lambda self: input("Enter a string: "))(self)


class Demo(DemoBase):
    options = DemoBase.options.copy()

    setup_prompt = "Select an option, or enter some random input:\n"

    setup_code = """\
# Setup code here.
foo = 1 + 1
bar = 5 * 2
spam = 14"""

    command_prompt = "Choose an option: "

    commands = [
        "1  # Comments will be removed.",
        "foo + bar  # Operations will print their result.",
        "eggs = spam + 5  # Assignments will print the assigned value.",
        "spam / 0  # Errors will get printed too!",
        "response + \" was your response\"  # Variables are stored in memory"
        ]

    def __init__(self):
        main = inspect.getmembers(sys.modules["__main__"],
            predicate=lambda obj: not inspect.ismodule(obj))
        self.locals = dict(main, demo=self)
        self.globals = __builtins__.copy()
        for name in ["__import__"]:
            del self.globals[name]

    @catch_exc
    def run(self):
        self.print_options(key="setup")
        self.make_setup()
        self.print_options(key="commands")
        while True:
            commands = self.get_commands()
            self.execute(commands)

    @options("s", "h", "o", "q", callback="setup")
    def make_setup(self):
        return input(self.setup_prompt)

    @options.register("s", retry=True)
    def sandbox(self):
        """Sandbox mode."""
        print("Switched to sandbox mode.")
        print("To leave sandbox mode, enter 'quit()'.")
        print()
        while True:
            prefix = ">>> "
            command = input(prefix)
            while True:
                if command.rstrip().endswith(":"):
                    prefix = "... "
                next_line = input(prefix)
                if next_line:
                    command += "\n" + next_line
                else:
                    break
            if command == "quit()":
                break
            self.execute([command], print_in=False)
        print()

    @options.register("setup")
    def setup_callback(self, response):
        print("Setting up...")
        self.print_in(self.setup_code)
        print()
        self.locals["response"] = response
        exec(compile(self.setup_code, "<string>", "exec"), self.locals)
        self.locals.pop("__builtins__")
    
    def setup_options(self):
        yield ("*", "Your response.")

    @options("s", "o", "r", "q", callback="commands")
    def get_commands(self):
        return input(self.command_prompt)

    @options.register("commands")
    def commands_callback(self, response):
        if response == "a":
            return self.commands[:]
        elif response in map(str, range(len(self.commands))):
            index = int(response)
            return self.commands[index:index+1]
        else:
            self.retry("Invalid index. Please try again.")

    def commands_options(self):
        for index, command in enumerate(self.commands):
            yield (str(index), "\n    ".join(command.splitlines()))
        yield ("a", "Execute all of the above.")

    def execute(self, commands, print_in=True):
        for command in commands:
            if print_in:
                self.print_in(command)
            assigned = []
            # Remove comments
            while "#" in command:
                hash_index = command.find("#")
                newline_index = command.find("\n", hash_index)
                if newline_index == -1:
                    command = command[:hash_index]
                else:
                    command = command[:hash_index] + command[newline_index:]
            # Compile command if multi-line or assignment
            if "\n" in command or " = " in command:
                if " = " in command:
                    assigned.append(command.split(" = ")[0].strip())
                command = compile(command, "<string>", "exec")
            # If command doing "print(", skip this
            elif not command.startswith("print("):
                command = "demo.print_out(" + command + ")"
            try:
                exec(command, self.globals, self.locals)
            except Exception as exc:
                print(repr(exc))
            # If a value was assigned, print it out
            if assigned:
                self.execute(assigned, print_in)
            else:
                print()

    def print_in(self, text):
        for line in text.splitlines():
            if line.startswith("    "):
                print("... " + line)
            else:
                print(">>> " + line)

    def print_out(self, *args):
        """If a list or tuple is in args, print every arg on a new line."""
        def print_recur(*args):
            # If there are no lists or tuples in args,
            if not any(isinstance(arg, (list, tuple)) for arg in args):
                # print all args in a line, 
                print(
                    # separated by commas,
                    ", ".join(
                        # putting double-quote marks around strings,
                        "\"" + arg + "\"" if isinstance(arg, str)
                        # and casting everything else to str.
                        else str(arg) for arg in args))
            # Otherwise,
            else:
                # iterate over args, doing the following:
                for arg in args:
                    # If arg isn't a list or tuple,
                    if not isinstance(arg, (list, tuple)):
                        # print str(arg) on a new line.
                        print(str(arg))
                    # If it is,  
                    else:
                        # recurse the entire process on arg.
                        print_recur(*arg)
        print_recur(*args)


if __name__ == '__main__':
    demo = Demo()
    demo.run()

