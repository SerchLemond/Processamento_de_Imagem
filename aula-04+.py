# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 18:58:35 2023

@author: aluno
"""

import cv2
import numpy
import matplotlib.pyplot as plt
foto = 'entrada2.jpg'
imagem = cv2.imread(foto)

#########################################################################################################
#=======================================================================================================#
#########################################################################################################

def deixaCinza (IMG):
    cinzas = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8)
    for i in range (imagem.shape[0]):
        for j in range (imagem.shape[1]):
            cinzas[i][j] = (IMG[i][j].sum()//3)
    cv2.imshow('Imagem em Tons de Cinza', cinzas)
    cv2.waitKey(0)
    return cinzas

def criaHistograma (IMG):
    histCinza = [0]*256
    for i in range (IMG.shape[0]):
        for j in range (IMG.shape[1]):
            histCinza[IMG[i][j]] = histCinza[IMG[i][j]] + 1
    pixel = [0]*256
    for i in range (256):
        pixel[i]=i
    plt.xlabel('ID do Pixel (0 a 255)')
    plt.ylabel('Quantidade')
    plt.title('Histograma dos Pixels da Imagem')
    plt.bar(pixel, histCinza, color='gray')
    plt.show()

#########################################################################################################
#=======================================================================================================#
#########################################################################################################

def expansao1 (IMG):
    expnd1 = IMG
    for i in range (IMG.shape[0]):
        for j in range (IMG.shape[1]):
            if expnd1[i][j] < 75:
                expnd1[i][j] = 0
            if (75 <= expnd1[i][j] <= 175):
                expnd1[i][j] = 255*(((IMG[i][j])-75)/(175-75))
            if expnd1[i][j] > 175:
                expnd1[i][j] = 255
    criaHistograma(expnd1)
    y=[0]*256
    x=[0]*256
    for i in range (256):
        x[i] = i
        if i < 75:
            y[i] = 0
        if (75 <= i <= 175):
            y[i] = 255*((i-75)/(175-75))
        if i > 175:
            y[i] = 255
    plt.xlabel('Origem - r')
    plt.ylabel('Destino - s')
    plt.title('Curva de Transformacao: Histograma Expandido V1')
    plt.plot(x, y, color='gray')
    plt.show()
    cv2.imshow("Contraste Expandido I", expnd1)
    cv2.waitKey(0)
    return expnd1

#########################################################################################################
#=======================================================================================================#
#########################################################################################################

def expansao2 (IMG):
    expnd2 = IMG
    for i in range (IMG.shape[0]):
        for j in range (IMG.shape[1]):
            expnd2[i][j] = IMG[i][j]
            if expnd2[i][j] < 75:
                expnd2[i][j] = (50/75)*(IMG[i][j])
            if (75 <= expnd2[i][j] <= 175):
                expnd2[i][j] = ((((IMG[i][j])-75)*(200-50))/(175-75))+(50)
            if expnd2[i][j] > 175:
                expnd2[i][j] = (((IMG[i][j])-175)*((255-200)/(255-175)))+(200)
    criaHistograma(expnd2)
    y=[0]*256
    x=[0]*256
    for i in range (256):
        x[i] = i
        if i < 75:
            y[i] = (50/75)*(i)
        if (75 <= i <= 175):
            y[i] = ((((i)-75)*(200-50))/(175-75))+(50)
        if i > 175:
            y[i] = (((i)-175)*((255-200)/(255-175)))+(200)
    plt.xlabel('Origem - r')
    plt.ylabel('Destino - s')
    plt.title('Curva de Transformação: Histograma Expandido V2')
    plt.plot(x, y, color='gray')
    plt.show()
    cv2.imshow("Contraste Expandido II", expnd2)
    cv2.waitKey(0)
    return expnd2

#########################################################################################################
#=======================================================================================================#
#########################################################################################################

imgCinza = deixaCinza(imagem)
criaHistograma(imgCinza)
imgExpandida1 = expansao1(imgCinza)
cv2.imwrite("saida2-iExpandida1.jpg",imgExpandida1)
imgExpandida2 = expansao2(imgCinza)
cv2.imwrite("saida2-iExpandida2.jpg",imgExpandida2)
