# Main.py
# integrará todos las funciones y clases que existen en los otros archivos que importaremos.

import interfaz, login, manejo_registros

# Nuestros Usuarios de prueba. Esto tendriamos que almacenar en otro lado, no en el código.
credenciales='''Yael,1234
              Cecilia,5678'''


### Pantalla de inicio ###
# Obtenesmos usuario y contraseña a través de la interfaz Tkinter, interfaz.py
# Esta sería lo haríamos por terminal según yo
registrarse_o_iniciarsesion=input("1. Iniciar sesión\n2. Registrarse\n")

#Para iniciar sesión
if registrarse_o_iniciarsesion=="1":
  interfaz_inicio_sesion = interfaz.InterfazSesion() # Se crea una instancia de la clase interfaz
  usuario = interfaz_inicio_sesion.usuario
  contrasena = interfaz_inicio_sesion.contrasena

  # Se crea una instancia de la clase InicioSesion con los datos ingresados por el usuario en interfaz.py
  # La siguiente linea tendría que enviarse a validar
  inicio_sesion = interfaz.InterfazSesion.validacion(usuario, contrasena)

#Para regiustrarse
if registrarse_o_iniciarsesion=="2":
  interfaz_registro_usuario = interfaz.InterfazSesion(usuario, contrasena) # Se crea una instancia de la clase interfaz
  usuario = interfaz_registro_usuario.usuario
  contrasena = interfaz_registro_usuario.contrasena
  # Se crea una instancia de la clase InicioSesion con los datos ingresados por el usuario en interfaz.py
  registro_usuario = interfaz.RegistroUsuario(usuario, contrasena)
  print(credenciales)



### Pantalla Principal ###

# Interfaz()
# InterfazPrincipal()
# InterfazEditarGrupoFamiliar()
# InterfazEditarRegistros()
# InterfazEditarRegistros.BorrarRegistros()
# InterfazEditarRegistros.EditarRegistros()

# Tenemos que captar datos del usuario y de nuestro archivo .xlsx(excel) de nuuestra INTERFAZ. 
# Luego los enviaremos nuestro archivo manejo_registros.py para guardarlos, editar la información que ya tenemos o borrarla.
