#!/usr/bin/env python3
from contextlib import nullcontext
import math
""" Algoritmo que encuentra la mejor combinacion de frutas
    para la bandeja."""

"""Definimos la clase fruta que contendra los parametros
    de peso, coste e id"""
from typing import Sized


class fruta:
    
    def __init__(self,peso,id,dias):
        self.peso=peso
        self.id=id
        self.dias=dias

    def muestraFruta(self):
        return 'Peso -->'+str(self.peso)+'\tId -->'+str(self.id)+'\tDias -->'+str(self.dias)

    def getPeso(self): return self.peso
    def getId(self): return self.id
    def getDias(self): return self.dias
    def getCoste(self): return 0.1+2.0*self.getPeso()+0.05*self.getDias()

    def setPeso(self,peso): self.peso=peso
    def setId(self,id): self.id=id
    def setDias(self,dias): self.dias=dias

class bandeja:

    def __init__(self,pesotot,costetot):
        self.lista=[]
        self.pesotot=pesotot
        self.costetot=costetot

    def getLista(self): return self.lista
    def getPesotot(self): return self.pesotot
    def getCostetot(self): return self.costetot

    def insertaFruta(self,fruta):
        self.lista.append(fruta)

    def setLista(self,lista): 
        for element in lista:
            self.lista.append(element)
    def setPesotot(self,pesotot): self.pesotot=pesotot
    def setCostetot(self,costetot): self.costetot=costetot

"""Declaramos los conjuntos de abiertos y cerrados de donde iremos sacando todas las frutas"""
abiertos=[
fruta(0.273, 1400001, 1.1),
fruta(0.405, 1400002, 1),
fruta(0.517, 1400003, 1.1),
fruta(0.533, 1400004, 1.7),
fruta(0.358, 1400005, 1.5),
fruta(0.562, 1400006, 1.9),
fruta(0.322, 1400007, 2.4),
fruta(0.494, 1400008, 1.8),
fruta(0.39, 1400009, 1.6),
fruta(0.281, 1400010, 2.2),
fruta(0.395, 1400011, 2),
fruta(0.407, 1400012, 2),
fruta(0.329, 1400013, 3),
fruta(0.629, 1400014, 2.7),
fruta(0.417, 1400015, 1.2),
fruta(0.278, 1400016, 1.4),
fruta(0.583, 1400017, 2.2),
fruta(0.598, 1400018, 1.9),
fruta(0.271, 1400019, 1.6),
fruta(0.265, 1400020, 2.1)]

cerrados=[]

pesoMax=2.0
pesoTot=0.0
costeTot=0.3

"""coeficiente tiene que ser cuanto mayor sea el coste y menor el precio
    si aumenta el coste, disminuye el coeficiente
    si aumenta el peso, aumenta el coeficiente
    Peso/Coste              1 / 3 = 0.33 --> si aumento coste 1 / 4 = 0.25
                                         --> si aumento el peso 2 / 3 = 0.66"""


listaBandejas=[]
mi_bandeja = bandeja(0.0,0.0)
funcionCoste=0.0
n=0
coeficiente=0.0
"""print(str(mejorCoef))"""
"""math.isclose(mejorCoef,coeficiente,rel_tol=0.02)"""

longitudAbiertos = len(abiertos)
longitudAbiertosX = longitudAbiertos-1
longitudCerrados = len(cerrados)
m=0

"""f(n)=g(n)+h(n)
    g(n) --> peso
    h(n) --> coste"""

def calculaMenorFn(lista):
    tmp=0.0
    menor=0.0
    for i in lista:
        tmp=i.getPeso()/i.getCoste()
        if(menor<tmp): menor=tmp
    return menor

def obtieneFruta(lista,valor):
    tmp=0.0
    for el in lista:
        tmp=el.getPeso()/el.getCoste()
        if(tmp==valor): return el
    return fruta(0.0,0.0,0.0)
"""
print('Valor elemento',str(elemento.muestraFruta()))
print('Valor fn',str(valor))
"""
while(longitudAbiertos != longitudCerrados) :
                valor=calculaMenorFn(abiertos)
                """elemento = abiertos[m]"""
                if(mi_bandeja.pesotot<=pesoMax):
                    elemento=obtieneFruta(abiertos,valor)
                    if(not(elemento in cerrados) & (elemento in abiertos)):
                        abiertos.remove(elemento)
                        cerrados.append(elemento)
                        longitudCerrados = len(cerrados)
                        pesoTot=pesoTot+elemento.getPeso()
                        costeTot=costeTot+elemento.getCoste()

                        mi_bandeja.setPesotot(pesoTot)
                        mi_bandeja.setCostetot(costeTot)
                        mi_bandeja.insertaFruta(elemento)
                if(mi_bandeja.getPesotot()>pesoMax):
                        listaBandejas.append(mi_bandeja)
                        n+=1
                        """print('\n\n')
                        print('Datos de la bandeja ',str(n))
                        print('El peso total es -->',str(mi_bandeja.getPesotot()))
                        print('El coste total es -->',str(mi_bandeja.getCostetot()))
                        print('La bandeja' ,str(n), 'contiene -->',len(mi_bandeja.lista),'frutas','\n')
                        for frutas in mi_bandeja.lista:
                            print(frutas.muestraFruta())
                        print('\n\n')"""
                        
                        mi_bandeja = bandeja(0.0,0.0)
                        pesoTot=0.0
                        costeTot=0.3
                longitudCerrados = len(cerrados)

print('\n\n')
print('----------------ABIERTOS-----------------')               
for el in abiertos:
    print(el.muestraFruta())
print('\n\n')
print('----------------CERRADOS-----------------')  
for el in cerrados:
    print(el.muestraFruta())

""""bandeja_secundaria= bandeja(0.0,0.0)

bandeja_secundaria.setLista(abiertos)"""

"""for i in bandeja_secundaria.lista:
    print(i.muestraFruta())"""



print('El numero de bandejas formadas es -->',str(len(listaBandejas)))
print('\n\n')
n=0

bandejita=bandeja(0.0,0.0)

for bandejita in listaBandejas:
    n+=1
    print('Datos de la bandeja ',str(n))
    print('El peso total es -->',str(bandejita.getPesotot()))
    print('El coste total es -->',str(bandejita.getCostetot()))
    print('La bandeja' ,str(n), 'contiene -->',len(bandejita.lista),'frutas','\n')
    for frutas in bandejita.lista:
            print(frutas.muestraFruta())
    print('\n\n')