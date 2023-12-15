import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random

def iniciar_sesion():
    # Obtiene los valores ingresados en los campos de entrada
    email_ingresado = entrada_email2.get()
    contraseña_ingresada = entrada_contraseña2.get()

    # Verifica si el usuario y la contraseña coinciden con los almacenados
    if verificar_credenciales(email_ingresado, contraseña_ingresada):
        tk.messagebox.showinfo("Éxito", "Inicio de sesión exitoso.")
        cambiar_ventana(ventana_iniciar_sesion, ventana_principal)
    else:
        tk.messagebox.showerror("Error", "Usuario o contraseña incorrectos.")
def verificar_credenciales(email, contraseña):
    # Abre el archivo de usuarios y verifica las credenciales
    with open("usuarios.txt", "r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            # Separa la línea en elementos usando la coma como separador
            elementos = linea.strip().split(',')
            # Asegúrate de que haya al menos 2 elementos en la línea
            if len(elementos) >= 2:
                email_guardado = elementos[0].strip()
                contraseña_guardada = elementos[1].strip()
                # Compara las credenciales ingresadas con las almacenadas
                if email == email_guardado and contraseña == contraseña_guardada:
                    return True
    return False
def guardar_pedido():
    # Obtén los valores seleccionados de los combobox
    numero_mesa = combo.get()
    nombre_plato = combo2.get()

    # Verifica que ambos combobox tengan valores seleccionados
    if not numero_mesa or not nombre_plato:
        tk.messagebox.showerror("Error", "Por favor, seleccione una mesa y un plato.")
        return

    # Guarda la información en el archivo de pedidos
    with open("pedidos.txt", "a") as archivo:
        archivo.write(f"{numero_mesa},{nombre_plato}\n")
def leer_platos():
    platos = []
    with open("platos.txt", "r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            # Separa la línea en elementos usando la coma como separador
            elementos = linea.strip().split(',')
            # Asegúrate de que hay al menos 4 elementos
            if len(elementos) >= 4:
                nombre = elementos[0].strip()
                precio = elementos[1].strip()
                descripcion = elementos[2].strip()
                disponibilidad = elementos[3].strip()

                # Agrega la información a la lista de platos
                platos.append([nombre, precio, descripcion, disponibilidad])
    return platos
def leer_mesas():
    mesas = []
    with open("mesas.txt", "r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            # Separa la línea en elementos usando la coma como separador
            elementos = linea.strip().split(',')
            
            # Asegúrate de que hay al menos 3 elementos
            if len(elementos) >= 4:
                mumero_mesa = elementos[0].strip()
                fecha = elementos[1].strip()
                hora = elementos[2].strip()
                num_personas = elementos[3].strip()

                # Agrega la información a la lista de mesas
                mesas.append([mumero_mesa, fecha, hora, num_personas])

    return mesas
def numero_mesas():
    mesas = leer_mesas()
    numeros = []
    for mesa in mesas:
        numeros.append(mesa[0])
    return numeros
def nombre_platos():
    platos = leer_platos()
    nombres = []
    for plato in platos:
        nombres.append(plato[0])
    return nombres
def agregar_a_archivo_mesas():
    numero_mesa = random.randint(1,100)
    fecha = entry1m.get()
    hora = entry2m.get()
    num_personas = entry3m.get()

    # Verifica que todos los campos estén llenos antes de agregar al archivo
    if not fecha or not hora or not num_personas:
        tk.messagebox.showerror("Error", "Por favor, complete todos los campos.")
        return

    # Agrega los datos al archivo
    with open("mesas.txt", "a") as archivo:
        archivo.write(f"{numero_mesa}, {fecha},{hora}, {num_personas}\n")
def agregar_a_archivo():
    nombre = entry1p.get()
    precio = entry2p.get()
    descripcion = entry3p.get()
    disponibilidad = entry4p.get()

    if not nombre or not precio or not descripcion or not disponibilidad:
        tk.messagebox.showerror("Error", "Por favor, complete todos los campos.")
        return
    with open("platos.txt", "a") as archivo:
        archivo.write(f"{nombre},{precio},{descripcion},{disponibilidad}\n")
def guardar_credenciales(correo, contraseña):
    with open("usuarios.txt", "a") as archivo:
        archivo.write(f"{correo},{contraseña}\n")
def registrar_usuario():
    correo = entrada_email1.get()
    contraseña = entrada_contraseña.get()
    confirmar_contraseña = entrada_confirmar_c.get()

    if contraseña != confirmar_contraseña:
        tk.messagebox.showerror("Error", "Las contraseñas no coinciden. Inténtelo de nuevo.")
        return 
    
    dominios_validos = ["gmail.com", "hotmail.com", "yahoo.com", "outlook.com"]
    dominio = correo.split('@')[-1]

    if dominio not in dominios_validos:
        tk.messagebox.showerror("Error", "Por favor, ingrese un correo válido de los dominios permitidos.")
        return
    guardar_credenciales(correo, contraseña)

    tk.messagebox.showinfo("Registro exitoso", "Usuario registrado con éxito.")
    ventana_registro.withdraw()
def cambiar_ventana(ventana_actual, ventana_nueva):
    ventana_actual.withdraw()
    ventana_nueva.deiconify()



# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Interfaz del Proyecto
    
# Crear todas las ventanas

ventana_inicial = tk.Tk()
ventana_registro = tk.Tk()
ventana_registro.withdraw()
ventana_iniciar_sesion = tk.Tk()
ventana_iniciar_sesion.withdraw()
ventana_principal = tk.Tk()
ventana_principal.withdraw()
ventana_platos = tk.Tk()
ventana_platos.withdraw()
ventana_mesas = tk.Tk()
ventana_mesas.withdraw()
ventana_pedidos = tk.Tk()
ventana_pedidos.withdraw()
ventana_agregar_platos = tk.Tk()
ventana_agregar_platos.withdraw()
ventana_agregar_mesas = tk.Tk()
ventana_agregar_mesas.withdraw()
ventana_mostrar_platos = tk.Tk()
ventana_mostrar_platos.withdraw()
ventana_mostrar_pedido = tk.Tk()
ventana_mostrar_pedido.withdraw()
ventana_agregar_pedido = tk.Tk()
ventana_agregar_pedido.withdraw()

# Primera Ventana

ventana_inicial.title("Ventana Inicio")
ancho_pantalla = ventana_inicial.winfo_screenwidth()
alto_pantalla = ventana_inicial.winfo_screenheight()
ancho_ventana = 500
alto_ventana = 500
x_pos = int((ancho_pantalla - ancho_ventana) / 2)  
y_pos = int((alto_pantalla - alto_ventana) / 2)  

ventana_inicial.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")

ventana_inicial.config(bg="gray")
ventana_inicial.resizable(0, 0)



espacio1 = tk.Frame(ventana_inicial, width=1000, height=100)

texto1 = tk.Label(espacio1, text="Mi Restaurante", font=("Arial", 20, "bold"), fg="black")
texto1.pack(pady=10, padx=150)

texto2 = tk.Label(espacio1,
                text=" \n\n\nNuevo Restaurante es un lugar donde ofrecemos"
                + "\n una variedad de platos deliciosos y recursos"
                + "\n culinarios para el público para satisfacer tus"
                + "\n necesidades culinarias y hacerte disfrutar de una"
                + "\n experiencia gastronómica excepcional.\n\n\n", bg="white", font=("Arial", 10, "bold"))
texto2.pack(pady=10)

boton_registrar = tk.Button(espacio1, text="Registrar", bg="white", font=("Arial", 10, "bold"), width=15, command= lambda : (cambiar_ventana(ventana_inicial, ventana_registro)))
boton_registrar.pack(pady=20)

boton_iniciar_sesion = tk.Button(espacio1, text="Iniciar sesión", bg="white", font=("Arial", 10, "bold"),width=15, command= lambda : (cambiar_ventana(ventana_inicial, ventana_iniciar_sesion)))
boton_iniciar_sesion.pack(pady=1)

espacio1.pack()

espacio2 = tk.Frame(ventana_inicial, width=500, height=200, padx=10, pady=10)
espacio2.pack()

# Segunda Ventana

ventana_registro.title("Ventana Registro")
ancho_pantalla = ventana_registro.winfo_screenwidth()
alto_pantalla = ventana_registro.winfo_screenheight()
ancho_ventana = 500
alto_ventana = 500
x_pos = int((ancho_pantalla - ancho_ventana) / 2)  
y_pos = int((alto_pantalla - alto_ventana) / 2)  
ventana_registro.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")


ventana_registro.resizable(0, 0)


espacio3 = tk.Frame(ventana_registro, width=1000, height=100)

campo_registro = tk.Frame(espacio3, width=1000, height=100, padx=10, pady=10, bg="white")
texto_titulo = tk.Label(campo_registro, text="Registrarse", font=("Arial", 15, "bold"), fg="black", bg="white")
texto_titulo.pack(pady=10, padx=120)

texto_email = tk.Label(campo_registro, text="Email", font=("Arial", 10, "bold"), fg="black", bg="white")
texto_email.pack(pady=5, padx=30, anchor="w")

entrada_email1 = tk.Entry(campo_registro, width=30)
entrada_email1.pack(pady=10, padx=30)

texto_contraseña = tk.Label(campo_registro, text="Contraseña", font=("Arial", 10, "bold"), fg="black", bg="white")
texto_contraseña.pack(pady=5, padx=30, anchor="w")

entrada_contraseña = tk.Entry(campo_registro, width=30)
entrada_contraseña.pack(pady=10, padx=30)

texto_confirmar_c = tk.Label(campo_registro, text="Confirmar contraseña", font=("Arial", 10, "bold"), fg="black", bg="white")
texto_confirmar_c.pack(pady=5, padx=30, anchor="w")

entrada_confirmar_c = tk.Entry(campo_registro, width=30)
entrada_confirmar_c.pack(pady=10, padx=30)

boton_registrar = tk.Button(campo_registro, text="Registrar", bg="white", font=("Arial", 10, "bold"), width=15, command=lambda: (registrar_usuario(), cambiar_ventana(ventana_registro, ventana_inicial)))
boton_registrar.pack(pady=20)

campo_registro.pack(pady=10, padx=20)

espacio3.pack( pady=50)

espacio4 = tk.Frame(ventana_registro, width=500, height=200, padx=10, pady=10)
espacio4.pack()



# Tercera Ventana

ventana_iniciar_sesion.title("Ventana Iniciar Sesión")

ancho_pantalla = ventana_iniciar_sesion.winfo_screenwidth()
alto_pantalla = ventana_iniciar_sesion.winfo_screenheight()
ancho_ventana = 500
alto_ventana = 500
x_pos = int((ancho_pantalla - ancho_ventana) / 2)  
y_pos = int((alto_pantalla - alto_ventana) / 2)  
ventana_iniciar_sesion.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")

ventana_iniciar_sesion.resizable(0, 0)


espacio5 = tk.Frame(ventana_iniciar_sesion, width=1000, height=100)

campo_registro2 = tk.Frame(espacio5, width=1000, height=100, padx=10, pady=10, bg="white")
texto_titulo2 = tk.Label(campo_registro2, text="Iniciar Sesión", font=("Arial", 15, "bold"), fg="black", bg="white")
texto_titulo2.pack(pady=10, padx=120)

texto_email2 = tk.Label(campo_registro2, text="Email", font=("Arial", 10, "bold"), fg="black", bg="white")
texto_email2.pack(pady=5, padx=30, anchor="w")

entrada_email2 = tk.Entry(campo_registro2, width=30)
entrada_email2.pack(pady=10, padx=30)

texto_contraseña2 = tk.Label(campo_registro2, text="Contraseña", font=("Arial", 10, "bold"), fg="black", bg="white")
texto_contraseña2.pack(pady=5, padx=30, anchor="w")

entrada_contraseña2 = tk.Entry(campo_registro2, width=30)
entrada_contraseña2.pack(pady=10, padx=30)

boton_registrar2 = tk.Button(campo_registro2, text="Registrar", bg="white", font=("Arial", 10, "bold"), width=15, command=lambda: (iniciar_sesion()))
boton_registrar2.pack(pady=20)

campo_registro2.pack(pady=10, padx=20)

espacio5.pack(pady=80)

espacio6 = tk.Frame(ventana_iniciar_sesion, width=500, height=200, padx=10, pady=10)
espacio6.pack()



# Cuarta Ventana

ventana_principal.title("Ventana Principal")

ancho_pantalla = ventana_principal.winfo_screenwidth()
alto_pantalla = ventana_principal.winfo_screenheight()
ancho_ventana = 500
alto_ventana = 500
x_pos = int((ancho_pantalla - ancho_ventana) / 2)  
y_pos = int((alto_pantalla - alto_ventana) / 2)  
ventana_principal.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")

ventana_principal.resizable(0, 0)


espacio7 = tk.Frame(ventana_principal, width=2000, height=100)

campo_registro3 = tk.Frame(espacio7, width=1000, height=100, padx=10, pady=20, bg="white")
texto_titulo3 = tk.Label(campo_registro3, text="Bienvenido", font=("Arial", 20, "bold"), fg="black", bg="white")
texto_titulo3.pack(pady=10, padx=120)

boton_platos = tk.Button(campo_registro3, text="Gestión Platos", bg="white", font=("Arial", 10, "bold"), width=25, height=4, command=lambda:cambiar_ventana(ventana_principal, ventana_platos))
boton_platos.pack(pady=2)

boton_mesas = tk.Button(campo_registro3, text="Gestión Mesas", bg="white", font=("Arial", 10, "bold"), width=25, height=4, command=lambda: cambiar_ventana(ventana_principal, ventana_mesas))
boton_mesas.pack(pady=2)

boton_pedidos = tk.Button(campo_registro3, text="Gestión Pedidos", bg="white", font=("Arial", 10, "bold"), width=25, height=4, command=lambda: cambiar_ventana(ventana_principal, ventana_pedidos))
boton_pedidos.pack(pady=2)

boton_cerrar_sesion = tk.Button(campo_registro3, text="Cerrar Sesión", bg="white", font=("Arial", 10, "bold"), width=25, height=4, command=lambda: cambiar_ventana(ventana_principal, ventana_inicial))
boton_cerrar_sesion.pack(pady=2)

campo_registro3.pack(pady=10, padx=20)

espacio7.pack(pady=20)

espacio8 = tk.Frame(ventana_principal, width=500, height=100, padx=10, pady=10)
espacio8.pack()


# Quinta Ventana

ventana_platos.title("Gestion de Platos")

ancho_pantalla = ventana_platos.winfo_screenwidth()
alto_pantalla = ventana_platos.winfo_screenheight()
ancho_ventana = 500
alto_ventana = 500
x_pos = int((ancho_pantalla - ancho_ventana) / 2)  
y_pos = int((alto_pantalla - alto_ventana) / 2)  
ventana_platos.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")

ventana_platos.resizable(0, 0)

espacio9 = tk.Frame(ventana_platos, width=2000, height=100)

campo_registro4 = tk.Frame(espacio9, width=1000, height=100, padx=10, pady=20, bg="white")
texto_titulo4 = tk.Label(campo_registro4, text="Mi Restaurante", font=("Arial", 20, "bold"), fg="black", bg="white")
texto_titulo4.pack(pady=10, padx=120)

campo_platos = tk.Frame(espacio9, width=1000, height=100, padx=10, pady=20, bg="white")
texto_titulo5 = tk.Label(campo_platos, text="Gestion de Platos", font=("Arial", 12, "bold"), fg="black", bg="white")
texto_titulo5.pack(pady=10, padx=120)

boton_agregar = tk.Button(campo_platos, text="Agregar", bg="white", font=("Arial", 10, "bold"), width=25, height=4, command=lambda: cambiar_ventana(ventana_principal, ventana_agregar_platos))
boton_agregar.pack(pady=2)

boton_eliminar = tk.Button(campo_platos, text="Eliminar", bg="white", font=("Arial", 10, "bold"), width=25, height=4, command=lambda:cambiar_ventana(ventana_principal, ventana_mostrar_platos))
boton_eliminar.pack(pady=2)

boton_actualizar = tk.Button(campo_platos, text="Actualizar", bg="white", font=("Arial", 10, "bold"), width=25, height=4, command=lambda: cambiar_ventana(ventana_principal, ventana_mostrar_platos))
boton_actualizar.pack(pady=2)

campo_registro4.pack(pady=10, padx=20)
campo_platos.pack(pady=10, padx=20)

espacio9.pack(pady=20)

# Sextava Ventana

ventana_mesas.title("Gestion de Mesas") 

ancho_pantalla = ventana_mesas.winfo_screenwidth()
alto_pantalla = ventana_mesas.winfo_screenheight()
ancho_ventana = 500
alto_ventana = 500
x_pos = int((ancho_pantalla - ancho_ventana) / 2)  
y_pos = int((alto_pantalla - alto_ventana) / 2)  
ventana_mesas.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")


ventana_mesas.resizable(0, 0)

espacio11 = tk.Frame(ventana_mesas, width=2000, height=100)

campo_registro5 = tk.Frame(espacio11, width=1000, height=100, padx=10, pady=20, bg="white")
texto_titulo6 = tk.Label(campo_registro5, text="Mi Restaurante", font=("Arial", 20, "bold"), fg="black", bg="white")
texto_titulo6.pack(pady=10, padx=120)

campo_mesas = tk.Frame(espacio11, width=1000, height=100, padx=10, pady=20, bg="white")
texto_titulo5 = tk.Label(campo_mesas, text="Gestion de Mesas", font=("Arial", 12, "bold"), fg="black", bg="white")
texto_titulo5.pack(pady=10, padx=120)

boton_agregar = tk.Button(campo_mesas, text="Agregar", bg="white", font=("Arial", 10, "bold"), width=25, height=4, command=lambda: cambiar_ventana(ventana_mesas, ventana_agregar_mesas))
boton_agregar.pack(pady=2)

boton_eliminar = tk.Button(campo_mesas, text="Eliminar", bg="white", font=("Arial", 10, "bold"), width=25, height=4, command=lambda:  cambiar_ventana(ventana_mesas, ventana_agregar_mesas))
boton_eliminar.pack(pady=2)

boton_actualizar = tk.Button(campo_mesas, text="Actualizar", bg="white", font=("Arial", 10, "bold"), width=25, height=4, command=lambda:  cambiar_ventana(ventana_mesas, ventana_agregar_mesas))
boton_actualizar.pack(pady=2)

campo_registro5.pack(pady=10, padx=20)
campo_mesas.pack(pady=10, padx=20)

espacio11.pack(pady=20)

espacio12 = tk.Frame(ventana_mesas, width=500, height=100, padx=10, pady=10)
espacio12.pack()

# Septima Ventana

ventana_pedidos.title("Gestion de Mesas")

ancho_pantalla = ventana_pedidos.winfo_screenwidth()
alto_pantalla = ventana_pedidos.winfo_screenheight()
ancho_ventana = 500
alto_ventana = 500
x_pos = int((ancho_pantalla - ancho_ventana) / 2)  
y_pos = int((alto_pantalla - alto_ventana) / 2)  
ventana_pedidos.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")


ventana_pedidos.resizable(0, 0)

espacio13 = tk.Frame(ventana_pedidos, width=2000, height=100)

campo_registro6 = tk.Frame(espacio13, width=1000, height=100, padx=10, pady=20, bg="white")
texto_titulo7 = tk.Label(campo_registro6, text="Mi Restaurante", font=("Arial", 20, "bold"), fg="black", bg="white")
texto_titulo7.pack(pady=10, padx=120)

campo_pedidos = tk.Frame(espacio13, width=1000, height=100, padx=10, pady=20, bg="white")
texto_titulo8 = tk.Label(campo_pedidos, text="Gestion de Pedidos", font=("Arial", 12, "bold"), fg="black", bg="white")
texto_titulo8.pack(pady=10, padx=120)

boton_agregar = tk.Button(campo_pedidos, text="Agregar", bg="white", font=("Arial", 10, "bold"), width=25, height=4, command=lambda: cambiar_ventana(ventana_pedidos, ventana_agregar_pedido))
boton_agregar.pack(pady=2)

boton_eliminar = tk.Button(campo_pedidos, text="Eliminar", bg="white", font=("Arial", 10, "bold"), width=25, height=4, command=lambda:cambiar_ventana(ventana_pedidos, ventana_principal))
boton_eliminar.pack(pady=2)

boton_actualizar = tk.Button(campo_pedidos, text="Actualizar", bg="white", font=("Arial", 10, "bold"), width=25, height=4, command=lambda: cambiar_ventana(ventana_pedidos, ventana_principal))
boton_actualizar.pack(pady=2)

campo_registro6.pack(pady=10, padx=20)
campo_pedidos.pack(pady=10, padx=20)

espacio13.pack(pady=20)

espacio14 = tk.Frame(ventana_pedidos, width=500, height=100, padx=10, pady=10)
espacio14.pack()

 
ventana_agregar_platos.title("Gestion de Platos")

ancho_pantalla = ventana_agregar_platos.winfo_screenwidth()
alto_pantalla = ventana_agregar_platos.winfo_screenheight()
ancho_ventana = 500
alto_ventana = 550
x_pos = int((ancho_pantalla - ancho_ventana) / 2)  
y_pos = int((alto_pantalla - alto_ventana) / 2)  
ventana_agregar_platos.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")

ventana_agregar_platos.resizable(0, 0)


espacio = tk.Frame(ventana_agregar_platos, width=2000, height=100)

campo_registro = tk.Frame(espacio, width=1000, height=100, padx=10, pady=1, bg="white")
texto_titulo = tk.Label(campo_registro, text="Mi Restaurante", font=("Arial", 20, "bold"), fg="black", bg="white")
texto_titulo.pack(pady=10, padx=120)

campo_platos = tk.Frame(espacio, width=1000, height=100, padx=10, pady=20, bg="white")
texto_titulo2 = tk.Label(campo_platos, text="Agregar Platos", font=("Arial", 12, "bold"), fg="black", bg="white")
texto_titulo2.pack(pady=10, padx=120)
    
campo_datos = tk.Frame(espacio, width=1000, height=100, padx=10, pady=20, bg="gray")

datos = tk.Frame(campo_datos, width=1000, height=100, padx=10, pady=20, bg="gray")

texto1 = tk.Label(datos, text="Nombre", font=("Arial", 10, "bold"), fg="white", bg="gray")
entry1p = tk.Entry(datos, width=30)

texto2 = tk.Label(datos, text="Precio", font=("Arial", 10, "bold"), fg="white", bg="gray")
entry2p = tk.Entry(datos, width=30)

texto3 = tk.Label(datos, text="Descripción", font=("Arial", 10, "bold"), fg="white", bg="gray")
entry3p = tk.Entry(datos, width=30)

texto4 = tk.Label(datos, text="Disponibilidad", font=("Arial", 10, "bold"), fg="white", bg="gray")
entry4p = tk.Entry(datos, width=30)

texto1.grid(row=0, column=0, pady=5, padx=5, sticky="w")
entry1p.grid(row=1, column=0, pady=5, padx=5, sticky="w",ipadx=5, ipady=5)

texto2.grid(row=0, column=2, pady=5, padx=5, sticky="w")
entry2p.grid(row=1, column=2, pady=5, padx=5, sticky="w",ipadx=5, ipady=5)

texto3.grid(row=2, column=0, pady=5, padx=5, sticky="w")
entry3p.grid(row=3, column=0, pady=5, padx=5, sticky="w",ipadx=5, ipady=5)

texto4.grid(row=2, column=2, pady=5, padx=5, sticky="w")
entry4p.grid(row=3, column=2, pady=5, padx=5, sticky="w",ipadx=5, ipady=5)

datos.pack(pady=5, padx=10)
boton_agregar = tk.Button(campo_datos, text="Agregar", bg="white", font=("Arial", 10, "bold"), width=10, command=lambda:(cambiar_ventana(ventana_agregar_platos, ventana_principal),agregar_a_archivo()))
boton_agregar.pack(pady=10)

campo_registro.pack(pady=10, padx=20)
campo_platos.pack(pady=10, padx=20)
campo_datos.pack(pady=10, padx=20)

espacio.pack(pady=20)

espacio10 = tk.Frame(ventana_agregar_platos, width=500, height=100, padx=10, pady=10)
espacio10.pack()




# Octava Ventana

ventana_agregar_mesas.title("Gestion de Mesas")

ancho_pantalla = ventana_agregar_mesas.winfo_screenwidth()
alto_pantalla = ventana_agregar_mesas.winfo_screenheight()
ancho_ventana = 500
alto_ventana = 550
x_pos = int((ancho_pantalla - ancho_ventana) / 2)  
y_pos = int((alto_pantalla - alto_ventana) / 2)  
ventana_agregar_mesas.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")


ventana_agregar_mesas.resizable(0, 0)


espacio = tk.Frame(ventana_agregar_mesas, width=2000, height=100)

campo_registro = tk.Frame(espacio, width=1000, height=100, padx=10, pady=1, bg="white")
texto_titulo = tk.Label(campo_registro, text="Mi Restaurante", font=("Arial", 20, "bold"), fg="black", bg="white")
texto_titulo.pack(pady=10, padx=120)

campo_platos = tk.Frame(espacio, width=1000, height=100, padx=10, pady=20, bg="white")
texto_titulo2 = tk.Label(campo_platos, text="Agregar Platos", font=("Arial", 12, "bold"), fg="black", bg="white")
texto_titulo2.pack(pady=10, padx=120)
    
campo_datos = tk.Frame(espacio, width=1000, height=100, padx=10, pady=20, bg="gray")

datos = tk.Frame(campo_datos, width=1000, height=100, padx=10, pady=20, bg="gray")

texto1 = tk.Label(datos, text="Fecha", font=("Arial", 10, "bold"), fg="white", bg="gray")
entry1m = tk.Entry(datos, width=30)

texto2 = tk.Label(datos, text="Hora", font=("Arial", 10, "bold"), fg="white", bg="gray")
entry2m = tk.Entry(datos, width=30)

texto3 = tk.Label(datos, text="Número de personas", font=("Arial", 10, "bold"), fg="white", bg="gray")
entry3m = tk.Entry(datos, width=30)


texto1.grid(row=0, column=0, pady=5, padx=5, sticky="w")
entry1m.grid(row=1, column=0, pady=5, padx=5, sticky="w",ipadx=5, ipady=5)

texto2.grid(row=0, column=2, pady=5, padx=5, sticky="w")
entry2m.grid(row=1, column=2, pady=5, padx=5, sticky="w", ipadx=5, ipady=5)

texto3.grid(row=2, column=0, pady=5, padx=5, sticky="w")
entry3m.grid(row=3, column=0, pady=5, padx=5, sticky="w", ipadx=5, ipady=5)

datos.pack(pady=5, padx=10)
boton_agregar = tk.Button(campo_datos, text="Agregar", bg="white", font=("Arial", 10, "bold"), width=10, command=lambda:(cambiar_ventana(ventana_agregar_mesas, ventana_principal),agregar_a_archivo_mesas()))
boton_agregar.pack(pady=10)

campo_registro.pack(pady=10, padx=20)
campo_platos.pack(pady=10, padx=20)
campo_datos.pack(pady=10, padx=20)

espacio.pack(pady=20)

espacio10 = tk.Frame(ventana_agregar_mesas, width=500, height=100, padx=10, pady=10)
espacio10.pack()

# Novena Ventana

ventana_mostrar_platos.title("Gestion de Mesas")

ancho_pantalla = ventana_mostrar_platos.winfo_screenwidth()
alto_pantalla = ventana_mostrar_platos.winfo_screenheight()
ancho_ventana = 500
alto_ventana = 550
x_pos = int((ancho_pantalla - ancho_ventana) / 2)  
y_pos = int((alto_pantalla - alto_ventana) / 2)  
ventana_mostrar_platos.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")

ventana_mostrar_platos.resizable(0, 0)

espacio = tk.Frame(ventana_mostrar_platos, width=2000, height=100)

campo_registro = tk.Frame(espacio, width=1000, height=100, padx=10, pady=1, bg="white")
texto_titulo = tk.Label(campo_registro, text="Mi Restaurante", font=("Arial", 20, "bold"), fg="black", bg="white")
texto_titulo.pack(pady=10, padx=120)

campo_platos = tk.Frame(espacio, width=500, height=50, padx=10, pady=1, bg="white")
texto_titulo2 = tk.Label(campo_platos, text="Platos", font=("Arial", 12, "bold"), fg="black", bg="white")
texto_titulo2.pack(pady=10, padx=120)
    
campo_datos = tk.Frame(espacio, width=600, height=100, padx=10, pady=1, bg="gray")

datos_platos = ttk.Treeview(campo_datos, columns=("Nombre", "Precio", "Descripción", "Disponibilidad"))

datos_platos.heading("#0")
datos_platos.heading("#1", text="Nombre", anchor="center")
datos_platos.heading("#2", text="Precio", anchor="center")
datos_platos.heading("#3", text="Descripción", anchor="center")
datos_platos.heading("#4", text="Disponibilidad", anchor="center")

datos_platos.column("#0", width=1)
datos_platos.column("#1", width=70)
datos_platos.column("#2", width=70)
datos_platos.column("#3", width=70)
datos_platos.column("#4", width=120)
    
campo_botones = tk.Frame(campo_datos, width=1000, height=100, padx=10, pady=1, bg="gray")

boton_eliminar = tk.Button(campo_botones, text="Eliminar", bg="red", font=("Arial", 10, "bold"), width=10, fg="white", command=lambda: cambiar_ventana(ventana_mostrar_platos, ventana_principal))
boton_eliminar.grid(row=0, column=0, pady=10, padx=10)

boton_actualizar = tk.Button(campo_botones, text="Actualizar", background="#343a40", font=("Arial", 10, "bold"), width=10, fg="white", command=lambda: cambiar_ventana(ventana_mostrar_platos, ventana_principal))
boton_actualizar.grid(row=0, column=1, pady=10, padx=10)

datos_platos.pack(pady=10, padx=20)
campo_botones.pack(pady=10, padx=20)

campo_registro.pack(pady=10, padx=20)
campo_platos.pack(pady=10, padx=20)
campo_datos.pack(pady=10, padx=20)

espacio.pack(pady=20)

espacio10 = tk.Frame(ventana_mostrar_platos, width=500, height=100, padx=10, pady=10)
espacio10.pack()

# Decima Ventana

ventana_mostrar_pedido.title("Gestion de Mesas")

ancho_pantalla = ventana_mostrar_pedido.winfo_screenwidth()
alto_pantalla = ventana_mostrar_pedido.winfo_screenheight()
ancho_ventana = 500
alto_ventana = 550
x_pos = int((ancho_pantalla - ancho_ventana) / 2)  
y_pos = int((alto_pantalla - alto_ventana) / 2)  
ventana_mostrar_pedido.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")
ventana_mostrar_pedido.resizable(0, 0)

espacio = tk.Frame(ventana_mostrar_pedido, width=2000, height=100)

campo_registro = tk.Frame(espacio, width=1000, height=100, padx=10, pady=1, bg="white")
texto_titulo = tk.Label(campo_registro, text="Mi Restaurante", font=("Arial", 20, "bold"), fg="black", bg="white")
texto_titulo.pack(pady=10, padx=120)

campo_platos = tk.Frame(espacio, width=500, height=50, padx=10, pady=1, bg="white")
texto_titulo2 = tk.Label(campo_platos, text="Mesas", font=("Arial", 12, "bold"), fg="black", bg="white")
texto_titulo2.pack(pady=10, padx=120)
    
campo_datos = tk.Frame(espacio, width=600, height=100, padx=10, pady=1, bg="gray")

datos_platos = ttk.Treeview(campo_datos, columns=("Nombre", "Precio", "Descripción", "Disponibilidad"))

datos_platos.heading("#0")
datos_platos.heading("#1", text="N° Plato", anchor="center")
datos_platos.heading("#2", text="N° Mesa", anchor="center")

datos_platos.column("#0", width=1)
datos_platos.column("#1", width=70)
datos_platos.column("#2", width=70)

campo_botones = tk.Frame(campo_datos, width=1000, height=100, padx=10, pady=1, bg="gray")

boton_eliminar = tk.Button(campo_botones, text="Eliminar", bg="red", font=("Arial", 10, "bold"), width=10, fg="white", command=lambda: cambiar_ventana(ventana_mostrar_pedido, ventana_principal))
boton_eliminar.grid(row=0, column=0, pady=10, padx=10)

boton_actualizar = tk.Button(campo_botones, text="Actualizar", background="#343a40", font=("Arial", 10, "bold"), width=10, fg="white", command=lambda: cambiar_ventana(ventana_mostrar_pedido, ventana_principal))
boton_actualizar.grid(row=0, column=1, pady=10, padx=10)

datos_platos.pack(pady=10, padx=20)
campo_botones.pack(pady=10, padx=20)

campo_registro.pack(pady=10, padx=20)
campo_platos.pack(pady=10, padx=20)
campo_datos.pack(pady=10, padx=20)

espacio.pack(pady=20)

espacio10 = tk.Frame(ventana_mostrar_pedido, width=500, height=100, padx=10, pady=10)
espacio10.pack()



ventana_agregar_pedido.title("Gestion de Platos")

ancho_pantalla = ventana_agregar_pedido.winfo_screenwidth()
alto_pantalla = ventana_agregar_pedido.winfo_screenheight()
ancho_ventana = 500
alto_ventana = 500
x_pos = int((ancho_pantalla - ancho_ventana) / 2)  
y_pos = int((alto_pantalla - alto_ventana) / 2)  
ventana_agregar_pedido.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")

ventana_agregar_pedido.resizable(0, 0)

espacio = tk.Frame(ventana_agregar_pedido, width=2000, height=100)

campo_registro = tk.Frame(espacio, width=1000, height=100, padx=10, pady=1, bg="white")
texto_titulo = tk.Label(campo_registro, text="Mi Restaurante", font=("Arial", 20, "bold"), fg="black", bg="white")
texto_titulo.pack(pady=10, padx=120)

campo_platos = tk.Frame(espacio, width=1000, height=100, padx=10, pady=20, bg="white")
texto_titulo2 = tk.Label(campo_platos, text="Agregar Pedido", font=("Arial", 12, "bold"), fg="black", bg="white")
texto_titulo2.pack(pady=10, padx=120)
    
campo_datos = tk.Frame(espacio, width=1000, height=100, padx=10, pady=20, bg="gray")
datos = tk.Frame(campo_datos, width=1000, height=100, padx=10, pady=20, bg="gray")

combo_values = numero_mesas()

selected_value = tk.StringVar()

combo = ttk.Combobox(datos)
combo['values'] = combo_values
combo.grid(row=0, column=0, pady=5, padx=5, sticky="w")

combo_values2 = nombre_platos()

selected_value2 = tk.StringVar()

combo2 = ttk.Combobox(datos)
combo2['values'] = combo_values2
combo2.grid(row=0, column=1, pady=5, padx=5, sticky="w")

datos.pack(pady=5, padx=10)
boton_agregar = tk.Button(campo_datos, text="Agregar", bg="white", font=("Arial", 10, "bold"), width=10, command=lambda: (guardar_pedido(),cambiar_ventana(ventana_agregar_pedido, ventana_principal)))
boton_agregar.pack(pady=10)

campo_registro.pack(pady=10, padx=20)
campo_platos.pack(pady=10, padx=20)
campo_datos.pack(pady=10, padx=20)

espacio.pack(pady=20)

espacio10 = tk.Frame(ventana_agregar_pedido, width=500, height=100, padx=10, pady=10)
espacio10.pack()

ventana_agregar_pedido.withdraw()
ventana_agregar_pedido.mainloop()  
ventana_agregar_platos.mainloop()   
ventana_mostrar_pedido.mainloop()
ventana_mostrar_platos.mainloop()
ventana_agregar_mesas.mainloop()
ventana_pedidos.mainloop()
ventana_mesas.mainloop()
ventana_platos.mainloop()
ventana_principal.mainloop()
ventana_iniciar_sesion.mainloop()
ventana_registro.mainloop()
ventana_inicial.mainloop()