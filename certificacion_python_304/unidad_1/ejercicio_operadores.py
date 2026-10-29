#realizar un programa que calcule
#la compra total, si la compra total
#es mayor de 2000 pesos me hagan un descuento
#del 10%
#datos de entrada
precio1=float(input("intriduce el precio del producto 1:"))
precio2=float(input("intriduce el precio del producto 2:"))
precio3=float(input("intriduce el precio del producto 3:"))
precio4=float(input("intriduce el precio del producto 4:"))
#proceso
total=precio1+precio2+precio3+precio4
if total>2000:
    total=(total-(total*.10))
    #total=(3000-(3000*.10)) total=2700
    print(total)
else:
    print("no tienes descuento")