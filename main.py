from gestor import Gestor

class Main:

    @staticmethod
    def run():
        _PASSWORD_SYSTEM:str = "contrasena!"
        intentos:int = 3
        gestor:Gestor = Gestor()
        print("Sistema GC")
        while(intentos > 0):
            password:str = input("Ingrese contraseña del sistema: ")
            if password == _PASSWORD_SYSTEM:
                print("Inicio de sesion")
                salida:bool = True
                while salida:
                    print("=======Modulos=======")
                    print("1 -> Crear Credencial")
                    print("2 -> Agregar Credencial")
                    print("3 -> Buscar Credencial")
                    print("4 -> Salir")
                    print("=====================")
                    opcion:str = input("Seleccione modulo: ")

                    match opcion:
                        case "1":
                            print("Saliendo del sistema!")
                        case "2":
                            gestor.agregar_credencial()
                        case "3": 
                            print("Saliendo del sistema!")
                        case "4": 
                            print("Saliendo del sistema!")
                            salida = False
                            
                        case _: 
                            print("Opcion no valida!")
                            
                        

            else:
                intentos -= 1
                print(f"Intentos {intentos}")
                

Main.run()
        
    