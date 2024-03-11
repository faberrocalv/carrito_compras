from carrito_app.interfaces.ReglaPrecioEA import ReglaPrecioEA
from carrito_app.interfaces.ReglaPrecioWE import ReglaPrecioWE
from carrito_app.interfaces.ReglaPrecioSP import ReglaPrecioSP


class CalculadoraAcumulado:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad
        self.lista_reglas = [ReglaPrecioEA, ReglaPrecioWE, ReglaPrecioSP]

    def _obtener_regla(self):
        # Preguntar a cada regla si es aplicable y guardar la que lo sea
        for regla in self.lista_reglas:
            if regla.aplica_regla(self.producto.sku):
                self.regla_precio = regla
                break

    def calcular_acumulado(self):
        # Obtener la regla de precio para calcular el valor acumulado del producto
        self._obtener_regla()
        # Calcular el acumulado
        acumulado = self.regla_precio.calcular_acumulado(self.cantidad, self.producto.precio_unitario)
        return acumulado
