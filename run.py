"""Un supermercado requiere un sistema de facturación que pueda calcular los totales
de las facturas que realizan las cajas registradoras. Cada caja ingresa el código del
producto (numérico) y tiene una base de productos, ya codificada en la lista_productos.py

Se tienen que cumplir los siguientes puntos:
a. Presentar un menú permitiendo al usuario elegir una de las siguientes
opciones: 1) Ingresar nueva factura 2) Ingresar nuevo producto al
catalogo 3) Salir

b. Si elige la opción 1, se debe permitir al usuario ingresar cada producto
a factura. Primero el código del producto. Si el producto se encuentra
en la lista, preguntar la cantidad. Si no se encuentra en el catalogo,
informarlo por pantalla para volver a reingresar. El código 0 se considera
que finaliza la factura. Al finalizar mostrar la factura, producto por
producto, con la cantidad y el total de la factura.

c. Con la opción de agregar nuevo producto al catalogo, debe solicitarle los
datos de descripción, y precio unitario con dos decimales.

Utilizar módulos permitiendo la reutilización del código y no debe encontrarse toda
la lógica en un solo archivo.

Tips: Se agrega a continuación un ejemplo de obtención del catalogo dentro del
modulo productos y su utilización, imprimiendo toda la información del mismo y
utilizando la función format para incluir cada campo de los productos

import productos
for i in productos.catalogo:
 print("Cod: {} - Desc: {} - Precio: {}".format(i['codigo'], i['desc'], i['precio']))
"""
from funciones import lista_productos
from funciones import facturacion
factura = []
total = 0
contador = 0
descripcion = ""
"""las de arriba son todas variables que tuve que crear para completar la facturacion y el ingreso de nuevos prod. 
El contador lo use para saber si existe el codigo en la facturacion y en el ingreso del nuevo producto """

opcion = input("\nSeleccione:\t1) Ingresar nueva factura\t2) Ingresar nuevo catalogo al producto\t3) Salir\n")

while int(opcion) < 1 or int(opcion) > 3: #verifico el ingreso correcto de la opcion
    print("Ingreso invalido!")
    opcion = input("Seleccione:\t1) Ingresar nueva factura\t2) Ingresar nuevo catalogo al producto\t3) Salir\n")

while int(opcion) != 3: # si es 3 sale del programa
    if int(opcion) == 1: #pasos para la facturacion
        codigo = input("Ingrese el codigo del producto (0 para finalizar):\t")
        while int(codigo) != 0:
            for sublist in lista_productos.lista: #recorre las sublistas en la lista
                if sublist[0] == int(codigo): #busco si existe el codigo, para ingresar la cantidad y sumar al total
                    cant = input("Cantidad:\t")
                    factura.append(facturacion.add(int(codigo), sublist[1], int(cant)))
                    total += int(cant) * sublist[2]
                else:
                    contador += 1
            if contador == len(lista_productos.lista): #condicion de producto no encontrado
                print("Producto no encontrado")
            contador = 0
            codigo = input("Ingrese un nuevo codigo (0 para finalizar):\t")
        if total != 0: #condicion para tener una facturacion real
            print("\nFactura:")
            for i in factura:
                print("Cod: {}\t Desc: {}\t Cant:\t{}".format(i[0], i[1], i[2]))
            print("Total:\t{}".format(round(total, 2)))
        else:
            print("No ingreso ningun producto a la factura")
        total = 0

    else: #si se el codigo es 2 se ingresa un producto al listado de productos
        codigo = input("Ingrese los datos del nuevo producto:\nIngrese el codigo (O para terminar):\t")
        while int(codigo) != 0:
            for sublist in lista_productos.lista: #para recorrer sublistas
                if sublist[0] != int(codigo):
                    contador += 1
                else:
                    contador -= 1
            if contador == len(lista_productos.lista): #condicion de codigo no encotrado
                descripcion = input("Ingrese la descripcion:\t")
                precio = input("Ingrese el precio unitario (con dos decimales):\t")
                facturacion.nuevo_producto(int(codigo), descripcion, round(float(precio), 2))
            else:
                print("El codigo ya existe!")
            contador = 0
            codigo = input("Ingrese los datos del nuevo producto:\nIngrese el codigo (O para terminar):\t")
        print("\n{}".format(lista_productos.lista)) #imprimo para ver el correcto ingreso del producto

    opcion = input("\nSeleccione:\t1) Ingresar nueva factura\t2) Ingresar nuevo catalogo al producto\t3) Salir\n")
    #reinicio la variable

    while int(opcion) < 1 or int(opcion) > 3:
        print("Ingreso invalido!")
        opcion = input("Seleccione:\t1) Ingresar nueva factura\t2) Ingresar nuevo catalogo al producto\t3) Salir\n")

print("Ingreso 3, saliendo del programa")