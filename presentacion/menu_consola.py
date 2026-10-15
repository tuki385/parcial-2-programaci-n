from datetime import date, datetime

from entidades.municipio import Municipio
from logica.excepciones import ReglaNegocioError


class MenuConsola:
    """Capa de presentación: único contacto con el usuario. No contiene reglas de negocio."""

    def __init__(self, servicio_clinicas, servicio_citas):
        self._servicio_clinicas = servicio_clinicas
        self._servicio_citas = servicio_citas

    # ------------------------------------------------------------------ menú
    def iniciar(self):
        opciones = {
            "1": self.cargar_datos_ejemplo,
            "2": self.registrar_clinica,
            "3": self.registrar_veterinario,
            "4": self.registrar_servicio,
            "5": self.registrar_propietario,
            "6": self.registrar_mascota,
            "7": self.programar_cita,
            "8": self.cancelar_cita,
            "9": self.atender_cita,
            "10": self.consultar_citas_clinica,
            "11": self.consultar_historial_mascota,
        }
        while True:
            self._mostrar_menu()
            try:
                opcion = input("Seleccione una opción: ").strip()
                if opcion == "0":
                    print("Hasta pronto.")
                    break
                accion = opciones.get(opcion)
                if accion is None:
                    print("Opción no válida. Intente de nuevo.")
                    continue
                accion()
            except ReglaNegocioError as error:
                # Regla 8: se informa el motivo y la aplicación continúa
                print(f"\n[No se pudo completar la operación] {error}")
            except EOFError:
                break

    def _mostrar_menu(self):
        print("\n" + "=" * 50)
        print("        CITAS VETERINARIAS")
        print("=" * 50)
        print(" 1. Cargar datos de ejemplo (clínicas)")
        print(" 2. Registrar clínica")
        print(" 3. Registrar veterinario")
        print(" 4. Registrar servicio en el catálogo")
        print(" 5. Registrar propietario")
        print(" 6. Registrar mascota")
        print(" 7. Programar cita")
        print(" 8. Cancelar cita")
        print(" 9. Atender cita y generar factura")
        print("10. Consultar citas de una clínica en una fecha")
        print("11. Consultar historial de citas de una mascota")
        print(" 0. Salir")

    # -------------------------------------------------------- datos de ejemplo
    def cargar_datos_ejemplo(self):
        sc = self._servicio_clinicas
        san_gil = Municipio("68679", "San Gil", "Santander")
        sc.registrar_clinica("901456789-1", "Clínica Veterinaria Huellitas", san_gil, "Calle 12 # 9-40", "Centro")
        sc.registrar_veterinario("901456789-1", "63512478", "Juliana Ortiz Ramírez", "TP-18452")
        sc.registrar_veterinario("901456789-1", "91254863", "Mauricio Pinzón Gómez", "TP-20117")
        sc.registrar_servicio("901456789-1", "CG", "Consulta general", 60000)
        sc.registrar_servicio("901456789-1", "VAC", "Vacunación", 45000)
        sc.registrar_servicio("901456789-1", "DES", "Desparasitación", 30000)
        sc.registrar_servicio("901456789-1", "PEL", "Baño y peluquería", 50000)

        floridablanca = Municipio("68276", "Floridablanca", "Santander")
        sc.registrar_clinica("900987654-3", "Clínica Veterinaria Patitas Felices", floridablanca,
                             "Carrera 27 # 30-15", "Cañaveral")
        sc.registrar_veterinario("900987654-3", "13745821", "Sergio Arenas Villamizar", "TP-15893")
        sc.registrar_veterinario("900987654-3", "37896542", "Diana Carolina Rey Moreno", "TP-22406")
        sc.registrar_veterinario("900987654-3", "1098654321", "Felipe Castellanos Díaz", "TP-31578")
        sc.registrar_servicio("900987654-3", "CG", "Consulta general", 65000)
        sc.registrar_servicio("900987654-3", "VAC", "Vacunación", 48000)
        sc.registrar_servicio("900987654-3", "DES", "Desparasitación", 32000)
        sc.registrar_servicio("900987654-3", "ECO", "Ecografía", 120000)
        print("\nDatos de ejemplo cargados: Clínica Veterinaria Huellitas (NIT 901456789-1) y "
              "Clínica Veterinaria Patitas Felices (NIT 900987654-3).")

    # ------------------------------------------------------------- registros
    def registrar_clinica(self):
        print("\n--- Registrar clínica ---")
        nit = self._pedir("NIT")
        nombre = self._pedir("Nombre de la clínica")
        codigo_dane = self._pedir("Código DANE del municipio")
        municipio = self._pedir("Municipio")
        departamento = self._pedir("Departamento")
        direccion = self._pedir("Dirección")
        barrio = self._pedir("Barrio")
        clinica = self._servicio_clinicas.registrar_clinica(
            nit, nombre, Municipio(codigo_dane, municipio, departamento), direccion, barrio)
        print(f"\nClínica registrada: {clinica.nombre} (NIT {clinica.nit}).")

    def registrar_veterinario(self):
        print("\n--- Registrar veterinario ---")
        nit = self._pedir("NIT de la clínica")
        cedula = self._pedir("Cédula")
        nombre = self._pedir("Nombre completo")
        tarjeta = self._pedir("Tarjeta profesional")
        vet = self._servicio_clinicas.registrar_veterinario(nit, cedula, nombre, tarjeta)
        print(f"\nVeterinario registrado: {vet.nombre} ({vet.tarjeta_profesional}).")

    def registrar_servicio(self):
        print("\n--- Registrar servicio en el catálogo ---")
        nit = self._pedir("NIT de la clínica")
        codigo = self._pedir("Código del servicio")
        nombre = self._pedir("Nombre del servicio")
        tarifa = self._pedir_numero("Tarifa")
        servicio = self._servicio_clinicas.registrar_servicio(nit, codigo, nombre, tarifa)
        print(f"\nServicio registrado: {servicio.codigo} - {servicio.nombre} ({self._dinero(servicio.tarifa)}).")

    def registrar_propietario(self):
        print("\n--- Registrar propietario ---")
        nit = self._pedir("NIT de la clínica")
        cedula = self._pedir("Cédula del propietario")
        nombre = self._pedir("Nombre completo")
        telefono = self._pedir("Teléfono")
        municipio = self._pedir("Municipio de residencia")
        departamento = self._pedir("Departamento")
        codigo_dane = input("Código DANE (opcional, Enter para omitir): ").strip()
        prop = self._servicio_clinicas.registrar_propietario(
            nit, cedula, nombre, telefono, Municipio(codigo_dane, municipio, departamento))
        print(f"\nPropietario registrado: {prop.nombre} (cédula {prop.cedula}).")

    def registrar_mascota(self):
        print("\n--- Registrar mascota ---")
        nit = self._pedir("NIT de la clínica")
        cedula = self._pedir("Cédula del propietario")
        nombre = self._pedir("Nombre de la mascota")
        especie = self._pedir("Especie")
        raza = self._pedir("Raza")
        anio = self._pedir("Año aproximado de nacimiento")
        peso = self._pedir_numero("Peso (kg)")
        mascota = self._servicio_clinicas.registrar_mascota(nit, cedula, nombre, especie, raza, anio, peso)
        print(f"\nMascota registrada: {mascota.nombre} ({mascota.especie}, {mascota.raza}) "
              f"de {mascota.propietario.nombre}.")

    # ----------------------------------------------------------------- citas
    def programar_cita(self):
        print("\n--- Programar cita ---")
        nit = self._pedir("NIT de la clínica")
        cedula = self._pedir("Cédula del propietario")
        mascota = self._pedir("Nombre de la mascota")
        fecha = self._pedir_fecha("Fecha de la cita (AAAA-MM-DD)")
        hora = self._pedir_hora("Hora de la cita (HH:MM)")
        servicio = self._pedir("Código del servicio")
        cedula_vet = self._pedir("Cédula del veterinario")
        cita = self._servicio_citas.programar_cita(nit, cedula, mascota, fecha, hora, servicio, cedula_vet)
        print(f"\nCita {cita.codigo} programada para {cita.mascota.nombre} el "
              f"{self._fecha(cita.fecha)} a las {cita.hora.strftime('%H:%M')} con {cita.veterinario.nombre}.")

    def cancelar_cita(self):
        print("\n--- Cancelar cita ---")
        codigo = self._pedir("Código de la cita")
        texto = input("Fecha actual (AAAA-MM-DD, Enter para usar la de hoy): ").strip()
        fecha_actual = self._convertir_fecha(texto) if texto else date.today()
        cita = self._servicio_citas.cancelar_cita(codigo, fecha_actual)
        print(f"\nLa cita {cita.codigo} fue cancelada. Queda en el historial y no genera factura.")

    def atender_cita(self):
        print("\n--- Atender cita ---")
        codigo = self._pedir("Código de la cita")
        texto = input("Códigos de servicios adicionales separados por coma (Enter si no hay): ").strip()
        adicionales = [s.strip() for s in texto.split(",") if s.strip()]
        factura = self._servicio_citas.atender_cita(codigo, adicionales)
        self._mostrar_factura(factura)

    def consultar_citas_clinica(self):
        print("\n--- Consultar citas de una clínica ---")
        nit = self._pedir("NIT de la clínica")
        fecha = self._pedir_fecha("Fecha (AAAA-MM-DD)")
        citas = self._servicio_citas.consultar_citas(nit, fecha)
        print(f"\nCitas del {self._fecha(fecha)}:")
        if not citas:
            print("  No hay citas en esa fecha.")
        for cita in citas:
            self._mostrar_cita(cita)

    def consultar_historial_mascota(self):
        print("\n--- Historial de citas de una mascota ---")
        nit = self._pedir("NIT de la clínica")
        cedula = self._pedir("Cédula del propietario")
        mascota = self._pedir("Nombre de la mascota")
        citas = self._servicio_citas.consultar_historial(nit, cedula, mascota)
        print(f"\nHistorial de {mascota}:")
        if not citas:
            print("  La mascota no tiene citas.")
        for cita in citas:
            self._mostrar_cita(cita)

    # ------------------------------------------------------ apoyo de entrada
    def _pedir(self, texto):
        return input(f"{texto}: ").strip()

    def _pedir_numero(self, texto):
        valor = self._pedir(texto)
        try:
            return float(valor.replace(",", "."))
        except ValueError:
            raise ReglaNegocioError(f"'{valor}' no es un número válido.")

    def _convertir_fecha(self, texto):
        try:
            return datetime.strptime(texto, "%Y-%m-%d").date()
        except ValueError:
            raise ReglaNegocioError(f"'{texto}' no es una fecha válida. Use el formato AAAA-MM-DD.")

    def _pedir_fecha(self, texto):
        return self._convertir_fecha(self._pedir(texto))

    def _pedir_hora(self, texto):
        valor = self._pedir(texto)
        try:
            return datetime.strptime(valor, "%H:%M").time()
        except ValueError:
            raise ReglaNegocioError(f"'{valor}' no es una hora válida. Use el formato HH:MM.")

    # ----------------------------------------------------- apoyo de salida
    def _fecha(self, fecha):
        return fecha.strftime("%d/%m/%Y")

    def _dinero(self, valor):
        return "$ " + f"{valor:,.0f}".replace(",", ".")

    def _mostrar_cita(self, cita):
        servicios = ", ".join(s.nombre for s in cita.servicios)
        factura = f" | Factura: {cita.factura.numero}" if cita.factura else ""
        print(f"  {cita.codigo} | {self._fecha(cita.fecha)} {cita.hora.strftime('%H:%M')} | "
              f"{cita.mascota.nombre} ({cita.mascota.propietario.nombre}) | {cita.veterinario.nombre} | "
              f"{servicios} | Estado: {cita.estado.value}{factura}")

    def _mostrar_factura(self, factura):
        propietario = factura.propietario
        mascota = factura.mascota
        print("\n" + "=" * 50)
        print(f"FACTURA {factura.numero}")
        print(f"Fecha: {self._fecha(factura.fecha)}")
        print(f"Propietario: {propietario.nombre} - C.C. {propietario.cedula} - Tel. {propietario.telefono}")
        print(f"Mascota: {mascota.nombre} ({mascota.especie}, {mascota.raza})")
        print("-" * 50)
        for detalle in factura.detalles:
            print(f"  {detalle.servicio:<30}{self._dinero(detalle.tarifa):>16}")
        print("-" * 50)
        print(f"  {'TOTAL':<30}{self._dinero(factura.total()):>16}")
        print("=" * 50)
