from credencial import Credencial

class Gestor:
    __credenciales: list = []

    def listar_credenciales(self) -> None:
        for credencial in self.__credenciales:
            print("Credencial - servicio: ", credencial.servicio)
    
    def crear_credencial(self) -> Credencial:
        print("Creando credencial")
        servicio: str = input("Agregar el servicio: ")
        usuario: str = input("Agregar el usuario: ")
        contrasena: str = input("Agregar la contraseña: ")

        credencial: Credencial = Credencial(
            in_servicio=servicio,
            in_usuario=usuario,
            in_contrasena=contrasena
        )
        print("Credencial creada!")
        return credencial
    
    def agregar_credencial(self, credencial: Credencial) -> None:
        self.__credenciales.append(credencial)
        print("Credencial agregada!")
