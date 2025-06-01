# import tkinter

# root = tkinter.Tk()
# root.tittle('Mi Calculadora')
# root.geometry('400x500')
# root.config(bg = '#61dafb')
# label = tk.Label(root, text='Hola, Tkimter')

# label.pack()
# button = tk.Button(root, text='Click aquí')
# button.pack()

#Menú desplegable
# import tkinter as tk

# ventana = tk.Tk()
# ventana.title('Menú Desplegable')
# ventana.geometry('600x400')

# barra_menu = tk.Menu(ventana)
# ventana.config(menu=barra_menu)

# menu_principal = tk.Menu(barra_menu)
# barra_menu.add_cascade(label =
# 'Principal', menu = menu_principal)

# submenu = tk.Menu(menu_principal)
# menu_principal.add_cascade(label =
# 'Opciones', menu = submenu)
print('Ingrese las opciones del sub menpu, para salir presione cero:')
inicio = 1
lista = []
while inicio ==1:
    opcion = input('Ingrese lista de opciones')
    if opcion !=0:
        lista.append(opcion)
        print(lista)
    else:
        inicio=opcion
        break
print(lista)
# for i in lista:
#     submenu.add_command(label = i)

# ventana.mainloop()
