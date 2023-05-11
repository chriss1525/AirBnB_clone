#!/usr/bin/env python3
"""This module hosts the HBNBCommand class which inherits from the Cmd class.
"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    Entry point Class HBNBCommand
    defines a prompt (hbnb)

    public class methods:
        do_quit - handles quit command
        do_EOF - handles exit using EOF
    """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """type quit to exit the program"""
        return True

    def do_EOF(self, arg):
        """Ctrl + D exits the program"""
        print()  # Print a new line before exiting
        return True

    def do_create(self, arg):
        """create command creates a new instance of a specified class

        example usage:
        (hbnb) create BaseModel
        """

        if not arg:
            print('** class name missing **')
            return

        class_name = arg.strip()
        if class_name not in ["BaseModel"]:
            print('** class doesn\'t exist **')
            return

        new_instance = BaseModel()

        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class
        name and id.

        example usage:
        (hbnb) show BaseModel 1234-5665-4321
        """

        # split arguement on white space and save the array
        args = arg.split()

        # check if the array has content
        if args:
            # check if 2 arguments were passed
            if len(args) == 2:
                # store first argument as class_name
                class_name = args[0]
                # store second arguement in instance_id
                instance_id = args[1]

                # check if valid class_name
                if class_name not in ["BaseModel"]:
                    print('** class doesn\'t exist **')
                    return

                # retrieve all records in storage
                all = storage.all()

                # check for matching record
                try:
                    record = all[class_name + "." + instance_id]

                    # use globals() to extract string stored in class_name
                    # and use it to create instance using the record
                    retrieved_record = globals()[class_name](**record)
                    print(retrieved_record)
                except Exception:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print('** class name missing **')

    def do_destroy(self, arg):
        """destroys an instance of a class based on the class
        name and id.

        example usage:
        (hbnb) destroy BaseModel 1234-5665-4321
        """
        # split arguement on white space and save the array
        args = arg.split()

        # check if the array has content
        if args:
            # check if 2 arguments were passed
            if len(args) == 2:
                # store first argument as class_name
                class_name = args[0]
                # store second arguement in instance_id
                instance_id = args[1]

                # check if valid class_name
                if class_name not in ["BaseModel"]:
                    print('** class doesn\'t exist **')
                    return

                # retrieve all records in storage
                all = storage.all()

                # check for matching record
                try:
                    record = class_name + "." + instance_id

                    if record in all:
                        del all[record]
                except Exception:
                    print("** no instance found **")
            else:
                print("** instance id missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
