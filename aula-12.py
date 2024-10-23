# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 17:04:10 2023

@author: aluno
"""

import cv2
import numpy
foto = 'entrada5+.png'
imagem = cv2.imread(foto)

    #####

opTres = opCompTr = opCruz = opCompCr = []
#####
opTres = [[255,255,255],[255,255,255],[255,255,255]]
opCompTr = [[255,255,255,255,255],[255,0,0,0,255],[255,0,0,0,255],[255,0,0,0,255],[255,255,255,255,255]]
#####
opCruz = [[0,255,0],[255,255,255],[0,255,0]]
opCompCr = [[255,255,255,255,255],[255,255,0,255,255],[255,0,0,0,255],[255,255,0,255,255],[255,255,255,255,255]]

#########################################################################################################
#=======================================================================================================#
#########################################################################################################

def criaOP (NUM1, NUM2):
    opNew = [[255 for _ in range(NUM2)] for _ in range(NUM1)]
    opNew = numpy.array(opNew)
    return opNew 

    #####
    
def criaComp (NUM1,NUM2):
    cmpNew = [[255 for _ in range(NUM2+2)] for _ in range(NUM1+2)]
    for i in range (NUM1):
        for j in range (NUM2):
            cmpNew[i+1][j+1] = 0
    cmpNew = numpy.array(cmpNew)
    return cmpNew 
    
    #####

def deixaCinza (IMG):
    cinzas = numpy.zeros((IMG.shape[0], IMG.shape[1]), dtype = numpy.uint8)
    for i in range (IMG.shape[0]):
        for j in range (IMG.shape[1]):
            cinzas[i][j] = (IMG[i][j].sum()//3)
    cv2.imshow('Imagem em Tons de Cinza', cinzas)
    #printaImagem(cinzas)
    return cinzas

    #####

def deixaPB (CNZ):
    preBra = numpy.zeros((CNZ.shape[0], CNZ.shape[1]), dtype = numpy.uint8)
    for i in range (CNZ.shape[0]):
        for j in range (CNZ.shape[1]):
            if ((CNZ[i][j])/2) > 127:
                preBra[i][j] = 255
            else:
                preBra[i][j] = 0
    cv2.imshow('Imagem em Preto e Branco', preBra)
    #printaImagem(preBra)
    return preBra

    #####

def inverteTomPB (IPB):
    negativo = numpy.zeros((IPB.shape[0], IPB.shape[1]), dtype = numpy.uint8)
    for i in range (IPB.shape[0]):
        for j in range (IPB.shape[1]):
            negativo[i][j] = ((-1)*(IPB[i][j]))  #(contraste * imagem cinza original + luminosidade)
            aux = 0
            aux = (negativo[i][j])
            negativo[i][j] = aux+255
    cv2.imshow('Imagem Invertida', negativo)
    #printaImagem(negativo)
    return negativo

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
    #printaImagem(borda)
    return borda

    #####

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
                    if comBorda[i + m][j + n] == 255 and OP[m][n] == 0:
                        auxF = 255
            if auxF > 0:
                dilatada[i+linhas//2][j+colunas//2] = 255
    cv2.imshow("Dilatacao da Imagem", dilatada)
    #printaImagem(dilatada)
    return dilatada

    #####

def erosao (IMG, OP):
    ALT = (IMG.shape[0])
    LRG = (IMG.shape[1])
    linhas = OP.shape[0]
    colunas = OP.shape[1]
    erodida = numpy.zeros((ALT,LRG), dtype = numpy.uint8)
    for x in range (ALT):
        for y in range (LRG):
            erodida[x][y] += 255
    for i in range (ALT-(linhas+1)):
        for j in range (LRG-(colunas+1)):
            auxF = 0
            for m in range (linhas):
                for n in range (colunas):
                    if (IMG[i + m][j + n] == 0 and OP[m][n] == 0):
                        auxF += 1
            if auxF == (linhas*colunas):
                erodida[i+linhas//2][j+colunas//2] -= 255
    cv2.imshow("Erosao da Imagem", erodida)
    #printaImagem(erodida)
    return erodida

def eroComp (IMG, OP):
    ALT = (IMG.shape[0])
    LRG = (IMG.shape[1])
    linhas = (OP.shape[0])
    colunas = (OP.shape[1])
    erodida = numpy.zeros((IMG.shape[0],IMG.shape[1]), dtype = numpy.uint8)
    for x in range (IMG.shape[0]):
        for y in range (IMG.shape[1]):
            erodida[x][y] = 255
    for i in range (ALT-(linhas+1)):
        for j in range (LRG-(colunas+1)):
            auxF = 0
            for m in range (linhas):
                for n in range (colunas):
                    if (IMG[i + m][j + n] == 0 and OP[m][n] == 0):
                        auxF += 1
            if auxF == ((linhas*colunas)-((linhas-2)*(colunas-2))):
                erodida[i+linhas//2][j+colunas//2] = 0
    cv2.imshow("Erosao da Imagem", erodida)
    #printaImagem(erodida)
    return erodida

#########################################################################################################
#=======================================================================================================#
#########################################################################################################

def interseccao(IMG0, IMG1, IMG2):
    ALT = (IMG0.shape[0])
    LRG = (IMG0.shape[1])
    intsc = numpy.zeros((IMG0.shape[0],IMG0.shape[1]), dtype = numpy.uint8)
    for x in range (IMG0.shape[0]):
        for y in range (IMG0.shape[1]):
            intsc[x][y] = 255
    for i in range (ALT):
        for j in range(LRG):
            auxF = 0
            if (IMG1[i][j] == 255 and IMG2[i][j] == 255):
                auxF = 255
            intsc[i][j] = auxF
    cv2.imshow("Interseccao das Imagens", intsc)
    return intsc

#########################################################################################################
#=======================================================================================================#
#########################################################################################################

print('')
print("Qual o tamanho do Operador (Altura x Largura)?")
operador = complemento = []
a = int(input('Altura: '))
l = int(input('Largura: '))
operador = criaOP(a,l)
print('Operador Cheio =')
print(operador)
print('')
complemento = criaComp(a,l)
print('Complemento Cheio =')
print(complemento)
print('')

cv2.imshow("Imagem Original", imagem)
imgCinza = deixaCinza(imagem)
imgPB = deixaPB(imgCinza)
imgErodPt1 = erosao(imgPB,operador)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("Imagem 1", imgErodPt1)
imgNegt = inverteTomPB(imgPB)
imgErodPt2 = eroComp(imgNegt,complemento)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("Imagem Original", imagem)
cv2.imshow("Alteracao I", imgErodPt1)
cv2.imshow("Alteracao II", imgErodPt2)
imgInterseccao = interseccao(imagem,imgErodPt1,imgErodPt2)
imgDilatF = dilatacao(imgInterseccao, operador)
cv2.waitKey(0)
cv2.destroyAllWindows()