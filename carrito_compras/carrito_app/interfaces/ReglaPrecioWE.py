from carrito_app.interfaces.ReglaPrecio import ReglaPrecio


class ReglaPrecioWE(ReglaPrecio):
    @staticmethod
    def aplica_regla(sku: str) -> bool:
        '''Validar si la regla de precio se aplica al producto'''
        if str(sku).startswith('WE'):
            return True
        else:
            return False

    @staticmethod
    def calcular_acumulado(cantidad: int, precio_unitario: float) -> float:
        '''Calcular el valor acumulado de la venta del producto'''
        acumulado = (1000 * cantidad) * precio_unitario
        return acumulado