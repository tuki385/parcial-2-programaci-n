from entidades.estado_cita import EstadoCita
from logica.excepciones import ReglaNegocioError


class Cita:
    def __init__(self, codigo, fecha, hora, mascota, veterinario, servicio):
        self._codigo = codigo
        self._fecha = fecha
        self._hora = hora
        self._estado = EstadoCita.PROGRAMADA          # Regla 1: al crearse queda Programada
        self._mascota = mascota
        self._veterinario = veterinario
        self._servicios = [servicio]
        self._factura = None

    @property
    def codigo(self):
        return self._codigo

    @property
    def fecha(self):
        return self._fecha

    @property
    def hora(self):
        return self._hora

    @property
    def estado(self):
        return self._estado

    @property
    def mascota(self):
        return self._mascota

    @property
    def veterinario(self):
        return self._veterinario

    @property
    def servicios(self):
        return list(self._servicios)

    @property
    def factura(self):
        return self._factura

    def esta_programada(self):
        return self._estado == EstadoCita.PROGRAMADA

    def cancelar(self, fecha_actual):
        """Regla 4: solo se cancela una cita Programada y antes de la fecha de la cita."""
        if not self.esta_programada():
            raise ReglaNegocioError(
                f"La cita {self._codigo} está en estado {self._estado.value}; "
                "solo se pueden cancelar citas en estado Programada.")
        if fecha_actual >= self._fecha:
            raise ReglaNegocioError(
                f"La cita {self._codigo} solo puede cancelarse antes de su fecha "
                f"({self._fecha.strftime('%d/%m/%Y')}).")
        self._estado = EstadoCita.CANCELADA

    def atender(self):
        """Regla 5: solo se atiende una cita Programada."""
        if not self.esta_programada():
            raise ReglaNegocioError(
                f"La cita {self._codigo} está en estado {self._estado.value}; "
                "solo se pueden atender citas en estado Programada.")
        self._estado = EstadoCita.ATENDIDA

    def agregar_servicio(self, servicio):
        if not self.esta_programada():
            raise ReglaNegocioError(
                f"No se pueden agregar servicios a la cita {self._codigo} porque está {self._estado.value}.")
        if any(s.codigo == servicio.codigo for s in self._servicios):
            raise ReglaNegocioError(
                f"El servicio {servicio.codigo} ya está incluido en la cita {self._codigo}.")
        self._servicios.append(servicio)

    def asignar_factura(self, factura):
        self._factura = factura
