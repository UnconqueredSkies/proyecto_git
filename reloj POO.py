# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 11:36:26 2023

@author: angels
"""

class Reloj:
    #Constructor
    def __init__(self, conversion, cantidad):
        self.conversion=conversion
        self.cantidad=cantidad

    def procesador(self):
        memoria=entrada_usuario
        lista=[]
        if entrada_usuario>=dias.cantidad:
            entrada=(entrada_usuario//dias.cantidad)%dias.cantidad
            lista.append(entrada)
            memoria=memoria-entrada*dias.cantidad
        else:
            lista.append(0)
        if memoria>=horas.cantidad:
            entrada=(memoria//horas.cantidad)%horas.cantidad
            lista.append(entrada)
            memoria=memoria-entrada*horas.cantidad
        else:
            lista.append(0) 
        if memoria>=minutos.cantidad:
            entrada=(memoria//minutos.cantidad)%minutos.cantidad
            lista.append(entrada)
            memoria=memoria-entrada*minutos.cantidad
        else:
            lista.append(0)    
        lista.append(memoria)
        return lista
        
entrada_usuario=int(input("Escribe tiempo en segundos\n:"))

segundos= Reloj("segundo", 1)
minutos= Reloj("minuto", 60)
horas= Reloj("hora", 3600)
dias= Reloj("dia", 86400 )


print(Reloj.procesador(entrada_usuario))