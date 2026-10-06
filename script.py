# ============================================================
# PYTHON 2: colecciones, bucles, funciones, lambda y debugging
# Para ejecutarlo, abre la terminal de VS Code y escribe: python script.py
# ============================================================

# ============================================================
# 1. LISTAS, TUPLAS Y SETS
# ============================================================
# Lista: colección ordenada y mutable (se pueden añadir, quitar y cambiar elementos). Se escribe con [].
productos_lista = ["Monitor", "Teclado", "Mouse"]
productos_lista.append("Webcam")  # añade un elemento al final
print(productos_lista[0])         # Monitor: los índices empiezan en 0
print(productos_lista)            # ['Monitor', 'Teclado', 'Mouse', 'Webcam']

# Tupla: colección ordenada e inmutable (no se puede modificar una vez creada). Se escribe con ().
# Si intentamos cambiar un valor, por ejemplo coordenadas_tupla[0] = 41.0, Python da un TypeError.
coordenadas_tupla = (40.4, -3.7)
print(coordenadas_tupla[0])  # 40.4

# Set: colección mutable de elementos únicos, sin duplicados y sin un orden fijo. Se escribe con {}.
numeros_set = {1, 2, 2, 3, 4, 5, 5, 5}
print(numeros_set)  # {1, 2, 3, 4, 5}: muestra solo los valores únicos

# Un set vacío se crea con set(), porque {} crea un diccionario vacío
numeros_vacio = set()
diccionario_vacio = {}
print(type(numeros_vacio))      # <class 'set'>
print(type(diccionario_vacio))  # <class 'dict'>

# set() también convierte otras colecciones en un set, quitando los duplicados
numeros = set([1, 2, 2, 3, 3])
print(numeros)  # {1, 2, 3}

# ============================================================
# 2. DICCIONARIOS ANIDADOS
# ============================================================
# El valor de una clave puede ser una lista u otro diccionario.
# Para llegar a un dato se encadenan los corchetes: primero la clave y después
# el índice de la lista o la clave del diccionario interior.
persona = {
    "nombre": "Aurelio García",
    "hobbies": [
        "Escalada",
        "Lectura",
        "Cocina"
    ],
    "contacto": {
        "email": "aurelio@gmail.com",
        "telefono": "123456789"
    }
}
print(persona["nombre"])                # Aurelio García
print(persona["hobbies"][1])            # Lectura: segundo elemento de la lista de hobbies
print(persona["contacto"]["telefono"])  # 123456789: clave del diccionario de contacto

# ============================================================
# 3. CONDICIONALES: VALIDAR UNA CONTRASEÑA
# ============================================================
# Ejercicio: según el número de caracteres de la contraseña se muestra un mensaje u otro.
# len() devuelve la longitud del texto; if/elif/else ejecuta solo el primer caso que se cumple.
contraseña = "mimamamemima"
longitud_minima = 8
longitud_maxima = 20
if len(contraseña) < longitud_minima:
    print(f"La contraseña es muy corta. Debe ser al menos {longitud_minima} caracteres.")
elif len(contraseña) > longitud_maxima:
    print(f"La contraseña es muy larga. No debe exceder {longitud_maxima} caracteres.")
else:
    print("La contraseña es válida. Contraseña aceptada.")

# ============================================================
# 4. BUCLE FOR
# ============================================================
# Un bucle repite un conjunto de instrucciones, como un coche que da varias vueltas a un circuito.
# for recorre uno a uno los elementos de una secuencia (una lista, un texto...):
# en cada repetición la variable toma el valor del siguiente elemento.
vueltas = [1, 2, 3, 4, 5, 6, 7, 8]
for vuelta in vueltas:
    print(f"Esta es la vuelta nº {vuelta}")

personas = ["PERSONA1", "PERSONA2", "PERSONA3", "PERSONA4"]
for persona in personas:
    print(persona)

# Ejercicio: mostrar por consola el nombre de cada color
colores = ["rojo", "verde", "azul", "amarillo"]
for color in colores:
    print(color)

# ============================================================
# 5. BUCLE WHILE
# ============================================================
# while repite el bloque mientras la condición sea True. Dentro del bucle hay que cambiar algo
# (por ejemplo, sumar 1 a un contador) para que la condición acabe siendo False;
# si no, el bucle no termina nunca.
contador = 0  # empieza en 0 porque es el índice del primer elemento de la lista
while contador < 5:
    print(f"Estoy en la vuelta {vueltas[contador]}")
    contador += 1  # suma 1 en cada vuelta

# Ejercicio: contar del 7 al 11
num = 7
while num <= 11:
    print(num)
    num += 1

