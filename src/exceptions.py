"""Excepciones propias del dominio Software FJ."""

class ErrorSoftwareFJ(Exception):
    """Excepción base para errores controlados de la aplicación."""

class ErrorValidacionCliente(ErrorSoftwareFJ):
    """Datos personales del cliente inválidos."""

class ErrorServicioNoDisponible(ErrorSoftwareFJ):
    """El servicio no está habilitado para nuevas reservas."""

class ErrorReservaInvalida(ErrorSoftwareFJ):
    """La reserva no cumple las reglas del negocio."""

class ErrorCalculoCosto(ErrorSoftwareFJ):
    """No fue posible calcular un costo coherente."""
