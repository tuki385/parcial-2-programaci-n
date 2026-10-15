from entidades.validaciones import texto_obligatorio


class Municipio:
    def __init__(self, codigo_dane, nombre, departamento):
        self._codigo_dane = str(codigo_dane or "").strip()
        self._nombre = texto_obligatorio(nombre, "municipio")
        self._departamento = texto_obligatorio(departamento, "departamento")

    @property
    def codigo_dane(self):
        return self._codigo_dane

    @property
    def nombre(self):
        return self._nombre

    @property
    def departamento(self):
        return self._departamento

    def __str__(self):
        return f"{self._nombre}, {self._departamento}"
