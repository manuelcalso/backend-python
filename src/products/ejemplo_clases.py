# Clase base
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        print(f"Producto: {self.nombre}\nPrecio: ${self.precio:.2f}\nStock disponible: {self.stock}")

    def actualizar_stock(self, cantidad):
        self.stock += cantidad
        print(f"Nuevo stock de {self.nombre}: {self.stock}")

    def aplicar_descuento(self, porcentaje):
        descuento = self.precio * (porcentaje / 100)
        self.precio -= descuento
        print(f"Precio con {porcentaje}% de descuento: ${self.precio:.2f}")

# Clase hija
class ProductoDigital(Producto):
    def __init__(self, nombre, precio, stock, formato, tamaño_descarga):
        super().__init__(nombre, precio, stock)
        self.formato = formato
        self.tamaño_descarga = tamaño_descarga  # en MB

    def descargar(self):
        print(f"Descargando {self.nombre} en formato {self.formato}... Tamaño: {self.tamaño_descarga}MB")

    def mostrar_info_digital(self):
        self.mostrar_info()
        print(f"Formato: {self.formato}\nTamaño de descarga: {self.tamaño_descarga}MB")