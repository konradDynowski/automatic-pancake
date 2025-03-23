from unittest import TestCase

from zajecia2.zadanie2.typing import average


class Test(TestCase):
    def test_average_floats(self):
        data = [6.5, 3.5, 12.0, -2.0]
        av = average(data)
        self.assertAlmostEqual(av, 5.0, 13)

    def test_average_floats_type_error(self):
        data = [6.5, 3.5, 12.0, "ABBA -2.0"]
        av = average(data)
        self.assertEqual(av, None)
