# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 18:31:00 2023

@author: aluno
"""

import cv2
import numpy
import matplotlib.pyplot as plt
foto = 'entrada1.jpg'
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

def inverteTom (IMG):
    negativo = numpy.zeros((IMG.shape[0], IMG.shape[1]), dtype = numpy.uint8)
    for i in range (IMG.shape[0]):
        for j in range (IMG.shape[1]):
            negativo[i][j] = ((-1)*(IMG[i][j]))  #(contraste * imagem cinza original + luminosidade)
            aux = 0
            aux = (negativo[i][j])
            if aux > 255:
                aux = 255
                negativo[i][j] = aux
            if aux < 0:
                aux = 0
                negativo[i][j] = aux
    y=[0]*256
    x=[0]*256
    for i in range (256):
        x[i] = i
        y[i] = i
        y[i] = ((-1)*(y[i]))
        if y[i]>255:
            y[i] = 255
    plt.xlabel('Origem - r')
    plt.ylabel('Destino - s')
    plt.title('Curva de Transformação: Imagem Negativa')
    plt.plot(x, y, color='gray')
    plt.show()
    cv2.imshow("Imagem Negativa", negativo)
    cv2.waitKey(0)
    return negativo

#########################################################################################################
#=======================================================================================================#
#########################################################################################################

def manipContraste1 (IMG):   
    contraste = numpy.zeros((IMG.shape[0], IMG.shape[1]), dtype = numpy.uint8)
    for i in range (IMG.shape[0]):
        for j in range (IMG.shape[1]):
            contraste[i][j] = ((2*(IMG[i][j]))+5)  
            aux = 0
            aux = (contraste[i][j])
            if aux > 255:
                aux = 255
                contraste[i][j] = aux
            if aux < 0:
                aux = 0
                contraste[i][j] = aux
    y=[0]*256
    x=[0]*256
    for i in range (256):
        x[i] = i
        y[i] = i
        y[i] = ((2*(y[i]))+5)
        if y[i]>255:
            y[i] = 255
        if y[i]<0:
            y[i] = 0
    plt.xlabel('Origem - r')
    plt.ylabel('Destino - s')
    plt.title('Curva de Transformação: Encurtando as Cores')
    plt.plot(x, y, color='gray')
    plt.show()
    cv2.imshow("Manipulacao de Contraste I", contraste)
    cv2.waitKey(0)
    return contraste

#########################################################################################################
#=======================================================================================================#
#########################################################################################################

def manipContraste2 (IMG):   
    contraste = numpy.zeros((IMG.shape[0], IMG.shape[1]), dtype = numpy.uint8)
    for i in range (IMG.shape[0]):
        for j in range (IMG.shape[1]):
            contraste[i][j] = ((((1/256)*IMG[i][j])**2)*256) 
        aux = 0
        aux = (contraste[i][j])
        if aux > 255:
            aux = 255
            contraste[i][j] = aux
        if aux < 0:
            aux = 0
            contraste[i][j] = aux
    y=[0]*256
    x=[0]*256
    for i in range (256):
        x[i] = i
        y[i] = i
        y[i] = (((1/256)*y[i])**2)
        if y[i]>255:
            y[i] = 255
        if y[i]<0:
            y[i] = 0
    plt.xlabel('Origem - r')
    plt.ylabel('Destino - s')
    plt.title('Curva de Transformação: Parábola')
    plt.plot(x, y, color='gray')
    plt.show()
    cv2.imshow("Manipulacao de Contraste II", contraste)
    cv2.waitKey(0)
    return contraste
    
#########################################################################################################
#=======================================================================================================#
#########################################################################################################

imgCinza = deixaCinza(imagem)
criaHistograma(imgCinza)
imgNegativa = inverteTom(imgCinza)
cv2.imwrite("saida1-iNegativa.jpg",imgNegativa)
imgManip1 = manipContraste1(imgCinza)
cv2.imwrite("saida1-iManip1.jpg",imgManip1)
imgManip2 = manipContraste2(imgCinza)
cv2.imwrite("saida1-iManip2.jpg",imgManip2)
