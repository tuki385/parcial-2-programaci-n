class DetalleFactura:
    def __init__(self, servicio, tarifa):
        self._servicio = servicio
        self._tarifa = tarifa

    @property
    def servicio(self):
        return self._servicio

    @property
    def tarifa(self):
        return self._tarifa


class Factura:
    def __init__(self, numero, fecha, propietario, mascota, detalles):
        self._numero = numero
        self._fecha = fecha
        self._propietario = propietario
        self._mascota = mascota
        self._detalles = list(detalles)

    @property
    def numero(self):
        return self._numero

    @property
    def fecha(self):
        return self._fecha

    @property
    def propietario(self):
        return self._propietario

    @property
    def mascota(self):
        return self._mascota

    @property
    def detalles(self):
        return list(self._detalles)

    def total(self):
        """Valor total: suma de las tarifas de los servicios prestados."""
        return sum(detalle.tarifa for detalle in self._detalles)
