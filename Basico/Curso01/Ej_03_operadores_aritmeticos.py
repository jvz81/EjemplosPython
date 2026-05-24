#Los operadores aritmeticos basicos:
#Suma           +
#Resta          -
#multiplicar    *
#dividir        /

numero_1 = 8
numero_2 = 4
print('El operador + suma: ', numero_1 + numero_2)
print('El operador - resta: ', numero_1 - numero_2)
print('El operador * multiplica: ', numero_1 * numero_2)
print('El operador / divide: ', numero_1/numero_2)

#El operador resto % se utiliza para obtener el residuo de 
#una division

print('El residuo de 5 entre 2 es: ', 5%2)
print('El residuo de 4 entre 3 es: ', 4%3)
print('El residuo de 26 entre 3 es: ', 26%3)

#Para realizar la operacion de potencia se utiliza **
#3^4 = 81,  

print('El resultado de 3^4 es: ', 3**4)

#para obtener la parte entera de una division se utiliza
#el operador division de flor //

print('El resultado de 23/4 es: ',23/4)
print('La parte entera de 23/4 es: ',23//4)
print('El residuo o resto de 23/4 es: ',23%4)

#Los operadores aritmeticos (+ y *) se pueden utilizar con
#strings, el operador + une texto 
print('Hola '+'a '+'todos')  #muestra Hola a todos

#El operador * se puede utilizar para multiplicar varios
#textos
print('chau '*6)

#Si se quiere concatenar (+) un texto con una variable
#se tiene que convertir el valor de la variable en texto
#utilizando str()
resultado = 15
print('El resultado es: '+ str(resultado))

msg_salida = 'El resultado es: ' + str(resultado + 5)
print(msg_salida)