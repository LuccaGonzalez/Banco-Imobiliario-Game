from classImmobile import Immobile as imb
from classPlayer import Player as player
import pandas as pd
import random


# Função iniciar jogo
def StartGame():
        
    print('\nBem-Vindo ao Banco Imobiliario!')
    print('O mínimo é de 2 jogadores e o máximo é de 6 jogadores.\n')

    player.collectPlayers()


def readFile():

    imbList = pd.read_excel('Imoveis.xlsx', sheet_name='Plan Imoveis')
    imbList = pd.DataFrame(imbList)
    imbList = imbList['Imovel'].tolist()

    imbChoicePC = random.choice(imbList)

    selectLine = pd.read_excel('Imoveis.xlsx', sheet_name='Plan Imoveis', index_col='Imovel')
    selectLine = selectLine.loc[imbChoicePC]


    # print(imbChoicePC)
    print(selectLine)
    # print(imbList)



# Iniciando o Game
# StartGame()
readFile()