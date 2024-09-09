# Main.py
# integrará todas las funciones y clases que existen en los otros archivos que importaremos.
import interfaz
import login
import manejo_registros



# Crear una instancia de la clase Interfaz
def main(): # main suele usarse como el punto de entrada principal para ejecutar el código.
    # Crear una instancia de la clase Interfaz
    mi_interfaz = interfaz.Interfaz()
    mi_interfaz.LoginApp()
    mi_interfaz.ventana.mainloop() # bucle principal, Sin mainloop(), la ventana de la GUI se cerraría inmediatamente después de abrirse.

if __name__ == "__main__": # asegura que la función main solo se ejecute cuando el archivo se ejecute directamente, no cuando se importe como módulo
    main()


