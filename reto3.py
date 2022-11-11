class Banco:
    def __init__(self,nombre, apellido,cedula, ciudad,numeroCuenta = 0, salario = 0):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.ciudad = ciudad
        self.numeroCuenta = numeroCuenta
        self.salario = salario

    def añadirCuenta(self):
        numberAccount = int(input(f"{self.nombre} Digita numero de cuenta: "))
        balance = int(input(f"{self.nombre} Digita saldo: ")) 

        self.numeroCuenta = numberAccount
        self.salario = balance
        print(f"Numero cuenta: {self.numeroCuenta}")
        print(f"salario: {self.salario}")

    def consultarCuenta (self):
        print(f"Tu consulta de saldo es : {self.salario}")

    def Retirar(self):
        retiro = int(input("para retirar 1 y consignar a tu saldo 2: "))

        if (retiro == 1):
            retirando = int(input("digitar monto del retiro: ")) 
            if(retirando > self.salario):
                print("no tienes suficiente dinero")
                retirando = int(input("digitar monto del retiro: "))
                self.salario - retirando 
                print(f"tu saldo es: {self.salario}")
            else:
                print(self.salario)

        if (retiro == 2):
            consignando = int(input("digitar monto a agregar: "))
            self.salario + consignando
            print(f"tu saldo es: {self.salario}")

cuentaBanco = Banco("daniel","mariaca","1000190898","Medellin")
cuentaBanco.añadirCuenta()
cuentaBanco.Retirar()