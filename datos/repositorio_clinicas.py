from logica.excepciones import ReglaNegocioError


class RepositorioClinicas:
    """Capa de datos: guarda las clínicas en memoria y entrega los consecutivos."""

    def __init__(self):
        self._clinicas = {}          # NIT -> Clinica
        self._consecutivo_cita = 0
        self._consecutivo_factura = 0

    def guardar_clinica(self, clinica):
        self._clinicas[clinica.nit] = clinica

    def buscar_clinica(self, nit):
        clinica = self._clinicas.get(str(nit).strip())
        if clinica is None:
            raise ReglaNegocioError(f"No existe una clínica con NIT {nit}.")
        return clinica

    def existe_clinica(self, nit):
        return str(nit).strip() in self._clinicas

    def buscar_cita(self, codigo):
        codigo = str(codigo).strip().upper()
        for clinica in self._clinicas.values():
            for cita in clinica.citas:
                if cita.codigo == codigo:
                    return cita
        raise ReglaNegocioError(f"No existe una cita con código {codigo}.")

    def buscar_clinica_de_cita(self, codigo):
        """Apoyo a atender_cita: devuelve la clínica a la que pertenece la cita."""
        codigo = str(codigo).strip().upper()
        for clinica in self._clinicas.values():
            if any(cita.codigo == codigo for cita in clinica.citas):
                return clinica
        raise ReglaNegocioError(f"No existe una cita con código {codigo}.")

    def siguiente_codigo_cita(self):
        self._consecutivo_cita += 1
        return f"CIT-{self._consecutivo_cita:03d}"

    def siguiente_numero_factura(self):
        self._consecutivo_factura += 1
        return f"FAC-{self._consecutivo_factura:03d}"
