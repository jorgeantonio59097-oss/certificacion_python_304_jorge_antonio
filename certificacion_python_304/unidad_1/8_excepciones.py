#ejemplo 1 sin manejo de excepciones
numero1=float(input("ingresa el primer numero"))
numero2=float(input("ingresa el segundo numero"))
try:
    numero1=10
    numero2=2
    resultado=numero1/numero2
    print(resultado)
except ZeroDivisionError:
    print("error:no se puede dividir cero")
except ValueError:
    print("error:no se puede dividir cero")