from datetime import date

from entidades.validaciones import texto_obligatorio, numero_positivo
from logica.excepciones import ReglaNegocioError


class Mascota:
    def __init__(self, nombre, especie, raza, anio_nacimiento, peso, propietario):
        self._nombre = texto_obligatorio(nombre, "nombre de la mascota")
        self._especie = texto_obligatorio(especie, "especie")
        self._raza = texto_obligatorio(raza, "raza")
        try:
            anio = int(anio_nacimiento)
        except (TypeError, ValueError):
            raise ReglaNegocioError("El año de nacimiento debe ser un número entero.")
        if anio < 1980 or anio > date.today().year:
            raise ReglaNegocioError(f"El año de nacimiento debe estar entre 1980 y {date.today().year}.")
        self._anio_nacimiento = anio
        self._peso = numero_positivo(peso, "peso")
        self._propietario = propietario

    @property
    def nombre(self):
        return self._nombre

    @property
    def especie(self):
        return self._especie

    @property
    def raza(self):
        return self._raza

    @property
    def anio_nacimiento(self):
        return self._anio_nacimiento

    @property
    def peso(self):
        return self._peso

    @property
    def propietario(self):
        return self._propietario
