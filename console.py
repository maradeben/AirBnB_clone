#!/usr/bin/python3
""" script implementing an interactive console for the AirBnB_clone """
import cmd
import sys


class HBnBShell(cmd.Cmd):
    """The AirBnB shell interpreter, based on cmd module"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ implement the quit """
        return (True)

    def do_EOF(self, arg):
        """ implement EOF """
        print("")
        return (True)

    def emptyline(self):
        """ prevent emptyline by overriding """
        pass


HBnBShell().cmdloop()
