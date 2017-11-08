# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 19:40:41 2017
@author: alice.marteli
"""

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