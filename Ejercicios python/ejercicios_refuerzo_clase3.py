# -*- coding: utf-8 -*-
"""Ejercicios-refuerzo-clase3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q1Q9RE1Sxxxc4APn5kTQSo7NkieJXEnA

**Ejercicio 1**

Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas, el vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.
"""

Sueldo_B= float(input("Digite su sueldo base: "))
venta1= float (input("Ingrese el valor de la primera venta: "))
venta2= float (input("Ingrese el valor de la segunda venta: "))
venta3= float (input("Ingrese el valor de la tercera venta: "))
Ventas= venta1 + venta2 + venta3
Comision= Ventas * 0.10
print("La comision de las tres ventas es= {}".format(Comision))
print("Su sueldo final es de: {}".format(Comision + Sueldo_B))

"""**Ejercicio 2**

Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuánto deberá pagar finalmente por su compra.
"""

Compra= float(input("Digite el total de la compra: "))
Descuento= Compra * 0.15
Total= Compra - Descuento
print("El total a pagar es $: {}".format(Total))

"""**Ejercicio 4**
Un maestro desea saber qué porcentaje de hombres y que porcentaje de mujeres hay en un grupo de estudiantes.
"""

Mujer= int (input("Digite el numero de mujeres que hay en el grupo: "))
Hombre= int (input("Digite el numero de hombres que hay en el grupo: "))
Grupo= Mujer + Hombre
P_M= Mujer/Grupo*100
P_H= Hombre/Grupo*100
print("Las Mujeres tienen un porcentaje del:{}".format(P_M))
print("Los Hombres tienen un porcentaje del:{}".format(P_H))