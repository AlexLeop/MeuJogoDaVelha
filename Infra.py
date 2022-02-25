

branco = ' '


def tela():

    """
    :board - responsavel por criar e armazenar um espaço para cada casa do jogo da velha
    :return -  Retorna um array de board
    """
    board = [
        [branco, branco, branco],
        [branco, branco, branco],
        [branco, branco, branco],
    ]

    return board


def printandotela(board) -> None:
    """
    :for - Printa na tela o board colocando um | entre cada um
    :if - A cada 3 board é printado na tela uma linha abaixo não ultrapassando a quantidade de duas linhas
    """
    for i in range(3):
        print('|'.join(board[i]))

        if i < 2:
            print('-----')


def movimento(board, i: int, j: int, jogador: int) -> None:
    try:
        if board[i][j] == branco:
            if jogador == 0:
                board[i][j] = 'X'
            elif jogador == 1:
                board[i][j] = 'O'
    except:
        print('Posição ocupada, por favor escolha outra posição')
        return movimento(board, i, j, jogador)


def verificaganhador(board) -> object:
    for i in range(3):
        # Linha
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != branco:
            return board[i][0]

    for i in range(3):
        # Coluna
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != branco:
            return board[0][i]

    # Diagonal 1
    if board[0][0] != branco and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]

    # Diagonal 2
    if board[0][2] != branco and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]

    for i in range(3):
        for j in range(3):
            if board[i][j] == branco:
                return False
    return 'EMPATE!'
