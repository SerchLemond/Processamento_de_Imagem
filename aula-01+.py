# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 17:40:16 2023

@author: aluno
"""

import cv2
import numpy
foto = 'entrada1.jpg'
imagem = cv2.imread(foto)


#########################################################################################################
#=======================================================================================================#
#########################################################################################################

def informacoes (IMG):
    print('Altura: ', end='')
    print(IMG.shape[0], end='')
    print(' Pixels')
    print('Largura: ', end='')
    print(IMG.shape[1], end='')
    print(' Pixels')
    print('Quantidade de Canais: ', end='')
    print(IMG.shape[2])
    cv2.imshow("Imagem Original", IMG)
    cv2.waitKey(0)

#########################################################################################################
#=======================================================================================================#
#########################################################################################################

def extraiAzul (IMG):
    azul = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8)
    azul[:,:] = IMG[:,:,0]  #[linhas (altura), colunas (largura), canais('profundidade')]
    cv2.imshow("Canal Azul",azul)
    cv2.waitKey(0)
    return azul

def extraiVerde (IMG):
    verde = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8)
    verde[:,:] = IMG[:,:,1]
    cv2.imshow("Canal Verde",verde)
    cv2.waitKey(0)
    return verde

def extraiVermelho (IMG):
    vermelho = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8)
    vermelho [:,:] = IMG[:,:,2]
    cv2.imshow("Canal Vermelho",vermelho)
    cv2.waitKey(0)
    return vermelho

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

#########################################################################################################
#=======================================================================================================#
#########################################################################################################

informacoes(imagem)
canalAzul = extraiAzul(imagem)
cv2.imwrite("saida1-cAzul.jpg",canalAzul)
canalVerde = extraiVerde(imagem)
cv2.imwrite("saida1-cVerde.jpg",canalVerde)
canalVermelho = extraiVermelho(imagem)
cv2.imwrite("saida1-cVermelho.jpg",canalVermelho)
imgCinza = deixaCinza(imagem)
cv2.imwrite("saida1-iCinza.jpg",imgCinza)
