#!/usr/bin/python3
"""console

This file contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    This class creates the command interpreter
    """
    prompt = '(hbnb) '

    def do_quit(self, line):
        """quits command to exit the console
        """
        return True

    def do_EOF(self, line):
        """quits the console
        """
        return True

    def emptyline(self):
        """prints an emptyline when no command is passed
        """
        pass

    def do_create(self, line):
        """creates a new instance and saves it
        """
        if (not line):
            print("** class name missing **")
        else:
            if (line != "BaseModel"):
                print("** class doesn't exist **")
            else:
                new_instance = BaseModel()
                new_instance.save()
                print(new_instance.id)

    # def do_show(self, line):
    #     """prints the string representation of an instance based
    #     on the class name and id
    #     """
    #     l = line.split()
    #     if (not line):
    #         print("** class name missing **")
    #     else:
    #         if (l[0] != "BaseModel"):
    #             print("** class doesn't exist **")
    #         else:
    #             if ((len(l) == 2)):
    #                 storage_dict = storage.all()
    #                 for key in storage_dict:
    #                     if key.endswith(l[1]):
    #                         string = "yayy it works"
    #                         break
    #                     else:
    #                         string = "** no instance found **"
    #                 print(string)
    #             else:
    #                 print("** instance id missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
