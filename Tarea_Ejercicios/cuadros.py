import random
from random import randint
num1=int(input("Introduzca un número"))
num2=int(input("Introduzca un segundo número mayor que el primero"))

while num1>num2:
    print("El segundo numero no puede ser inferior al primer número")
    num2=int(input("Segundo número:"))
num=randint(num1,num2)
cuadros=("▄ "*num)
for i in range(num):
    print(cuadros)