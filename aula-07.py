# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 17:13:41 2023

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

#cria uma imagem (matriz) e preenche seus pixels com tons de cinza
#cada tom de cinza equivale à média dos tres canais daquele pixel
contrtCinzas = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8)
for i in range (imagem.shape[0]):
    for j in range (imagem.shape[1]):
        contrtCinzas[i][j] = (imagem[i][j].sum()//3)
cv2.imshow("Imagem Original", contrtCinzas)

histCinza = [0]*256
for i in range (imagem.shape[0]):
    for j in range (imagem.shape[1]):
        histCinza[contrtCinzas[i][j]]+=1

#cria o eixo x e nomeia o eixo x e y
pixel = [0]*256
for i in range (256):
    pixel[i]=i
plt.xlabel('Tom de Cinza')
plt.ylabel('Quantidade')

#nomeia e plota o histograma
plt.title('Histograma de Tons de Cinza')
plt.bar(pixel, histCinza, color='gray')
plt.show()

#########################################################################################################
#=======================================================================================================#
#########################################################################################################

normaliza = [0]*256
for i in range (256):
    normaliza[i] = (histCinza[i])/((imagem.shape[0])*(imagem.shape[1]))

#cria o eixo x e nomeia o eixo x e y
pixel = [0]*256
for i in range (256):
    pixel[i]=i
plt.xlabel('Tom de Cinza')
plt.ylabel('Quantidade')

#nomeia e plota o histograma
plt.title('Histograma de Tons de Cinza Normalizado')
plt.bar(pixel, normaliza, color='blue')
plt.show()

acumula = [0]*256
for i in range (256):
    if i == 0:
        acumula[i] = normaliza[i]
    else:
        acumula[i] = normaliza[i] + acumula[i-1]

#cria o eixo x e nomeia o eixo x e y
pixel = [0]*256
for i in range (256):
    pixel[i]=i
plt.xlabel('Tom de Cinza')
plt.ylabel('Quantidade')

#nomeia e plota o histograma
plt.title('Histograma Normalizado Acumulado')
plt.bar(pixel, acumula, color='blue')
plt.show()

mapeamento = [0]*256
for i in range (256):
    mapeamento[i] = round(acumula[i]*255)

equaliza = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8)
for i in range (imagem.shape[0]):
    for j in range (imagem.shape[1]):
        equaliza[i][j] = mapeamento[contrtCinzas[i][j]]
cv2.imshow("Imagem Equalizada", equaliza)

#cria o eixo x e nomeia o eixo x e y
histEqlz = [0]*256
for i in range (imagem.shape[0]):
    for j in range (imagem.shape[1]):
        histEqlz[equaliza[i][j]]+=1
        
pixel = [0]*256
for i in range (256):
    pixel[i]=i
plt.xlabel('Tom de Cinza')
plt.ylabel('Quantidade')
plt.title('Histograma Equalizado')
plt.bar(pixel, histEqlz, color='blue')
plt.show()

#########################################################################################################
#=======================================================================================================#
#########################################################################################################

newHistCinza = [0]*256
for i in range (256):
    if (i<25):
        newHistCinza[i] = 50
    if (25<i<50):
        newHistCinza[i] = 500
    if (50<i<75):
        newHistCinza[i] = 5000
    if (75<i<110):
        newHistCinza[i] = 10000
    if (110<i<125):
        newHistCinza[i] = 20000
    if (125<i<175):
        newHistCinza[i] = 15000
    if (175<i<200):
        newHistCinza[i] = 1500
    if (200<i<225):
        newHistCinza[i] = 1000
    if (225<i<250):
        newHistCinza[i] = 500
    if (i>250):
        newHistCinza[i] = 100
itensHist = 0
for i in range (256):
    itensHist+=newHistCinza[i]

#cria o eixo x e nomeia o eixo x e y
pixel = [0]*256
for i in range (256):
    pixel[i]=i
plt.xlabel('Tom de Cinza')
plt.ylabel('Quantidade')

#nomeia e plota o histograma
plt.title('Novo Histograma de Tons de Cinza')
plt.bar(pixel, newHistCinza, color='red')
plt.show()

newNormaliza = [0]*256
for i in range (256):
    newNormaliza[i] = (newHistCinza[i])/(itensHist)

#cria o eixo x e nomeia o eixo x e y
pixel = [0]*256
for i in range (256):
    pixel[i]=i
plt.xlabel('Tom de Cinza')
plt.ylabel('Quantidade')

#nomeia e plota o histograma
plt.title('Novo Histograma de Tons de Cinza Normalizado')
plt.bar(pixel, newNormaliza, color='red')
plt.show()

newAcumula = [0]*256
for i in range (256):
    if i == 0:
        newAcumula[i] = newNormaliza[i]
    else:
        newAcumula[i] = newNormaliza[i] + newAcumula[i-1]

#cria o eixo x e nomeia o eixo x e y
pixel = [0]*256
for i in range (256):
    pixel[i]=i
plt.xlabel('Tom de Cinza')
plt.ylabel('Quantidade')

#nomeia e plota o histograma
plt.title('Novo Histograma Normalizado Acumulado')
plt.bar(pixel, newAcumula, color='red')
plt.show()

newMapeamento = [0]*256
for i in range (256):
    newMapeamento[i] = round(newAcumula[i]*255)

#########################################################################################################
#=======================================================================================================#
#########################################################################################################

def semRepet (LST):
    l = []
    for i in LST:
        if i not in l:
            l.append(i)
    return l

def mapaTotal(EQLZ,ACML):
    mapaT = {}
    for i in EQLZ:
        menor = abs(i-ACML[0])
        menIndex = 0
        for j in range (len(ACML)):
            if (abs(i-ACML[j]))<menor:
                menor = (abs(i-ACML[j]))
                menIndex = j
        mapaT[i] = menIndex
    return mapaT

#########################################################################################################
#=======================================================================================================#
#########################################################################################################

eqlzSemRept = semRepet(mapeamento)
print('eqlzSemRept: ')
print(eqlzSemRept)
print('')
finalMapeamento = mapaTotal(eqlzSemRept,newMapeamento)
print('finalMapeamento: ')
print(finalMapeamento)

imgFinal = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8)
for i in range (imagem.shape[0]):
    for j in range (imagem.shape[1]):
        imgFinal[i][j] = finalMapeamento[mapeamento[contrtCinzas[i][j]]]

histFinal = [0]*256
for i in range (imagem.shape[0]):
    for j in range (imagem.shape[1]):
        histFinal[imgFinal[i][j]]+=1

#cria o eixo x e nomeia o eixo x e y
pixel = [0]*256
for i in range (256):
    pixel[i]=i
plt.xlabel('Tom de Cinza')
plt.ylabel('Quantidade')

#nomeia e plota o histograma
plt.title('Novo Histograma Equalizado')
plt.bar(pixel, histFinal, color='purple')
plt.show()

cv2.imshow("Nova Imagem Equalizada", imgFinal)
cv2.waitKey(0)