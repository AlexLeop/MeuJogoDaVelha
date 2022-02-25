from Infra import tela, movimento, printandotela, verificaganhador
import os


''' :Jogo_da_Velha: Responsavel por fazer a comunicação com o arquivo Infra.py para que o jogo seja executado'''


class JVelha:

    def __init__(self):
        self.vitoria = {
            'Jogador 1': 0,
            'Jogador 2': 0
        }
        self.jogador = 0

    def jogando(self, ganhador, board) -> None:
        while not ganhador:
            os.system('cls')
            printandotela(board)

            """ if jogador == 0:
                 i = random.randint(1, 3)
                 j = random.randint(1, 3)
                 board[i][j]
            else: """

            i = int(input('Qual a linha?'))
            j = int(input('Qual a coluna?'))

            self.jogador = (self.jogador + 1) % 2
            movimento(board, i-1, j-1, self.jogador)

            ganhador = verificaganhador(board)

    def resultado_do_jogo(self, ganhador, board) -> None:

        """ Verificando o jogador que venceu e atribuindo 1 ponto a mais ao respectivo vencedor"""
        if ganhador == 'O':
            self.vitoria['Jogador 1'] = self.vitoria['Jogador 1'] + 1
        else:
            self.vitoria['Jogador 2'] = self.vitoria['Jogador 2'] + 1

        os.system('cls')
        printandotela(board)

        print('============================')
        print('    FIM DE JOGO')
        print('============================')
        print(f'O vencedor foi: {ganhador} \n')

        """Plotando na tela o total de vitórias e quem foi o jogador que venceu"""

        print('============================')
        print('    Total de vitórias:')
        print('============================')
        print('1° Jogador :' + str(self.vitoria['Jogador 1']))
        print('2° Jogador :' + str(self.vitoria['Jogador 2']))


"""
:BOARD: Instância a função tela() em Infra.py
:ganhador: Verifica se houve um vencedor instânciando a função verificaganhador passando como parâmetro o board
"""
board = tela()
ganhador = verificaganhador(board)

'''
:Jogo: Instância a classe Jogo_da_Velha e a funçao jogando passando como parâmetros ganhador e board
'''
jogo = JVelha()
jogo.jogando(ganhador, board)

jogo.resultado_do_jogo(ganhador, board)
