"""
Clase Producto: Representa la entidad básica del inventario.
Supuesto: Se utiliza un guion bajo(_) antes de los atributos para indicar
que deben ser tratados como privados, accediendo a ellos mediante getters y setters
"""
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        # El ID debe ser único (validado en la clase Inventario)
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Métodos Getter para obtener valores de forma segura
    def get_id(self): return self._id
    def get_nombre(self): return self._nombre
    def get_cantidad(self): return self._cantidad
    def get_precio(self): return self._precio

    # Métodos Setter para modificar valores (Permitido para cantidad y precio según requerimiento)
    def set_cantidad(self, cantidad): self._cantidad = cantidad
    def set_precio(self, precio): self._precio = precio

    # Método para representar el objeto como texto al imprimirlo
    def __str__(self):
        return f"ID: {self._id} | Producto: {self._nombre} | Cantidad: {self._cantidad} | Precio: ${self._precio:.2f}"
