# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 13:52:17 2023

@author: Angel
"""

def calculador_tiempo(segundos):
    minutos=segundos//60
    hora=minutos//60
    dias=hora//24
    conversion=dias,hora%24,minutos%60,segundos%60
    return conversion


entrada=int(input("Escribe tiempo en ssegundos\n:"))

print(calculador_tiempo(entrada))
