# -*- coding: utf-8 -*-
"""Taller1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WfyhML-IKD51V7f24s5cyQYjgG-MDc9p

1. No de Identificación, Nombres, Apellidos, Dirección, Teléfono, Edad, Estado Civil, Número de hijos, Estatura en centímetros, fecha de contratación (Día/mes/año), Sueldo básico, Días Laborados.

2. Dando continuidad con la primera entrega del proyecto, en esta oportunidad el estudiante debe realizar las siguientes validaciones utilizando la sentencia condicional IF.
- Si el empleado es mayor de 55 años disfrutará de un bono de prepensión correspondiente al 5% de su sueldo básico.
- Si el empleado es casado y tiene hijos se le otorgará un paseo cada diciembre
- Si el sueldo básico está entre 1000000 y 1500000 tendrá una comisión del 2% sobre el valor del sueldo; Si el sueldo básico está entre 1500001 y 2000000 tendrá una comisión del 5% sobre el valor del sueldo; para todos los demás casos no habrá comisión.
- Si el empleado trabajó más de 20 días al mes y su sueldo es menor a 1000000 tendrá derecho a un bono de alimentación.

3. aplicar ciclos
"""

#recolencion de datos por pantalla
No_identificacion= int(input("Digite su numero de identificacion: "))
Nombre_p= input("Digite el nombre: ")
Apellido= input("Digite los Apellidos: ")
Direccion= input("Digite la direccion: ")
Telefono= input("Digite el numero de contacto: ")
Edad= int(input("Digite la edad: "))
Estado_c= input("Digite su estado civil: ")
N_hijos= int(input("Digite su numero de Hijos: "))
Estatura= input("Digite la Estatura: ")
Fecha_c= input("Digite la fecha de contratacion: ")
Sueldo_b= float(input("Digite su sueldo: "))
Dias_l= int(input("Digite sus dias laborados: "))
#imprime datos por pantalla
print(" ")
print("identificacion:",No_identificacion)
print("Nombre:" +" "+ Nombre_p+" "+Apellido)
print("Direccion:" +" "+Direccion)
print("Telefono:" +" "+Telefono)
print("Edad:",Edad)
print("Estado Civil:",Estado_c)
print("Numero de hijos:",N_hijos)
print("Estatura:" +" "+Estatura)
print("Fecha de contratacion:" +" "+Fecha_c)
print("Sueldo Basico:",Sueldo_b)
print("Dias laborados:",Dias_l)
#validacion con condicionales
if Edad > 55:
    bono= Sueldo_b*0.05
    Total_s= bono + Sueldo_b
    print("\n Por ser mayor a 55 años obtuvo un bono de prepension del 5% de su sueldo que equivale a: ${:,.0f}".format(bono))
    print("\n Y Su saldo total con el bono es de: ${:,.0f}".format(Total_s))
else:
    print("\n No obtiene el bono de prepension por ser menor de 55 años")
#__________________________________________________________________________________

if Estado_c=="casado" and N_hijos > 0:
  print("\n Se gano un paseo en diciembre por estar casado y tener hijos ")

elif Estado_c=="casada" and N_hijos > 0:
  print("\n Se gano un paseo en diciembre por estar casada y tener hijos ")

else:
  print("\n No participa por que no cumple las dos condiciones de estar casado (a) y tener hijos")
#___________________________________________________________________________________
if Sueldo_b >=1000000 and Sueldo_b <=1500000:
  comision= Sueldo_b*0.02
  T_c=Sueldo_b + comision
  print("\n Su comision en base al sueldo es de: ${:,.0f}".format(comision))
  print("Y su sueldo total es de: ${:,.0f}".format(T_c))

elif Sueldo_b >=1500001 and Sueldo_b <= 2000000:
    comision= Sueldo_b*0.05
    T_c= Sueldo_b + comision
    print("\n Su comision en base al sueldo es de: ${:,.0f}".format(comision))
    print("Y su sueldo total es de: ${:,.0f}".format(T_c)) 

