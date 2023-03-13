#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO

UA: Algoritmos Geneticos
Profesor: Asdrubal Lopez Chau
    
Alumno: Sanchez Alanis Jose Antonio
        
Tema: Laboratorio - Diseño de una caja rectangular
Descripción: Clase Seleccion

@author: anton
Created on Fri May 06 13:46:04 2022
"""

import numpy as np
import random

class Seleccion:
    
    def selecciona(self, aptitudes, k=2):       # Metodo para seleccionar k individuos
                                                
        aptitudes = np.array(aptitudes) + .01   # Para darle chance a los menos aptos le sumamos a las aptitudes
                                                # de los individuos .01 para que puedan ser seleccionados                             
       
        probabilidades = [np.exp(aptitud)/np.sum(np.exp(aptitudes)) for aptitud in aptitudes]# Calcula la probabilidad de                       
                                                                                             # cada individuo para ser
                                                                                             # elegido
        indices = list(range(len(aptitudes)))                                                # Guarda los indices de los
                                                                                             # individuos 
        return random.choices(indices, probabilidades, k=k)                                  # Escoge a k individuos de la
                                                                                             # lista y guarda sus indices
        
        











