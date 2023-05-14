#!/usr/bin/env python3
"""This module hosts the HBNBCommand class which inherits from the Cmd class.
"""
import cmd
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Entry point Class HBNBCommand
    defines a prompt (hbnb)

    public class methods:
        do_quit - handles quit command
        do_EOF - handles exit using EOF
    """

    prompt = '(hbnb) '
    __models = ["BaseModel", "User", "State",
                "City", "Amenity", "Place", "Review"]

    def emptyline(self):
        """
        Override the default emptyline method
        to avoid repeating the last command
        when an empty line is entered.
        """
        pass

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
            print('** class name missing ** ')
            return

        class_name = arg.strip()
        if class_name not in self.__models:
            print("** class doesn't exist **")
            return

        new_instance = globals()[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class
        name and id.

        example usage:
        (hbnb) show BaseModel 1234-5665-4321
        """

        try:
            [class_name, instance_id] = self.get_args(arg)

            if class_name not in self.__models:
                print("** class doesn't exist **")
                return

            record = self.find_record(class_name, instance_id)
            retrieved_record = globals()[class_name](**record)
            print(retrieved_record)
        except Exception:
            pass

    def do_destroy(self, arg):
        """Destroys an instance of a class based on the class name and id.

        Example usage:
        (hbnb) destroy BaseModel 1234-5665-4321
        """

        try:
            [class_name, instance_id] = self.get_args(arg)

            if class_name not in self.__models:
                print("** class doesn't exist **")
                return

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
            if class_name not in self.__models:
                print("** class doesn\'t exist **")
                return
            # Print instances of a specific class
            file_storage = storage._FileStorage__objects
            instance_list = []
            for instance in file_storage.values():
                if instance['__class__'] == class_name:
                    instance_list.append(str(instance))
            print(instance_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)

        example usage:
        (hbnb) update BaseModel 1234-5676-4321 email "aibnb@mail.com" """

        args = self.get_update_args(arg)

        if args is None:
            return

        [class_name, instance_id, attribute, value] = args

        try:
            record = self.find_record(class_name, instance_id)

            if record is None:
                print('** no instance found **')
                return

            retrieved_record = globals()[class_name](**record)
            setattr(retrieved_record, attribute, value)
            setattr(retrieved_record, "updated_at", datetime.now())
            storage.new(retrieved_record)
        except Exception:
            pass

    def get_update_args(self, arg):
        args = arg.split()

        if args:
            if len(args) > 1:
                if len(args) > 2:
                    if len(args) > 3:
                        return [*args[:3] + [self.get_value(args)]]
                    else:
                        print("** value missing **")
                else:
                    print("** attribute name missing **")
            else:
                print("** instance id missing **")
        else:
            print('** class name missing **')

    def get_value(self, args):
        found = False
        arr = " ".join([str(item) for item in args[3:]])
        value = ""

        for j in arr:
            if found and j == '"':
                found = not found
                break
            elif not found and j == '"':
                found = not found
            else:
                value += j

        return value

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
        # check if valid class_name
        if class_name not in self.__models:
            print("** class doesn't exist **")
            return

        # retrieve all records in storage
        all = storage.all()

        # check for matching record
        try:
            record = all[class_name + "." + instance_id]
            return record
        except Exception:
            print("** no instance found **")
            return None


if __name__ == '__main__':
    HBNBCommand().cmdloop()
