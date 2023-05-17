#!/usr/bin/python3
"""console

This file contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage, avail_classes
import re


class HBNBCommand(cmd.Cmd):
    """
    This class creates the command interpreter
    """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """quits command to exit the console
        """
        return True

    def do_EOF(self, line):
        """quits the console
        """
        print()
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
            if (line not in avail_classes):
                print("** class doesn't exist **")
            else:
                new_instance = avail_classes[line]()
                new_instance.save()
                print(new_instance.id)

    def do_show(self, line):
        """prints the string representation of an instance based
        on the class name and id
        """
        value = find(line)
        if value is None:
            return
        else:
            print(value)

    def do_destroy(self, line):
        """deletes an instance based on the class's name and id
        """
        value = find(line)
        if value is None:
            return
        else:
            key = "{}.{}".format(value.__class__.__name__, value.id)
            store = storage.all()
            del store[key]
            storage.save()

    def do_all(self, line):
        """prints a string representation of all instance based
        on the class or not
        """
        list = storage.all()
        str_list = []
        val = line.split()
        if (not line):
            for values in list.values():
                str_list.append(str(values))
            print(str_list)
            return
        if (line not in avail_classes):
            print("** class doesn't exist **")
        else:
            for values in list.values():
                if values.__class__.__name__ == val[0]:
                    str_list.append(str(values))
                else:
                    continue
            print(str_list)

    def do_update(self, line):
        """updates an instance
        """
        value = find(line)
        if value is None:
            return
        else:
            split = parse_args(line)
            # if (split[2] not in value.keys()):
            #     print("** attribute name missing **")
            if len(split) >= 4:
                setattr(value, split[2], split[3])
                value.save()
            elif len(split) == 2:
                print("** attribute name missing **")
            elif len(split) == 3:
                print("** value missing **")


def find(line):
    """checks for an object in a storage
    """
    attr = line.split()
    if (not line):
        print("** class name missing **")
        return None
    else:
        if (attr[0] not in avail_classes):
            print("** class doesn't exist **")
            return None
        else:
            if ((len(attr) == 1)):
                print("** instance id missing **")
            else:
                fin = get_obj(attr[0], attr[1])
                if fin is None:
                    print("** no instance found **")
                return fin


def get_obj(cls_name, id):
    """gets the object of the class given
    """
    key = "{}.{}".format(cls_name, id)
    storage_dict = storage.all()
    return (storage_dict.get(key))


def parse_args(line):
    """Parses the command line argument and
    returns a tuple of all the arguments
    """
    args = re.findall(r'[^"\s]+|"[^"]+"', line)
    return tuple([arg.replace('"', "") for arg in args])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
