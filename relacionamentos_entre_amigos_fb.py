# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 17:41:05 2017

@author: alice.marteli
"""
import json
import networkx as nx 
import matplotlib.pyplot as plt
import random

   
with open('entrada_relacionamentos_amigos.json', encoding='UTF-8') as data_file:
    data = json.load(data_file)  #<class 'dict'>  len = 4 
  
   
dicionario = {}
for indice in range(len(data['links'])):
    #print( type( data['links'][indice]['target']))
    target = data['links'][indice]['target']  #destino   <class 'int'>
    source = data['links'][indice]['source']  # origem   <class 'int'>
             
             
    if target not in dicionario:
        dicionario[target] = [source]
        #print(source)

    else:
        if source not in dicionario[target]:  #<class 'list'>
            dicionario[target].append(source)

pessoa = ''
quantidade = 0
for chave in dicionario:
    lista = dicionario[chave]
    if len(lista) > quantidade:
        quantidade = len(lista)
        pessoa = data['nodes'][chave]['name']
print(pessoa, quantidade)

dicionario[len(data['nodes'])+1] = dicionario.keys()  # insere alice

            
color_map = ['blue', 'green', "red", "pink", "orange"] #<class 'list'>
g = nx.Graph(dicionario)   # g  = <class 'networkx.classes.graph.Graph'>




# Para plotar a matriz

plt.figure(1, figsize = (50,50))  # <class 'matplotlib.figure.Figure'>

nx.draw(g, node_color = color_map, with_labels = True)
plt.savefig("relacionamentos_entre_amigos_fb.png")
#plt.show()





# PARA SALVAR ARQUIVO DE SAIDA COM OS ÍNDICES CALCULADOS
file = open('arquivo_saida_relacionamentos_entre_amigos_facebook.txt', 'w') 
file.write('Numero de Vertices: '+str(len(nx.degree(g))) +'\n') 
file.write('\nNumero de arestas: ' + str(len(nx.edges(g)))+'\n')
file.write('\nLista de arestas:'+str(nx.edges(g))+'\n')
file.write('\nGraus: '+str(nx.degree(g))+'\n')
file.write('\nMinimo Caminho Medio funcao(py):'+str(nx.average_shortest_path_length(g)))
file.write('\nCoeficientede Aglomeração:  '+ str(nx.clustering(g)))
file.write('\nMatriz de adjacencia funcao(py):'+str(nx.adjacency_matrix(g)))
file.write('\nDiametro funcao(py):'+str(nx.diameter(g)))


dic_aglomeracao = nx.clustering(g)
total_aglomeracao = 0

for chave in dic_aglomeracao:
    total_aglomeracao += dic_aglomeracao[chave]
    
media_aglomeracao = total_aglomeracao/len(dic_aglomeracao)
file.write('\nCoeficiente de Aglomeração Médio calculado:  '+ str(media_aglomeracao))

file.close()



'''
#print('Grau Medio:' + str(mean(nx.degree(g))))  # não funciona
print('Grau Medio:' + str(nx.average_node_connectivity(g)))
#Retorna a conectividade média de um gráfico G.   A conectividade média  de um gráfico G é a 
#média de conectividade de nó local em todos os pares de nós de G [

print('Grau Medio:' + str(nx.average_degree_connectivity(g)))
# Calcule a conectividade de grau médio do gráfico. 
#O grau médio de conectividade é o grau médio de vizinho mais próximo nós com grau k. 
#Para gráficos ponderados, uma medida análoga pode
#ser calculado usando o grau médio ponderado de vizinhos definido em
#Retorna   d: dict      Um dicionário codificado pelo grau k com o valor da conectividade média. 
#Esse algoritmo às vezes é chamado de "vizinhos mais próximos" 

print('Grau Medio:' + str(nx.average_neighbor_degree(g)))
#Retorna o grau médio da vizinhança de cada nó.
#Retorna       Um dicionário codificado por nó com o valor médio do grau de vizinho.
'''








