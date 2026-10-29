tabla= [
    ["nombre","edad","calificacion"],
    ["jesus",16,7.0],
    ["melisa",16,9.0],
    ["sherlin",15,7.0],
    ["mariel",16,8.0],
    ["ximena",16,6.0],
    ["cintia",16,9.0],
    ["oscar",16,8.0],
    ["carlos",16,7.0],
    ["valeria",16,6.0],
    ["dulce",16,8.0]
]

filas=len(tabla)
columnas=len(tabla[0])
buscar_alumno = input("ingresa el nombre del alumno:")
for i in range(filas):
        for j in range(columnas):
                if j == 0 and tabla[i][j] == buscar_alumno:
                    print(f"alumno encontrado en la posision =[{i}][{j}]")