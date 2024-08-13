import json



class Card:
    def __init__(self, suit, value, face) -> None:
        self.suit = suit
        self.value = value
        self.face = face
    
class CardMaster:
    def __init__(self) -> None:
        self.config = self.readConfig()
        self.buildDeck()

    def readConfig(self, path:str):
        with open(path) as jfile:
            config = json.load(jfile)
        return config
    
    def buildDeck(self):
        default_suits = ['♠','♣','♡','♢']
        default_valus = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        for suit in default_suits:
            
    