
import notas.nota as modelo

class Acciones:

    def crear(self, usuario):
        print(f"Ok {usuario[1]} !! Creando Nueva Nota...")

        titulo = input("Introduce el titulo de tu nota: ")
        descripcion = input("Contenido de tu nota: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\nPerfecto Nota guardada: {nota.titulo}")
        else:
            print(f"\nNo se ha guardado la nota {usuario[1]}")

    def mostrar(self, usuario):

        print(f"\nVale {usuario[1]} !! Aqui tienes tus notas: ")

        nota = modelo.Nota(usuario[0], "", "")
        notas = nota.listar()

        for nota in notas:
            print(f"\n******************************************")
            print(f"Titulo: {nota[2]}")
            print(f"Descripcion: {nota[3]}")
            print(f"******************************************")

    def borrar(self, usuario):

        print(f"OK {usuario[1]}!! Vamos a borrar notas")

        titulo = input("Introduce el titulo: ")

        nota = modelo.Nota(usuario[0], titulo, "")
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f"Hemos Borrado la nota: {nota.titulo}")
        else:
            print("No se ha borrado la nota")