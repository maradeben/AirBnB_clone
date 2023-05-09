#!/usr/bin/python3
""" script implementing an interactive console for the
    AirBnB_clone """
import cmd
import sys


class AirBnB_shell(cmd.Cmd):
    """The AirBnB shell interpreter, based on cmd module"""
    prompt = "(hbnb) "

    def __init__(self, completekey='tab', stdin=None, stdout=None):
        """ the init fnction """
        super().__init__(completekey=completekey, stdin=stdin, stdout=stdout)
        pass
    
    def do_quit(self, arg):
        """ quit shell """
        return True
    
    def do_EOF(self, arg):
        """ respond to EOF """
        return True


AirBnB_shell().cmdloop()
