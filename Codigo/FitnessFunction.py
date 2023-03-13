#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO

UA: Algoritmos Geneticos
Profesor: Asdrubal Lopez Chau
    
Alumno: Sanchez Alanis Jose Antonio
        
Tema: Laboratorio - Diseño de una caja rectangular
Descripción: Clase FitnessFunction

@author: anton
Created on Fri May 06 13:30:20 2022
"""

import numpy as np

class FitnessFunction:
    
    def __init__(self, target):     # Constructor de FitnessFunction
        self.target = target        # Definimos el volumen a tratar
        self.lamda = 1              # Definimos la variable lamda
        self.beta = 1               # Definimos la variable beta
        
    def evaluate(self, ind):                    # Metodo de evaluacion
        ladosCaja = ind.getValue()              # Obtenemos los lados de la caja de individuo (genes)
        vol = 1                                 # Definimos la variable volumen para calcularlo
        
        for lado in ladosCaja:                  # Ciclo para calcular el volumen segun el individuo
            vol *= lado                         # evaluado
        
        x = np.abs(self.target - vol)           # Calculamos la diferencia del volumen real al representado por
                                                # el individuo
        return self.beta*np.exp(-self.lamda*x)  # Calculamos y retornamos la aptitud del individuo
    