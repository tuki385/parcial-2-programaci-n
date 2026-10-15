from entidades.validaciones import texto_obligatorio
from logica.excepciones import ReglaNegocioError


class Propietario:
    def __init__(self, cedula, nombre, telefono, municipio):
        self._cedula = texto_obligatorio(cedula, "cédula del propietario")
        self._nombre = texto_obligatorio(nombre, "nombre del propietario")
        self._telefono = texto_obligatorio(telefono, "teléfono")
        self._municipio = municipio
        self._mascotas = []

    @property
    def cedula(self):
        return self._cedula

    @property
    def nombre(self):
        return self._nombre

    @property
    def telefono(self):
        return self._telefono

    @property
    def municipio(self):
        return self._municipio

    @property
    def mascotas(self):
        return list(self._mascotas)

    def agregar_mascota(self, mascota):
        for existente in self._mascotas:
            if existente.nombre.lower() == mascota.nombre.lower():
                raise ReglaNegocioError(
                    f"{self._nombre} ya tiene una mascota llamada '{mascota.nombre}'.")
        self._mascotas.append(mascota)

    def buscar_mascota(self, nombre):
        for mascota in self._mascotas:
            if mascota.nombre.lower() == str(nombre).strip().lower():
                return mascota
        raise ReglaNegocioError(f"{self._nombre} no tiene una mascota llamada '{nombre}'.")
