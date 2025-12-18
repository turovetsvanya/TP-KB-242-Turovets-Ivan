import unittest
import os
from unittest.mock import patch
from lab_3 import StudentList, Utils


class TestLab3(unittest.TestCase):

    def setUp(self):
        self.group_list = StudentList()
        self.test_data = [
            {"Name": "Max", "Phone": "380631112233"},
            {"Name": "Anna", "Phone": "380632223344"},
            {"Name": "Bohdan", "Phone": "380633334455"},
            {"Name": "Maria", "Phone": "380634445566"},
        ]

        self.test_data.sort(key=lambda x: x["Name"])

    def test_addNewElement(self):
        for data in self.test_data:
            with patch("builtins.input", side_effect=[data["Name"], data["Phone"]]):
                self.group_list.addNewElement()

        self.assertEqual(self.group_list.list_students[0].name, "Anna")
        self.assertEqual(self.group_list.list_students[1].name, "Bohdan")
        self.assertEqual(self.group_list.list_students[2].name, "Maria")
        self.assertEqual(self.group_list.list_students[3].name, "Max")

    def test_updateElement(self):
        for data in self.test_data:
            with patch("builtins.input", side_effect=[data["Name"], data["Phone"]]):
                self.group_list.addNewElement()

        with patch("builtins.input", side_effect=["Anna", "Ivan", "380635556677"]):
            self.group_list.updateElement()

        self.assertNotIn("Anna", [s.name for s in self.group_list.list_students])
        self.assertIn("Ivan", [s.name for s in self.group_list.list_students])

    def test_deleteElement(self):
        for data in self.test_data:
            with patch("builtins.input", side_effect=[data["Name"], data["Phone"]]):
                self.group_list.addNewElement()

        with patch("builtins.input", side_effect=["Bohdan"]):
            self.group_list.deleteElement()

        self.assertNotIn("Bohdan", [s.name for s in self.group_list.list_students])

    def test_save_csv(self):
        Utils.save_csv(self.group_list, "lab3test.csv")
        self.assertTrue(os.path.isfile("lab3test.csv"))
        os.remove("lab3test.csv")


if __name__ == "__main__":
    unittest.main()
