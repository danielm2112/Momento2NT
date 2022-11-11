numero1 = int(input("Digite el primer numero a agregar: "))
numero2 = int(input("Digite el segundo numero a agregar: "))

funcion= lambda numero1,numero2: 1 if numero1>numero2 else -1

calcular=funcion(numero1,numero2)

if calcular == 1:
    print("El primer número es mayor") 
else:
    print("El segundo número es mayor")