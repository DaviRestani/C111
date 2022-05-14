import numpy as np
# Questão 1
musicas = {'nome': ['Yesterday', 'Starway to Heaven', 'Comfortably Numb', 'Satisfaction', 'Baba O Riley'],
  'ano_lancamento': [1980, 1975, 1979, 1983, 1975]}

for k,v in musicas.items():
 print('Quantidade de musicas cadastradas:',musicas.values())

# dados da musica mais antiga
musica_antiga = musicas['ano_lancamento'][0]
for i in range(len(musicas['ano_lancamento'])):
  if musicas['ano_lancamento'][i] < musica_antiga:
   musica_antiga = musicas['ano_lancamento'][i]
   musica_antiga_nome = musicas['nome'][i]
 
print('A musica mais antiga eh:', musica_antiga_nome, 'que foi lancada em', musica_antiga)


# Questão 2

#a)
arr1 = np.array(['John', 'Paul', 'George', 'Ringo'])
arr2 = np.array(['Jimi', 'Freddie', 'Janis', 'Jim'])

#b)
arr3 = np.concatenate((arr1, arr2))
print('Array concatenado:',arr3)

#c)
arr4 = arr3.reshape(4,2)
print('Array reshape:',arr4)

#d)
# ordenar o array em ordem alfabetica
arr5 = np.sort(arr3)
print('Array ordenado:',arr5)


#Questão 3
colors = [
{"color": "black", "type": "primary", "code": {"rgba": [255,255,255,1],"hex": "#000"}},
{"color": "green", "type": "secondary", "code": {"rgba": [0,255,0,0.1],"hex": "#0F0"}},
{"color": "yellow", "type": "primary","code": {"rgba": [255,255,0,0.7],"hex": "#FF0"}},
{"color": "blue", "type": "primary","code": {"rgba": [0,0,255,1],"hex": "#00F"}}
]

#a)
primary = np.char.find(colors, 'primary')
print('Cor primaria:',colors[primary])
