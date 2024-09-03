# Nuestros Usuarios de prueba. Esto tendriamos que almacenar en otro lado, no en el código.
credenciales='''Yael,1234
Cecilia,5678'''

class InicioSesion:
    def __init__(self, usuario, contrasena):
        self.usuario1 = usuario
        self.contrasena1 = contrasena
        self.validar_credenciales()

    def validar_credenciales(self):
        for linea in credenciales.splitlines():
          usuario, contrasena = linea.strip().split(',')
          if usuario == self.usuario1 and contrasena == self.contrasena1:
            print("Inicio de sesión exitoso")
            return True
          else:
            print("Inicio de sesión fallido")
            return False



class RegistroUsuario:
    def __init__(self, usuario, contrasena):
        global credenciales
        credenciales= f"{credenciales}\n{usuario},{contrasena}"
        print("Usuario registrado exitosamente")
        print(credenciales)

    # def registrar_usuario(self):
    #     global credenciales
    #     credenciales= f"{credenciales}\n{self.usuario},{self.contrasena}"
    #     print("Usuario registrado exitosamente")
    #     print(credenciales)
    #     return credenciales


        # Almacenamos en credenciales.txt usuario y contraseña
#        with open(credenciales.txt, 'a') as credenciales:
#        credenciales.write(f'{usuario},{contrasena}\n')


