import os
from producto import Producto

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.productos = []
        self.archivo = archivo
        # Al iniciar, cargamos los productos automáticamente desde el archivo
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        """Carga los datos del archivo .txt al iniciar el programa."""
        try:
            if not os.path.exists(self.archivo):
                # Si el archivo no existe, lo crea vacío para evitar errores
                with open(self.archivo, 'w') as f: pass
                return

            with open(self.archivo, "r") as f:
                for linea in f:
                    datos = linea.strip().split(',')
                    if len(datos) == 4:
                        # Reconstruimos el objeto Producto con los datos del archivo
                        p = Producto(datos[0], datos[1], int(datos[2]), float(datos[3]))
                        self.productos.append(p)
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error al acceder al archivo: {e}")
        except Exception as e:
            print(f"Error inesperado al cargar: {e}")

    def guardar_en_archivo(self):
        """Guarda la lista actual de productos en el archivo de texto."""
        try:
            with open(self.archivo, "w") as f:
                for p in self.productos:
                    f.write(f"{p.get_id()},{p.get_nombre()},{p.get_cantidad()},{p.get_precio()}\n")
        except PermissionError:
            print("Error: No se tienen permisos para escribir en el archivo.")

    def añadir_producto(self, producto):
        """Añade un producto y actualiza el archivo inmediatamente."""
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: El ID ya existe en el inventario.")
        else:
            self.productos.append(producto)
            self.guardar_en_archivo() # Persistencia en archivo
            print(f"Sistema: Producto '{producto.get_nombre()}' guardado con éxito.")

    def eliminar_producto(self, id_producto):
        original = len(self.productos)
        self.productos = [p for p in self.productos if p.get_id() != id_producto]
        if len(self.productos) < original:
            self.guardar_en_archivo() # Guardamos los cambios
            print(f"Sistema: Producto {id_producto} eliminado correctamente.")
        else:
            print("Error: No se encontró el producto para eliminar.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None: p.set_cantidad(cantidad)
                if precio is not None: p.set_precio(precio)
                self.guardar_en_archivo() # Sincronizamos con el archivo
                print("Sistema: Producto actualizado exitosamente.")
                return
        print("Error: Producto no encontrado.")

    def mostrar_todos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for p in self.productos: print(p)
