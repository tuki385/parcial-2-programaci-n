from entidades.validaciones import texto_obligatorio
from logica.excepciones import ReglaNegocioError


class Clinica:
    def __init__(self, nit, nombre, municipio, direccion, barrio):
        self._nit = texto_obligatorio(nit, "NIT")
        self._nombre = texto_obligatorio(nombre, "nombre de la clínica")
        self._municipio = municipio
        self._direccion = texto_obligatorio(direccion, "dirección")
        self._barrio = texto_obligatorio(barrio, "barrio")
        self._veterinarios = {}   # cédula -> Veterinario
        self._servicios = {}      # código -> Servicio (catálogo)
        self._propietarios = {}   # cédula -> Propietario
        self._citas = []

    @property
    def nit(self):
        return self._nit

    @property
    def nombre(self):
        return self._nombre

    @property
    def municipio(self):
        return self._municipio

    @property
    def direccion(self):
        return self._direccion

    @property
    def barrio(self):
        return self._barrio

    @property
    def veterinarios(self):
        return list(self._veterinarios.values())

    @property
    def servicios(self):
        return list(self._servicios.values())

    @property
    def propietarios(self):
        return list(self._propietarios.values())

    @property
    def citas(self):
        return list(self._citas)

    def agregar_veterinario(self, vet):
        if vet.cedula in self._veterinarios:
            raise ReglaNegocioError(
                f"Ya existe un veterinario con cédula {vet.cedula} en la clínica {self._nombre}.")
        self._veterinarios[vet.cedula] = vet

    def agregar_servicio(self, servicio):
        # Regla 7: no repetir el código de servicio dentro de la misma clínica
        if servicio.codigo in self._servicios:
            raise ReglaNegocioError(
                f"Ya existe un servicio con código {servicio.codigo} en la clínica {self._nombre}.")
        self._servicios[servicio.codigo] = servicio

    def agregar_propietario(self, prop):
        # Regla 7: no repetir la cédula del propietario dentro de la misma clínica
        if prop.cedula in self._propietarios:
            raise ReglaNegocioError(
                f"Ya existe un propietario con cédula {prop.cedula} en la clínica {self._nombre}.")
        self._propietarios[prop.cedula] = prop

    def agregar_cita(self, cita):
        self._citas.append(cita)

    def buscar_veterinario(self, cedula):
        vet = self._veterinarios.get(str(cedula).strip())
        if vet is None:
            raise ReglaNegocioError(f"No existe un veterinario con cédula {cedula} en la clínica {self._nombre}.")
        return vet

    def buscar_servicio(self, codigo):
        servicio = self._servicios.get(str(codigo).strip().upper())
        if servicio is None:
            raise ReglaNegocioError(f"No existe el servicio '{codigo}' en el catálogo de la clínica {self._nombre}.")
        return servicio

    def buscar_propietario(self, cedula):
        prop = self._propietarios.get(str(cedula).strip())
        if prop is None:
            raise ReglaNegocioError(f"No existe un propietario con cédula {cedula} en la clínica {self._nombre}.")
        return prop

    def veterinario_ocupado(self, vet, fecha, hora):
        """Regla 2: el veterinario ya tiene una cita Programada en esa fecha y hora."""
        return any(c.esta_programada() and c.veterinario is vet and c.fecha == fecha and c.hora == hora
                   for c in self._citas)

    def mascota_ocupada(self, mascota, fecha, hora):
        """Regla 3: la mascota ya tiene una cita Programada en esa fecha y hora."""
        return any(c.esta_programada() and c.mascota is mascota and c.fecha == fecha and c.hora == hora
                   for c in self._citas)

    def citas_del_dia(self, fecha):
        return sorted((c for c in self._citas if c.fecha == fecha), key=lambda c: c.hora)
