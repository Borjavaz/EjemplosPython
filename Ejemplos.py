# Comentario de una sola línea!!

"""
Comentario
de varias
líneas
"""

# Variables de diferentes tipos!!
nombre = "Juan"       # String (texto)
edad = 25             # Entero (int)
altura = 1.75         # Decimal (float)
es_estudiante = True  # Booleano (True o False)

# Imprimir valores!!
print(nombre, edad, altura, es_estudiante)

# Matemáticos!!
suma = 10 + 5      # 15
resta = 10 - 5     # 5
multiplicacion = 10 * 5  # 50
division = 10 / 3  # 3.333...
division_entera = 10 // 3  # 3
modulo = 10 % 3    # 1 (resto)
potencia = 2 ** 3  # 8

# Comparación!!
print(5 > 3)    # True
print(5 == 3)   # False
print(5 != 3)   # True

# Lógicos!!
print(True and False)  # False
print(True or False)   # True
print(not True)        # False


# Crear lista!!
frutas = ["manzana", "banana", "naranja"]

# Acceder a elementos
print(frutas[0])  # manzana
print(frutas[-1]) # naranja (último elemento)

# Modificar valores
frutas[1] = "pera"
print(frutas)  # ['manzana', 'pera', 'naranja']

# Agregar elementos
frutas.append("uva")

# Eliminar elementos
frutas.remove("pera")  # Elimina por valor
frutas.pop(0)          # Elimina por índice

# Recorrer lista
for fruta in frutas:
    print(fruta)

# Condicionales (if, elif, else)!!
edad = 18

if edad >= 18:
    print("Eres mayor de edad")
elif edad >= 13:
    print("Eres adolescente")
else:
    print("Eres menor de edad")

# Bucles (while y for)!!
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1

# Recorrer una lista
nombres = ["Ana", "Luis", "Pedro"]
for nombre in nombres:
    print(nombre)

# Usando range()
for i in range(5):  # 0,1,2,3,4
    print(i)

# Funciones !!
def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Carlos")
saludar("María")


# Diccionarios !!
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Acceder
print(persona["nombre"])  # Juan

# Agregar un nuevo valor
persona["profesion"] = "Ingeniero"

# Recorrer
for clave, valor in persona.items():
    print(clave, ":", valor)


# Manejo de errores (try-except) ""
try:
    numero = int(input("Ingresa un número: "))
    print("El doble es:", numero * 2)
except ValueError:
    print("Error: Debes ingresar un número válido")


# Importar modulos ""
import math

print(math.sqrt(16))  # Raíz cuadrada = 4.0

"""
Listas
"""

# Listas

l = [23, 25.4, 3 +4j, -15,[23,3,34.5],"unha cadea"]
print(type(l))
print(l[-2])