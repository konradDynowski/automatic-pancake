from unittest import TestCase

from zajecia2.zadanie1.TextAnalyzer import TextAnalyzer


class TestTextAnalyzer(TestCase):
    def test_word_count_1(self):
        testedObject = TextAnalyzer()
        text = "To był naprawdę wspaniały dzień!"
        word_count = testedObject.word_count(text)
        self.assertEqual(5, word_count)

    def test_word_count_2(self):
        testedObject = TextAnalyzer()
        text = "To był naprawdę okropny dzień!"
        word_count = testedObject.word_count(text)
        self.assertEqual(5, word_count )

    def test_word_count_3(self):
        # no word after one of spaces
        testedObject = TextAnalyzer()
        text = "To był naprawdę okropny dzień! Co dalej? "
        word_count = testedObject.word_count(text)
        self.assertEqual(7, word_count)

    def test_char_count_1(self):
        testedObject = TextAnalyzer()
        text = "To był naprawdę wspaniały dzień!"
        char_count = testedObject.char_count(text)
        self.assertEqual(32, char_count)

    def test_char_count_2(self):
        testedObject = TextAnalyzer()
        text = "To był naprawdę okropny dzień!"
        char_count = testedObject.char_count(text)
        self.assertEqual(30, char_count)

    def test_unique_words_1(self):
        testedObject = TextAnalyzer()
        text = "To był naprawdę okropny dzień To był naprawdę okropny dzień!!"
        uq_word_counts = testedObject.unique_words(text)
        self.assertEqual(6, uq_word_counts)

