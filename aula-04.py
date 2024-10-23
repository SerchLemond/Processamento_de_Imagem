# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 16:49:40 2023

@author: aluno
"""

import cv2
import numpy
import matplotlib.pyplot as plt
foto = 'entrada2.jpg'
imagem = cv2.imread(foto)

###################################
###################################

#cria uma imagem (matriz) e preenche seus pixels com tons de cinza
#cada tom de cinza equivale à média dos tres canais daquele pixel
contrtCinzas = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8)
for i in range (imagem.shape[0]):
    for j in range (imagem.shape[1]):
        contrtCinzas[i][j] = (imagem[i][j].sum()//3)

cv2.imshow("Tons de Cinza", contrtCinzas)

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

###################################
###################################

#cria uma nova imagem, escolhendo um intervalo do histograma e expandindo-o
#o intervalo escolhido foi entre 75 e 175
#os valores fora desse intervalo são reduzuidos a 0 (se menores que 75) ou aumentados a 255 (se maiores que 175)
expansao1 = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8)
for i in range (imagem.shape[0]):
    for j in range (imagem.shape[1]):
        expansao1[i][j] = contrtCinzas[i][j]
        if expansao1[i][j] < 75:
            expansao1[i][j] = 0
        if (75 <= expansao1[i][j] <= 175):
            expansao1[i][j] = 255*(((contrtCinzas[i][j])-75)/(175-75))
        if expansao1[i][j] > 175:
            expansao1[i][j] = 255
cv2.imshow("Contraste Expandido V1", expansao1)

#cria um novo histograma, agora com o contrsye expandido
histExpn = [0]*256
for i in range (imagem.shape[0]):
    for j in range (imagem.shape[1]):
        histExpn[expansao1[i][j]]+=1
pixel = [0]*256
for i in range (256):
    pixel[i]=i
plt.xlabel('Tom de Cinza')
plt.ylabel('Quantidade')
plt.title('Histograma Expandido V1')
plt.bar(pixel, histExpn, color='gray')
plt.show()

#cria a curva da função, mostrando a transformação de uma imagem para a outra
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
plt.title('Curva de Transformação: Histograma Expandido V1')
plt.plot(x, y, color='gray')
plt.show()

###################################
###################################

#cria uma nova imagem, escolhendo agora dois intervalos
#o intervalo na imagem original é entre 75 e 175 (r1 e r2)
#o intervalo na imagem final é entre 50 e 200 (s1 e s2)
#o teto de cada imagem é 255 (rmax = smax = 255)
#os intervalos antes, dentro e após os intervalos definidos sofrem transformações diferentes
expansao2 = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8)
for i in range (imagem.shape[0]):
    for j in range (imagem.shape[1]):
        expansao2[i][j] = contrtCinzas[i][j]
        if expansao2[i][j] < 75:
            expansao2[i][j] = (50/75)*(contrtCinzas[i][j])
        if (75 <= expansao2[i][j] <= 175):
            expansao2[i][j] = ((((contrtCinzas[i][j])-75)*(200-50))/(175-75))+(50)
        if expansao2[i][j] > 175:
            expansao2[i][j] = (((contrtCinzas[i][j])-175)*((255-200)/(255-175)))+(200)
cv2.imshow("Contraste Expandido V2", expansao2)

#cria um novo histograma, agora com o contrsye expandido
histExpn = [0]*256
for i in range (imagem.shape[0]):
    for j in range (imagem.shape[1]):
        histExpn[expansao2[i][j]]+=1
pixel = [0]*256
for i in range (256):
    pixel[i]=i
plt.xlabel('Tom de Cinza')
plt.ylabel('Quantidade')
plt.title('Histograma Expandido V2')
plt.bar(pixel, histExpn, color='gray')
plt.show()

#cria a curva da função, mostrando a transformação de uma imagem para a outra
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

cv2.waitKey(0)
cv2.imwrite("im_contrExpsV1.jpg", expansao1)
cv2.imwrite("im_contrExpsV2.jpg", expansao2)