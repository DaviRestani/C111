import numpy as np
import pandas as pd

# CRIANDO UMA SERIES NO PANDAS
indexes = ['a', 'b', 'c']
values = [10, 20, 30]
# s1 = pd.Series(index=indexes, data=values)
s1 = pd.Series({'a':10, 'b':20, 'c':30})
s2 = pd.Series({'a':10, 'c':50, 'd':80})

# print(s1.add(s2, fill_value=0))
# print(s1 + s2)
# print(s1)
# print(s1['b'])

# SLICING NO PANDAS
# Mostrando apenas os elementos B e C
# Notacao pandas
# print(s1[['b', 'c']])
# Notacao numpy
# print(s1[1:])

# CRIANDO UM DATAFRAME
np.random.seed(10)
dados = np.random.randint(1, 50, [5, 4])
linhas = ['A', 'B', 'C', 'D', 'E']
colunas = ['W', 'X', 'Y', 'Z']
df1 = pd.DataFrame(data=dados,
                   index=linhas,
                   columns=colunas)

# print(df1)
#
# # SLICINGS NO DATAFRAME
# # PEGANDO APENAS UMA COLUNA
# print(df1['X'])
#
# # PEGANDO MULTIPLAS COLUNAS
# print(df1[['X', 'Y']])
#
# # PEGANDO UM VALOR ESPECIFICO NO DATAFRAME
# print(df1['Y']['C'])

# IMPORTANDO UM DATASET NO PANDAS
dfPaises = pd.read_csv('paises.csv',
                       delimiter=';')

print(dfPaises.head(0))
print(dfPaises['Country'])




