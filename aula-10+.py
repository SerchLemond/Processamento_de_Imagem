# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 17:53:14 2023

@author: aluno
"""

import cv2
import numpy
foto = 'entrada4.png'
imagem = cv2.imread(foto)

#########################################################################################################
#=======================================================================================================#
#########################################################################################################

'''opFull = [[255,255,255],[255,255,255],[255,255,255]]
print('Operador Cheio =')
print(opFull)
print('')'''

opCruz = [[0,255,0],[255,255,255],[0,255,0]]
print('Operador Em Cruz =')
print(opCruz)
print('')

#cria uma imagem (matriz) e preenche seus pixels com tons de cinza
#cada tom de cinza equivale à média dos tres canais daquele pixel
def deixaCinza (IMG):
    cinzas = numpy.zeros((IMG.shape[0], IMG.shape[1]), dtype = numpy.uint8)
    for i in range (IMG.shape[0]):
        for j in range (IMG.shape[1]):
            cinzas[i][j] = (IMG[i][j].sum()//3)
    cv2.imshow('Imagem em Tons de Cinza', cinzas)
    return cinzas

    #####
#pega a imagem em tons de cinza e transforma eles em preto ou branco dependendo do seu valor
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

#adiciona uma borda preta de 1 px na imagem
def botaBorda (IMG, OP):
    borda = numpy.zeros(((IMG.shape[0]+(OP.shape[0])%2), (IMG.shape[1])+(OP.shape[1]%2)), dtype = numpy.uint8)
    for i in range (IMG.shape[0]):
        for j in range (IMG.shape[1]):
            borda[i+((OP.shape[0])%2)][j+((OP.shape[1])%2)] = IMG[i][j]
    cv2.imshow('Borda Criada', borda)
    return borda

#########################################################################################################
#=======================================================================================================#
#########################################################################################################

def erosao (PRBR, OP):
    erodida = numpy.zeros((PRBR.shape[0], PRBR.shape[1]), dtype = numpy.uint8)
    mascara = numpy.zeros((OP.shape[0], OP.shape[1]), dtype = numpy.uint8)
    cont = 0
    for i in range ((PRBR.shape[0])-((OP.shape[0]%2)*2)):
        for j in range ((PRBR.shape[1])-((OP.shape[1]%2)*2)):
            for m in range (OP.shape[0]):
                for n in range (OP.shape[1]):
                    mascara[m][n] = PRBR[i+m][j+n]
                    for x in range (m*n):
                        y = round(x/m)
                        z = round(x/n)
                        if (mascara[y][z] == 255) and (OP[y][z] == 255):
                            cont = cont + 1
                        if (cont == 9):
                            erodida[i][j] = 255
            '''m = n = 0
            auxF = 0
            ###
            if (PRBR[i][j] == 255) and (OP[m][n] == 255):((OP.shape[0]%2)+1)
                auxF = auxF + 1
            if (PRBR[i][j+(OP.shape[0]%2)] == 255) and (OP[m][n+(OP.shape[0]%2)] == 255):
                auxF = auxF + 1
            if (PRBR[i][j+2] == 255) and (OP[m][n+2] == 255):
                auxF = auxF + 1
            if (PRBR[i+(OP.shape[0]%2)][j] == 255) and (OP[m+(OP.shape[0]%2)][n] == 255):
                auxF = auxF + 1
            if (PRBR[i+(OP.shape[0]%2)][j+(OP.shape[0]%2)] == 255) and (OP[m+(OP.shape[0]%2)][n+1] == 255):
                auxF = auxF + 1
            if (PRBR[i+(OP.shape[0]%2)][j+2] == 255) and (OP[m+(OP.shape[0]%2)][n+2] == 255):
                auxF = auxF + 1
            if (PRBR[i+2][j] == 255) and (OP[m+2][n] == 255):
                auxF = auxF + 1
            if (PRBR[i+2][j+(OP.shape[0]%2)] == 255) and (OP[m+2][n+1(OP.shape[0]%2)] == 255):
                auxF = auxF + 1
            if (PRBR[i+2][j+2] == 255) and (OP[m+2][n+2] == 255):
                auxF = auxF + 1
            ###
            if auxF == 9:
                erodida[i+1][j+1] = 255'''
    cv2.imshow('Erosao da Imagem', erodida)
    return erodida


#########################################################################################################
#=======================================================================================================#
#########################################################################################################

def dilatacao (ERDD, OP):
    dilatada = botaBorda(ERDD, OP)
    mascara = numpy.zeros((OP.shape[0], OP.shape[1]), dtype = numpy.uint8)
    cont = 0
    for i in range ((ERDD.shape[0])-((OP.shape[0]%2)*2)):
        for j in range ((ERDD.shape[1])-((OP.shape[1]%2)*2)):
            for m in range (OP.shape[0]):
                for n in range (OP.shape[1]):
                    mascara[m][n] = ERDD[i+m][j+n]
                    for x in range (m*n):
                        y = round(x/m)
                        z = round(x/n)
                        if (mascara[y][z] == 255) and (OP[y][z] == 255):
                            cont = cont + 1
                        if (cont > 0):
                            dilatada[i][j] = 255
            '''m = n = 0
            auxF = 0
            ###
            if (ERDD[i][j] == 255) and (OP[m][n] == 255):
                auxF = auxF + 1
            if (ERDD[i][j+1] == 255) and (OP[m][n+1] == 255):
                auxF = auxF + 1
            if (ERDD[i][j+2] == 255) and (OP[m][n+2] == 255):
                auxF = auxF + 1
            if (ERDD[i+1][j] == 255) and (OP[m+1][n] == 255):
                auxF = auxF + 1
            if (ERDD[i+1][j+1] == 255) and (OP[m+1][n+1] == 255):
                auxF = auxF + 1
            if (ERDD[i+1][j+2] == 255) and (OP[m+1][n+2] == 255):
                auxF = auxF + 1
            if (ERDD[i+2][j] == 255) and (OP[m+2][n] == 255):
                auxF = auxF + 1
            if (ERDD[i+2][j+1] == 255) and (OP[m+2][n+1] == 255):
                auxF = auxF + 1
            if (ERDD[i+2][j+2] == 255) and (OP[m+2][n+2] == 255):
                auxF = auxF + 1
            ###
            if auxF > 0:
                dilatada[i+1][j+1] = 255'''
    cv2.imshow('Dilatacao da Imagem', dilatada)
    return dilatada

#########################################################################################################
#=======================================================================================================#
#########################################################################################################

'''print('Escolha o tipo de operador:')
print('Tipo 1: Cheio')
print('Tipo 2: Cruz')
tipoOp = input('Tipo 1 ou 2? ')
print('')
if (tipoOp == 1):
    print("Qual o tamanho (Altura x Largura)?")
    print()
    altura = input()
    print()
    largura = input('Largura: ')
    operador = [numpy.zeros((altura, largura), dtype = numpy.uint8)]
    for i in range (altura):
        for j in range (largura):
            operador[i][j] = 255 
if (tipoOp == 2):
    operador = [[0,255,0],[255,255,255],[0,255,0]]'''
    
a = l = int
print('Escolha o tamanho do operador cheio.')
a = int(input('Altura: '))
l = int(input('Largura: '))
operador = numpy.zeros ((a, l), dtype = numpy.uint8)
for i in range (a):
    for j in range (l):
        operador[i][j] = 255

cinzas = deixaCinza(imagem)

pretoBranco = deixaPB(cinzas)

imgErodida = erosao(pretoBranco, operador)

imgDilatada = dilatacao(pretoBranco, operador)
'''
erosDilat = dilatacao(imgErodida, operador)
'''
cv2.waitKey(0)