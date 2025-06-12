# Perros de caza
import time, random
conejos=0
completo=0
incompleto=0
while True:
    try:
        perro=int(input("Cuentos perros hay?: "))
        while perro<1:
            print("Debe ingresar 1 o más perros!")
            perro=int(input("Introduzca una cantidad de perros: "))
        n1=random.randint(1,5)
        n2=random.randint(6,15)
        cuota=random.randint(n1,n2)

        print(f"{perro} perros irán a cazar... Cuota mínima de conejos por perro es de {cuota}")
        time.sleep(1)
        for i in range(perro):
            time.sleep(1)
            conejos=random.randint(n1,n2)
            print(f"Perro {i+1} ha traído {conejos} conejos")
            if conejos>=cuota:
                print(f"El perro {i+1} ha traído la cuota necesaria... Hay filete!")
                completo+=1
            else:
                print(f"El perro no ha alcanzado la cuota de {cuota}... No hay filete!")
                incompleto+=1    
        if completo>0:
            print(f"La cantidad de perros que alcanzaron la cuota son {completo}. Los que fallaron en cumplir fueron {incompleto}") 
        else:
            print(f"Ningún perro alcanzó la cuota! ({incompleto})")
    except Exception:
        print("Introduzca un número")