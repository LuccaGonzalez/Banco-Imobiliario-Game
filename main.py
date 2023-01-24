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



# Iniciando o Game
Initializing()

# with open('Players.csv', 'r', encoding='UTF8') as file:
#         reader = csv.reader(file)

# definindo o jogador inicial
initialPlayer = random.choice(players)
print('\nO jogador {}, irá começar!'.format(initialPlayer))
print('\n***** Rodada 1 *****')

