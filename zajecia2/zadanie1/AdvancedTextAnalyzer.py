from zajecia2.zadanie1.TextAnalyzer import TextAnalyzer
from transformers import pipeline


class AdvancedTextAnalyzer(TextAnalyzer):
    def sentiment_analysis(self, text):
        sentiment_pipeline = pipeline("sentiment-analysis")
        return sentiment_pipeline(text)