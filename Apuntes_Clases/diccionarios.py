# Diccionarios
# Son conjuntos de pares de datos
# kilo=[
#     [3,4] #Elemento 0
#     [9,8] #Elemento 1
# ]
# print(kilo[1][1]) #Llama a segundo valor (1) dentro de la segunda lista o elemento(1)

diccionario={
    "Nombre": "Jose Saavedra", # Key: Value
    "Numero": 971534428,       # Key: Value
    "Casado": True,             # Key: Value
    123     :88
} 
# print(diccionario)
# print(diccionario["Nombre"]) # Solo dá el value

# for key in diccionario:
#     print(key)

# items() es la funcion que permite desplegar el valor del diccionario, se debe usar siempre que lo quiera recorrer.
# for key, value in diccionario.items():
#     print(key, value)
frutas={
    "Manzana": 1500,
    "Frutilla": 1600,
    "Durazno": 3800
}

print(frutas)
frutas["Pera"]=1200 # Se agrera primero la key y luego el value
print(frutas)

fru=input("Que fruta desea agregar: ")
val=int(input("Ingrese el precio: "))
frutas[fru]=val
print(frutas)