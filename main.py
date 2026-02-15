# Importamos las clases necesarias
from producto import Producto
from inventario import Inventario


def mostrar_menu():
    # Creamos una instancia del inventario
    mi_inventario = Inventario()

    while True:
        print("\n--- SISTEMA DE GESTIÓN DE INVENTARIO ---")
        print("1. Añadir Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto por nombre")
        print("5. Ver Inventario")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_p = input("ID: ")
            nom = input("Nombre: ")
            cant = int(input("Cantidad: "))
            prec = float(input("Precio: "))
            mi_inventario.añadir_producto(Producto(id_p, nom, cant, prec))

        elif opcion == "2":
            id_p = input("ID a eliminar: ")
            mi_inventario.eliminar_producto(id_p)

        elif opcion == "3":
            id_p = input("ID del producto: ")
            c = input("Nueva cantidad (dejar vacío para no cambiar): ")
            p = input("Nuevo precio (dejar vacío para no cambiar): ")
            mi_inventario.actualizar_producto(
                id_p,
                int(c) if c else None,
                float(p) if p else None
            )

        elif opcion == "4":
            nom = input("Nombre a buscar: ")
            resultados = mi_inventario.buscar_por_nombre(nom)
            for r in resultados: print(r)

        elif opcion == "5":
            mi_inventario.mostrar_todos()

        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    mostrar_menu()
