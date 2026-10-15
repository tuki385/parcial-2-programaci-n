"""Funciones de apoyo para validar datos de entrada en las entidades."""
from logica.excepciones import ReglaNegocioError


def texto_obligatorio(valor, campo):
    if valor is None or not str(valor).strip():
        raise ReglaNegocioError(f"El campo '{campo}' es obligatorio.")
    return str(valor).strip()


def numero_positivo(valor, campo):
    try:
        numero = float(valor)
    except (TypeError, ValueError):
        raise ReglaNegocioError(f"El campo '{campo}' debe ser un número.")
    if numero <= 0:
        raise ReglaNegocioError(f"El campo '{campo}' debe ser mayor que cero.")
    return numero
