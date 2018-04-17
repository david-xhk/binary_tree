#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This module contains Demo, a framework for interactive command line demonstrations.

For a demonstration of the Demo class, run 'binary_tree/tools/demo.py' in your terminal.

To look at implementations of the Demo class, you may refer to 'binary_tree/tree_demo.py' and 'binary_tree/node_demo.py'.
"""

# For py2.7 compatibility
from __future__ import print_function
import sys
if sys.version_info < (3,3):
    input = raw_input

import functools
import re

def raise_on_exit(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        response = func(*args, **kwargs)
        if response == "q":
            raise DemoExit
        else:
            return response
    return inner

def raise_on_restart(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        response = func(*args, **kwargs)
        if response == "r":
            raise DemoRestart
        else:
            return response
    return inner

class DemoException(Exception):
    text = ""
    def __init__(self, text=None):
        if text is not None:
            self.text = text

class DemoRestart(DemoException):
    text = "Restarting."

class DemoExit(DemoException):
    text = "Goodbye!"

class Demo:
    help_text = """\
Each line is a new point.
    Indented lines are a sub point.
        Two levels of indentation are supported.

Sections can be separated with whitespace.
* Lines that start with '*' are notes."""

    setup_text = "Type 'h' for help, or 'q' to quit."

    setup_prompt = "Enter some input here: "

    setup_code = """\
# Setup code here.
foo = 1 + 1
bar = 5 * 2
spam = 14"""

    command_text = """\
Type 'r' to restart, or 'q' to quit.
To see this information again, type 'h'."""
    
    command_prompt = "Select a command, or 'a' for all: "

    commands = [
        "1  # Comments will be removed.",
        "foo + bar  # Operations will print their result.",
        "eggs = spam + 5  # Assignments will print the assigned value.",
        "spam / 0  # Errors will get printed too!",
        "response + \" was your response\"  # Variables are retained in memory"
        ]

    def run(self):
        while True:
            try:
                print(self.setup_text)
                context = self.get_context()
                self.print_commands()
                while True:
                    commands = self.get_commands()
                    context = self.execute_commands(commands, context)
            except (KeyboardInterrupt, DemoException) as exc:
                if isinstance(exc, KeyboardInterrupt):
                    print()
                    exc = DemoExit()
                print(exc.text)
                print()
                if isinstance(exc, DemoExit):
                    return

    def get_context(self):
        while True:
            response = self.input_setup()
            print()
            if response == "h":
                self.print_help()
            else:
                self.print_setup()
                return self.setup_context(response)

    @raise_on_exit
    def input_setup(self):
        return input(self.setup_prompt)

    def setup_context(self, response):
        context = dict(sys.modules["__main__"].__dict__, **locals())
        exec(compile(self.setup_code, "<string>", "exec"), context)
        return context

    def get_commands(self):
        while True:
            response = self.input_commands()
            if response == "a":
                return self.commands[:]
            elif response in map(str, range(len(self.commands))):
                return self.commands[int(response): int(response)+1]
            elif response == "h":
                print()
                self.print_commands()
            else:
                print("Invalid index. Please try again.\n")

    @raise_on_exit
    @raise_on_restart
    def input_commands(self):
        return input(self.command_prompt)

    def execute_commands(self, commands, context):
        for command in commands:
            self.print_in(command)
            assigned = None
            while "#" in command:
                hash_index = command.find("#")
                newline_index = command.find("\n", hash_index)
                if newline_index == -1:
                    command = command[:hash_index]
                else:
                    command = command[:hash_index] + command[newline_index:]
            if "\n" in command or " = " in command:
                if " = " in command:
                    assigned = command.split(" = ")[0].strip()
                command = compile(command, "<string>", "exec")
            elif not command.startswith("print("):
                command = "self.print_out(" + command + ")"
            try:
                exec(command, context)
            except Exception as exc:
                print(repr(exc))
            if assigned:
                context = self.execute_commands([assigned], context)
            else:
                print()
        return context

    def print_help(self):
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

    def print_setup(self):
        print("Setting up...")
        self.print_in(self.setup_code)
        print()

    def print_commands(self):
        print("Commands:")
        for index, command in enumerate(self.commands):
            command = "{:2}: {}".format(
                index, "\n    ".join(command.splitlines()))
            print(command)
        print()
        print(self.command_text)
        print()
    
    @staticmethod
    def print_in(text):
        for line in text.splitlines():
            if line.startswith("    "):
                print("... " + line)
            else:
                print(">>> " + line)

    @staticmethod
    def print_out(*args):
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

