# def iva():
#     monto=int(input("Ingrese el monto de dinero $"))
#     print(f"El iva (19%) de {monto} es {round(monto*0.19)} con el total siento {round(monto*1.19)}")
# iva()

# def descuento():
#     monto=int(input("Cuál es el monto que tiene? $"))
#     porcentaje=int(input("Cuánto portentaje de descuento aplica? %"))/10
#     print(f"Su monto ${monto} queda en {monto*porcentaje} con el descuento aplicado")
# descuento()

def calcular_iva(n):
    return n*0.19

def calcular_descuento(precio, porcentaje):
    return precio*(porcentaje/100)
neto=500

print(f"El IVA es {calcular_iva(neto)}")
print(f"El precio total es {calcular_iva(neto)+neto}")

