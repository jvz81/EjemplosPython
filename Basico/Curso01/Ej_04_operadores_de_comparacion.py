#Los operadores de comparacion entregan un resultado
#del tipo booleano 1(True) o 0 (False)
# A == B  se utiliza para evaluar si A es igual a B
# A != B  se utiliza para evaluar si A es diferente de B
# A > B  se utiliza para evaluar si A es mayor a B
# A < B  se utiliza para evaluar si A es menor a B
# A >= B  se utiliza para evaluar si A es mayor o igual a B
# A <= B  se utiliza para evaluar si A es menor o igual a B

dato_1 = 15
dato_2 = 10
dato_3 = 20
dato_4 = 20

print(dato_1 == dato_2)   #resultado False
print(dato_1 != dato_3)   #resultado True
print(dato_2 > dato_3)    #resultado False
print(dato_2 < dato_3)    #resultado True
print(dato_3 >= dato_4)   #resultado True
print(dato_3 <= dato_2)   #resultado False

#Los operadores de comparacion tambien se pueden utilizar
#con strings :
# == (igualdad) compara si dos strings son iguales
# != (desigualdad) compara si dos strings son diferentes
print("Hola" == "Hola")  # True
print("Hola" == "hola")  # False
print("Python" != "Java")  # True

# <, >, <=, >= (relacionales) comparan el orden alfabetico
#o lexicografico, letras en mayuscula estan 

print("ajo" < "banana")  # True (a va antes que b)
print("zebra" < "ajo")     # False (z va después que a)
print("Marta" >= "Marta")   # True 
print('nombre' > 'apellido') #true