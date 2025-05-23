def calculadora():
    print('Operaciones disponibles: 1-Suma, 2-Resta, 3-Multiplicación, 4-División')
    operacion = int(input('Ingrese la operación que desea realizar, o cero para termina:'))
    while True:
        if operacion == 1:
            suma()
            break
        elif operacion == 2:
            resta()
            break
        elif operacion == 3:
            multiplicacion()
            break
        elif operacion == 4:
            division()
            break
        elif operacion == 0:
            break
        else:
            print('opción inválida. Ingrese nuevamente una opción')

def suma():
    numerouno = int(input('Ingrese el primer número para la suma:'))
    numerodos = int(input('Ingrese el segundo número para la suma:'))
    suma = numerouno + numerodos
    print('El resultado de la suma es;', suma)

def resta():
    numerouno = int(input('Ingrese el primer número para la resta:'))
    numerodos = int(input('Ingrese el segundo número para la resta:'))
    resta = numerouno - numerodos
    print('El resultado de la resta es;', resta)

def multiplicacion():
    numerouno = int(input('Ingrese el primer número para la multiplicación:'))
    numerodos = int(input('Ingrese el segundo número para la multiplicación:'))
    multiplicacion = numerouno * numerodos
    print('El resultado de la multiplicación es;', multiplicacion)

def division():
    numerouno = int(input('Ingrese el primer número para la división:'))
    numerodos = int(input('Ingrese el segundo número para la división:'))
    division = numerouno / numerodos
    print('El resultado de la división es;', division)

calculadora()
