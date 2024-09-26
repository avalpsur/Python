
# 1.Imprime "Hola, mundo!" en la pantalla. 
# print("Hola Mundo")
'''
2. Calcula la suma de dos números ingresados por el usuario. 

num1=int(input("Introduzca el primer valor"))
num2=int(input("Introduzca el segundo valor"))

res=num1+num2

print("La suma de "+str(num1)+" y "+str(num2)+" es "+str(res))
'''

'''
3. Calcula el área de un triángulo con la fórmula: Área = (base * altura) / 2. 


base=int(input("Introduzca la base"))
altura=int(input("Introduzca la altura"))

area=(base*altura)/2

print("El área del triángulo con base "+str(base)+" y altura "+str(altura)+" es "+str(area))
'''

'''
4.Convierte grados Celsius a Fahrenheit

celsius=int(input("Introduzca los grados Celsius"))
fahr=(celsius*9/5)+32

input(str(celsius)+" grados Celsius son "+str(fahr)+" grados Fahrenheit")
'''
'''
5.Calcula el factorial de un número.


num=int(input("Introduzca un valor"))
mul=1
for i in range(1,num+1):
    mul*=i
    print(mul)
print("El factorial de ",num," es ",mul)
'''

'''
6. Verifica si un número es par o impar. 

num=int(input("Introduzca un valor"))
if num%2==0:
    print("Es par")
else:
    print("Es impar")

'''

'''
7. Calcula el MCD de dos números

num1=int(input("Introduzca el primer valor"))
num2=int(input("Introduzca el segundo valor"))


if num2<num1:
    aux=num2
    num2=num1
    num1=aux

for i in range(1,num1+1):
    if (num1%i==0)&(num2%i==0):
        mcd=i
    
print("El MCD de ",num1," y ",num2," es ",mcd)

'''

''' 8. Imprime los números del 1 al 10 usando un for

for i in range(1,10+1):
    print(i)
    
'''
'''
9. Calcula la suma de los 100 primeros números
sum=0
for i in range(1,100+1):
    sum+=i
print(sum)
'''

'''
10. Crea una lista de números y calcula su promedio.

sum=0
lista = [4,5,6,9]
for i in lista:
    sum+=i
media=sum/len(lista)

print("La media es igual a ",media)

'''