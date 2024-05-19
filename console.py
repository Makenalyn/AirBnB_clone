#!/usr/bin/python3
""" the console of the AirBnB"""
import cmd


"""
hbnb class importing the public Cmd class
"""


class HBNBCommand(cmd.Cmd):
    def do_EOF(self, line):
        return True

    def do_quit(self, line):
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
