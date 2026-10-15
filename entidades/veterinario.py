from entidades.validaciones import texto_obligatorio


class Veterinario:
    def __init__(self, cedula, nombre, tarjeta_profesional):
        self._cedula = texto_obligatorio(cedula, "cédula del veterinario")
        self._nombre = texto_obligatorio(nombre, "nombre del veterinario")
        self._tarjeta_profesional = texto_obligatorio(tarjeta_profesional, "tarjeta profesional")

    @property
    def cedula(self):
        return self._cedula

    @property
    def nombre(self):
        return self._nombre

    @property
    def tarjeta_profesional(self):
        return self._tarjeta_profesional
