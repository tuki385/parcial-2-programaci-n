from entidades.clinica import Clinica
from entidades.mascota import Mascota
from entidades.propietario import Propietario
from entidades.servicio import Servicio
from entidades.veterinario import Veterinario
from logica.excepciones import ReglaNegocioError


class ServicioClinicas:
    """Lógica de registro de clínicas, veterinarios, catálogo, propietarios y mascotas."""

    def __init__(self, repositorio):
        self._repositorio = repositorio

    def registrar_clinica(self, nit, nombre, municipio, direccion, barrio):
        if self._repositorio.existe_clinica(nit):          # Regla 7
            raise ReglaNegocioError(f"Ya existe una clínica registrada con NIT {str(nit).strip()}.")
        clinica = Clinica(nit, nombre, municipio, direccion, barrio)
        self._repositorio.guardar_clinica(clinica)
        return clinica

    def registrar_veterinario(self, nit, cedula, nombre, tarjeta):
        clinica = self._repositorio.buscar_clinica(nit)
        veterinario = Veterinario(cedula, nombre, tarjeta)
        clinica.agregar_veterinario(veterinario)
        return veterinario

    def registrar_servicio(self, nit, codigo, nombre, tarifa):
        clinica = self._repositorio.buscar_clinica(nit)
        servicio = Servicio(codigo, nombre, tarifa)
        clinica.agregar_servicio(servicio)
        return servicio

    def registrar_propietario(self, nit, cedula, nombre, telefono, municipio):
        clinica = self._repositorio.buscar_clinica(nit)
        propietario = Propietario(cedula, nombre, telefono, municipio)
        clinica.agregar_propietario(propietario)
        return propietario

    def registrar_mascota(self, nit, cedula, nombre, especie, raza, anio, peso):
        clinica = self._repositorio.buscar_clinica(nit)
        propietario = clinica.buscar_propietario(cedula)
        mascota = Mascota(nombre, especie, raza, anio, peso, propietario)
        propietario.agregar_mascota(mascota)
        return mascota
