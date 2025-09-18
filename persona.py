def persona (nombre, dni, **masDatos):
    print("El nombre es: " + nombre)
    print("El DNI es:: " + dni)
    for variable in masDatos.keys():
        print("El/La ", variable, " es: " , masDatos[variable])

persona("Borja","17463292J", edad=16, altura=1.80, ocupado=True)