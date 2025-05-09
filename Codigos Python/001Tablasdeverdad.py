#Primero el usuario ingresara la compuerta que quiere ver
# Según la opción que elija, le mostrará la tabla de verdad.
# Al finalizar se le preguntará de nuevo al usuario si desea ver otra compuerta.

resultado = 0  # Variable donde guardaremos el resultado booleano(True o False)
opcion = "Si"  # Variable para poder comenzar el ciclo while

print() #Solo para que sean mas legibles
print("En pantalla mostraremos las variantes de las compuertas lógicas")

while opcion == "Si" or opcion == "si":
    print("")
    compuerta = input("Ingrese compuerta a saber (AND, OR, NOT, XOR, NAND, NOR) :")

    # Compuerta AND
    if compuerta.lower() == "and":
        
        print()
        print("Compuerta And: ")
        print("A  |  B  | AND")
        
        for a in range(0, 2):  # Ciclo para A = 0 y 1
            for b in range(0, 2): #Ciclo para B = 0 y 1
                resultado = a and b #Resultado booleano
            
                if resultado == 1:
                    print(f"{a}  |  {b}  | {resultado} verdadero")
                else:
                    print(f"{a}  |  {b}  | {resultado} falso")
        print()
        print("La compuerta AND solo será verdadera si ambas entradas son verdaderas")

    # Compuerta OR
    elif compuerta.lower() == "or":
        
        print()
        print("Compuerta OR:")
        print("A  |  B  | OR")
        
        for a in range(0, 2): #Ciclo para A
            for b in range(0, 2):#Ciclo para B
                resultado = a or b
                if resultado == 1:
                    print(f"{a}  |  {b}  | {resultado} verdadero")
                else:
                    print(f"{a}  |  {b}  | {resultado} falso")
        print("La compuerta OR será verdadera si al menos una de las entradas es verdadera")

    # Compuerta NOT
    elif compuerta.lower() == "not":
        
        print()
        print("Compuerta NOT:")
        print("A | NOT")
        
        for a in range(0, 2): #Ciclo para A
            resultado = not a
            print(f"{a} | {resultado}")
        print("Invierte el valor de la entrada, si a = 1, lo cambiará a 0")

    # Compuerta XOR
    elif compuerta.lower() == "xor":
        siw
        print()
        print("Compuerta XOR:")
        print("A | B | XOR")
        
        for a in range(0, 2):     #Ciclo para A
            for b in range(0, 2): #Ciclo para B
                resultado = int(a ^ b)
                if resultado == 1:
                    print(f"{a} | {b} | {resultado} verdadero")
                else:
                    print(f"{a} | {b} | {resultado} falso")
        print("La compuerta XOR será verdadera si las entradas son diferentes")

    # Compuerta NAND
    elif compuerta.lower() == "nand":
        
        print()
        print("Compuerta NAND:")
        print("A  |  B  | NAND")
        
        for a in range(0, 2): #Ciclo para A
            for b in range(0, 2): #Ciclo para B
                resultado = int(not (a and b))  # Convertimos a entero para mostrar 1 o 0, Se uso chat gpt para arreglar posible error
                if resultado == 1:
                    print(f"{a}  |  {b}  | {resultado} verdadero")
                else:
                    print(f"{a}  |  {b}  | {resultado} falso")
        print("Es igual que AND, pero negada")

    # Compuerta NOR
    elif compuerta.lower() == "nor":
        
        print()
        print("Compuerta NOR:")
        print("A  |  B  | NOR")
        
        for a in range(0, 2): #Ciclo para A
            for b in range(0, 2): #Ciclo para B
                resultado = int(not (a or b)) #Convertimos a entero, codigo mejorado por chatgpt
                if resultado == 1:
                    print(f"{a}  |  {b}  | {resultado} verdadero")
                else:
                    print(f"{a}  |  {b}  | {resultado} falso")
        print("Es igual que OR, pero negada")

    # Entrada no válida
    else:
        print()
        print("¡Error!, entrada no reconocida, tiene que ingresar 'AND, OR, XOR, NOT, NAND, NOR'.")
        # Mensaje de error si la entrada no es válida
    
    ##Opcion en donde al usuario se le pregunta si quiere volver a ingresar una compuerta nueva
    print()
    print("¿Quiere ingresar una compuerta nueva? (si / no)")
    opcion = input()

print("Finalizado.")