#!/usr/bin/python3
""" Must use the cmd module """
import cmd

""" class definition  to the entry point of the cmd interpreter """

prompt="(hbnb)"

class HBNBCommand(cmd.Cmd):

    """ Return exit """
    

    def do_quit(self, arg):
        print("Goodbye")
        return True

    def do_EOF(self, arg):
        return True

    """ File must end with """
if __name__ == '__main__':
    HBNBCommand().cmdloop()
