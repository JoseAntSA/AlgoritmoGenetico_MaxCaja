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
Created on Fri May 06 14:05:45 2022
"""

import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from Poblacion import Poblacion
from Seleccion import Seleccion
from FitnessFunction import FitnessFunction

class AlgoritmoEvolutivo:

    def __init__(self,  minis, maxis, nbits, target, size=100):   # Constructor de Algoritmo evolutivo
       
        self.minis = minis              # Definimos los valores minimos del algortimo evolutivo
        self.maxis = maxis              # Definimos los valores maximos del algortimo evolutivo
        self.nbits = nbits              # Definimos los valores de no de bits del algortimo evolutivo
        self.target = target            # Definimos el volumen a calcular con el algortimo evolutivo
        self.size = size                # Definimos el tamaño de poblacion
        self.pob = None                 # Definimos la poblacion inicialmente como nula
        
    def showPob(self, showAptitude=False):  # Metodo para mostrar la poblacion
                   
        aptitudes = [self.ff.evaluate(ind) for ind in self.pob.poblacion] # Evalua las aptitudes de cada
                                                                          # individuo y lo guarda en
                                                                          # aptitudes
            
        for i in range(self.size):  # Ciclo para iterar sobre la poblacion
        
            valorInd = self.pob.poblacion[i].getValue()
            if showAptitude:        # Condicional para imprimir o no las aptitudes
                print(valorInd, "\t-> ", str(format(aptitudes[i])))  # Muestra al individuo junto a su
                                                                     # aptitud
            else:
                print(valorInd)                                      # Muestra al individuo sin aptitud
    
    def init(self):        # Metodo inicializar una poblacion y los elementos para
                           # poder seleccionar a los mas aptos y despues entrenarlos
        pob = Poblacion(self.minis, self.maxis, self.nbits, self.size)  # Prepara una nueva poblacion
        pob.init()                                                      # Inicializa la poblacion
        self.pob = pob                                                  # Se guarda la poblacion
        self.seleccion = Seleccion()                                    # Definimos el metodo de
                                                                        # seleccion para seleccionar a
                                                                        # los mas aptos
        self.ff = FitnessFunction(self.target)                          # Definimos el metodo de
                                                                        # entrenamiento para 
                                                                        # evaluar a los mas aptos

    def evolucion(self):                        # Metodo para evolucionar una poblacion
        # 1) Evaluar individuos
        # 2) Seleccionar padres para cruza
        # 3) Generar hijos (cruza)
        # 4) Mutar a algunos
        # 5) Evaluar hijos
        # 6) Seleccionar miembros de la siguiente población

        ####################################
        #####      IMPLEMENTACION      #####
        ####################################    

        if self.pob is None:                    # Condicion por si la poblacion
            print("Inicialice la población")    # inicial no se inicializo, entonces
            return                              # terminamos el programa.
        
        
        # 1) Evaluar individuos     
        poblacion = self.pob.poblacion                             # Aislamos la poblacion
        aptitudes = [self.ff.evaluate(ind) for ind in poblacion]   # Obtenemos sus aptitutes
        
        # 2) Seleccionar padres para cruza
        k = int(self.size/2)                          # Divide el tamaño de la poblacion en 2
        if k%2 == 1:                                  # Condicional por si k es impar, por lo que
            k += 1#le suma 1                          # le sumamos 1 para evitar problemas en la cruza
        idx = self.seleccion.selecciona(aptitudes, k) # Guarda k individuos seleccionados, se le manda 
                                                      # las aptitudes y un numero k
                                                      
        #3) Generar hijos (cruza)
        descendencia = []                   # Arreglo para guardar la descendencia
        for i in list(range(0,k-1,2)):      # Ciclo para recorrer la poblacion cada 2 individuos
            ip = idx[i]                     # Selecciona el indice del padre
            im = idx[i+1]                   # Selecciona el indice de la madre
            papa = poblacion[ip]            # Apartamos al padre guardadolo en una variable
            mama = poblacion[im]            # Apartamos a la madre guardadola en una variable
            hijos = papa.cruzar(mama)       # Cruzamos al papa con la mama y obtenemos a los hijos
            descendencia.append(hijos[0])   # Agregamos a la descendencia el primer hijo
            descendencia.append(hijos[1])   # Agregamos a la descendencia el segundo hijo
        
        
        # 4) Mutar a algunos (5%)
        totalMutar = int(np.ceil(len(descendencia)*0.1))   # Convierte a entero un numero redondeado
                                                           # del 1 porciento del tamaño de la            
                                                           # descendencia siendo el numero obtenido
                                                           # la cantidad de individuos a mutar
        for i in range(totalMutar):                        # Ciclo para mutar individuos segun el 
                                                           # numero obtenido anteriormente, donde
            idx = random.choice(range(len(descendencia)))  # los individuos son elegidos
            descendencia[idx].mutar()                      # aleatoriamente
        
        
        # 5) Evaluar hijos
        for hijo in descendencia:                                # Ciclo para recorrer la descendencia y
            poblacion.append(hijo)                               # agregar los hijos a la poblacion
            
        aptitudes = [self.ff.evaluate(ind) for ind in poblacion] # Obtengo las aptitutes de la poblacion
        
        # 6) Seleccionar miembros de la siguiente población
        # ELITISMO!!!!!
        idxMejor = np.argmax(aptitudes)                         # Obtiene al individuo con la mejor 
                                                                # aptitud
        siguientePob = []                                       # Se crea la lista de individuos de la 
                                                                # siguiente generación               
        siguientePob.append(poblacion[idxMejor])                # Agrega a la siguiente poblacion al 
                                                                # individuo con la mejor aptitud
        idx = self.seleccion.selecciona(aptitudes, self.size)   # Selecciona a los siguientes individuos
        
        for i in idx:                                           # Ciclo para reccorer a los individuos     
                                                                # seleccionados y agregarlos en la
            siguientePob.append(poblacion[i])                   # siguiente poblacion

        self.pob.poblacion = siguientePob                       # Guardo la siguiente poblacion para 
                                                                # su evolución
        
    def calMejores(self):                        # Metodo para obtener los mejores 5 individuos
        aux = self.pob.poblacion                 # Creamos un auxiliar de la poblacion actual
        aptitudes = [self.ff.evaluate(ind) for ind in self.pob.poblacion] # Obtengo las aptitutes de la 
                                                                          # poblacion
        mejoresInd = []                          # Arreglo para los mejores individuos   
        cont = 0                                 # Contador para determinar si se obtuvieron los 5
                                                 # individuos
        
        while len(aptitudes) != 0 and cont < 5:  # Ciclo para obtener los mejores 5 individuos,
            idxMejor = np.argmax(aptitudes)      # se obtiene el indice del mejor individuo de las
            dato = aptitudes[idxMejor]           # aptitudes y su individuo correspodiente es agregado
            mejoresInd.append(aux[idxMejor])     # al arreglo de mejoresInd, luego se borran todas las
                                                 # coincidencias del mismo individuo del arreglo 
            while dato in aptitudes:             # auxiliar de poblacion al igual que en el del 
                aux.pop(idxMejor)                # apititudes y se procede a buscar el siguiente mejor
                aptitudes.pop(idxMejor)          # individuo. Nota: Debido a las evoluciones pueden
                                                 # caer la posibilidad de que en la poblacion haya menos
            cont += 1                            # menos de 5 individuos diferentes, es decir los
                                                 # indivudos se repiten.
                                                 
        # Condicion por si se llegan a obtener menos de 5 individuos debido a la evolucion, por
        # lo que se envia de una advertencia de ello.
        if cont < 5:
            print("-------------------------------------------------------------------")
            print("IMPORTANTE!")
            print("Se obtuvieron solo", cont, "resultados debido al numero de evoluciones...")
            print("-----------------------------------------------------------------\n")
        
        return mejoresInd                       # Retornamos el arreglo de mejores individuos
        
    def graficarInd(self, inds=None):           # Metodo para graficar las cajas de los individuos
        zF, yF, xF = inds[0].getValue()         # Extraigo los valores de xyz del mejor individuo para
                                                # usarlos como limites de los ejes en las graficas
        colores = ["yellow", "blue", "pink", "green", "red"] # Arreglo de colores para pintar las cajas
        
        if inds is None:                             # Condicion por si no hay individuos
            print("No hay individuos a graficar")    # en el arreglo inds
            return
        
        print("No. Caja  Largo (Eje x)     Ancho (Eje y)    Altura (Eje z)   Volumen")
        print("----------------------------------------------------------------------------")
        
        for i in range (len(inds)):                 # Ciclo para recorrer el arreglo de inds
            lados = inds[i].getValue()              # done obtengo los lados, calculo el volumen
            vol = lados[0]*lados[1]*lados[2]        # y lo imprimo.
            
            print(i+1, "\t\t", " %.12f"%lados[2], "  %.12f"%lados[1], "  %.12f"%lados[0],"  %.12f"%vol)
           
            # Creamos una cadena que almacenara los datos de la caja
            cad = "Datos:\n" + "\nLargo   (Eje x) = %.6f"%lados[2] + "\nAncho  (Eje y) =  %.6f"%lados[1]
            cad += "\nAltura  (Eje z) =  %.6f"%lados[0] + "\nVolumen = %.6f"%vol
            
            z, y, x = lados                     # Extraigo los lados del individuo
            P = np.array([[0, 0, 0],            # Arreglo que representa los vertices de la caja    
                          [x, 0, 0],
                          [x, y, 0],
                          [0, y, 0],
                          [0, 0, z],
                          [x, 0, z],
                          [x, y, z],
                          [0, y, z],])
            
            # Configuracion del espacio grafico
            fig = plt.figure(figsize=(7,4))           # Creamos una nueva figura y definimos su tamaño
            fig.suptitle("Caja No. " + str(i+1))      # Agregamos su titulo
            fig.legend("",                            # Mandamos una cadena vacia
                       loc="upper left" ,             # Definimos la posicion de la legenda
                       bbox_to_anchor=(0.05, 0.68),   # Definimos mas especificamente su ubicacion
                       borderaxespad=0.1,             # Agregamos un borde a la leyenda
                       title=cad)                     # Agregamos el titulo a la leyenda, en este caso
                                                      # aqui mandamos los datos de la caja, pues en
                                                      # donde se mando la cadena vacia deberia ir 
                                                      # pero no lo imprime debido a que no se esta
                                                      # graficando una funcion u graficas de puntos 
            ax = fig.add_axes((0.2, 0.1, 0.85, 0.85),projection='3d' ) # Agregamos a la figura los 
                                                                       # ejes, definiendo su tamaño
                                                                       # y su posicion dentro de la
                                                                       # figura
            ax.set_xlabel('Eje X (Largo)')            # Asignamos el nombre al eje x
            ax.set_ylabel('Eje Y (Ancho)')            # Asignamos el nombre al eje y
            ax.set_zlabel('Eje Z (Altura)')           # Asignamos el nombre al eje z
            ax.set_xlim(-1, xF+1)                     # Definimos los limites del eje x
            ax.set_ylim(-1, yF+1)                     # Definimos los limites del eje y
            ax.set_zlim(-1, zF+1)                     # Definimos los limites del eje z 
            
            # Graficacion de la figura
            ax.scatter3D(P[:, 0], P[:, 1], P[:, 2])   # Graficamos los vertices
            carasP = self.crearCaras(P)               # Creamos el arreglo de las caras de las caja
                                                       
                                                     
            ax.add_collection3d(Poly3DCollection(     # Agregamos las caras a la caja con este metodo
                                carasP,               # Mandamos el arreglo de las las caras
                                facecolors=colores[i],# Definimos el color de las caras
                                linewidths=1,         # Definimos la anchura de sus aristas
                                edgecolors='black',   # Definimos el color de las aristas
                                alpha=.25))           # Definimos la transparencia de las caras
            plt.show()                                # Mostramos la figuras

                          
    def crearCaras(self,arr):                       # Metodo para crear la caras de la caja
        temp = [[arr[0],arr[1],arr[2],arr[3]],      # Arreglo que define las caras de las caja
                [arr[4],arr[5],arr[6],arr[7]], 
                [arr[0],arr[1],arr[5],arr[4]], 
                [arr[2],arr[3],arr[7],arr[6]], 
                [arr[1],arr[2],arr[6],arr[5]],
                [arr[4],arr[7],arr[3],arr[0]]]    
        return temp                                 # Retornamos el arreglo de caras

