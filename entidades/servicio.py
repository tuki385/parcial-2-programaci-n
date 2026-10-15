from entidades.validaciones import texto_obligatorio, numero_positivo


class Servicio:
    def __init__(self, codigo, nombre, tarifa):
        self._codigo = texto_obligatorio(codigo, "código del servicio").upper()
        self._nombre = texto_obligatorio(nombre, "nombre del servicio")
        self._tarifa = numero_positivo(tarifa, "tarifa")

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def tarifa(self):
        return self._tarifa
