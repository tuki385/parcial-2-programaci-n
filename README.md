# Citas veterinarias – Parcial 2 de Programación II

Aplicación de consola en Python para gestionar las citas de clínicas veterinarias.

## Cómo ejecutarla

```
python main.py
```
Requiere Python 3.8 o superior. No usa librerías externas.

## Estructura (arquitectura en capas)

| Carpeta | Capa | Contenido |
|---|---|---|
| `presentacion/` | Presentación | `Main`, `MenuConsola` |
| `logica/` | Lógica | `ServicioClinicas`, `ServicioCitas`, `ReglaNegocioError` |
| `datos/` | Datos | `RepositorioClinicas` |
| `entidades/` | Entidades | `Clinica`, `Municipio`, `Veterinario`, `Servicio`, `Propietario`, `Mascota`, `Cita`, `EstadoCita`, `Factura`, `DetalleFactura` |

`main.py` solo lanza `Main.main()`.

## Uso rápido
1. Opción **1** carga las dos clínicas del ejemplo (veterinarios y catálogos).
2. Registrar propietarios y mascotas (opciones 5 y 6) y programar citas (opción 7).
3. Ver `pruebas/guion_pruebas.md` para los datos de los 5 casos de prueba.

## Reglas de negocio
Se validan en las clases indicadas en el documento de diseño; cuando una se incumple se lanza
`ReglaNegocioError` y el menú muestra el motivo sin detener la aplicación.
