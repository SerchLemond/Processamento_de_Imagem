# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 17:19:15 2023

@author: aluno
"""

import cv2
import numpy
foto = 'entrada4.png'
imagem = cv2.imread(foto)

    #####

opFull = [[255,255,255],[255,255,255],[255,255,255]]
opCruz = [[0,255,0],[255,255,255],[0,255,0]]

#########################################################################################################
#=======================================================================================================#
#########################################################################################################

def deixaCinza (IMG):
    cinzas = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8)
    for i in range (imagem.shape[0]):
        for j in range (imagem.shape[1]):
            cinzas[i][j] = (IMG[i][j].sum()//3)
    cv2.imshow('Imagem em Tons de Cinza', cinzas)
    return cinzas

    #####

def deixaPB (CNZ):
    preBra = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8)
    for i in range (imagem.shape[0]):
        for j in range (imagem.shape[1]):
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
    borda = numpy.zeros(((IMG.shape[0]+2), (IMG.shape[1]+2)), dtype = numpy.uint8)
    for i in range (IMG.shape[0]):
        for j in range (IMG.shape[1]):
            borda[i+1][j+1] = IMG[i][j]
    #cv2.imshow('Borda Criada', borda)
    return borda

#########################################################################################################
#=======================================================================================================#
#########################################################################################################

def dilatacao0 (IMG, OP):
    comBorda = botaBorda(IMG, OP)
    dilatada = numpy.zeros((IMG.shape[0], IMG.shape[1]), dtype = numpy.uint8)
    for i in range ((IMG.shape[0])-2):
        for j in range ((IMG.shape[1])-2):
            m = n = 0
            auxF = 0
            #####
            if (comBorda[i][j] == 255) and (OP[m][n] == 255):
                auxF = auxF + 1
            if (comBorda[i][j+1] == 255) and (OP[m][n+1] == 255):
                auxF = auxF + 1
            if (comBorda[i][j+2] == 255) and (OP[m][n+2] == 255):
                auxF = auxF + 1
            if (comBorda[i+1][j] == 255) and (OP[m+1][n] == 255):
                auxF = auxF + 1
            if (comBorda[i+1][j+1] == 255) and (OP[m+1][n+1] == 255):
                auxF = auxF + 1
            if (comBorda[i+1][j+2] == 255) and (OP[m+1][n+2] == 255):
                auxF = auxF + 1
            if (comBorda[i+2][j] == 255) and (OP[m+2][n] == 255):
                auxF = auxF + 1
            if (comBorda[i+2][j+1] == 255) and (OP[m+2][n+1] == 255):
                auxF = auxF + 1
            if (comBorda[i+2][j+2] == 255) and (OP[m+2][n+2] == 255):
                auxF = auxF + 1
            #####
            if auxF > 0:
                dilatada[i+1][j+1] = 255
    cv2.imshow("Dilatacao da Imagem", dilatada)
    return dilatada

    #####

def erosao1 (IMG, OP):
    erodida1 = numpy.zeros((IMG.shape[0], IMG.shape[1]), dtype = numpy.uint8)
    for i in range ((IMG.shape[0])-2):
        for j in range ((IMG.shape[1])-2):
            m = n = 0
            auxF = 0
            #####
            if (IMG[i][j] == 255) and (OP[m][n] == 255):
                auxF = auxF + 1
            if (IMG[i][j+1] == 255) and (OP[m][n+1] == 255):
                auxF = auxF + 1
            if (IMG[i][j+2] == 255) and (OP[m][n+2] == 255):
                auxF = auxF + 1
            if (IMG[i+1][j] == 255) and (OP[m+1][n] == 255):
                auxF = auxF + 1
            if (IMG[i+1][j+1] == 255) and (OP[m+1][n+1] == 255):
                auxF = auxF + 1
            if (IMG[i+1][j+2] == 255) and (OP[m+1][n+2] == 255):
                auxF = auxF + 1
            if (IMG[i+2][j] == 255) and (OP[m+2][n] == 255):
                auxF = auxF + 1
            if (IMG[i+2][j+1] == 255) and (OP[m+2][n+1] == 255):
                auxF = auxF + 1
            if (IMG[i+2][j+2] == 255) and (OP[m+2][n+2] == 255):
                auxF = auxF + 1
            #####
            if auxF == 9:
                erodida1[i+1][j+1] = 255
    cv2.imshow("Erosao I da Imagem", erodida1)
    return erodida1

    #####

def erosao2 (IMG, OP):
    erodida2 = numpy.zeros((IMG.shape[0], IMG.shape[1]), dtype = numpy.uint8)
    for i in range ((IMG.shape[0])-2):
        for j in range ((IMG.shape[1])-2):
            m = n = 0
            auxF = 0
            #####
            #if (IMG[i][j] == 255) and (OP[m][n] == 255):
                #auxF = auxF + 1
            if (IMG[i][j+1] == 255) and (OP[m][n+1] == 255):
                auxF = auxF + 1
            #if (IMG[i][j+2] == 255) and (OP[m][n+2] == 255):
                #auxF = auxF + 1
            if (IMG[i+1][j] == 255) and (OP[m+1][n] == 255):
                auxF = auxF + 1
            if (IMG[i+1][j+1] == 255) and (OP[m+1][n+1] == 255):
                auxF = auxF + 1
            if (IMG[i+1][j+2] == 255) and (OP[m+1][n+2] == 255):
                auxF = auxF + 1
            #if (IMG[i+2][j] == 255) and (OP[m+2][n] == 255):
                #auxF = auxF + 1
            if (IMG[i+2][j+1] == 255) and (OP[m+2][n+1] == 255):
                auxF = auxF + 1
            #if (IMG[i+2][j+2] == 255) and (OP[m+2][n+2] == 255):
                #auxF = auxF + 1
            #####
            if auxF == 5:
                erodida2[i+1][j+1] = 255
    cv2.imshow("Erosao II da Imagem", erodida2)
    return erodida2

#########################################################################################################
#=======================================================================================================#
#########################################################################################################

def abertura1 (IMG):
    aberta = erosao1(IMG, opFull)
    aberta = dilatacao0(aberta, opFull)
    cv2.imshow("Abertura I da Imagem", aberta)
    return aberta;

def fechamento1 (IMG):
    fechada = dilatacao0(IMG, opFull)
    fechada = erosao1(fechada, opFull)
    cv2.imshow("Fechamento I da Imagem", fechada)
    return fechada;

    #####

def abertura2 (IMG):
    aberta = erosao2(IMG, opCruz)
    aberta = dilatacao0(aberta, opCruz)
    cv2.imshow("Abertura II da Imagem", aberta)
    return aberta;

def fechamento2 (IMG):
    fechada = dilatacao0(IMG, opCruz)
    fechada = erosao2(fechada, opCruz)
    cv2.imshow("Fechamento i da Imagem", fechada)
    return fechada;

#########################################################################################################
#=======================================================================================================#
#########################################################################################################

imgCinza = deixaCinza(imagem)
imgPB = deixaPB(imgCinza)
cv2.waitKey(0)
    #####
cv2.imshow('Imagem em Preto e Branco', imgPB)
imgAbrt1 = abertura1(imgPB)
cv2.waitKey(0)
cv2.imshow('Imagem em Preto e Branco', imgPB)
imgFchd1 = fechamento1(imgPB)
cv2.waitKey(0)
    #####
cv2.imshow('Imagem em Preto e Branco', imgPB)
imgAbrt2 = abertura2(imgPB)
cv2.waitKey(0)
cv2.imshow('Imagem em Preto e Branco', imgPB)
imgFchd2 = fechamento2(imgPB)
cv2.waitKey(0)
    #####
cv2.imshow('Imagem em Preto e Branco', imgPB)
cv2.imshow("Abertura I da Imagem", imgAbrt1)
cv2.imshow("Fechamento I da Imagem", imgFchd1)
cv2.imshow("Abertura II da Imagem", imgAbrt2)
cv2.imshow("Fechamento II da Imagem", imgFchd2)
cv2.waitKey(0)
