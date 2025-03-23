from unittest import TestCase

from zajecia2.zadanie1.AdvancedTextAnalyzer import AdvancedTextAnalyzer


class TestAdvancedTextAnalyzer(TestCase):
    def test_sentiment_analysis_1(self):
        testObject = AdvancedTextAnalyzer()
        sentiments = testObject.sentiment_analysis("Welcome to costco. I love You")
        sentiment_label = sentiments[0]["label"]
        self.assertEqual("POSITIVE", sentiment_label)

    def test_sentiment_analysis_2(self):
        testObject = AdvancedTextAnalyzer()
        sentiments = testObject.sentiment_analysis("Welcome to costco. I love You")
        sentiment_score = sentiments[0]["score"]
        self.assertGreater(sentiment_score, 0.9)

    def test_sentiment_analysis_3(self):
        testObject = AdvancedTextAnalyzer()
        sentiments = testObject.sentiment_analysis("You cannot program in python, hipster")
        sentiment_label = sentiments[0]["label"]
        self.assertEqual("NEGATIVE", sentiment_label)

    def test_sentiment_analysis_4(self):
        testObject = AdvancedTextAnalyzer()
        sentiments = testObject.sentiment_analysis("You cannot program in python, hipster")
        sentiment_score = sentiments[0]["score"]
        self.assertGreater(sentiment_score, 0.9)