# Ejercicio: un while dentro de otro (bucles anidados) para mostrar una cuenta atrás en triángulo:
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
num = 5
while num > 0:
    fila = ""  # texto de la fila actual (mejor no llamarlo sum, que es una función de Python)
    nuevo_num = num
    while nuevo_num > 0:  # el bucle interior construye la fila de nuevo_num hasta 1
        fila += f"{nuevo_num} "
        nuevo_num -= 1
    print(fila)
    num -= 1  # el bucle exterior pasa a la fila siguiente, que empieza un número más abajo

# Ejercicio: mostrar los números entre 150 y 350 divisibles a la vez entre 5 y 7.
# % devuelve el resto de la división: si el resto es 0, el número es divisible.
numero = 150
while numero <= 350:
    if (numero % 5 == 0) and (numero % 7 == 0):
        print(numero)  # 175, 210, 245, 280, 315, 350
    numero += 1

# ============================================================
# 6. EJERCICIO: RECORRER UNA LISTA DE DICCIONARIOS
# ============================================================
productos = [
    {"nombre": "Laptop", "categoria": "Electrónica", "precio": 799.99, "stock": 25},
    {"nombre": "Auriculares Bluetooth", "categoria": "Accesorios", "precio": 59.99, "stock": 50},
    {"nombre": "Cámara Digital", "categoria": "Fotografía", "precio": 399.99, "stock": 10},
    {"nombre": "Smartwatch", "categoria": "Relojes", "precio": 149.99, "stock": 75},
    {"nombre": "Teclado Mecánico", "categoria": "Accesorios", "precio": 89.99, "stock": 30}
]

# 1. Nombre de cada producto con for: en cada vuelta, producto es uno de los diccionarios
for producto in productos:
    print(producto["nombre"])

# 2. Nombre de los 3 primeros productos con while, usando el contador como índice
i = 0
while i < 3:
    print(productos[i]["nombre"])
    i += 1

# 3. Nombre de los productos cuyo precio es mayor que 100
for producto in productos:
    if producto["precio"] > 100:
        print(producto["nombre"])

# 4. Nombre de los productos cuyo stock es menor o igual que 25
for producto in productos:
    if producto["stock"] <= 25:
        print(producto["nombre"])

# ============================================================
# 7. FUNCIONES
# ============================================================
# Una función es un bloque de código reutilizable que hace una tarea concreta:
# puede recibir datos (parámetros), procesarlos y devolver un resultado.
# Se define con def, seguido del nombre, los parámetros entre paréntesis y dos puntos.
def suma(a, b):
    return a + b  # return termina la función y devuelve el valor a quien la llamó

print(suma(3, 5))  # 8: al llamar a la función, 3 y 5 son los argumentos

# Docstring: texto entre triples comillas justo debajo del def que explica qué hace la función.
# Se puede consultar con nombre_de_la_funcion.__doc__
# (aquí volvemos a definir suma, ahora con su docstring; la nueva versión sustituye a la anterior)
def suma(a, b):
    """Suma dos números."""
    return a + b

print(suma.__doc__)  # Suma dos números.

# Ejercicio: función que recibe un nombre y devuelve un saludo
def saludar(nombre):
    """Saluda a la persona con el nombre proporcionado."""
    return f"Hola, {nombre}!"

print(saludar("Aurelio"))  # Hola, Aurelio!

# Parámetro con valor por defecto y función con if:
# si no se pasa greeting se usa "Hello"; si name está vacío se devuelve solo el saludo.
# Un texto vacío ("") cuenta como False, así que not name es True cuando no hay nombre.
def greet(name, greeting="Hello"):
    if not name:
        return greeting
    else:
        return f"{greeting} {name}"

print(greet("Sofía"))          # Hello Sofía
print(greet("Sofía", "Hola"))  # Hola Sofía
print(greet(""))               # Hello

# ============================================================
# 8. EJERCICIOS DE FUNCIONES
# ============================================================
# Media de una lista de números: se suman todos con un for y se divide entre cuántos hay
def calcular_promedio(numeros):
    """Devuelve la media de una lista de números."""
    total = 0
    for numero in numeros:
        total += numero

    cantidad = len(numeros)

    return total / cantidad

print(calcular_promedio([4, 8, 6]))  # 6.0

# Función con varios parámetros que devuelve un mensaje con todos ellos
def presentarse(nombre, apellido, edad):
    """Devuelve un mensaje de presentación."""
    return f"Hola, me llamo {nombre} {apellido} y tengo {edad} años."

print(presentarse("Oscar", "Herreros", 23))

# Funciones que se usan dentro de otra operación: el valor devuelto se puede sumar y multiplicar
def area_cuadrado(lado):
    """Devuelve el área del cuadrado."""
    return lado * lado

def area_triangulo(base, altura):
    """Devuelve el área del triángulo."""
    return base * altura / 2

# Área total de un cuadrado de lado 10 y cinco triángulos de base 2 y altura 4
area_total = area_cuadrado(10) + 5 * area_triangulo(2, 4)
print(area_total)  # 120.0

