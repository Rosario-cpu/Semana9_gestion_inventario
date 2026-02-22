from producto import Producto
from inventario import Inventario


def menu():
    inv = Inventario()

    while True:
        print("\n--- MENÚ DE GESTIÓN DE INVENTARIO ---")
        print("1. Añadir\n2. Eliminar\n3. Actualizar\n4. Mostrar Todo\n5. Salir")
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                id_p = input("ID: ")
                nom = input("Nombre: ")
                cant = int(input("Cantidad: "))
                prec = float(input("Precio: "))
                inv.añadir_producto(Producto(id_p, nom, cant, prec))

            elif opcion == "2":
                id_p = input("ID a eliminar: ")
                inv.eliminar_producto(id_p)

            elif opcion == "3":
                id_p = input("ID del producto: ")
                c_in = input("Nueva cantidad (vacío para omitir): ")
                p_in = input("Nuevo precio (vacío para omitir): ")
                cant = int(c_in) if c_in else None
                prec = float(p_in) if p_in else None
                inv.actualizar_producto(id_p, cant, prec)

            elif opcion == "4":
                inv.mostrar_todos()

            elif opcion == "5":
                print("¡Hasta luego!")
                break
        except ValueError:
            print("Error: Ingrese valores numéricos válidos en cantidad y precio.")


if __name__ == "__main__":
    menu()