else:
  print("\n No hay comision porque no se encuentra entre los valores establecidos")
  #_______________________________________________________________________________

if Dias_l >20 and Sueldo_b < 1000000:
  print("\n Tiene derecho a un bono de alimentacion")
   print('\n')
else:
  print("\n No tiene derecho al bono de alimentacion")
  print('\n')

#************************************************************************************
# validacion con ciclos
pregunta= input("¿desea realizar una nueva consulta? ")

def validaraño(Edad):
  if Edad > 55:
    bono= Sueldo_b*0.05
    Total_s= bono + Sueldo_b
    print("\n Por ser mayor a 55 años obtuvo un bono de prepension del 5% de su sueldo que equivale a: ${:,.0f}".format(bono))
    print("\n Y Su saldo total con el bono es de: ${:,.0f}".format(Total_s))
    print('\n')
  else:
    print("\n No obtiene el bono de prepension por ser menor de 55 años")
    print('\n')
    
pregunta="si"
while pregunta == "si" or pregunta == "SI":
  print('\n')
  print("--consulta de la Edad actual--")
  print('\n')
  Edad= int(input("Digite la nueva edad: "))
  Sueldo_b= float(input("Digite su sueldo: "))
  validaraño(Edad)
  pregunta=input("¿Consultar con otra edad?")

print('\n')
print("--consulta de estado civil y numero de hijos--")
print('\n')
#************************************************************************

def validarec(Estado_c):
  if Estado_c=="casado" and N_hijos > 0:
    print("\n Se gano un paseo en diciembre por estar casado y tener hijos ")
    print('\n')

  elif Estado_c=="casada" and N_hijos > 0:
    print("\n Se gano un paseo en diciembre por estar casada y tener hijos ")
    print('\n')

  else:
    print("\n No participa por que no cumple las dos condiciones de estar casado (a) y tener hijos")
    print('\n')

pregunta="si"
while pregunta == "si" or pregunta == "SI":
  Estado_c= input("Digite el estado civil: ")
  N_hijos= int(input("Digite el numero de Hijos: "))
  validarec(Estado_c)
  pregunta=input("¿Consultar de nuevo el estado civil y su edad?")
#_______________________________________________________________________________________________
print('\n')
print("--consulta del salario para una comision--")
print('\n')
def validarsb(Sueldo_b): 
  if Sueldo_b >=1000000 and Sueldo_b <=1500000:
    comision= Sueldo_b*0.02
    T_c=Sueldo_b + comision
    print("\n Su comision en base al sueldo es de: ${:,.0f}".format(comision))
    print("Y su sueldo total es de: ${:,.0f}".format(T_c))
    print('\n')

  elif Sueldo_b >=1500001 and Sueldo_b <= 2000000:
      comision= Sueldo_b*0.05
      T_c= Sueldo_b + comision
      print("\n Su comision en base al sueldo es de: ${:,.0f}".format(comision))
      print("Y su sueldo total es de: ${:,.0f}".format(T_c)) 
      print('\n')

  else:
    print("\n No hay comision porque no se encuentra entre los valores establecidos")
    print('\n')

pregunta="si"
while pregunta == "si" or pregunta == "SI":
  Sueldo_b= float(input("Digite el sueldo: "))
  validarsb(Sueldo_b)
  pregunta=input("¿Consultar con otro sueldo para la comision?")
#_______________________________________________________________________________________________
print('\n')
print("--consulta de los dias laborados--")
print('\n')

def validardia(Dias_l):
  if Dias_l >20 and Sueldo_b < 1000000:
    print("\n Tiene derecho a un bono de alimentacion")
    print('\n')
  else:
    print("\n No tiene derecho al bono de alimentacion")
    print('\n')

pregunta="si"
while pregunta == "si" or pregunta == "SI":
  Sueldo_b= float(input("Digite su sueldo: "))
  Dias_l= int(input("Digite dias laborados: "))
  validardia(Dias_l)
  pregunta=input("¿Consultar de nuevo los dias laborados con el sueldo?")