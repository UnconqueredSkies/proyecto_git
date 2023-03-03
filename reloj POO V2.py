# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 13:59:12 2023

@author: angel
"""
class Reloj:
    #Constructor
    def __init__(self, cantidad):
        self.cantidad=cantidad

    def procesador(self):
        return dias.cantidad, horas.cantidad%24, minutos.cantidad%60, segundos.cantidad%60
        
entrada_usuario=int(input("Escribe tiempo en ssegundos\n:"))

segundos= Reloj(entrada_usuario)
minutos= Reloj(segundos.cantidad//60)
horas= Reloj(minutos.cantidad//60)
dias= Reloj(horas.cantidad//24)

print(Reloj.procesador(entrada_usuario))