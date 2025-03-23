from unittest import TestCase

from zajecia2.zadanie3.Library import Library


class TestLibrary(TestCase):
    def test_find_book_empty(self):
        testObject = Library()
        self.assertIsNone(testObject.find_book("There and back AGAIN"))

    def test_find_book_success(self):
        testBooks = {
            "123": "There and back again",
            "23123": "Some other book"
        }
        testObject = Library(testBooks)
        self.assertEqual(testObject.find_book("123"), "There and back again")

    def test_find_book_not_found(self):
        testBooks = {
            "123": "There and back again",
            "23123": "Some other book"
        }
        testObject = Library(testBooks)
        self.assertIsNone(testObject.find_book("124"))
