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

    def do_create(self, arg):
        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)

        """ if class name is missing, print class name missing """
        """ if doesn't exist, create MyModel """

    def do_show(self, arg):
        """ print string rep of an instance  based on the class name and id"""

    def do_destroy(self, arg):
        """ Delete an instance based on the class name and id """

    def do_all(self, arg):
        """ prints all string representation of all instances based or not on
            the class name """

    def do_update(self, arg):
        """ update instance based on the class name and id by adding or updating
            attribute"""



    """ File must end with """
if __name__ == '__main__':
    HBNBCommand().cmdloop()
