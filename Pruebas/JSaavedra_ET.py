# Una tienda online llamada Pybooks se ha especializado en la venta de notebooks. La información de cada modelo de notebook está registrada en un diccionario llamado “produc-
# tos”, donde las llaves son los modelos y los valores asociados a las llaves son listas que contiene información asociada a cada modelo. Los puntos suspensivos indican que pueden
# existir muchos más datos. A continuación, se muestra un ejemplo del diccionario “productos”

#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video],]
productos = {
'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD':['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

#stock = {modelo: [precio, stock], ...]
stock = {
'8475HD': [387990,10],
'2175HD': [327990,4], 
'JjfFHD': [424990,1],
'fgdxFHD':[664990,21], 
'123FHD': [290890,32], 
'342FHD':[444990,7],
'GF75HD': [749990,2], 
'UWU131HD':[349990,1], 
'FS1230HD':[249990,0],
}

def stock_marca(marca):
    sum=0
    st=input("Ingrese marca a consultar: ").lower()
    for k, v in productos.items():
        if v[0].lower()==st:
            sum+=stock[k][1]            
    print(f"El stock es: {sum}")

def busqueda_precio():
    while True:
        try:
            p_min=int(input("Ingrese el valor mínimo: "))
            p_max=int(input("Ingrese el valor máximo: "))
            if p_min<0 or p_max<0:
                print("Los valores deben ser positivos.")
            if p_min>p_max:
                print("El valor mínimo no puede ser mayor que el valor máximo.")
            break
        except Exception as err:
            print(err)
    for k, v in stock.items():
        if v[0]>=p_min and v[0]<=p_max:
            print(f"Modelo: {k}, Precio: {v[0]}, Stock: {v[1]}")

def actualizar_precio():
    while True:
        for k, v in stock.items():
            print(k,v)
        nuevo=input("Ingrese el modelo a actualizar: ")
        if nuevo in stock:
            p=int(input("Ingrese el nuevo precio: "))
            if nuevo in stock:
                stock[nuevo][0]=p
                print(f"El precio del modelo {nuevo} ha sido actualizado a {p}.")
                res=input("Desea actualizar otro modelo? (s/n)").lower()
                if res=='n':
                    break
            else:   
                print(f"El modelo {nuevo} no existe en el stock.")
        else:
            print("El modelo no existe!!")
 
while True:
    try:
        opc=int(input('''
        *** MENU PRINCIPAL ***
        1. Stock marca.
        2. Búsqueda por precio.
        3. Actualizar precio.
        4. Salir.
        Seleccione su opción: '''))
        match opc:
            case 1:
                stock_marca(productos)
            case 2:
                busqueda_precio()
            case 3:
                actualizar_precio()
            case 4:
                print("Programa finalizado...")
                exit()
            case _:
                print("Debe seleccionar una opción válida!!")
    except Exception as e:
        print(e)