#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO

UA: Algoritmos Geneticos
Profesor: Asdrubal Lopez Chau
    
Alumno: Sanchez Alanis Jose Antonio
        
Tema: Laboratorio - Diseño de una caja rectangular
Descripción: Clase Poblacion

@author: anton
Created on Mon May 02 13:00:20 2022
"""

from CromosomaReal import CromosomaReal as Cr

class Poblacion:
    
    def __init__(self, minis, maxis, nbits, size=100):      # Constructor de la poblacion
        
        self.minis = minis                                  # Definimos los valores minimos de la poblacion
        self.maxis = maxis                                  # Definimos los valores maximos de la poblacion
        self.nbits = nbits                                  # Definimos los valores de no de bits de la poblacion
        self.size = size                                    # Definimos el tamaño de la poblacion

    def init(self):                                         # Metodo para inicializar la poblacion
        poblacion = []                                      # Arreglo vacio para guardar la poblacion
        for i in range(self.size):                          # Ciclo para crear individuos para el arreglo poblacion
            ind = Cr(self.minis, self.maxis, self.nbits)    # Creamos individuos (Objeto de tipo CromosomaReal)
            ind.init();                                     # Inicializmos cada individuo
            poblacion.append(ind)                           # Agregamos el individuo a la poblacion
        self.poblacion = poblacion                          # Guardamos la poblacion
        