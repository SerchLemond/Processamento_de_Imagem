# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 18:32:18 2023

@author: aluno
"""

import cv2
import numpy
foto = 'entrada4.png'
imagem = cv2.imread(foto)

    #####

#opTres = [[255,255,255],[255,255,255],[255,255,255]]
#opCruz = [[0,255,0],[255,255,255],[0,255,0]]

#########################################################################################################
#=======================================================================================================#
#########################################################################################################

def criaOP (NUM1, NUM2):
    opNew = [[255 for _ in range(NUM2)] for _ in range(NUM1)]
    opNew = numpy.array(opNew)
    return opNew 

    #####

def deixaCinza (IMG):
    cinzas = numpy.zeros((IMG.shape[0], IMG.shape[1]), dtype = numpy.uint8)
    for i in range (IMG.shape[0]):
        for j in range (IMG.shape[1]):
            cinzas[i][j] = (IMG[i][j].sum()//3)
    cv2.imshow('Imagem em Tons de Cinza', cinzas)
    return cinzas

    #####

def deixaPB (CNZ):
    preBra = numpy.zeros((CNZ.shape[0], CNZ.shape[1]), dtype = numpy.uint8)
    for i in range (CNZ.shape[0]):
        for j in range (CNZ.shape[1]):
            if ((CNZ[i][j])/2) > 100:
                preBra[i][j] = 255
            else:
                preBra[i][j] = 0
    cv2.imshow('Imagem em Preto e Branco', preBra)
    return preBra

#########################################################################################################
#=======================================================================================================#
#########################################################################################################

def botaBorda (IMG, OP):
    ALT = (IMG.shape[0])
    LRG = (IMG.shape[1])
    linhas = OP.shape[0]
    colunas = OP.shape[1]
    borda = numpy.zeros((ALT+(linhas%2),LRG+(colunas%2)), dtype = numpy.uint8)
    for i in range (ALT):
        for j in range (LRG):
            borda[i+(linhas%2)][j+(colunas%2)] = IMG[i][j]
    #cv2.imshow('Borda Criada', borda)
    return borda

#########################################################################################################
#=======================================================================================================#
#########################################################################################################

def dilatacao (IMG, OP):
    ALT = (IMG.shape[0])
    LRG = (IMG.shape[1])
    linhas = OP.shape[0]
    colunas = OP.shape[1]
    comBorda = botaBorda(IMG, OP)
    dilatada = numpy.zeros((IMG.shape[0],IMG.shape[1]), dtype = numpy.uint8)
    for i in range (ALT-(linhas+1)):
        for j in range (LRG-(colunas+1)):
            auxF = 0
            for m in range (linhas):
                for n in range (colunas):
                    if comBorda[i + m][j + n] == 255 and OP[m][n] == 255:
                        auxF = 255
            if auxF > 0:
                dilatada[i+linhas//2][j+colunas//2] = 255
    cv2.imshow("Dilatacao da Imagem", dilatada)
    return dilatada

    #####

def erosao (IMG, OP):
    ALT = (IMG.shape[0])
    LRG = (IMG.shape[1])
    linhas = OP.shape[0]
    colunas = OP.shape[1]
    erodida = numpy.zeros((IMG.shape[0],IMG.shape[1]), dtype = numpy.uint8)
    for i in range (ALT-(linhas+1)):
        for j in range (LRG-(colunas+1)):
            auxF = 0
            for m in range (linhas):
                for n in range (colunas):
                    if IMG[i + m][j + n] == 255 and OP[m][n] == 255:
                        auxF += 1
            if auxF == (linhas*colunas):
                erodida[i+linhas//2][j+colunas//2] = 255
    cv2.imshow("Erosao da Imagem", erodida)
    return erodida

#########################################################################################################
#=======================================================================================================#
#########################################################################################################

def abertura (IMG, OP):
    aberta = erosao(IMG, OP)
    aberta = dilatacao(aberta, OP)
    cv2.imshow("Abertura  da Imagem", aberta)
    return aberta;

def fechamento (IMG, OP):
    fechada = dilatacao(IMG, OP)
    fechada = erosao(fechada, OP)
    cv2.imshow("Fechamento  da Imagem", fechada)
    return fechada;

#########################################################################################################
#=======================================================================================================#
#########################################################################################################

print('Escolha o tipo de operador:')
print('Tipo 1: Cheio')
print('Tipo 2: Cruz')
operador = []
tipoOp = input('Tipo 1 ou 2? ')
print('')
    #####
if (tipoOp == '1'):
    print("Qual o tamanho (Altura x Largura)?")
    a = int(input('Altura: '))
    l = int(input('Largura: '))
    operador = criaOP(a,l)
    print('Operador Cheio =')
    print(operador)
    print('')
    #####
if (tipoOp == '2'):
    operador = [[0,255,0],[255,255,255],[0,255,0]]
    print('Operador Em Cruz =')
    print(operador)
    print('')

imgCinza = deixaCinza(imagem)
imgPB = deixaPB(imgCinza)
cv2.waitKey(0)
    #####
cv2.imshow('Imagem em Preto e Branco', imgPB)
imgAbrt = abertura(imgPB,operador)
cv2.waitKey(0)
cv2.imshow('Imagem em Preto e Branco', imgPB)
imgFchd = fechamento(imgPB,operador)
cv2.waitKey(0)
