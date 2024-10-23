# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 17:02:29 2023

@author: aluno
"""

import cv2
import numpy
foto = 'entrada4.png'
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

#pega a imagem em tons de cinza e transforma eles em preto ou branco dependendo do seu valor
pretoBranco = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8)
for i in range (imagem.shape[0]):
    for j in range (imagem.shape[1]):
        if ((cinzas[i][j])/2) > 100:
            pretoBranco[i][j] = 255
        else:
            pretoBranco[i][j] = 0
cv2.imshow("Preto e Branco", pretoBranco)

#########################################################################################################
#=======================================================================================================#
#########################################################################################################

opFull = [[255,255,255],[255,255,255],[255,255,255]]
print('Operador Cheio =')
print(opFull)
print('')

opCruz = [[0,255,0],[255,255,255],[0,255,0]]
print('Operador Em Cruz =')
print(opCruz)
print('')

#########################################################################################################
#=======================================================================================================#
#########################################################################################################

dilatada1 = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8)
for i in range ((imagem.shape[0])-2):
    for j in range ((imagem.shape[1])-2):
        m = n = 0
        auxF = 0

        if (pretoBranco[i][j] == 255) and (opFull[m][n] == 255):
            auxF = auxF + 1
        if (pretoBranco[i][j+1] == 255) and (opFull[m][n+1] == 255):
            auxF = auxF + 1
        if (pretoBranco[i][j+2] == 255) and (opFull[m][n+2] == 255):
            auxF = auxF + 1
        if (pretoBranco[i+1][j] == 255) and (opFull[m+1][n] == 255):
            auxF = auxF + 1
        if (pretoBranco[i+1][j+1] == 255) and (opFull[m+1][n+1] == 255):
            auxF = auxF + 1
        if (pretoBranco[i+1][j+2] == 255) and (opFull[m+1][n+2] == 255):
            auxF = auxF + 1
        if (pretoBranco[i+2][j] == 255) and (opFull[m+2][n] == 255):
            auxF = auxF + 1
        if (pretoBranco[i+2][j+1] == 255) and (opFull[m+2][n+1] == 255):
            auxF = auxF + 1
        if (pretoBranco[i+2][j+2] == 255) and (opFull[m+2][n+2] == 255):
            auxF = auxF + 1

        if auxF > 0:
            dilatada1[i+1][j+1] = 255
cv2.imshow("Dilatacao I", dilatada1)

#########################################################################################################
#=======================================================================================================#
#########################################################################################################

dilatada2 = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8)
for i in range ((imagem.shape[0])-2):
    for j in range ((imagem.shape[1])-2):
        m = n = 0
        auxF = 0

        #if (pretoBranco[i][j] == 255) and (opCruz[m][n] == 255):
            #auxF = auxF + 1
        if (pretoBranco[i][j+1] == 255) and (opCruz[m][n+1] == 255):
            auxF = auxF + 1
        #if (pretoBranco[i][j+2] == 255) and (opCruz[m][n+2] == 255):
            #auxF = auxF + 1
        if (pretoBranco[i+1][j] == 255) and (opCruz[m+1][n] == 255):
            auxF = auxF + 1
        if (pretoBranco[i+1][j+1] == 255) and (opCruz[m+1][n+1] == 255):
            auxF = auxF + 1
        if (pretoBranco[i+1][j+2] == 255) and (opCruz[m+1][n+2] == 255):
            auxF = auxF + 1
        #if (pretoBranco[i+2][j] == 255) and (opCruz[m+2][n] == 255):
            #auxF = auxF + 1
        if (pretoBranco[i+2][j+1] == 255) and (opCruz[m+2][n+1] == 255):
            auxF = auxF + 1
        #if (pretoBranco[i+2][j+2] == 255) and (opCruz[m+2][n+2] == 255):
            #auxF = auxF + 1

        if auxF > 0:
            dilatada2[i+1][j+1] = 255
cv2.imshow("Dilatacao II", dilatada2)

#########################################################################################################
#=======================================================================================================#
#########################################################################################################

erosao1 = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8)
for i in range ((imagem.shape[0])-2):
    for j in range ((imagem.shape[1])-2):
        m = n = 0
        auxF = 0

        if (pretoBranco[i][j] == 255) and (opFull[m][n] == 255):
            auxF = auxF + 1
        if (pretoBranco[i][j+1] == 255) and (opFull[m][n+1] == 255):
            auxF = auxF + 1
        if (pretoBranco[i][j+2] == 255) and (opFull[m][n+2] == 255):
            auxF = auxF + 1
        if (pretoBranco[i+1][j] == 255) and (opFull[m+1][n] == 255):
            auxF = auxF + 1
        if (pretoBranco[i+1][j+1] == 255) and (opFull[m+1][n+1] == 255):
            auxF = auxF + 1
        if (pretoBranco[i+1][j+2] == 255) and (opFull[m+1][n+2] == 255):
            auxF = auxF + 1
        if (pretoBranco[i+2][j] == 255) and (opFull[m+2][n] == 255):
            auxF = auxF + 1
        if (pretoBranco[i+2][j+1] == 255) and (opFull[m+2][n+1] == 255):
            auxF = auxF + 1
        if (pretoBranco[i+2][j+2] == 255) and (opFull[m+2][n+2] == 255):
            auxF = auxF + 1

        if auxF == 9:
            erosao1[i+1][j+1] = 255
cv2.imshow("Erosa I", erosao1)

dilatadaErosao1 = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8)
for i in range ((imagem.shape[0])-2):
    for j in range ((imagem.shape[1])-2):
        m = n = 0
        auxF = 0

        if (erosao1[i][j] == 255) and (opFull[m][n] == 255):
            auxF = auxF + 1
        if (erosao1[i][j+1] == 255) and (opFull[m][n+1] == 255):
            auxF = auxF + 1
        if (erosao1[i][j+2] == 255) and (opFull[m][n+2] == 255):
            auxF = auxF + 1
        if (erosao1[i+1][j] == 255) and (opFull[m+1][n] == 255):
            auxF = auxF + 1
        if (erosao1[i+1][j+1] == 255) and (opFull[m+1][n+1] == 255):
            auxF = auxF + 1
        if (erosao1[i+1][j+2] == 255) and (opFull[m+1][n+2] == 255):
            auxF = auxF + 1
        if (erosao1[i+2][j] == 255) and (opFull[m+2][n] == 255):
            auxF = auxF + 1
        if (erosao1[i+2][j+1] == 255) and (opFull[m+2][n+1] == 255):
            auxF = auxF + 1
        if (erosao1[i+2][j+2] == 255) and (opFull[m+2][n+2] == 255):
            auxF = auxF + 1

        if auxF > 0:
            dilatadaErosao1[i+1][j+1] = 255
cv2.imshow("Dilatando a Erosao I", dilatadaErosao1)

cv2.waitKey(0)