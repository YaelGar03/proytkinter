from tkinter import ttk
from tkinter import PhotoImage
import tkinter as tk
from PIL import Image, ImageTk
import os
import login


class Interfaz:
    def __init__(self):
      #Variable
      self.bgcolor = "white"  # Color de fondo

      #Funciones
    # def Centrar ventana
    def centrar_ventana(self, ventana, ancho, alto):
        # Obtén las dimensiones de la pantalla
        ancho_pantalla = ventana.winfo_screenwidth()
        alto_pantalla = ventana.winfo_screenheight()
        
        # Calcula la posición de la ventana
        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (alto_pantalla // 2) - (alto // 2)
        
        # Establece el tamaño y la posición de la ventana
        ventana.geometry(f"{ancho}x{alto}+{x}+{y}")
      
    # def crear ventana
    def crear_ventana(self, ancho, alto):
        self.ventana = tk.Tk() # Ventana raiz
        ventana = self.ventana
        self.centrar_ventana(self.ventana, ancho, alto) # centrar ventana

        self.ventana.geometry(f"{ancho}x{alto}") # Tamaño ventana
        self.ventana.configure(bg=self.bgcolor)

        # Frame para colocar el contenido 
        self.frame_ventana = tk.Frame(self.ventana, bg="gray")
        self.frame_ventana.grid(row=0, column=0, padx=10, pady=10)  # Asegura que el frame se expanda
        
        
        # Configurar las columnas para que se expandan con diferentes pesos, 0 = no se expande
        # También asegura que la barra ocupe toda la ventana
        
        self.ventana.grid_columnconfigure(0, weight=0)  # Columna izq
        self.ventana.grid_columnconfigure(1, weight=0)
        self.ventana.grid_columnconfigure(2, weight=1)
        self.ventana.grid_columnconfigure(3, weight=1)
        self.ventana.grid_columnconfigure(4, weight=0)
        self.ventana.grid_columnconfigure(5, weight=0)
        self.ventana.grid_columnconfigure(6, weight=0)  # Columna der
        
        # Eliminar la barra de título estándar
        self.ventana.overrideredirect(1)
        
        # Configurar el evento de restauración
        ventana.bind("<Map>", self.reactivar_barra_titulo)

        # Llamada a la barra de título custom
        self.barra_titulo(ventana)

        # def barra de titulo custom, si es posible.
    # Función para crear la barra de título custom
    def barra_titulo(self, ventana):
        bgbarra = "#4D4D4D"

        # Crear la barra de título
        barra_titulo = tk.Frame(ventana, bg=bgbarra, relief="raised", bd=0, pady=5)
        barra_titulo.grid(row=0, column=0, columnspan=7, sticky="ew")
        
        # Configurar las columnas internas de la barra de título
        barra_titulo.grid_columnconfigure(1, weight=1)  # Para que el título se expanda
    

        # Añadir un ícono a la barra de título
        try:
            ruta_icono = os.path.join(os.path.dirname(__file__), 'LOGO.ico')
            imagen = Image.open(ruta_icono)
            imagen_redimensionada = imagen.resize((20, 20))
            icono = ImageTk.PhotoImage(imagen_redimensionada)
            icono_label = tk.Label(barra_titulo, image=icono,bg=bgbarra)
            icono_label.image = icono  # Necesario para evitar que el ícono sea recolectado por el GC
            icono_label.grid(row=0, column=0, padx=10)
        except Exception as e:
            print(f"No se pudo cargar el ícono: {e}")

        # Etiqueta para el título
        titulo = tk.Label(barra_titulo, text="Economía Hogar", bg=bgbarra, fg="white") #bgbarra
        titulo.grid(row=0, column=1, sticky="w")  # Título pegado al logo, sin padding horizontal
        
        # Botón minimizar
        btn_minimizar = tk.Button(barra_titulo, text="_", command=self.minimizar, bg=bgbarra, fg="white", bd=0)
        btn_minimizar.grid(row=0, column=4, padx=(80, 10))
        
        # Botón maximizar (deshabilitado, incluido por una cuestión puramente estética)
        btn_maximizar = tk.Button(barra_titulo, text="□", state="disabled", bg=bgbarra, fg="white", bd=0)
        btn_maximizar.grid(row=0, column=5, padx=10)

        # Botón cerrar
        btn_cerrar = tk.Button(barra_titulo, text="X", command=ventana.destroy, bg=bgbarra, fg="white", bd=0)
        btn_cerrar.grid(row=0, column=6, padx=10)

        # Permitir mover la ventana arrastrando la barra de título
        barra_titulo.bind("<Button-1>", self.detectar_movimiento)
        barra_titulo.bind("<B1-Motion>", self.moverse)

    def minimizar(self):
        self.ventana.overrideredirect(0)
        self.ventana.wm_state('iconic')

    def reactivar_barra_titulo(self, evento):
        # Verificar si la ventana está en el estado normal (no minimizada)
        if self.ventana.wm_state() == 'normal':
            # Reactivar la barra de título personalizada
            self.ventana.overrideredirect(1)

    # Función para detectar el inicio del movimiento de arrastre
    def detectar_movimiento(self, evento):
        self.ventana.x = evento.x
        self.ventana.y = evento.y

    # Función para mover la ventana al arrastrarla
    def moverse(self, evento):
        deltax = evento.x - self.ventana.x
        deltay = evento.y - self.ventana.y
        self.ventana.geometry(f"+{self.ventana.winfo_x() + deltax}+{self.ventana.winfo_y() + deltay}")

# Widgets para mostrar contenido: #
    def texto(self, alineacion, contenido, ancho_maximo, row, column, padx, pady):
        etiqueta_texto = tk.Label(
            self.ventana,
            text=contenido,
            justify=alineacion,
            wraplength=ancho_maximo ,  # Ajusta el ancho de envoltura del texto para evitar que se desborde.
            bg=self.bgcolor,
            font=("Consolas", 14)
            ) 
        etiqueta_texto.grid(row=row, column=column, padx=padx, pady=pady)
        #contenido= str
        #justify= "left", "center", o "right"
        return etiqueta_texto

        # def Campos para escribir(args)
    def campo_entrada(self, row, column, padx, pady):
        campo = ttk.Entry(self.ventana)
        campo.grid(row=row, column=column, padx=padx, pady=pady)
        return campo

        # def lista desplegable(args)
    def campo_lista_desplegable():
        campo = ttk.Combobox(
        state="readonly",
        values=["opcion1", "opcion2", "opcion3", "opcion4"]
        )
        campo.pack(pady=10)
        return campo
        
        # def Botones(text, command)
    def boton(self, contenido, row, column, padx, pady, command):
        boton = tk.Button(bg=self.bgcolor, text=contenido, command=command)
        boton.grid(row=row, column=column, padx=padx, pady=pady)

        # def cuadro para mostrar resumen registros, lista de miembros(?)
    def resumen_registros(self, row, column, padx, pady):
        tree = ttk.Treeview(self.ventana, columns=list(self.df.columns), show="headings")
        tree.grid(row=row, column=column, padx=padx, pady=pady)

        # def total_grupo_familiar
        def total_grupofam(self, totaldinero):
            total=Interfaz.texto(1, f"$ total restante de grupo familiar: $ {totaldinero}", "Left")
            return total
        
        # def Grafico resumen
        def total_grupofam_grafico():
            return None
    

    # VENTANA LOGIN
    def LoginApp(self):
        self.crear_ventana(400, 750)

        # Campos de usuario y contraseña
        self.texto("left", "Usuario", 200, 2, 0, 0, 10)
        self.entry_usuario = self.campo_entrada(2, 1, 20, 10)

        self.texto("left", "Contraseña", 200, 4, 0, 0, 10)
        self.entry_contrasena = tk.Entry(self.ventana, show='*')
        self.entry_contrasena.grid(row=4, column=1, padx=20, pady=10)
        
        # Enviamos "usuario" y "contraseña", introducidos en la GUI, a validar en login.py
        def enviar_credenciales():
            usuario = self.entry_usuario.get()
            contrasena = self.entry_contrasena.get()
            verificar_login = login.InicioSesion()
            if verificar_login.validar_credenciales(usuario, contrasena):
                self.ventana.destroy()
                self.PantallaPrincipal()
            
        self.btn_login = self.boton("Iniciar Sesión", 200, 6, 1, 10, 10, enviar_credenciales)
        
        self.btn_registro = tk.Button(self.ventana, text="Registrar Usuario")
        self.btn_registro.grid(row=7, column=1, padx=10, pady=10)
        
        
        

    def PantallaPrincipal(self):
        self.crear_ventana(1250, 900)
        
        #Columna 1
        
        # llamar def texto de bienvenida
        self.texto("center", "Comienza a gestionar la economía de tu hogar.\n\nRegistra los gastos e ingresos de cada miembro de tu grupo familiar", 300, 2, 1, 50, 50)
        #alineacion, contenido, ancho_maximo, row, column, padx, pady
        
        
        
        # llamar listas desplegables
        self.texto("left", "Selecciona el tipo de registro:", 200, 1, 0, 10, 10)
        self.lista_desplegable_tipo = self.campo_lista_desplegable()
        # llamar campos para escribir
        self.texto("left", "Nombre del miembro:", 200, 2, 0, 10, 10)
        self.campo_nombre = self.campo_entrada(2, 1, 10, 10)
        self.texto("left", "Cantidad:", 200, 3, 0, 10, 10)
        self.campo_cantidad = self.campo_entrada(3, 1, 10, 10)
    
        self.texto("left", "Fecha (dd/mm/aaaa):", 200, 4, 0, 10, 10)
        self.campo_fecha = self.campo_entrada(4, 1, 10, 10)
        # llamar def Botones
        self.boton("Añadir Gasto", 5, 1, 10, 20, self.añadir_gasto)
        self.boton("Añadir Ingreso", 6, 1, 10, 20, self.añadir_ingreso)

      #Columna 2
      # llamar cuadro resumen registros
        self.texto("left", "Resumen de Registros:", 200, 1, 2, 10, 10)
        self.resumen_registros(2, 2, 10, 20)
      # llamar total_registros
        total = self.calcular_total_registros()
        self.texto("left", f"Total: {total}", 200, 3, 2, 10, 10)
      # llamar grafico
        self.grafico_resumen()  # falta definir esta función
        
        return None
    
      
    

class  InterfazEditarGrupoFamiliar:
    def __init__(self):
      # llamar texto
      # llamar cuadro miembros del grupo familiar registrados
      # llamar campos para escribir
      # llamar def Botones
      return None

class  InterfazEditarRegistros:
    def __init__(self):
      # llamar texto
      # llamar cuadro registros
      # llamar def Botones
      return None

    class BorrarRegistros:
      def __init__(self):
        # llamar texto
      self.texto("left", "¿Quieres borrar un registro?", 200, 0, 0, 10)
        # llamar cuadro registros
      self.cuadro_registros()
        # llamar def Botones
      self.boton("Borrar", 2, 1, 10, 20, self.borrar_registro)
      self.boton("Cancelar", 2, 2, 10, 20, self.cancelar)
        def borrar_registro(self):
        # Lógica para borrar el registro seleccionado
        pass

       def cancelar(self):
        # Lógica para cancelar la acción
         pass
        return None

    class EditarRegistros:
      def __init__(self):
        # llamar texto
        self.texto("left", "Editar Registro", 200, 0, 0, 10)
        # llamar cuadro registros
        self.cuadro_registros()

        # llamar lista desplegable
        self.campo_lista_desplegable()
        # llamar campos para escribir
        self.campo_entrada(2, 1, 10, 10)  # Por ejemplo, para un campo de entrada de texto
        # llamar def Botones
          self.boton("Guardar", 3, 1, 10, 20, self.guardar_cambios)
        self.boton("Cancelar", 3, 2, 10, 20, self.cancelar)

      def guardar_cambios(self):
        # Lógica para guardar los cambios en el registro
         pass

      def cancelar(self):
        # Lógica para cancelar la acción
        pass
        return None
