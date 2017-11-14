# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 19:40:41 2017
@author: alice.marteli
"""
import networkx as nx 
import matplotlib.pyplot as plt

print('\nmatriz --> lista\n')

arq = open('matriz_aula.txt')
texto = arq.readlines()
matriz=[]
dicionario = {} 
for linha in texto:
    linha = linha.replace('\n','').split(',')
    matriz.append(linha) 
   
arq.close()

for linha in range(len(matriz)): 
    
    temp_list = []
    for coluna in range(len(matriz[linha])):        
        valor = int(matriz[linha][coluna])       
        
        if valor != 0:
            temp_list.append(coluna+1)
    dicionario[linha+1] = temp_list
print(dicionario)


print('\nlista --> matriz\n')

matriz2 = []
for x in range(len(dicionario)): 
    temp_list = []   
    for y in range(len(dicionario)): 
        if y+1 in dicionario[x+1]:
            temp_list.append(1)
        else:
            temp_list.append(0)
    matriz2.append(temp_list)
print(matriz2) 


g = nx.Graph(dicionario)  
plt.figure( 3  ,figsize=(5,5))
nx.draw(g, font_size=8, with_labels = True)
plt.savefig('grafo.png')
plt.show()


# Parte  II  - Cálculos dos indices

dic_grau  = {}
for i in range(len(matriz2)):
    dic_grau[i+1] = 0
    for j in range(len(matriz2[i])):
        dic_grau[i+1] = dic_grau[i+1] + matriz2[i][j]
        
print('\nGraus:', dic_grau)


total = 0
for valor in dic_grau:
    total = total + dic_grau[valor]
media = total/len(dic_grau)
print('\nGrau Medio:', media)



n_vertice = len(dicionario) 
print('\nNumero de Vertices: ', n_vertice)


temp_list = []
matriz_adjacente = []
for i in dicionario:
    for j in range(len(dicionario[i])):
        valor = (i,dicionario[i][j])
        temp_list.append(valor)
        matriz_adjacente.append(valor)

for i in range(len(temp_list)):
    temp_list[i] = tuple(set(temp_list[i]))
    
total_arestas = len(set(temp_list))
  
print('\nNumero de Arestas: ', total_arestas)  
    
print('\nDiametro:'+str(nx.diameter(g)))


print('\nCoeficientede Aglomeração: ', nx.clustering(g))
dic_aglomeracao = nx.clustering(g)
total_aglomeracao = 0

for chave in dic_aglomeracao:
    total_aglomeracao += dic_aglomeracao[chave]
    
media_aglomeracao = total_aglomeracao/len(dic_aglomeracao)
print('\nCoeficiente de Aglomeração Médio: ', media_aglomeracao)


print('\nMinimo Caminho Medio:'+str(nx.average_shortest_path_length(g)))

print('\nMatriz de adjacencia:', matriz_adjacente)



