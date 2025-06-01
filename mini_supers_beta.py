import tkinter as tk
from tkinter import ttk, messagebox, Button

# Creamos la ventanita
ventana = tk.Tk()
ventana.title('MiniSupers')
ventana.geometry('600x500')

# Esto es el menú de arriba
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

menu_productos = tk.Menu(barra_menu, tearoff=0)
menu_productos.add_command(label="Ver productos")

menu_info = tk.Menu(barra_menu, tearoff=0)
menu_info.add_command(label="Quiénes somos")

barra_menu.add_cascade(label="Productos", menu=menu_productos)
barra_menu.add_cascade(label="Quiénes somos", menu=menu_info)

# Este es el lugar donde va la tabla que muestra los productos
frame_tabla = tk.Frame(ventana)
frame_tabla.pack(expand=True, fill=tk.BOTH, padx= 8, pady=5)

# Barra para pueder bajar y ver mas cosas si hay muchas
scroll = ttk.Scrollbar(frame_tabla, orient=tk.VERTICAL)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

# Con esto decimos que la tabla va a tener 4 columnas
detalle_productos = ('nombre', 'precio', 'producto', 'seleccionado')
tabla = ttk.Treeview(frame_tabla, columns=detalle_productos, show='headings', yscrollcommand=scroll.set)
#defino la función carga nuevo producro

def carga_nuevo_producto(tabla, nuevo_nombre, nuevo_precio, nuevo_producto):
    tabla.insert(
        "",
        tk.END,
        values=(nuevo_nombre, nuevo_precio, nuevo_producto, ""),
    )

def alternar_check(event):
    item_id = tabla.identify_row(event.y)
    col = tabla.identify_column(event.x)
    if not item_id or col != '#4':  # '#4' es la columna "seleccionado"
        return
    valores = list(tabla.item(item_id, "values"))
    valores[3] = "" if valores[3] == "✓" else "✓"
    tabla.item(item_id, values=valores)
    

tabla.bind("<Double-1>", alternar_check)


#Ponemos nombre a las columnas 
tabla.heading('nombre', text='Nombre')
tabla.heading('precio', text='Precio')
tabla.heading('producto', text='Producto')
tabla.heading('seleccionado', text='✓')

# Esto es para darle un tamaño a cada columna
tabla.column('nombre', width=150)
tabla.column('precio', width=150)
tabla.column('producto', width=150)
tabla.column('seleccionado', width=50, anchor='center')

tabla.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
scroll.config(command=tabla.yview)

#Definimos la función eliminar seleccionados
def eliminar_seleccionados():
    for item in tabla.get_children():
        valores = tabla.item(item, "values")
        if len(valores) > 3 and valores[3] == "✓":
            mensaje = messagebox.askquestion('Advertencia',"Está seguro que quiere eliminar el item, S/N")
            if mensaje == "yes":
                tabla.delete(item)
            else:
               return
            
            

# Este es el botón para eliminar productos (todavía no hace nada...)
boton_eliminar = tk.Button(ventana, text="Eliminar", bg="#ffdddd", command=eliminar_seleccionados)
boton_eliminar.pack(pady=5)
''' definimos la función buscar en tabla, con un ciclo For. Con el método get_children(), que devuelve una tupla de identificadores 
de elementos, luego iteramos esa tupla con el ciclo for y compararamos los valores asociados al item con la consulta. Si son iguales,
seleccionamos el elemento del arból, con el método selection_add().
'''
def buscar_en_tabla(consulta):
    items = tabla.get_children()
    contador = 0
    tabla.selection_remove(items)
    for item in items:  
        if consulta.lower() in str(tabla.item(item)['values']).lower():
            tabla.selection_add(item)
            tabla.focus(item)
            contador +=1
            pass
    if contador == 0:
        messagebox.showinfo("Buscar", f"No encontró resultados para '{consulta}'.")

# entrada de busqueda
buscar_entrada= ttk.Entry(ventana)
buscar_entrada.pack(side=tk.TOP, padx=10, pady=5)

# Boton de busqueda
busqueda_button = ttk.Button(ventana, text="Buscar", command=lambda: buscar_en_tabla(buscar_entrada.get()))
busqueda_button.pack(side=tk.TOP, padx=10, pady=5)

# (Frame = Caja) Aquí va la parte de abajo donde escribís los datos
frame_ingreso = tk.Frame(ventana)
frame_ingreso.pack(fill=tk.X, side=tk.BOTTOM, padx=10, pady=10)#(pack es el metodo que coloca la caja en la ventana)

# (Frame = Caja) Aquí va la parte de abajo donde escribís los datos
frame_ingreso = tk.Frame(ventana)
frame_ingreso.pack(fill=tk.X, side=tk.BOTTOM, padx=10, pady=10)#(pack es el metodo que coloca la caja en la ventana)

# Estas son etiquetas de cada campo que hicimos
tk.Label(frame_ingreso, text="Nombre:").grid(row=0, column=0, sticky="w", padx=(10, 5))
tk.Label(frame_ingreso, text="Precio:").grid(row=0, column=1, sticky="w", padx=(10, 5))
tk.Label(frame_ingreso, text="Producto:").grid(row=0, column=2, sticky="w", padx=(0, 5))

# En esta parte creamos cajitas para escribir los datos que se van a ingersarr

entrada_nombre = tk.Entry(frame_ingreso, width=20)
entrada_nombre.grid(row=1, column=0, padx=(10, 5))


entrada_precio = tk.Entry(frame_ingreso, width=15)
entrada_precio.grid(row=1, column=1, padx=(10, 5))


entrada_producto = tk.Entry(frame_ingreso, width=20)
entrada_producto.grid(row=1, column=2, padx=(0, 5))

# Esto hace que la columna del botón no se expanda
frame_ingreso.grid_columnconfigure(3, weight=1)


# Este es un botón para agregar el producto, agregué una acción del botón con command, al presionar el botón llama a la función carga_nuevo_producto
boton_agregar = tk.Button(frame_ingreso, text="Agregar", bg="#ddffdd", command = lambda:carga_nuevo_producto(tabla, entrada_nombre.get(), entrada_precio.get(), entrada_producto.get()))
boton_agregar.grid(row=1, column=3, padx=(20, 0), sticky="e")

# Mostramos la ventana
ventana.mainloop()

