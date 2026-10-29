#creando un diccionario
persona={
    "nombre":"jorge",
    "edad":16,
    "profecion":"ingeniero",
    "estudiante":True
}
print(persona)
#accediendo a un valor en especifico
print(persona["nombre"])
#se pude usar el metodo get()
#es util porque no marca error si el valor no existe
print(persona.get("profeciomn"))
#modificar el valor existente
persona["edad"]=16
print(persona["edad"])   
#agregar un par(clave:valor)
persona["ciudad"]="san pepe ranch"
print(persona)
#recorrer un diccionario con un bucle