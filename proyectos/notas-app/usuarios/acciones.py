
import usuarios.usuario as modelo
import notas.acciones

class Acciones:

    def registro(self):
        print("\nVamos a registrarte en el sistema")

        nombre = input("Cual es tu nombre?: ")
        apellidos = input("Cual es tu apellido?: ")
        email = input("Cual es tu email?: ")
        password = input("Cual es tu contraseña?: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()
        
        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("\nNo te has registrado correctamente")

    def login(self):
        print("\nIdentificate en el sistema\n")

        try:
            email = input("Cual es tu email?: ")
            password = input("Cual es tu contraseña?: ")

            usuario = modelo.Usuario('', '', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"\nBienvenido {login[1]} te has registrado {login[5]}")
                self.proximasAcciones(login)
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"\nIntentalo mas tarde")

    def proximasAcciones(self, usuario):
        
        print("""
            Acciones Disponibles:

             [1] - Crear nota
             [2] - Mostrar notas
             [3] - Eliminar nota
             [4] - Salir
        """)

        accion = int(input("Que quieres hacer?: "))
        hazEl = notas.acciones.Acciones()

        if accion == 1:
            print("\nCrear Nota")
            hazEl.crear(usuario)

            self.proximasAcciones(usuario)

        elif accion == 2:
            print("\nMostrar Nota")
            hazEl.mostrar(usuario)

            self.proximasAcciones(usuario)

        elif accion == 3:
            print("\nEliminar Nota")
            hazEl.borrar(usuario)

            self.proximasAcciones(usuario)

        elif accion == 4:
            print("\nSaliendo...")
            exit()

        else:
            print("\nOpcion Invalida")
            self.proximasAcciones(usuario)

        return None

