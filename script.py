#muestra solo valores únicos
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