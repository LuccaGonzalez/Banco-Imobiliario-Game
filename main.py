import pandas as pd
import random
import csv


# variáveis dos jogadores
initialBalance = 5000
actualBalance = 0
properties = []


# Função iniciar jogo
def Initializing():
        
    print('\nBem-Vindo ao Banco Imobiliario!')
    print('O mínimo é de 2 jogadores e o máximo é de 6 jogadores.\n')

    CollectPlayers()


def CollectPlayers():

    global players

    playersCollect = []

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

        n = ''

        while n == '':
            n = input('Digite o nome do jogador {}: '.format((i+1)))
        
            if n in playersCollect:
                n = ''
                
        playersCollect.insert(i, n)


    # visualizando o nome dos jogadores
    print('\nOs jogadores são:')
    for a in range(numberOfPlayers):

        print('> jogador {}: {}'.format((a+1), playersCollect[a]))

    players = playersCollect
    CreateFile(numberOfPlayers, playersCollect)


def CreateFile(nmbPlayers, playersCollecteds):

    # definindo o cabeçalho do arquivo csv
    header = ['Player', 'Balance', 'Properties']

    # abre e limpa o arquivo existente para escrever ou cria um novo 
    with open('Players.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)

        # escreve o cabeçalho do csv
        writer.writerow(header)

        # escreve o nome de cada player, o saldo inicial e zera as propriedades
        for i in range(nmbPlayers):
            dataPlayers = [playersCollecteds[i], initialBalance, 'null']
            csv.writer(f, delimiter=',').writerow(dataPlayers)


def ChoiceImmobile():

    global imbChoicePC

    imbChoicePC = random.randrange(0, 60)
   
    selectLine = pd.read_excel('Imoveis.xlsx', sheet_name='Plan Imoveis', index_col='Codigo')
    selectLine = selectLine.loc[imbChoicePC]


def ChoiceInitialPlayer():

    global players, initialPlayer

    # definindo o jogador inicial
    initialPlayer = random.choice(players)
    chosenIndex = players.index(initialPlayer)

    i = 0
    newList = []

    # enquanto o "i" for menor que o tamanho da "lista"
    while i < len(players):

        # adiciona o item escolhido da "lista" como PRIMEIRO item da "newList"
        newList.append(players[chosenIndex])

        # se o "index do item escolhido" for MENOR do que o "tamanho da lista" - 1, ou seja:
        # Ex.: (1) é menor que (3 - 1)?
        if (chosenIndex) < (len(players) - 1):
            # se sim, então: "choseIndex" = 1 + 1 (2)
            chosenIndex = chosenIndex + 1
        else:
            # se não, ou seja, quando "choseIndex" for igual a 2.
            # Então: "choseIndex" é modificado para 0
            chosenIndex = 0

        # enquanto isso, incrementamos +1 no "i", para interromper o while
        i = i+1

    # atualiza a lista inicial para a nova seqûencia de jogadores
    players = newList



# Iniciando o Game
Initializing()

# escolhe o jogador que irá começar
ChoiceInitialPlayer()

print('\nO jogador {}, irá começar!'.format(initialPlayer))
print('\n***** Rodada 1 *****')

# Criar um loop onde o programa:
# 1) Escolhe o imóvel aleatoriamente
# 2) Verifica se o jogador escolhido pode comprar o imóvel
# 3) Efetua a compra ou passa a vez
# 4) segue para o próximo jogador
# 5) repete os passos 1, 2 e 3
# 6) Faz isso até o último jogador da lista
# 7) Finaliza a rodada e inicia a próxima repetindo os mesmos passos
