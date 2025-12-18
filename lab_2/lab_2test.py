import unittest
import os
from unittest.mock import patch
from lab_2 import add_student, find_student, load_students, save_students

TEST_CSV = "lab2test.csv"

class TestLab2(unittest.TestCase):
    def setUp(self):
        self.list_students = [
            {"Name": "Max", "Phone": "380631112233"},
            {"Name": "Anna", "Phone": "380632223344"},
            {"Name": "Bohdan", "Phone": "380633334455"},
            {"Name": "Maria", "Phone": "380634445566"},
        ]
        self.list_students.sort(key=lambda x: x["Name"])

    def test_add_student(self):
        with patch('builtins.input', side_effect=['Ivan', '380635556677']):
            name = input()
            phone = input()
            add_student(self.list_students, name, phone)

        self.assertEqual(self.list_students[-1]["Name"], "Ivan")
        self.assertEqual(self.list_students[-1]["Phone"], "380635556677")

    def test_find_student(self):
        with patch('builtins.input', side_effect=['Max']):
            name = input()
            student = find_student(self.list_students, name)
            self.assertEqual(student["Phone"], "380631112233")

        with patch('builtins.input', side_effect=['Unknown']):
            name = input()
            student = find_student(self.list_students, name)
            self.assertIsNone(student)

    def test_save_and_load_students(self):
        try:
            save_students(TEST_CSV, self.list_students)
            self.assertTrue(os.path.isfile(TEST_CSV))
            data = load_students(TEST_CSV)
            self.assertEqual(data, self.list_students)
        finally:
            if os.path.isfile(TEST_CSV):
                os.remove(TEST_CSV)

if __name__ == '__main__':
    unittest.main()