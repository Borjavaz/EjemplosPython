# Definición de una función con dos parámetros
def nombre_de_la_funcion(parametro1, parametro2):
    """Instrucciones de la función que procesan los parámetros"""
    print(parametro1)
    print(parametro2)

# Llamadas a la función
nombre_de_la_funcion(3, "Hola")
nombre_de_la_funcion(parametro2=4.5, parametro1="Creo que era como se llamaba")


# Función con un parámetro y otro con valor por defecto
def repetir_mensaje(mensaje, veces=1):
    print(mensaje * veces)

# Llamadas a la función
repetir_mensaje("Hola", 5)
repetir_mensaje("Adios")


# Función con parámetros extra (usando *args)
def repetir_mensaje2(mensaje, veces=1, *masMensajes):
    print(mensaje * veces)
    for otroMensage in masMensajes:
        print(otroMensage * veces)

        repetir_mensaje("Hola", 4, "Chao", "Adeus", )
