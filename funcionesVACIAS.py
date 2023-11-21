from principal import *
from configuracion import *
import random
import math
from extras import *


# lee el archivo y carga en la lista lista_producto todas las palabras

def lectura():
    asd = open("productos.txt","r")
    palabra = ""
    lista = []
    listaLetra = []

    for linea in asd:
        linea = linea[0:-1]
        for letra in linea:
            if letra != ",":
                palabra += letra
            else:
                listaLetra.append(palabra)
                palabra = ""
        listaLetra.append(palabra)
        palabra = ""
        lista.append(listaLetra)
        listaLetra = []
    return lista
#De la lista de productos elige uno al azar y devuelve una lista de 3 elementos, el primero el nombre del producto, el segundo si es economico
#o premium y el tercero el precio.
def buscar_producto(lista_productos):
    numP = random.randint(0,len(lista_productos)-1)
    numEOP = random.randint(1,2)
    if numEOP == 1:
        producto = [lista_productos[numP][0],"(economico)",int(lista_productos[numP][1])]
    else:
        producto = [lista_productos[numP][0],"(premium)",int(lista_productos[numP][2])]
    return producto

#Elige el producto. Debe tener al menos dos productos con un valor similar
def dameProducto(lista_productos, margen):
    producto = buscar_producto(lista_productos)
    precioProd = int(producto[2])
    asd = esUnPrecioValido(precioProd,lista_productos,MARGEN)
    if asd == True:
        return producto
    else:
        dameProducto(lista_productos, MARGEN)



#Devuelve True si existe el precio recibido como parametro aparece al menos 3 veces. Debe considerar el Margen.
def esUnPrecioValido(precio, lista_productos, margen):
    cont = 0
    for linea in lista_productos:
        preciodif = int(linea[1])-precio
        if preciodif <= margen and preciodif >= -margen:
            cont +=1
        else:
            preciodif = int(linea[2])-precio
            if preciodif <= margen and preciodif >= -margen:
                cont +=1

    if cont > 1:
        return True
    else:
        return False

# Busca el precio del producto_principal y el precio del producto_candidato, si son iguales o dentro
# del margen, entonces es valido y suma a la canasta el valor del producto. No suma si eligió directamente
#el producto
def procesar(producto_principal, producto_candidato, margen):
    precioProd1 = int(producto_principal[2])
    precioProd2 = int(producto_candidato[2])
    precioDif = precioProd1-precioProd2
    if precioDif <= margen and precioDif >= -margen:
        return precioProd2
    else:
        return 0


#Elegimos productos aleatorios, garantizando que al menos 2 tengan el mismo precio.
#De manera aleatoria se debera tomar el valor economico o el valor premium. Agregar al nombre '(economico)' o '(premium)'
#para que sea mostrado en pantalla.
def dameProductosAleatorios(producto, lista_productos, margen):
    lista = []
    cont = 0
    while cont < 2:
        numAle = random.randint(0,len(lista_productos)-1)
        preciodif = int(lista_productos[numAle][1])-producto[2]
        if preciodif >= -margen and preciodif <= margen:
            lista.append([lista_productos[numAle][0],"(economico)",lista_productos[numAle][1]])
            cont += 1
        else:
            preciodif = int(lista_productos[numAle][2])-producto[2]
            if preciodif >= -margen and preciodif <= margen:
                lista.append([lista_productos[numAle][0],"(premium)",lista_productos[numAle][2]])
                cont += 1

    productos_seleccionados = [producto]
    while len(productos_seleccionados)<6:
        cont0 = 0
        numAl = random.randint(2,5)
        if numAl == 2:
            if cont0 < 2:
                if lista[cont0] not in productos_seleccionados:
                    productos_seleccionados.append(lista[cont0])
                    cont0 += 1
        else:
            prodNuevo = buscar_producto(lista_productos)
            if prodNuevo not in productos_seleccionados:
                productos_seleccionados.append(prodNuevo)
    return productos_seleccionados

