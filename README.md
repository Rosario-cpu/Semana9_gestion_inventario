# Sistema de Gestión de Inventarios Mejorado

Este proyecto es una aplicación de consola en Python diseñada para gestionar el inventario de un negocio de forma persistente y segura.

## Implementación Técnica

### 1. Persistencia de Datos (Archivos)
Para cumplir con el requisito de almacenamiento, el sistema utiliza un archivo llamado `inventario.txt`.
- **Carga Automática**: Al iniciar, el programa busca el archivo y carga los datos existentes.
- **Guardado Automático**: Cada vez que se añade, elimina o actualiza un producto, los cambios se escriben inmediatamente en el archivo.

### 2. Manejo de Excepciones (Robustez)
Se implementaron bloques `try-except` para asegurar que el programa sea "resiliente":
- **ValueError**: Captura errores cuando el usuario ingresa texto en campos numéricos (como en el precio o cantidad).
- **FileNotFoundError**: Maneja la situación donde el archivo de inventario no existe, creándolo desde cero sin interrumpir el programa.

### 3. Estructura del Código
- `producto.py`: Contiene la clase con atributos encapsulados.
- `inventario.py`: Lógica principal del manejo de datos.
- `main.py`: Interfaz de usuario y control de errores.

##  Pruebas Realizadas
Se verificó el funcionamiento con productos reales (Videojuego, Impresora, MemoriaUSB) y se forzaron errores de entrada para validar la estabilidad del sistema.
