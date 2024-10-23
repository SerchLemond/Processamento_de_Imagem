# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 18:26:50 2023

@author: aluno
"""

import cv2
import numpy
import matplotlib.pyplot as plt
foto = 'entrada.jpg'
imagem = cv2.imread(foto)

###

#cria uma imagem (matriz) e preenche seus pixels com tons de cinza
#cada tom de cinza equivale à média dos tres canais daquele pixel
cinzas = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8)
for i in range (imagem.shape[0]):
    for j in range (imagem.shape[1]):
        cinzas[i][j] = (imagem[i][j].sum()//3)

cv2.imshow("Tons de Cinza", cinzas)

###################################
###################################

#criando uma imagem (matriz) e preenche seus pixels com os valores do pixels da imagem 'cinzas' multiplicados por -1
#isso inverte os valores da imagem, ou seja, deixa ela negativa
negativo = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8)
for i in range (imagem.shape[0]):
    for j in range (imagem.shape[1]):
        negativo[i][j] = ((-1)*(cinzas[i][j]))  #(contraste * imagem cinza original + luminosidade)
        aux = 0
        aux = (negativo[i][j])
        if aux > 255:
            aux = 255
            negativo[i][j] = aux
        if aux < 0:
            aux = 0
            negativo[i][j] = aux

#criando e plotando o grafico que representa a transformação para negativo
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

###################################
###################################

#criando uma imagem (matriz) e preenche seus pixels com os valores do pixels da imagem 'cinzas' manipulados pela função f
#f = ((contraste * (imagem cinza original)) + luminosidade)
#isso manipula o contraste e o brilho da imagem
contraste = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8)
for i in range (imagem.shape[0]):
    for j in range (imagem.shape[1]):
        contraste[i][j] = ((2*(cinzas[i][j]))+5)  
        aux = 0
        aux = (contraste[i][j])
        if aux > 255:
            aux = 255
            contraste[i][j] = aux
        if aux < 0:
            aux = 0
            contraste[i][j] = aux

#criando e plotando o grafico que representa a transformação para negativo
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
plt.title('Curva de Transformação: Contraste e Luminosidade')
plt.plot(x, y, color='gray')
plt.show()

cv2.imshow("Imagem com Contraste/Luminosidade Alterada", contraste)

###################################
###################################

parabola = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8)
for i in range (imagem.shape[0]):
    for j in range (imagem.shape[1]):
        parabola[i][j] = ((((1/256)*cinzas[i][j])**2)*256) 
        aux = 0
        aux = (parabola[i][j])
        if aux > 255:
            aux = 255
            parabola[i][j] = aux
        if aux < 0:
            aux = 0
            parabola[i][j] = aux

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

cv2.imshow("Curva de Tom Parabolica", parabola)

###

cv2.waitKey(0)
cv2.imwrite("im_negativa.jpg", negativo)
cv2.imwrite("im_contrLumin.jpg", contraste)
cv2.imwrite("im_parabola.jpg", parabola)
