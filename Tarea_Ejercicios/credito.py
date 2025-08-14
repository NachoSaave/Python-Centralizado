credito=0
ingreso=int(input("Introduzca sus ingresos mensuales"))

if ingreso>500000 or ingreso<1000000:
    credito+=300000
elif ingreso>1000001 or ingreso<1500000:
    credito+=650000
elif ingreso>15000001:
    credito+=1000000
else:
    print("Fuera ed rango")
print(f"Su credito es {credito}")

educacion=input("Introduzca su nivel de educación. 1.-Básica    2.-Media    3.-Superior")
if educacion=="1":
    credito*=1
elif educacion=="2":
    credito*=1.3
elif educacion=="3":
    credito*=1.5
else:
    print("Error, intente de nuevo")

nacionalidad=input("Introduzca su nacionalidad. 1.- Chilena     2.- Extranjero")
if nacionalidad=="1":
    credito+=300000
else:
    credito*=1

print(f"Su credito total es {credito}")