import json

class ModelAI:
    liczba_modeli = 0
    
    def __init__(self, nazwa_modelu, wersja):
        self.nazwa_modelu = nazwa_modelu
        self.wersja = wersja
        self.nowy_model()

        
    @classmethod
    def nowy_model(cls):
        cls.liczba_modeli += 1
    
    @classmethod
    def ile_modeli(cls):
        return cls.liczba_modeli

    @classmethod
    def z_pliku(cls, nazwa_pliku):
        with open(nazwa_pliku, 'r') as f:
            data = json.load(f)
            return ModelAI(data["nazwa_modelu"], data["wersja"])

#
#
# obj = ModelAI.z_pliku("myjson.json")
# print(obj)
# print(ModelAI.liczba_modeli)
#
