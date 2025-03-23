from unittest import TestCase

from zajecia2.zadanie4.Generator import generator


class Test(TestCase):
    def test_generator_1(self):
        self.assertListEqual([x for x in generator(3)], [0, 1, 1])

    def test_generator_2(self):
        self.assertListEqual([x for x in generator(4)], [0, 1, 1, 2])

    def test_generator_3(self):
        self.assertListEqual([x for x in generator(1)], [0, 1])

    def test_generator_4(self):
        self.assertListEqual([x for x in generator(0)], [0, 1])

    def test_generator_5(self):
        self.assertRaises(Exception, generator(-6))