# Ejercicio: contar los caracteres de un texto, comprobando antes que sea un string con type()
def cuentaCaracteres(cadena):
    """Cuenta la cantidad de caracteres en una cadena."""
    if type(cadena) == str:
        return len(cadena)
    else:
        return "Debo ser ejecutada con un string"

print(cuentaCaracteres("Hola, soy una cadena de texto"))  # 29
print(cuentaCaracteres(123))                              # Debo ser ejecutada con un string

# Último carácter de un texto: el índice -1 es la última posición
def ultimo_caracter(texto):
    """Devuelve el último carácter de un texto."""
    if type(texto) == str:
        return texto[-1]
    else:
        return "Debo ser ejecutada con un string"

print(ultimo_caracter("Python"))  # n

# Comparar dos números con if / elif / else y devolver un mensaje
def comparar(a, b):
    """Indica si dos números son iguales o cuál es mayor."""
    if a == b:
        return "Son iguales"
    elif a < b:
        return "El segundo es mayor"
    else:
        return "El primero es mayor"

print(comparar(3, 3))  # Son iguales
print(comparar(2, 9))  # El segundo es mayor
print(comparar(9, 2))  # El primero es mayor

# Contar cuántas veces aparece una letra en un texto.
# lower() pasa ambas a minúsculas para que "A" y "a" cuenten igual.
def contar_letra(texto, letra):
    """Cuenta cuántas veces aparece una letra en un texto, sin distinguir mayúsculas."""
    contador = 0
    for caracter in texto:
        if caracter.lower() == letra.lower():
            contador += 1
    return contador

print(contar_letra("Abracadabra", "a"))  # 5

# Cuenta atrás con while: muestra "Pum!" en los múltiplos de 4 y el número en el resto
def cuenta_atras(n):
    """Hace una cuenta atrás desde n hasta 1 y termina con un despegue."""
    while n > 0:
        if n % 4 == 0:
            print("Pum!")
        else:
            print(n)
        n -= 1
    print("¡Despegue!")

cuenta_atras(8)

# Parámetro opcional: si no se indica incidencia, vale False
def venta_online(pedido, fecha_entrega, incidencia=False):
    """Devuelve el mensaje para el cliente según haya o no incidencia."""
    if incidencia:
        return "Contacte con Att. Cliente"
    else:
        return f"Su pedido {pedido} se entregará el {fecha_entrega}"

print(venta_online(1234, "10/10/2026"))        # Su pedido 1234 se entregará el 10/10/2026
print(venta_online(1234, "10/10/2026", True))  # Contacte con Att. Cliente

# ============================================================
# 9. FUNCIONES LAMBDA
# ============================================================
# Una lambda es una función anónima (sin nombre propio) para operaciones cortas y simples:
#   lambda argumentos: expresión
# Solo puede tener una expresión, y su resultado es lo que devuelve (no hace falta return).
suma_lambda = lambda a, b: a + b
print(suma_lambda(3, 5))   # 8
print(type(suma_lambda))   # <class 'function'>: una lambda es una función como las demás

a_mayus = lambda texto: texto.upper()
print(a_mayus("sofía"))  # SOFÍA

# Ejercicio: obtener la primera letra de una palabra o texto
primeraLetra = lambda palabra: palabra[0]
print(primeraLetra("Hola"))  # H

# ============================================================
# 10. DEBUGGING
# ============================================================
# El debugger de VS Code pausa el programa para ver el valor de cada variable línea a línea,
# sin tener que llenar el código de print(). Es útil cuando no sabes dónde se rompe la lógica
# o cuando el código no da error pero no hace lo que esperas.
# 1. Pon un breakpoint haciendo clic a la izquierda del número de línea (aparece un punto rojo).
# 2. Abre Run and Debug (Ctrl + Shift + D) y pulsa F5 para empezar a depurar.
# 3. Avanza con los controles: continuar (F5), siguiente línea (F10),
#    entrar en la función (F11) y parar (Shift + F5).

# Ejercicio: ¿por qué fallaba este código?
# El primer usuario no tiene la clave "apellido", así que usuario["apellido"] daba
# KeyError: 'apellido' y el programa se paraba.
# Solución: usar get(), que devuelve un valor por defecto ("") cuando la clave no existe,
# y que la función solo añada el apellido cuando lo hay.
def obtener_nombre_completo(nombre, apellido=""):
    """Une nombre y apellido; si no hay apellido devuelve solo el nombre."""
    if apellido:
        return nombre + " " + apellido
    return nombre

def main():
    usuarios = [
        {"nombre": "Sofía"},
        {"nombre": "Luis", "apellido": "Martínez"},
    ]

    for usuario in usuarios:
        completo = obtener_nombre_completo(usuario["nombre"], usuario.get("apellido", ""))
        print(completo)

main()
