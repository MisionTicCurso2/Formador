numero1 = 15
numero2 = 16
resultado = 0

resultado = numero1 + numero2

print("La suma es:", resultado) 


numer3 = 6.7
decimal = 74.9879987987987986
d = 8.8
resultadoDecimal = 0.0

resultadoDecimal = numer3 + decimal
print("La suma de los decimales es", resultadoDecimal)


character = 'a'
a = 'a'
letraDeNumero = '1'

print("Caracter", letraDeNumero)


mi_Nombre = "Cristian Palta"
mi_Cuidad = "Popayan"
presentacion = "Hola. soy cristian, soy ingeniero y vivo en Popayan"

print(mi_Nombre)
print(presentacion)
print("Que mas", mi_Nombre, 'eres de', mi_Cuidad)


plata = 45

#Operador igual

if plata == 45:
    print("Gracias por su compra")
else:
    print("Uy la plata no te alcanzo")

edad = 17
#Operado diferente
if edad != 18:
    print("Uy ud es menor de edad")
else:
    print("Bienvenido a la rumba")


#Operador mayor
edad2 = 17
if (edad2 > 18):
    print("Siga a la rumba")
else: 
    print("Lo siento pero no puedes entrar")


#Operador mayor o igual
edad3 = 16
if(edad3 >= 18):
    print("La rumba apenas inicio. Bienvenido")
else:
    print("No que pena vuelve dentro de un ano o mas")



#### Condiciones doble
numeroLeido = 25

if(numeroLeido > 10 and numeroLeido < 35):
    print("El numero leido si cumple con lo requerido")
else:
    print("El numero leido no cumple con la condicion")


#La discoteca deja entrar jovenes mayores o iguales que 18 y que vistan de ropa es de color negro

edad4 = 18
ropa = 'verde'

# and | & &&

if(edad4 >= 18 and ropa == 'negro'):
    print("Sigue, gracias por venir")
else:
    print("Amigo no puedes entar :C")



##Operador o

# or - |  || 
if(edad4 >= 18 or ropa == 'negro'):
    print("Sigue, gracias por venir .......")
else:
    print("Amigo no puedes entar :C .......")


# #mensajes hacia la maquina
# print("Hola, calculo tu edad. Porfavor ingresa tu ano de nacimiento")
# mensaje_Entrante = input()
# fechaActual = 2021
# resEdad =  fechaActual - int(mensaje_Entrante)
# print("Su edad es", resEdad)

# print("Hola, escribe tu peso")
# mensaje_Entrante = input()
# peso_ideal = 40.5
# resPeso =  float(mensaje_Entrante) - peso_ideal
# print("Su sobre pes es", resPeso)


print("Hola, te elevo cualquier numero a la 2")
mensaje_Entrante = input()
resElevado =  int(mensaje_Entrante) ** 2
print("El numero elevado de", mensaje_Entrante, "es", resElevado)

