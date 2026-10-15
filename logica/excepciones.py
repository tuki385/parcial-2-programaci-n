class ReglaNegocioError(Exception):
    """Se lanza cuando una operación incumple una regla de negocio o una validación de datos."""

    def __init__(self, mensaje):
        super().__init__(mensaje)
        self._mensaje = mensaje

    @property
    def mensaje(self):
        return self._mensaje
