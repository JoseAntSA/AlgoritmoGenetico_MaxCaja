#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO

UA: Algoritmos Geneticos
Profesor: Asdrubal Lopez Chau
    
Alumno: Sanchez Alanis Jose Antonio
        
Tema: Laboratorio - Diseño de una caja rectangular
Descripción: Archivo Test

@author: anton
Created on Fri May 06 13:30:20 2022
"""

from AlgoritmoEvolutivo import AlgoritmoEvolutivo
import numpy as np


v = float(input("Favor de ingresar el volumen deseado: "))      # Pedimos al usuario el volumen de la caja

k  = np.power(v, 1/3)           

minis = [k/6, k/4, 3*k]        # Iniciamos los valores minimos
maxis = [k/3, k/2, 6*k]        # Iniciamos los valores maximos
nbits = [ 16,  16,  16]        # Iniciamos los valores del numero de bits

ae = AlgoritmoEvolutivo(minis, maxis, nbits, v, 200)     # Creamos el algoritmo genetico
ae.init()                                                # Inicializamos el algoritmo

print("\nGeneracion Inicial: ")
print("Valores: [Altura, Ancho, Largo] -> Aptitud")
print("------------------------------------------------------------------------------------------")
ae.showPob(True)                                         # Muestro la poblacion que se creo                      

for i in range(150):                                     # Ciclo para realizar la evolucion de la poblacion
    ae.evolucion()                                       # Evoluciono la poblacion a la siguiente generacion
    
print("\nGeneracion Final: ")
print("Valores: [Altura, Ancho, Largo] -> Aptitud")
print("------------------------------------------------------------------------------------------")                      
ae.showPob(True)                                         # Muestra la poblacion final

print("\n\nLas siguientes son las mejores 5 cajas:")
print("Volumen Objetivo = ", v, "\n") 
mejoresInd = ae.calMejores()                             # Obtenemos los mejores 5 indivuos (cajas)
ae.graficarInd(mejoresInd)                               # Graficamos las cajas de los mejores individuos