#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO

UA: Algoritmos Geneticos
Profesor: Asdrubal Lopez Chau
    
Alumno: Sanchez Alanis Jose Antonio
        
Tema: Laboratorio - Diseño de una caja rectangular
Descripción: Clase GenReal

@author: anton
Created on Mon May 02 12:20:20 2022
"""

import numpy as np
import random

class GenReal:
    
    def __init__(self, mini=-1., maxi=1., nbits=16):    # Constructor de GenReal
        
        self.mini = mini                                # Define el numero minimo que tomara el cromosoma
        self.maxi = maxi                                # Define el numero maximo que tomara el cromosoma
        self.nbits = nbits                              # Define el no de bits que tomara el cromosoma
        self.delta = (abs(mini-maxi)/2**nbits)          # Define el valor de delta
        

    def initGen(self):                                  # Metodo para inicializar el GenReal
        self.gen = random.choices([0, 1], k=self.nbits) # Inicializa el cromosa con 0's y 1's
    
    def cruzar(self, genMadre):                     # Metodo para cruzat dos GenReal
        padre = self.gen.copy()                     # Guardamos una copia del cromosoma del padre
        madre = genMadre.gen.copy()                 # Guardamos una copia del cromosoma de la madre
        cp1 = int(np.floor((self.nbits - 1)/3.))    # Calcula la tercera parte de la longitud del cromosoma
        cp2 = 2 * cp1                               # Calcula dos terceras parte de la longitud del cromosoma
        
        son1 = padre[0:cp1]                         # Le pasamos al hijo 1 la primera parte del padre
        son1.extend(madre[cp1:cp2])                 # Le pasamos al hijo 1 la segunda parte de la madre
        son1.extend(padre[cp2:])                    # Le pasamos al hijo 1 la tercera parte del padre
        
        son2 = madre[0:cp1]                         # Le pasamos al hijo 2 la primera parte de la madre
        son2.extend(padre[cp1:cp2])                 # Le pasamos al hijo 2 la segunda parte del padre
        son2.extend(madre[cp2:])                    # Le pasamos al hijo 2 la tercera parte de la madre
        
        s1 = GenReal(self.mini, self.maxi, self.nbits)        # Creamos el GenReal del Hijo 1
        s2 = GenReal(self.mini, self.maxi, self.nbits)        # Creamos el GenReal del Hijo 2
       
        s1.gen = son1                               # Le pasamos al hijo 1 su cromosoma correpondiente
        s2.gen = son2                               # Le pasamos al hijo 2 su cromosoma correpondiente
        
        return [s1, s2]                             # Retornamos los hijos
    
    def mutar(self):                                # Metodo para mutar un GenReal
        idx = np.random.randint(self.nbits - 1) + 1       # Escoge al azar un indice del gen
    
        if self.gen[idx] == 0:                            # Muta el bit del indice aleatorio
                self.gen[idx] = 1                         # a 0 si bit es 1
        else:                                             # a 1 si bit es 0
            self.gen[idx] = 0
            
    def __str__(self):                  # Metodo para pasar a cadena un GenReal
        return str(self.gen)            # Regresa el gen como cadena de 0's y 1's
    
    def getValue(self):                                                # Metodo para obtenr el valor de un GenReal
        particion = int(''.join([str(i) for i in self.gen[:]]), 2)     # Convierte en cadena el numero binario del
                                                                       # cromosoma, luego lo convierte en entero 
        return self.mini + self.delta * particion                      # Regresamos el valor del gen