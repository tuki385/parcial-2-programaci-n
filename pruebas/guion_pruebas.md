# Guion para los 5 casos de prueba

Ejecutar `python main.py` y seguir este orden. Entre paréntesis, el número de opción del menú.
Tomar una captura al final de cada caso.

**Preparación** – Opción **1** (cargar datos de ejemplo).

## Caso 1 – Cita atendida con servicio adicional
1. Opción **5** (propietario): NIT `901456789-1`, cédula `1098765432`, `Laura Méndez Plata`, teléfono `3157894561`, municipio `Bucaramanga`, departamento `Santander`, DANE (Enter).
2. Opción **6** (mascota): NIT `901456789-1`, cédula `1098765432`, `Rocky`, `Perro`, `Criolla`, `2023`, `18`.
3. Opción **7** (programar): NIT `901456789-1`, cédula `1098765432`, `Rocky`, `2026-11-10`, `09:00`, `CG`, veterinaria `63512478` → **CIT-001**.
4. *(Hacer el caso 2 antes de atender, porque la cita debe seguir programada.)*
5. Opción **9** (atender): `CIT-001`, adicionales `VAC` → **FAC-001** por **$ 105.000**.

## Caso 2 – Veterinario ocupado
1. Opción **5**: NIT `901456789-1`, cédula `1005678912`, `Camila Duarte Serrano`, teléfono `3204567812`, `San Gil`, `Santander`, DANE `68679`.
2. Opción **6**: NIT `901456789-1`, cédula `1005678912`, `Copito`, `Conejo`, `Cabeza de león`, `2025`, `1,5`.
3. Opción **7**: NIT `901456789-1`, cédula `1005678912`, `Copito`, `2026-11-10`, `09:00`, `DES`, `63512478` → **rechazada** (veterinaria ocupada).
4. Opción **7** otra vez, igual pero hora `10:00` → **CIT-002**.

## Caso 3 – Cita cancelada
1. Opción **5**: NIT `900987654-3`, cédula `1102345678`, `Andrés Rueda Ardila`, teléfono `3016789023`, `Piedecuesta`, `Santander`, DANE (Enter).
2. Opción **6**: NIT `900987654-3`, cédula `1102345678`, `Luna`, `Gato`, `Siamés`, `2022`, `4`.
3. Opción **7**: NIT `900987654-3`, cédula `1102345678`, `Luna`, `2026-11-12`, `15:00`, `ECO`, veterinario `13745821` → **CIT-003**.
4. Opción **8** (cancelar): `CIT-003`, fecha actual `2026-11-11` → cancelada, sin factura.

## Caso 4 – Cancelación no permitida
- Opción **8**: `CIT-001`, fecha actual `2026-11-11` → **rechazada** (ya fue atendida).

## Caso 5 – Consultas
- Opción **10**: NIT `901456789-1`, fecha `2026-11-10` → CIT-001 Atendida y CIT-002 Programada.
- Opción **11**: NIT `900987654-3`, cédula `1102345678`, `Luna` → CIT-003 Cancelada.
