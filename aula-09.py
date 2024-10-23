# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 17:49:07 2023

@author: aluno
"""

import cv2
import numpy
foto = 'entrada3.jpg'
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

operador3 = [[255,255,255],[255,255,255],[255,255,255]]
print('Operador III =')
print(operador3)
print('')

transformada3 = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8)
for i in range ((imagem.shape[0])-2):
    for j in range ((imagem.shape[1])-2):
        m = n = 0
        auxF = 0

        if (pretoBranco[i][j] == 255) and (operador3[m][n] == 255):
            auxF = auxF + 1
        if (pretoBranco[i][j+1] == 255) and (operador3[m][n+1] == 255):
            auxF = auxF + 1
        if (pretoBranco[i][j+2] == 255) and (operador3[m][n+2] == 255):
            auxF = auxF + 1
        if (pretoBranco[i+1][j] == 255) and (operador3[m+1][n] == 255):
            auxF = auxF + 1
        if (pretoBranco[i+1][j+1] == 255) and (operador3[m+1][n+1] == 255):
            auxF = auxF + 1
        if (pretoBranco[i+1][j+2] == 255) and (operador3[m+1][n+2] == 255):
            auxF = auxF + 1
        if (pretoBranco[i+2][j] == 255) and (operador3[m+2][n] == 255):
            auxF = auxF + 1
        if (pretoBranco[i+2][j+1] == 255) and (operador3[m+2][n+1] == 255):
            auxF = auxF + 1
        if (pretoBranco[i+2][j+2] == 255) and (operador3[m+2][n+2] == 255):
            auxF = auxF + 1

        if auxF == 9:
            transformada3[i+1][j+1] = 255
cv2.imshow("Transformacao III", transformada3)

#########################################################################################################
#=======================================================================================================#
#########################################################################################################

operador4 = [[0,255,0],[255,255,255],[0,255,0]]
print('Operador IV =')
print(operador4)
print('')

transformada4 = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8)
for i in range ((imagem.shape[0])-2):
    for j in range ((imagem.shape[1])-2):
        m = n = 0
        auxF = 0

        #if (pretoBranco[i][j] == 255) and (operador4[m][n] == 255):
            #auxF = auxF + 1
        if (pretoBranco[i][j+1] == 255) and (operador4[m][n+1] == 255):
            auxF = auxF + 1
        #if (pretoBranco[i][j+2] == 255) and (operador4[m][n+2] == 255):
            #auxF = auxF + 1
        if (pretoBranco[i+1][j] == 255) and (operador4[m+1][n] == 255):
            auxF = auxF + 1
        if (pretoBranco[i+1][j+1] == 255) and (operador4[m+1][n+1] == 255):
            auxF = auxF + 1
        if (pretoBranco[i+1][j+2] == 255) and (operador4[m+1][n+2] == 255):
            auxF = auxF + 1
        #if (pretoBranco[i+2][j] == 255) and (operador4[m+2][n] == 255):
            #auxF = auxF + 1
        if (pretoBranco[i+2][j+1] == 255) and (operador4[m+2][n+1] == 255):
            auxF = auxF + 1
        #if (pretoBranco[i+2][j+2] == 255) and (operador4[m+2][n+2] == 255):
            #auxF = auxF + 1

        if auxF == 5:
            transformada4[i+1][j+1] = 255
cv2.imshow("Transformacao IV", transformada4)
cv2.waitKey(0)

#########################################################################################################
#=======================================================================================================#
#########################################################################################################

cv2.imshow("Original", cinzas)
cv2.imshow("Preto e Branco", pretoBranco)

#kernel =~ operador
kernel = numpy.ones((5,5), numpy.uint8)
#kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
#kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
#kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
print('Kernel =')
print(kernel)
print('')

#erosion =~ transformada
erosion = cv2.erode(pretoBranco, kernel, iterations = 1)

cv2.imshow("Erosao", erosion)
cv2.waitKey(0)