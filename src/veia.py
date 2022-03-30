class jogoDaVeia:
    def __init__(self):
        self.tabuleiro = [' ' for _ in range(9)]
        self.ganheikkj = None

    def print_tabuleiro(self):
        for row in [self.tabuleiro[i*3:(i+1)*3] for j in range(3)]
            print('| ' + ' | '.join(row) + ' |')
    
    @staticmethod
    def print_tabuleiro_num():
        numero_tabuleiro = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in numero_tabuleiro:
            print('| ' + ' | '.join(row) + ' |')

    def onde_mover(self):
        return [i for i, spot in enumerate(self.tabuleiro) if spot == ' ']
