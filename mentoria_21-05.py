'''Divisibles por 3 y 5: Imprime los números del 1 al 30. Si un número es divisible por 3, imprime "Fizz". 
Si es divisible por 5, imprime "Buzz". Si es divisible por ambos (3 y 5), imprime "FizzBuzz". 
Si no es divisible por ninguno, imprime el número.'''

# for i in range (1,31):
#     if i%3 == 0:
#         if i%5 == 0:
#             print('FizzBuzz')
#         else:
#             print('Fizz')

#     elif i%5 == 0:
#         print('Buzz')
#     else:
#         print(f'{i}')

'''Pirámide de asteriscos: Imprime una pirámide de asteriscos de 5 filas. 
La primera fila tendrá 1 asterisco, la segunda 2, y así sucesivamente. 
(Usa bucles anidados, si es necesario).
         *        
        * *
       * * *
      * * * *
     * * * * * '''

#Nivel 1 pirámide de astericos isoceles

# filas =int(input('Ingrese el número de filas que tendrá sú pirámide:')) # pedimos ingreso del número de filas que tendrá la pirámide.
# for i in range (filas):                                                 #aplicamos un bucle for en un rango igual al número de filas.
#     print('*'*(i +1))                                                   #imprimimos tantos asteriscos cómo número de fila. 


# #Nivel 2 Pirámide de asteriscos, sin espacios entre los asteriscos. 
# filas =int(input('Ingrese el número de filas que tendrá sú pirámide:'))
# for i in range (filas):
#     print(' '*(filas-i-1)+('*'*(i*2+1)))
    

#Nivel 3 Pirámide de asteríscos, con la cantidad de asteriscos igual a la fila
filas =int(input('Ingrese el número de filas que tendrá sú pirámide:'))
for i in range (filas):
    print(' '*(filas-i-1)+('* '*(i +1)))