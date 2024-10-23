# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 18:11:28 2023

@author: aluno
"""

import cv2
import numpy
foto = 'entrada.jpg'
imagem = cv2.imread(foto)


###

print('Largura: ', end='')
print(imagem.shape[1], end='')
print(' Pixels')

###

print('Altura: ', end='')
print(imagem.shape[0], end='')
print(' Pixels')

###

print('Quantidade de Canais: ', end='')
print(imagem.shape[2])

###

(b,g,r) = imagem[100,50]   #verifica as cores em um pixel [x,y]
print('Valores de canais no pixel [752,407]: ', end='')
print(b,g,r)

###

azul = imagem[:,:,0]  #[linhas (altura), colunas (largura), canais('profundidade')]
cv2.imshow("Canal Azul",azul)
cv2.waitKey(0)

verde = imagem[:,:,1]
cv2.imshow("Canal Verde",verde)
cv2.waitKey(0)

vermelho = imagem[:,:,2]
cv2.imshow("Canal Vermelho",vermelho)
cv2.waitKey(0)

###

canalAzul = numpy.zeros((imagem.shape[0], imagem.shape[1], imagem.shape[2]), dtype = numpy.uint8)
canalVerde = numpy.zeros((imagem.shape[0], imagem.shape[1], imagem.shape[2]), dtype = numpy.uint8)
canalVermelho = numpy.zeros((imagem.shape[0], imagem.shape[1], imagem.shape[2]), dtype = numpy.uint8)

canalAzul[:,:,0] = imagem[:,:,0]
canalVerde[:,:,1] = imagem[:,:,1]
canalVermelho[:,:,2] = imagem[:,:,2]

cv2.imshow("Canal Azul", canalAzul)
cv2.waitKey(0)
cv2.imshow("Canal Verde", canalVerde)
cv2.waitKey(0)
cv2.imshow("Canal Vermelho", canalVermelho)
cv2.waitKey(0)

###

cinzas = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8)
for i in range (imagem.shape[0]):
    for j in range (imagem.shape[1]):
        cinzas[i][j] = (imagem[i][j].sum()//3)
cv2.imshow("Tons de Cinza", cinzas)
cv2.waitKey(0)

###

cv2.imshow("Imagem Real",imagem)
cv2.waitKey(0)
cv2.imwrite("saida.jpg",imagem)

