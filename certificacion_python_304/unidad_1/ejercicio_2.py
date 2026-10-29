try:
    alumnos=["jesus","darina","melisa","mariel","sherlyn"]
    calificaciones=[8,7,9,10,7]
    print(alumnos[1],"-",calificaciones[1])
    print(alumnos[3],"-",calificaciones[3])

except IndexError:
    print("indice incorrecto")