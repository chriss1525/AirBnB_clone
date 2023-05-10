#!/usr/bin/env python3
"""
Entry point Class HBNBCommand
defines a prompt (hbnb)

public class methods:
do_quit - handles quit command
do_EOF - handles exit using EOF
"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print()  # Print a new line before exiting
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
