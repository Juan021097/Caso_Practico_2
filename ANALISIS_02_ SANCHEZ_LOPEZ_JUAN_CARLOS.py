# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 18:56:38 2021

@author: Usuario
"""
###pregunta a
datos = []
with open('base2.csv', 'r') as archivo:
  lineas = archivo.read().splitlines()
  lineas.pop(0)
  for l in lineas:
    lineas=l.split(',')
    datos.append([int(lineas[0]), (lineas[1]),(lineas[2]),(lineas[3])])

nueva = []#Nueva lista  para usar el campo requerido
for contador in datos:
  nueva.append((contador[1],contador[2],contador[3]))

repeticiones = {}
for n in nueva:
  if n in repeticiones:
    repeticiones[n] += 1
  else:
    repeticiones[n] = 1

resultado = {}
for clave in repeticiones:
  valor = repeticiones[clave]
  if valor != 0:
   resultado[clave] = valor
print(resultado)

###pregunta b

datos1 = []
with open('base2.csv', 'r') as archivo:
  lineas = archivo.read().splitlines()
  lineas.pop(0)
  for l in lineas:
    lineas=l.split(',')
    datos1.append([(lineas[1]),(lineas[7]),(lineas[9])])
   
nueva1 = []#Nueva lista  para usar el campo requerido
for contador1 in datos1:
  nueva1.append((contador1[1]))

repeticiones1 = {}
for n in nueva1:
  if n in repeticiones1:
    repeticiones1[n] += 1
  else:
    repeticiones1[n] = 1

resultado1 = {}
for clave1 in repeticiones1:
  valor1 = repeticiones1[clave1]
  if valor1 != 0:
   resultado1[clave1] = valor1
   
print(resultado1)
