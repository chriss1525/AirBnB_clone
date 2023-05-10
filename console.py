#!/usr/bin/env python3
"""
Entry point Class HBNBCommand
defines a prompt (hbnb)

public class methods:
do_quit - handles quit command
do_EOF - handles exit using EOF
"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """type quit to exit the program"""
        return True

    def do_EOF(self, arg):
        """Ctrl + D exits the program"""
        print()  # Print a new line before exiting
        return True

    def do_create(self, arg):
        """create command creates a new instance of a specified class"""
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
