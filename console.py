#!/usr/bin/python3
""" script implementing an interactive console for the
    AirBnB_clone """
import cmd
import sys


class AirBnB_shell(cmd.Cmd):
    """The AirBnB shell interpreter, based on cmd module"""
    prompt = "(hbnb) "
    file = None


AirBnB_shell().cmdloop()
