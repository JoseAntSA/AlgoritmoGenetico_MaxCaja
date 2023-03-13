#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO

UA: Algoritmos Geneticos
Profesor: Asdrubal Lopez Chau
    
Alumno: Sanchez Alanis Jose Antonio
        
Tema: Laboratorio - Diseño de una caja rectangular
Descripción: Clase CromosomaReal

@author: anton
Created on Mon May 02 12:40:13 2022
"""

from GenReal import GenReal as Real

class CromosomaReal:
    
    def __init__(self, minis, maxis, nbits):    # Constructor de CromosomaReal
        
        if len(minis) != len(maxis):            # Verifica que el numero de intervalos no sea igual
            return                              # Retorna en caso de no serlo
        
        self.minis = minis               # Define los valores minimos del cromosoma
        self.maxis = maxis               # Define los valores maximos del cromosoma
        self.nbits = nbits               # Define los valores de no de bits del cromosoma
        self.genes = []                  # Creamos un arreglo de genes
        
        for mini, maxi, nbit in zip(minis, maxis, nbits):      # Ciclo para crear cada gen
            gen = Real(mini, maxi, nbit)                       # Creamos el gen con sus valores correspondientes
            self.genes.append(gen)                             # Agregamos al arreglo genes el gen
        
    def init(self):                     # Metodo para inicializar el CromosomaReal
        
        for gen in self.genes:          # Inicializa los genes de cada cromosoma del arreglo
           gen.initGen()                # de genes
    
    def cruzar(self, madre):            # Metodo para cruzar dos CromosomaReal
        genesHijos1 = []                # Creamos un arreglo de genes hijos 1
        genesHijos2 = []                # Creamos un arreglo de genes hijos 2
        
        for papa, mama in zip(self.genes, madre.genes):         # Hacemos la cruza de cada padre con la madre
            g = papa.cruzar(mama)                               # y almacenamos cada cruza en su arreglo
            genesHijos1.append(g[0])                            # correspodiente de hijos
            genesHijos2.append(g[1])
        
        h1 = CromosomaReal(self.minis, self.maxis, self.nbits)  # Creamos el GenReal de los hijos 1
        h2 = CromosomaReal(self.minis, self.maxis, self.nbits)  # Creamos el GenReal de los hijos 2
        
        h1.genes = genesHijos1                                  # Le pasamos a los hijos 1 su gen correpondiente
        h2.genes = genesHijos2                                  # Le pasamos a los hijos 2 su gen correpondiente
        
        return [h1, h2]                                         # Retornamos al arreglo de hijos resultante
    
    def mutar(self):                            # Metodo para mutar un CromosomaReal
        for genInd in self.genes:               # Mutamos cada gen del arreglo 
            genInd.mutar()
    
    def getValue(self):                         # Metodo para obtener el valor de un CromosomaReal
        values = []                             # Creamos una arreglo de valores vacio
        for gen in self.genes:                  # Sacamos el valor de cada gen
            values.append(gen.getValue())       # y lo agreamos al arreglo
        return values                           # Retornamos el arreglo
    
    def __str__(self):                          # Metodo para pasar a cadena un CromosomaReal
        cad = ""                                # Creamos un cadena vacia
        for gen in self.genes:                  # Pasamos a la cadena cada gen
            cad = cad + gen.__str__()
        return cad                              # Retornamos la cadena