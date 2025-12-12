import unittest
import os
from unittest.mock import patch
from lab_2 import load_students, add_student, find_student, save_students

TEST_CSV = "lab2test.csv"

class TestLab2(unittest.TestCase):
    def setUp(self):
        self.list_students = [
            {"Name": "Max", "Phone": "380631112233"},
            {"Name": "Anna", "Phone": "380632223344"},
            {"Name": "Bohdan", "Phone": "380633334455"},
            {"Name": "Maria", "Phone": "380634445566"},
        ]

    def test_add_student(self):
        add_student(self.list_students, "Ivan", "380635556677")
        self.assertEqual(self.list_students[-1]["Name"], "Ivan")
        self.assertEqual(self.list_students[-1]["Phone"], "380635556677")

    def test_find_student(self):
        student = find_student(self.list_students, "Max")
        self.assertEqual(student["Phone"], "380631112233")
        student = find_student(self.list_students, "Unknown")
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