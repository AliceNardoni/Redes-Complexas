# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 17:41:05 2017

@author: alice.marteli
"""
import json
import networkx as nx 
import matplotlib.pyplot as plt
import random




with open('entrada_amigos_proximos.json', encoding='UTF-8') as data_file:
    data = json.load(data_file)  #<class 'dict'>  len = 4 
 

# PARA SALVAR ARQUIVO DE SAIDA COM OS ÍNDICES CALCULADOS


my_randoms = [0, 1, 2, 3, 5, 6, 13, 17]

nome_my_randoms = []
for indice in my_randoms:
    nome_my_randoms.append(data['nodes'][indice]['name'] )




print('** Amigos próximos **')
dic_rel_random = {}
for alvo in my_randoms:
    print(alvo, ' - ', data['nodes'][alvo]['name']) 
    
    for indice in range(len(data['links'])): #range(0, 7333)
        target = data['links'][indice]['target'] # destino/relaciomamentos ? <class 'int'>
        source = data['links'][indice]['source'] # origem ? <class 'int'>
        t_nome = data['nodes'][target]['name']
        s_nome =data['nodes'][source]['name']

        if alvo == target:
            #print('target', target)
            #print('source', source)
            if target not in dic_rel_random: # target é os num sorteados
                
                dic_rel_random[target] = [source]   #
                
                
            else:
                if source not in dic_rel_random[target]:
                    dic_rel_random[target].append(source)
                    
#print(dic_rel_random)        
dicionario_p2 = {}

for chave in dic_rel_random:  # é os nós (pessoas) da chave dic_rel_random que são os elementos my_randoms
    dicionario_p2[chave] = [] # para cada nova chave seu conteudo é criado com uma lista vazia
    #print(dicionario_p2)

    for valor in dic_rel_random[chave]: # vai verificar quais relacionamentos coincidem com as pessoas da lista my_randoms
                                        #{0: [634, 629, 8, 6, 3, 1] para cada elemento da lista da chave 0: (valor sao os elementos da lista das chaves)
                                        # chave 0: valores da lista --->  6 esta dentro da lista my_randoms ? 
                                        # dic_rel_random[chave] = conteudo da chave (a lista..)
        if valor in my_randoms: # se esta dentro da lista, então para essa chave (zero), insere no dicionario_p2[chave zero] valor 6
            dicionario_p2[chave].append(valor) # dicionario_p2[0].append(6) dicionario_p2[0].append(1) {0: [6, 1]}
                                               # dicionario_p2[1].append(0) dicionario_p2[0].append(2) dicionario_p2[0].append(6) {mae: [ma, le, pai]} -> {1: [0, 1, 6]}
#print(set(dicionario_p2))
#print(dicionario_p2)

        #print( dic_rel_random[target])
               
    
    
#print('dicionario criado com base nos numeros sorteados')
#print(dic_rel_random)  #<class 'dict'>

#troca indice por nomes
#print(dicionario_p2)

dicionario_p3 = {}
for chave in dicionario_p2:
    temp_list = []
    for indice in range(len( dicionario_p2[chave])):
        nome =  data['nodes'][dicionario_p2[chave][indice]]['name']
        temp_list.append(nome)

    nome_chave =  data['nodes'][chave]['name']
    dicionario_p3[nome_chave] = temp_list
    


    
#troca valores na lista

    
    

dicionario_p3['alice'] = nome_my_randoms
#print(type(dic_rel_random))
g2 = nx.Graph(dicionario_p3)  

plt.figure( 3  ,figsize=(10,5))
nx.draw(g2, font_size=8, with_labels = True)
plt.savefig('amigos_proximos_fb.png')
#plt.show()




# PARA SALVAR ARQUIVO DE SAIDA COM OS ÍNDICES CALCULADOS
file = open('arquivo_saida_amigos_proximos_facebook.txt', 'w') 
file.write('Numero de Vertices: '+str(len(nx.degree(g2))) +'\n') 
file.write('\nNumero de arestas: ' + str(len(nx.edges(g2)))+'\n')
file.write('\nLista de arestas:'+str(nx.edges(g2))+'\n')
file.write('\nGraus: '+str(nx.degree(g2))+'\n')
file.write('\nMinimo Caminho Medio:'+str(nx.average_shortest_path_length(g2)))
file.write('\nCoeficientede Aglomeração:  '+ str(nx.clustering(g2)))
file.write('\nMatriz de adjacencia:'+str(nx.adjacency_matrix(g2)))
file.write('\nDiametro:'+str(nx.diameter(g2)))

file.close()



