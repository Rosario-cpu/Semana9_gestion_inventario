# Importamos la clase Producto del archivo anterior
from producto import Producto

class Inventario:
    """
    Clase Inventario: Gestiona la colección de objetos Producto.
    Supuesto: Se utiliza una lista como estructura de datos principal.
    """
    def __init__(self):
        # Estructura de datos personalizada: una lista de objetos
        self.productos = []

    def añadir_producto(self, producto):
        # Lógica: Se verifica que el ID no exista antes de agregar
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: El ID ya existe en el inventario.")
        else:
            self.productos.append(producto)
            print("Sistema: Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        # Lógica: Filtramos la lista para quitar el producto con ese ID
        original = len(self.productos)
        self.productos = [p for p in self.productos if p.get_id() != id_producto]
        if len(self.productos) < original:
            print(f"Sistema: Producto {id_producto} eliminado.")
        else:
            print("Error: No se encontró el producto.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        # Lógica: Buscamos por ID y actualizamos solo lo que el usuario pida
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None: p.set_cantidad(cantidad)
                if precio is not None: p.set_precio(precio)
                print("Sistema: Producto actualizado.")
                return
        print("Error: Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        # Lógica: Retorna una lista con nombres similares (sin importar mayúsculas)
        return [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]

    def mostrar_todos(self):
        # Lógica: Recorre e imprime cada producto
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for p in self.productos:
                print(p)
