import math
import random

class Jogador:
    def __init__(self,letra):
        #letra  pode ser X ou O
        self.letra = letra
    
    #fazer os próximos jogadores jogarem
    def get_move(self,jogo):
        pass
class JogadorAleatorio(Jogador):
    def __init__(self, letra):
        super().__init__(letra)
    def get_move(self, jogo):
       pass
class JogadorVerdadeiro(Jogador):
    def __init__(self, letra):
        super().__init__(letra)
    def __init__(self, letra):
        pass