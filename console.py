#!/usr/bin/python3
"""
I am creating the entry point of the command interpreter
"""

import cmd


class BNBCommand(cmd.Cmd):
    """ Cmd interpreter class """
    prompt = "(ourbnb) "

    def do_quit(self, inp):
        """ This quits command to exit program. """
    return True

    def do_EOF(self, inp):
        """ This exits the program on EOF """
        print("failed")
    return True


if __name__ == "__main__":
    BNBcommand().cmdloop()
