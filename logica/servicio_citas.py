from entidades.cita import Cita
from entidades.factura import DetalleFactura, Factura
from logica.excepciones import ReglaNegocioError


class ServicioCitas:
    """Lógica de las citas: aplica las reglas de negocio y coordina las entidades."""

    def __init__(self, repositorio):
        self._repositorio = repositorio

    def programar_cita(self, nit, cedula, mascota, fecha, hora, cod_servicio, cedula_vet):
        clinica = self._repositorio.buscar_clinica(nit)
        propietario = clinica.buscar_propietario(cedula)
        animal = propietario.buscar_mascota(mascota)
        servicio = clinica.buscar_servicio(cod_servicio)
        veterinario = clinica.buscar_veterinario(cedula_vet)

        if clinica.veterinario_ocupado(veterinario, fecha, hora):          # Regla 2
            raise ReglaNegocioError(
                f"El veterinario {veterinario.nombre} ya tiene una cita programada el "
                f"{fecha.strftime('%d/%m/%Y')} a las {hora.strftime('%H:%M')}.")
        if clinica.mascota_ocupada(animal, fecha, hora):                    # Regla 3
            raise ReglaNegocioError(
                f"La mascota {animal.nombre} ya tiene una cita programada el "
                f"{fecha.strftime('%d/%m/%Y')} a las {hora.strftime('%H:%M')}.")

        codigo = self._repositorio.siguiente_codigo_cita()
        cita = Cita(codigo, fecha, hora, animal, veterinario, servicio)
        clinica.agregar_cita(cita)
        return cita

    def cancelar_cita(self, codigo, fecha_actual):
        cita = self._repositorio.buscar_cita(codigo)
        cita.cancelar(fecha_actual)                                          # Regla 4
        return cita

    def atender_cita(self, codigo, servicios_adicionales):
        cita = self._repositorio.buscar_cita(codigo)
        clinica = self._repositorio.buscar_clinica_de_cita(codigo)
        if not cita.esta_programada():                                       # Regla 5
            raise ReglaNegocioError(
                f"La cita {cita.codigo} está en estado {cita.estado.value}; "
                "solo se pueden atender citas en estado Programada.")

        # Se validan todos los servicios antes de modificar la cita
        adicionales = []
        usados = {s.codigo for s in cita.servicios}
        for codigo_servicio in servicios_adicionales:
            servicio = clinica.buscar_servicio(codigo_servicio)
            if servicio.codigo in usados:
                raise ReglaNegocioError(
                    f"El servicio {servicio.codigo} ya está incluido en la cita {cita.codigo}.")
            usados.add(servicio.codigo)
            adicionales.append(servicio)

        for servicio in adicionales:
            cita.agregar_servicio(servicio)
        cita.atender()

        numero = self._repositorio.siguiente_numero_factura()
        detalles = [DetalleFactura(s.nombre, s.tarifa) for s in cita.servicios]
        factura = Factura(numero, cita.fecha, cita.mascota.propietario, cita.mascota, detalles)  # Regla 6
        cita.asignar_factura(factura)
        return factura

    def consultar_citas(self, nit, fecha):
        clinica = self._repositorio.buscar_clinica(nit)
        return clinica.citas_del_dia(fecha)

    def consultar_historial(self, nit, cedula, mascota):
        clinica = self._repositorio.buscar_clinica(nit)
        animal = clinica.buscar_propietario(cedula).buscar_mascota(mascota)
        citas = [c for c in clinica.citas if c.mascota is animal]
        return sorted(citas, key=lambda c: (c.fecha, c.hora))
