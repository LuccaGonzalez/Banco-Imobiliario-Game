import random
import pandas as pd

global imbChoicePC

imbChoicePC = random.randrange(0, 60)

# selectLine = pd.read_excel('Imoveis.xlsx', sheet_name='Plan Imoveis', index_col='Codigo')
# selectLine = selectLine.loc[imbChoicePC]
# selectValue = selectLine.iloc[]

table = pd.read_excel('Imoveis.xlsx', sheet_name='Plan Imoveis', engine='openpyxl')
immobileValue = table.iloc[imbChoicePC, 3]

# print('\n{}'.format(imbChoicePC))
# print('\n{}'.format(selectedLine))
print(immobileValue)
