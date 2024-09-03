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
    def __init__(self,usuario,contrasena):
        self.usuario=usuario
        self.contrasena=contrasena
        self.registrar_usuario()

    def registrar_usuario(self, usuario, contrasena):
        global credenciales
        credenciales= credenciales+"\n"+usuario+","+contrasena
        print("Usuario registrado exitosamente")
        return credenciales


        # Almacenamos en credenciales.txt usuario y contraseña
#        with open(credenciales.txt, 'a') as credenciales:
#        credenciales.write(f'{usuario},{contrasena}\n')


