try:
    numer1=float(input("ingresa el primer numero"))
    numer2=float(input("ingresa el segundo numero"))
    resultado=numer1/numer2
except ValueError:
    print("solo introduce numeros")
except ZeroDivisionError:
    print("division entre cero")
else:
    print("el resultado es", resultado)
finally:
    print("programa finalizado")