opcion=100
i=0

print("Tiempo De Ciclistas")
print("1. Agregar Ciclista: ")
print("2. Mostrar Mayor Tiempo: ")
print("0. Salir")

ciclistas = []

ciclista = {}

tiempo = []


while opcion != 2:
    opcion = int(input("Digite la opcion que desee: "))
    if(opcion == 1):
        ciclista['nombre'] = input("Digite nombre de ciclista: ")
        ciclista['edad'] = input("Digite edad de ciclista: ")
        ciclista['pais'] = input("Digite pais de ciclista: ")
        ciclista['equipo'] = input("Digite equipo de ciclista: ")
        tiempo.append(int(input("Digite minutos recorridos: ")))
        ciclistas.insert(i, ciclista)
        i = i + 1

    
def ganador(tiempo):
    ganador = tiempo[0]
    for a in tiempo:
        if a < ganador:
            ganador = a
    return ganador
    
print(f"El ciclista mas rapido es {ciclista['nombre']} con un tiempo de: {tiempo} minutos")
