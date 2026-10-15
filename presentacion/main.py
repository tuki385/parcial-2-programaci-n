from datos.repositorio_clinicas import RepositorioClinicas
from logica.servicio_citas import ServicioCitas
from logica.servicio_clinicas import ServicioClinicas
from presentacion.menu_consola import MenuConsola


class Main:
    """Punto de entrada: crea los objetos de cada capa y arranca el menú."""

    @staticmethod
    def main():
        repositorio = RepositorioClinicas()
        servicio_clinicas = ServicioClinicas(repositorio)
        servicio_citas = ServicioCitas(repositorio)
        menu = MenuConsola(servicio_clinicas, servicio_citas)
        menu.iniciar()
