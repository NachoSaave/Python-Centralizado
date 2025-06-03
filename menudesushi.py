# Menu de sushi

import time
global productos , subtotal, pr, otr, pvr, aer, total
descuento="soyotaku"
descuento1=0
productos=0
subtotal=0
total=0
pr=0
otr=0
pvr=0
pvr=0
aer=0

def pagar():
    global productos , subtotal, pr, otr, pvr, aer, total
    codigo=input("Ingrese código de descuento: ")
    if codigo==descuento:
        print(f"Descuento activado de 10%.")
        descuento1=subtotal*0.1
        total=subtotal-descuento1
        boleta()
    else:
        op=int(input("Código no válido. Desea ingresarlo nuevamente? 1 - Si. 2 - No."))
        match op:
            case 1:
                pagar()
                boleta()
            case 2:
                total=subtotal
                boleta()       
def boleta():
    print(f'''
    ******************************
    TOTAL PRODUCTOS:{productos}
    ******************************
    Pikachu Roll : {pr}
    Otaku Roll : {otr}
    Pulpo Venenoso Roll:{pvr}
    Anguila Eléctrica Roll:{aer}
    ******************************
    Subtotal por pagar: ${subtotal}
    Descuento por código: ${descuento1}
    TOTAL: ${total}
    ''')
def menu():
    global productos , subtotal, pr, otr, pvr, aer, total
    while True:
        rolls=int(input('''Que desea llevar?
                        1. Pikachu Roll $4500
                        2. Otaku Roll $5000
                        3. Pulpo Venenoso Roll $5200
                        4. Anguila Eléctrica Roll $4800
                        5. Completar pedido'''))
        match rolls:
            case 1:
                subtotal+=4500
                productos+=1
                pr+=1
                print("Lleva Pikachu roll")
            case 2:
                subtotal+=5000
                productos+=1
                otr+=1
                print("Lleva Otaku  roll")
            case 3:
                subtotal+=5200
                productos+=1
                pvr+=1
                print("Lleva pulpo venenoso roll")
            case 4:
                subtotal+=4800
                productos+=1
                aer+=1
                print("Lleva anguila electrica roll")
            case 5:
                print("Completado pedido...")
                time.sleep(1)
                pagar()
                break
            case _:
                print("Seleccione una opción válida")
menu()
