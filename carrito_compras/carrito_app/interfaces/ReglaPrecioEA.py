from carrito_app.interfaces.ReglaPrecio import ReglaPrecio


class ReglaPrecioEA(ReglaPrecio):
    @staticmethod
    def aplica_regla(sku: str) -> bool:
        '''Validar si la regla de precio se aplica al producto'''
        if str(sku).startswith('EA'):
            return True
        else:
            return False

    @staticmethod
    def calcular_acumulado(cantidad: int, precio_unitario: float) -> float:
        '''Calcular el valor acumulado de la venta del producto'''
        acumulado = cantidad * precio_unitario
        return acumulado