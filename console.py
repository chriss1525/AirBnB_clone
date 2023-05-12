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

    def get_args(self, arg):
        args = arg.split()

        # check if the array has content
        if args:
            # check if 2 arguments were passed
            if len(args) == 2:
                return args
            else:
                print("** instance id missing **")
        else:
            print('** class name missing **')
        return None

    def find_record(self, class_name, instance_id):
        # retrieve all records in storage
        all = storage.all()

        # check if valid class_name
        if class_name not in ["BaseModel"]:
            print('** class doesn\'t exist **')
            return

        # check for matching record
        try:
            record = all[class_name + "." + instance_id]
            return record
        except Exception:
            print("** no instance found **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class
        name and id.

        example usage:
        (hbnb) show BaseModel 1234-5665-4321
        """

        try:
            [class_name, instance_id] = self.get_args(arg)

            # use globals() to extract string stored in class_name
            # and use it to create instance using the record
            record = self.find_record(class_name, instance_id)
            retrieved_record = globals()[class_name](**record)
            print(retrieved_record)
        except Exception:
            pass

    def do_destroy(self, arg):
        """destroys an instance of a class based on the class
        name and id.

        example usage:
        (hbnb) destroy BaseModel 1234-5665-4321
        """

        [class_name, instance_id] = self.get_args(arg)

        # check for matching record
        try:
            record = self.find_record(class_name, instance_id)
            retrieved_record = globals()[class_name](**record)
            storage.destroy(retrieved_record)
        except Exception:
            pass

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.

        example usage:
        (hbnb) all
        (hbnb) all BaseModel
        """

        if not arg:
            # Print all instances
            instances = storage.all()
            instance_list = []
            for instance in instances.values():
                instance_list.append(str(instance))
            print(instance_list)
        else:
            class_name = arg.strip()
            if class_name not in ["BaseModel"]:
                print('** class doesn\'t exist **')
                return
            # Print instances of a specific class
            file_storage = storage._FileStorage__objects
            instance_list = []
            for instance in file_storage.values():
                if instance['__class__'] == "BaseModel":
                    instance_list.append(str(instance))
            print(instance_list)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
