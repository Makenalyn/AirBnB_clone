#!/usr/bin/python3
""" the console of the AirBnB"""
import cmd


"""
hbnb class importing the public Cmd class
"""


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """ EOF command to exit the program """
        return True

    def do_quit(self, line):
        """ Quit command to exit the program 

        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
