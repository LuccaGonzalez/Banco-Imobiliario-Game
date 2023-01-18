class Player:

    # # atributos
    global name, initialBalance, actualBalance, properties

    name = ''
    initialBalance = 5000
    actualBalance = 0
    properties = []


    def collectPlayers():

        players = []

        numberOfPlayers = int(input('Digite o número de jogadores: '))

        # determinando a quantidade de jogadores
        if numberOfPlayers < 2:
            numberOfPlayers = int(input('Tente novamente: '))

        elif numberOfPlayers > 6:
            numberOfPlayers = int(input('Tente novamente: '))

        else:
            pass

        # determinando o nome dos jogadores
        for i in range(numberOfPlayers):

            n = input('Digite o nome do jogador {}: '.format((i+1)))
            if n != '':
                players.insert(i, n)
            else:
                n = input('Digite o nome do jogador {}: '.format((i+1)))
                players.insert(i, n)

        # visualizando o nome dos jogadores
        print('\nOs jogadores são:')
        for a in range(numberOfPlayers):

            print('> jogador {}: {}'.format((a+1), players[a]))
