# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 17:15:12 2023

@author: aluno
"""

import cv2
import numpy
foto = 'entrada.jpg'
imagem = cv2.imread(foto)

#########################################################################################################
#=======================================================================================================#
#########################################################################################################

#cria uma imagem (matriz) e preenche seus pixels com tons de cinza
#cada tom de cinza equivale à média dos tres canais daquele pixel
cinzas = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8)
for i in range (imagem.shape[0]):
    for j in range (imagem.shape[1]):
        cinzas[i][j] = (imagem[i][j].sum()//3)
cv2.imshow("Original", cinzas)

#########################################################################################################
#=======================================================================================================#
#########################################################################################################

#adiciona uma borda preta de 1 px na imagem
borda = numpy.zeros(((imagem.shape[0]+2), (imagem.shape[1]+2)), dtype = numpy.uint8)
for i in range (imagem.shape[0]):
    for j in range (imagem.shape[1]):
        borda[i+1][j+1] = cinzas[i][j]
cv2.imshow("Borda Preta", borda)

#########################################################################################################
#=======================================================================================================#
#########################################################################################################

operador1 = [[1,0,1],[0,1,0],[1,0,1]]
for i in range (3):
    for j in range (3):
        operador1[i][j] = ((i+j)%2)
print('Operador 1 =')
print(operador1)
print('')

transformada1 = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8)
for i in range ((imagem.shape[0])):
    for j in range ((imagem.shape[1])):
        m = n = 0
        aux1 = ((borda[i-1][j-1]) * (operador1[m][n]))
        aux2 = ((borda[i-1][j]) * (operador1[m][n+1]))
        aux3 = ((borda[i-1][j+1]) * (operador1[m][n+2]))
        aux4 = ((borda[i][j-1]) * (operador1[m+1][n]))
        aux5 = ((borda[i][j]) * (operador1[m+1][n+1]))
        aux6 = ((borda[i][j+1]) * (operador1[m+1][n+2]))
        aux7 = ((borda[i+1][j-1]) * (operador1[m+2][n]))
        aux8 = ((borda[i+1][j]) * (operador1[m+2][n+1]))
        aux9 = ((borda[i+1][j+1]) * (operador1[m+2][n+2]))
        transformada1 [i][j] = aux1 + aux2 + aux3 + aux4 + aux5 + aux6 + aux7 + aux8 + aux9
cv2.imshow("Transformacao I", transformada1)

#########################################################################################################
#=======================================================================================================#
#########################################################################################################

operador2 = [[0,1,0],[1,-4,1],[0,1,0]]
print('Operador 2 =')
print(operador2)
print('')

transformada2 = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8)
for i in range ((imagem.shape[0])):
    for j in range ((imagem.shape[1])):
        m = n = 0
        aux1 = ((borda[i-1][j-1]) * (operador2[m][n]))
        aux2 = ((borda[i-1][j]) * (operador2[m][n+1]))
        aux3 = ((borda[i-1][j+1]) * (operador2[m][n+2]))
        aux4 = ((borda[i][j-1]) * (operador2[m+1][n]))
        aux5 = ((borda[i][j]) * (operador2[m+1][n+1]))
        aux6 = ((borda[i][j+1]) * (operador2[m+1][n+2]))
        aux7 = ((borda[i+1][j-1]) * (operador2[m+2][n]))
        aux8 = ((borda[i+1][j]) * (operador2[m+2][n+1]))
        aux9 = ((borda[i+1][j+1]) * (operador2[m+2][n+2]))
        auxF = (aux1 + aux2 + aux3 + aux4 + aux5 + aux6 + aux7 + aux8 + aux9)
        if auxF < 0:
            auxF = 0
        if auxF > 255:
            auxF = 255
        transformada2 [i][j] = auxF
cv2.imshow("Transformacao II", transformada2)
cv2.waitKey(0)