"""
Created on Mon Feb 27 13:05:27 2023

@author: Angel
"""
class Student:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(self.name+" says hi")

obj = Student("John")
obj.greet()
print("###END###")

##########################################################

class Dog:
  def __init__(self, name, color):
    self.name = name
    self.color = color

  def bark(self):
    print("Woof!")

fido = Dog("Fido", "brown")
print(fido.name)
fido.bark()
print("###END###")

#########################################################

class A:
  def a(self):
    print(1)
    
class B(A):
  def a(self):
    print(2)

class C(B):
  def c(self):
    print(3)
		
c = C()
c.a()
print("###END###")

########################################################

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector2D(self.x, self.y + other.y)

first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x)
print(result.y)
print("###END###")

########################################################

class Time:
    
    def __init__(self, d, h, m, s):
        self.s = s
        self.m = s//60
        self.h = m//60
        self.d = h//24
    def __mod__(self, other):
        return Time(self.d, self.h%60, self.m%60, self.s)
print("###END###")
    
########################################################

#clases
class Auto:
    marca = ""
    modelo = 2004
    placa = ""

taxi = Auto()
print(taxi.modelo)
print("###END###")  
    
########################################################
class jugadores:
    j1 = "messi"
    j2 = "c. ronaldo"
class jugadores_B:
    j3 = "marcelo"
    j1 = "falcao"
print(jugadores_B.j1)

########################################################

class nombre:
    pass
victor = nombre()
maria = nombre()


victor.edad = 30
victor.sexo = "masculino"
victor.pais = "bolivia"

    
maria.edad = 25
maria.sexo = "femeninao"
maria.pais = "colombia"
    
print(victor.edad)
print(maria.edad)   
    
########################################################
    

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
        
entrada_usuario=int(input("Escribe tiempo en segundos\n:"))

segundos= Reloj(entrada_usuario)
minutos= Reloj(segundos.cantidad//60)
horas= Reloj(minutos.cantidad//60)
dias= Reloj(horas.cantidad//24)

print(Reloj.procesador(entrada_usuario))
