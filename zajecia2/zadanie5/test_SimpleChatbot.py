from unittest import TestCase

from zajecia2.zadanie5.SimpleChatbot import SimpleChatbot


class TestSimpleChatbot(TestCase):
    pass
    def test_SimpleChatbot(self):
        bot = SimpleChatbot(["Jak się nazywasz?", "Jaki jest Twój ulubiony kolor?"])
        for question in bot:
            print(question)
            input()  # Użytkownik wpisuje odpowiedź
