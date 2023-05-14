#!/usr/bin/python3
"""This test module defines tests for console.py"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """
    Unit tests for the HBNBCommand class
    """

    def setUp(self):
        """
        Set up the test environment before each test method is executed.
        """
        self.console = HBNBCommand()

    def tearDown(self):
        """
        Clean up the test environment after each test method is executed.
        """
        self.console = None

    def test_quit_command(self):
        """
        Test the quit command.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd('quit'))
            self.assertEqual(f.getvalue(), '')

    def test_EOF_command(self):
        """
        Test the EOF command.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd('EOF'))
            self.assertEqual(f.getvalue(), '\n')

    def test_emptyline_command(self):
        """
        Test the emptyline command.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertIsNone(self.console.onecmd(''))
            self.assertEqual(f.getvalue(), '')

    def test_create_command(self):
        """
        Test the create command.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('create BaseModel')
            output = f.getvalue().strip()
            self.assertTrue(len(output) > 0)

    def test_show_command(self):
        """
        Test the show command.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('show BaseModel 1234-5678-9012')
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_destroy_command(self):
        """
        Test the destroy command.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('destroy BaseModel 1234-5678-9012')
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_all_command(self):
        """
        Test the all command.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('all')
            output = f.getvalue().strip()
            self.assertTrue(len(output) > 0)

    # def test_update_command(self):
    #     """
    #     Test the update command.
    #     """
    #     with patch('sys.stdout', new=StringIO()) as f:
    #         self.console.onecmd(
    #             'update BaseModel 1234-5678-9012 name "John Doe"')
    #         output = f.getvalue().strip()
    #         self.assertEqual(output, "** no instance found **")

    def test_help(self):
        """
        Test the help command.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help")


if __name__ == '__main__':
    unittest.main()
