# #muestra solo valores únicos
numeros_set = {1,2,2,3,4,5,5,5}
print(numeros_set)

persona= {
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
print(persona["nombre"])
print(persona["hobbies"][1])
print(persona["contacto"]["telefono"])

contraseña = "mimamamemima"
longitud_minima = 8
longitud_maxima = 20
if len(contraseña) < longitud_minima:
    print(f"La contraseña es muy corta. Debe ser al menos {longitud_minima} caracteres.")
elif len(contraseña) > longitud_maxima:
    print(f"La contraseña es muy larga. No debe exceder {longitud_maxima} caracteres.")
else:
    print("La contraseña es válida. Contraseña aceptada.")

personas = ["PERSONA1", "PERSONA2", "PERSONA3", "PERSONA4"]
for persona in personas:
    print(persona)

colores = ["rojo", "verde", "azul", "amarillo"]
for color in colores:
    print(color)

num = 7
while num <= 11:
    print(num)
    num += 1

num = 5
while num > 0:
    sum = ""
    nuevo_num = num
    while nuevo_num > 0:
        sum += f"{nuevo_num} "
        nuevo_num -= 1
    print(sum)
    num -= 1

numero = 150
# Escribe el while aquí
while numero <= 350:
    if (numero % 5 == 0) and (numero % 7 == 0):
        print(numero)
    numero += 1

def suma(a,b):
    return a + b

print(suma(3,5))

def suma(a,b):
    """Suma dos números."""
    return a + b

print(suma.__doc__)

def saludar (nombre):
    """Saluda a la persona con el nombre proporcionado."""
    return f"Hola, {nombre}!"
print(saludar("Aurelio"))

def calcular_promedio(numeros):
    total = 0
    # Completa el bucle y el return
    for numero in numeros:
        total += numero

    cantidad = len(numeros)

    return total/cantidad

def presentarse(nombre, apellido, edad):
    # Devuelve el mensaje
    return(f"Hola, me llamo {nombre} {apellido} y tengo {edad} años.")

def area_cuadrado(lado):
    # Escribe el docstring y el return
    """Devuelve el area del cuadrado"""
    return lado * lado

def area_triangulo(base, altura):
    # Escribe el docstring y el return
    """Devuelve el area del triangulo"""
    return base * altura /2

# Calcula area_total
area_total = area_cuadrado(10) + 5 * area_triangulo(2,4)
print(area_total)

def cuentaCaracteres(cadena):
    """Cuenta la cantidad de caracteres en una cadena."""
    if type(cadena) == str:
        return len(cadena)
    else:
        return "Debo ser ejecutada con un string"

print(cuentaCaracteres("Hola, soy una cadena de texto"))

def ultimo_caracter(texto):
    # tu código aquí
    if type(texto) == str:
        return texto[-1]
    else:
        return "Debo ser ejecutada con un string"

def comparar(a,b):
    if a == b:
        return "Son iguales"
    elif a < b:
        return "El segundo es mayor"
    else:
        return "El primero es mayor"

def contar_letra(texto,letra):
    contador = 0
    for caracter in texto:
        if caracter.lower() == letra.lower():
            contador += 1
    return contador

def cuenta_atras(n):
    # Escribe el while con su condición
    while n > 0:
        if n % 4 == 0:
            print("Pum!")
        else:
            print(n)
        n -= 1
    print("¡Despegue!")
cuenta_atras(8)

def venta_online(pedido, fecha_entrega, incidencia=False):
    # Devuelve el mensaje según la incidencia
    if incidencia:
        return "Contacte con Att. Cliente"
    else:
        return f"Su pedido {pedido} se entregará el {fecha_entrega}"