print("Ingrese su nombre")
nom=input()
print("Ingrese su edad")
edad=int(input())

print("Su nombre es ",nom," y su edad es ",edad)

if edad>=18:
    print("Usted es mayor de edad!")
else:
    print("Usted es menor de edad!")

# Sacar el promedo de 3 números

print("Ingrese 3 notas")
n1,n2,n3=float(input()),float(input()),float(input())
prom=(n1+n2+n3)/3
print("Su promedio de notas es ", round(prom,1))

if prom>=4:
    print("Aprobado")
else:
    print("Reprobado")

# Calificar por 3 edades
# >12 niño, 12 y 17 adolecente, 18+ adulto, 65+ adulto mayor

edad=int(input("Ingrese su edad"))

if edad<12:
    print("Usted es un niño")
elif edad>=12 and edad<18:
    print("Usted es un adolecente")
elif edad>=18 and edad<64:
    print("Usted es mayor de edad")
else:
    print("Usted es un adulto mayor")

# explicación y uso de for

# 1
# num=int(print("Ingrese un numero"))
# for i in range(num):
#     print("i")

# 2
# Tabla de multiplicar
# num=int(input("Ingrese un número"))
# for i in range (10):  
#    print(num,"x",i+1,"=", (i+1)*num)

# 3
# Promedio
cant=int(input("Ingrese el numero de notas"))
suma=0
for i in range(cant):
    print("Ingrese la nota", i+1)
    nota=float(input())
    suma=suma+nota
prom=suma/cant
print("El promedio es ", round(prom,1))

if prom>=4:
    print("Aprobado")
else:
    print("Reprobado")

# # nombre="Nacho"
# edad=19


# nombre=input()
# # ejemplo concatenacion
# print("hola ", nombre,"y su edad es ",edad)  


# print("Hola ",nombre," y su edad en 5 años será ",edad+5)


n1=int(input("Ingrese 1 número"))
n2=int(input("Ingrese 1 número"))
print(n1+n2)
print("el resultado de la suma es",n1+n2)
