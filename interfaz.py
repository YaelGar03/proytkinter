class InterfazSesion:
    def __init__(self):
      self.usuario=input("Ingrese su usuario: ")
      self.contrasena=input("Ingrese su contraseña: ")
        # Hay que implementarlo como interfaz tkinter



class Interfaz:
    def __init__(self):
      #Variable
      bgcolor="lightblue"

      #Funciones
      # def Centrar ventana
      def centrar_ventana(ventana, ancho, alto):
        # Obtén las dimensiones de la pantalla
        ancho_pantalla = ventana.winfo_screenwidth()
        alto_pantalla = ventana.winfo_screenheight()
        
        # Calcula la posición de la ventana
        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (alto_pantalla // 2) - (alto // 2)
        
        # Establece el tamaño y la posición de la ventana
        ventana.geometry(f"{ancho}x{alto}+{x}+{y}")
      
      # def crear ventana
      def crear_ventana():
        ventana = tk.Tk() # Ventana raiz
        centrar_ventana(ventana, 600, 350) # centrar ventana
        ventana.geometry("600x350") # Tamaño ventana
        ventana.title("") # Título de la ventana
        # venta.iconbitmap()  # Archivo .ico para el icono
        ventana.configure(bgcolor)


      # def dividir en 2 colunas
      def ventana2columnas(ventana):
        # Divide la ventana en 2 columnas
        frame_left = tk.Frame(ventana, padx=10, pady=10)
        frame_left.grid(row=1, column=0, sticky="nsew")
        frame_left.configure(bgcolor)

        frame_right = tk.Frame(ventana, padx=10, pady=10)
        frame_right.grid(row=1, column=1, sticky="nsew") 
        frame_right.configure(bgcolor)

        # Configurar el peso de las columnas y filas para que se expandan correctamente
        ventana.grid_rowconfigure(1, weight=1)
        ventana.grid_columnconfigure(0, weight=1)
        ventana.grid_columnconfigure(1, weight=1)

      # def Texto(text)
      def texto(posicion, contenido, alineacion):
        etiqueta_themes = tk.Label(
        posicion, 
        text=contenido,
        wraplength=200,  # Ajusta el ancho de envoltura del texto para evitar que se desborde.
        justify=alineacion, 
        bg='lightblue'
    )
        #posicion= qué columna
        #contenido= str
        #justify= "left" Alinea el texto a la Izq. "Right" Alinea el texto a la Der.

      # def Campos para escribir(args)
      # def lista desplegable(args)
      # def Botones(text, command)
      # def cuadro para mostrar resumen registros, lista de miembros(?)
      # def total_registros
      # def Grafico resumen

      # def barra de titulo custom, si es posible.
        # Hay que desactivar la barra original,
        # y armar una propia para cambiar colores

        return None


class InterfazPrincipal:
    def __init__(self):
      #Columna 1
      # llamar def texto de bienvenida
      # llamar listas desplegables
      # llamar campos para escribir
      # llamar def Botones

      #Columna 2
      # llamar cuadro resumen registros
      # llamar total_registros
      # llamar grafico
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
        # llamar cuadro registros
        # llamar def Botones
        return None

    class EditarRegistros:
      def __init__(self):
        # llamar texto
        # llamar cuadro registros
        # llamar lista desplegable
        # llamar campos para escribir
        # llamar def Botones
        return None
