#!/usr/bin/python3
""" Must use the cmd module """
import cmd

""" class definition  to the entry point of the cmd interpreter """


class HBNBCommand(cmd.Cmd):

    """ Return exit """
    

    def do_exit(self, arg):
        print("Goodbye")
        return True
    

    """ File must end with """
if __name__ == '__main__':
    HBNBCommand().cmdloop()
