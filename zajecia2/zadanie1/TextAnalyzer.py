class TextAnalyzer:
    def word_count(self, text):
        return len([word for word in text.split(" ") if word])

    def char_count(self, text):
        return len(text)

    def unique_words(self, text):
        return len(set(text.split(" ")))
