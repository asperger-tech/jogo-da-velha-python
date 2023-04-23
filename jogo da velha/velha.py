class JogoDaVelha():
    tabuleiro = {'7':" ",'8':" ",'9':" ",
                 '4':" ",'5':" ",'6':" ",
                 '1':" ",'2':" ",'3':" ",}
    turno = None
    
    def __init__(self, jogador_inicial="X"):
        self.turno = jogador_inicial

    def numeracaoTabuleiro(self):
        print(f" 7 | 8 | 9 ")
        print("-----------")
        print(f" 4 | 5 | 6 ")
        print("-----------")
        print(f" 1 | 2 | 3 ")

    def exibirtabuleiro(self):
        print(f"{self.tabuleiro['7']} | {self.tabuleiro['8']} | {self.tabuleiro['9']}")
        print("---------")
        print(f"{self.tabuleiro['4']} | {self.tabuleiro['5']} | {self.tabuleiro['6']}")
        print("---------")
        print(f"{self.tabuleiro['1']} | {self.tabuleiro['2']} | {self.tabuleiro['3']}")
    
    def verificarJogada(self,jogada):
        if jogada in self.tabuleiro.keys():
            if self.tabuleiro[jogada] == " ":
                return True
        return False
    
    def verificarTabuleiro(self):
        #verificações verticais 
        if self.tabuleiro['7'] == self.tabuleiro['4'] == self.tabuleiro['1'] != 0:
            return self.tabuleiro['7']
        elif self.tabuleiro['8'] == self.tabuleiro['5'] == self.tabuleiro['2'] != 0:
            return self.tabuleiro['8']
        elif self.tabuleiro['9'] == self.tabuleiro['6'] == self.tabuleiro['3'] != 0:
            return self.tabuleiro['9']
        
        #verificação horizontal
        if self.tabuleiro['7'] == self.tabuleiro['8'] == self.tabuleiro['9'] != 0:
            return self.tabuleiro['7']
        elif self.tabuleiro['4'] == self.tabuleiro['5'] == self.tabuleiro['6'] != 0:
            return self.tabuleiro['4']
        elif self.tabuleiro['1'] == self.tabuleiro['2'] == self.tabuleiro['3'] != 0:
            return self.tabuleiro['1']
        
        #verificaçao diagonal
        if self.tabuleiro['7'] == self.tabuleiro['5'] == self.tabuleiro['3'] != 0:
            return self.tabuleiro['7']
        elif self.tabuleiro['1'] == self.tabuleiro['5'] == self.tabuleiro['9'] != 0:
            return self.tabuleiro['1']
        
        #verifica empate
        if [*self.tabuleiro.values()].count(" ") == 0:
            return "empate!"
        else:
            return [*self.tabuleiro.values()].count(" ")

    def jogar(self):

        self.numeracaoTabuleiro()
        while True:
            self.exibirtabuleiro()

            print(f"Turno do {self.turno}, qual sua jogada?")
            
            while True:
                jogada = input("jogada: ")

                if self.verificarJogada(jogada):
                    break
                else: 
                    print(f"jogada do {self.turno} inválida.")
            
            self.tabuleiro[jogada] = self.turno

            estado = self.verificarTabuleiro()

            if estado == "X":
                print("X é o vencedor!")
                break
            elif estado == "O":
                print("O é o vencedor!")
                break
            if estado == "empate":
                print("EMPATE!")
                break

            self.turno = "X" if self.turno == "O" else "O"


    
