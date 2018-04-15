#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This module contains the Demo class.

Note:
    For a demonstration of the Demo class, run 'demo/demo.py' in your terminal.
"""

# For backwards compatibility
from __future__ import print_function

import sys
if sys.version_info < (3,3):
    input = raw_input

from functools import wraps

def raise_on_exit(func):
    @wraps(func)
    def inner(*args, **kwargs):
        response = func(*args, **kwargs)
        if response == "q":
            raise DemoExit
        else:
            return response
    return inner

def raise_on_restart(func):
    @wraps(func)
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

class DemoExit(DemoException):
    text = "Goodbye!"

class DemoRestart(DemoException):
    pass

class Demo:
    commands = ["'This is a default string'", "1+1", "ERROR!@#$%"]
    help_text = "Help not written yet."
    setup_text = "Enter some input here: "
    selection_text = "Select a command, or 'a' for all: "

    def __init__(self):
        self.setup_text = (
            "Type 'h' for help, or 'q' to quit.\n" 
            + self.setup_text)
        self.selection_text = (
            "Type 'r' to restart, or 'q' to quit.\n"
            "To view the commands again, type 'c'.\n"
            + self.selection_text)

    def run(self):
        while True:
            try:
                try:
                    context = self.get_context()  # 82-96
                    self.print_commands()
                    while True:
                        commands = self.get_commands()  # 98-113
                        self.execute_commands(commands, *context)  # 115-124
                except KeyboardInterrupt as exc:
                    print()  # Advance to the next line
                    raise DemoExit from exc
            except DemoException as exc:
                print(exc.text)
                if isinstance(exc, DemoExit):
                    return
                elif isinstance(exc, DemoRestart):
                    continue

    def get_context(self):
        while True:
            response = self.get_setup_response()
            if response == "h":
                self.print_help()
            else:
                return self.setup_context(response)

    @raise_on_exit
    def get_setup_response(self):
        return input(self.setup_text)

    def setup_context(self, response):
        print("Okay!")  # Implement the setup logic here.
        return globals(), locals()  # Return globals(), locals().

    def get_commands(self):
        while True:
            selection = self.get_commands_selection()
            if selection == "a":
                return self.commands[:]
            elif selection in map(str, range(len(self.commands))):
                return self.commands[int(selection): int(selection)+1]
            elif selection == "c": 
                self.print_commands()
            else:
                print("Invalid index. Please try again.\n")

    @raise_on_exit
    @raise_on_restart
    def get_commands_selection(self):
        return input(self.selection_text)

    def execute_commands(self, commands, *context):
        for command in commands:
            # Print the command first
            self.print_in(command)
            # Then print the return value of the command
            try:
                exec("self.print_out(" + command + ")", *context)
            except Exception as exc:
                self.print_out(exc)
            print()

    def print_help(self):
        width = max(map(len, self.help_text.splitlines()))
        self.print_dashes(width)
        print("Help:")
        print(self.help_text)
        self.print_dashes(width)

    def print_commands(self):
        width = max(map(len, self.commands)) + 4
        self.print_dashes(width)
        print("Commands:")
        for index, command in enumerate(self.commands):
            print("{:2}: {}".format(index, command))
        self.print_dashes(width)

    @staticmethod
    def print_dashes(width):
        print("".join("-" for i in range(width)))
    
    @staticmethod
    def print_in(*args):
        print(">>>", *args)

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


if __name__ == "__main__":
    demo = Demo()
    demo.run()

