import random

'''piedra papel o tijera
1 = piedra
2 = papel
3 = tijera'''

def objeto_elegido(opcion):
    if opcion ==1:
        opcion = 'Piedra'
        return opcion
    if opcion ==2:
        opcion = 'Papel'
        return opcion
    else:
        opcion = 'Tijera'
        return opcion

def piedra_rompe_tijera(mano_maquina,mano_jugador):
    if objeto_elegido(mano_maquina)=='Tijera' and objeto_elegido(mano_jugador) == 'Piedra':
        return print(f'\n máquina eligio {objeto_elegido(mano_maquina)}, y usted eligió {objeto_elegido(mano_jugador)}, gana jugador! {objeto_elegido(mano_jugador)} rompe a {objeto_elegido(mano_maquina)} \n')
    elif objeto_elegido(mano_jugador)=='Tijera' and objeto_elegido(mano_maquina) == 'Piedra':
        return print(f'\n máquina eligio {objeto_elegido(mano_maquina)}, y usted eligió {objeto_elegido(mano_jugador)}, gana máquina! {objeto_elegido(mano_maquina)} rompe a {objeto_elegido(mano_jugador)} \n')


def papel_envuelve_piedra(mano_maquina, mano_jugador):
    if objeto_elegido(mano_maquina)=='Papel' and objeto_elegido(mano_jugador) == 'Piedra':
        return print(f'\n máquina eligio {objeto_elegido(mano_maquina)}, y usted eligió {objeto_elegido(mano_jugador)}, gana máquina! {objeto_elegido(mano_maquina)} envuelve a {objeto_elegido(mano_jugador)} \n')
    elif objeto_elegido(mano_jugador)=='Tijera' and objeto_elegido(mano_maquina) == 'Piedra':
        return print(f'\n máquina eligio {objeto_elegido(mano_maquina)}, y usted eligió {objeto_elegido(mano_jugador)}, gana jugador! {objeto_elegido(mano_jugador)} envuelve a {objeto_elegido(mano_maquina)} \n')

def tijera_corta_papel(mano_maquina, mano_jugador):
    if objeto_elegido(mano_maquina)=='Tijera' and objeto_elegido(mano_jugador) == 'Papel':
        return print(f'\n máquina eligio {objeto_elegido(mano_maquina)}, y usted eligió {objeto_elegido(mano_jugador)}, gana máquina! {objeto_elegido(mano_maquina)} corta a {objeto_elegido(mano_jugador)} \n')
    elif objeto_elegido(mano_jugador)=='Tijera' and objeto_elegido(mano_maquina) == 'Piedra':
        return print(f'\n máquina eligio {objeto_elegido(mano_maquina)}, y usted eligió {objeto_elegido(mano_jugador)}, gana jugador! {objeto_elegido(mano_jugador)} corta a {objeto_elegido(mano_maquina)} \n')

def jugar():
    mano_jugador = 0
    while mano_jugador != 4:
        print('''Para jugar al piedra, papel, tijera debera elegir su mano. \n Elegir su opción \n
                    1 - Piedra
                    2 - Papel
                    3 - Tijera 
                    4 - Dejar de jugar\n''') 
        try: 
            mano_jugador = int(input('Ingrese su opción elegida:'))
        except ValueError:
            print('\n la opción elegida no es un número, por favor elija nuevamente\n')
            mano_jugador = 0
            print('''Para jugar al piedra, papel, tijera deberá elegir su mano. \n Elegir su opción \n
                    1 - Piedra
                    2 - Papel
                    3 - Tijera 
                    4 - Dejar de jugar\n''')
            mano_jugador = int(input('Ingrese su opción elegida:'))
        finally:
            mano_maquina = random.randint(1,3)
                    
            if mano_jugador == mano_maquina:
                    print(f'\n máquina eligio {objeto_elegido(mano_maquina)}, y usted eligió {objeto_elegido(mano_jugador)}, hay empate!ambos eligieron {objeto_elegido(mano_jugador)} \n')
                        
            elif mano_jugador ==1:    
                if mano_maquina == 2:
                    papel_envuelve_piedra(mano_maquina, mano_jugador)
                else:
                    piedra_rompe_tijera(mano_maquina,mano_jugador)

            elif mano_jugador == 2:
                if mano_maquina == 1:
                    papel_envuelve_piedra(mano_maquina, mano_jugador)
                else:
                    tijera_corta_papel(mano_maquina, mano_jugador)

            elif mano_jugador == 3:
                if mano_maquina == 1:
                    piedra_rompe_tijera(mano_maquina,mano_jugador)
                            
                else:
                    tijera_corta_papel(mano_maquina, mano_jugador)
                            
            elif mano_jugador == 4:
                print('\n hasta pronto\n')
                break
            else:
                print('\n la opción elegida es incorrecta, por favor elija nuevamente\n')
    

jugar()