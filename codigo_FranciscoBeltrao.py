# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 14:02:46 2017

@author: alicenmart2@gmail.com
"""

import networkx as nx 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy as sp
import collections


dir_shapes = '..\\Grafos_FB\\'


nome_shape_vertices = 'pontos_subbacia'
nome_shape_edges = 'linhas_subbacia'
'''
nome_shape_vertices = 'pontos_teste_manual'
nome_shape_edges = 'linhas_teste_manual' 
''' 

pos = {}

def abrir_shape(nome_shape, tipo ):
    
    print('carregando arquivo: ', nome_shape)
    lista_objetos = []
    arquivo_shape = "{dir_entrada}{nome_arquivo}{extensao}"
    arquivo_shape = arquivo_shape.format(dir_entrada = dir_shapes, nome_arquivo = nome_shape, extensao = '.shp')
    
    driver = ogr.GetDriverByName('ESRI Shapefile')
    data_source =  driver.Open(arquivo_shape, 0)
    layer = data_source.GetLayer()

    for feature in layer:
    #print( feature.GetField("vertx_name"))
        if tipo == 'V':
            lista_objetos.append( feature.GetField("vertx_name") )
            geom = feature.GetGeometryRef()
            pos[ feature.GetField("vertx_name") ] = (geom.GetX(), geom.GetY())
                 
        else:
            #lista_objetos.append({'de':feature.GetField("edgetex_to"),  'para':feature.GetField("edgex_from")        })
            lista_objetos.append({'de':feature.GetField("edgex_from"),  'para':feature.GetField("edgetex_to")        })
        
    layer.ResetReading() 
    
    data_source = None
    
    return lista_objetos
    
    
vertices = abrir_shape(nome_shape_vertices,'V')
edges = abrir_shape(nome_shape_edges,'E')


print('Criando Grafo ')

dicionario = {}

for vertice in vertices:
    
    for indice in range(len(edges)):
        de = edges[indice]['de']
        para =  edges[indice]['para']
        
        if vertice == de:
            if vertice not in dicionario:
                dicionario[de] = [para]
            else:
                if para not in dicionario[de]:
                    dicionario[de].append(para)
                    
                    

g = nx.Graph(dicionario)


plt.figure(1, figsize = (60,60))
nx.draw( g, pos, font_size=9 , with_labels = True)
plt.savefig("labels.png")
plt.show()



dic_vertices_associados = {}

for valor in range(len(vertices)):
    
    dic_vertices_associados[vertices[valor]] = valor
    dic_vertices_associados[valor] = vertices[valor]
    

print('gerando matriz')

matriz = np.zeros( ( len(vertices), len(vertices) ), dtype=np.int )


for indice_vertice in range(len(vertices)):
    
    vertice = dic_vertices_associados[indice_vertice]
    
    
    if vertice in dicionario.keys():
        
        linha = vertices.index(vertice)
        
        lista = dicionario[vertice]      
        
        for indice in lista:
            
            coluna = vertices.index(indice)
            matriz[linha][coluna] = 1
            
    
# salvando matriz em arquivo  
cabecalho = []

for indice in range(len(vertices)):
    cabecalho.append(  dic_vertices_associados[indice]    )


my_df = pd.DataFrame(matriz, columns=cabecalho, index=cabecalho)

my_df.to_csv('saida_csv.csv', index=True, header=True, sep=';')



# PARA SALVAR ARQUIVO DE SAIDA COM OS ÍNDICES CALCULADOS
file = open('indices_calculados.csv', 'w') 
file.write('Numero de Vertices: '+str(len(nx.degree(g))) +'\n') 
file.write('\nNumero de arestas: ' + str(len(nx.edges(g)))+'\n')
file.write('\nLista de arestas:'+str(nx.edges(g))+'\n')

file.write('\nGraus: '+str(nx.degree(g))+'\n') 

grau = pd.DataFrame.from_dict(nx.degree(g), orient='index')
file.write('\nGrau médio do componente principal: ' + str(sp.mean(grau)[0]))   

file.write('\nMinimo Caminho Medio:'+str(nx.average_shortest_path_length(g))) #Graph is not connected
file.write('\nDiametro funcao(py):'+str(nx.diameter(g))) #NetworkXError: Graph not connected: infinite path length
file.write('\n Densidade da rede: ' + str(nx.density(g)))  


file.write('\nMatriz de adjacencia funcao(py):'+str(nx.adjacency_matrix(g)))

file.write('\nCoeficientede Aglomeração:  '+ str(nx.clustering(g)))

dic_aglomeracao = nx.clustering(g)
total_aglomeracao = 0

for chave in dic_aglomeracao:
    total_aglomeracao += dic_aglomeracao[chave]
    
media_aglomeracao = total_aglomeracao/len(dic_aglomeracao)
file.write('\nCoeficiente de Aglomeração Médio calculado:  '+ str(media_aglomeracao))

file.close()


lista = []
dicionario = g.degree()
for chave in dicionario:
    lista.append(dicionario[chave])
    
degree_sequence = sorted(lista, reverse=True)  
degreeCount = collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())

fig, ax = plt.subplots()
plt.bar(deg, cnt, width=0.80, color='b')

plt.title("Degree Histogram")
plt.ylabel("Count")
plt.xlabel("Degree") 
ax.set_xticks([d + 0.4 for d in deg])
ax.set_xticklabels(deg)
plt.savefig("histogram.png")

plt.show()