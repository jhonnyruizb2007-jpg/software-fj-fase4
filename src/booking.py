"""Reservas y operaciones del sistema en memoria."""
from .models import Entidad, Cliente
from .services import Servicio
from .exceptions import ErrorReservaInvalida, ErrorServicioNoDisponible

class Reserva(Entidad):
    """Relaciona un cliente con un servicio, duración y estado."""
    ESTADOS = {"PENDIENTE", "CONFIRMADA", "CANCELADA", "PROCESADA"}

    def __init__(self, identificador: str, cliente: Cliente, servicio: Servicio, duracion: float):
        super().__init__(identificador)
        if not isinstance(cliente, Cliente) or not isinstance(servicio, Servicio):
            raise ErrorReservaInvalida("La reserva requiere un Cliente y un Servicio válidos.")
        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)) or duracion <= 0:
            raise ErrorReservaInvalida("La duración debe ser un número positivo.")
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = float(duracion)
        self.estado = "PENDIENTE"

    def confirmar(self) -> None:
        if self.estado != "PENDIENTE":
            raise ErrorReservaInvalida(f"No se puede confirmar una reserva en estado {self.estado}.")
        self.servicio.validar_disponibilidad()
        self.estado = "CONFIRMADA"

    def cancelar(self) -> None:
        if self.estado in {"CANCELADA", "PROCESADA"}:
            raise ErrorReservaInvalida(f"No se puede cancelar una reserva en estado {self.estado}.")
        self.estado = "CANCELADA"

    def procesar(self, *, impuesto: float = 0.19, descuento: float = 0) -> float:
        if self.estado != "CONFIRMADA":
            raise ErrorReservaInvalida("Solo se pueden procesar reservas confirmadas.")
        self.servicio.validar_disponibilidad()
        costo = self.servicio.calcular_costo(self.duracion, impuesto=impuesto, descuento=descuento)
        self.estado = "PROCESADA"
        return costo

    def describir(self) -> str:
        return f"Reserva {self.id}: {self.cliente.nombre} -> {self.servicio.nombre} ({self.estado})"

class SistemaSoftwareFJ:
    """Fachada sencilla que administra listas internas, sin base de datos."""
    def __init__(self, logger):
        self.clientes = []
        self.servicios = []
        self.reservas = []
        self.logger = logger

    def registrar_cliente(self, cliente: Cliente) -> None:
        if not isinstance(cliente, Cliente):
            raise ErrorReservaInvalida("Se esperaba un objeto Cliente.")
        if any(c.id == cliente.id for c in self.clientes):
            raise ErrorReservaInvalida(f"Ya existe el cliente {cliente.id}.")
        self.clientes.append(cliente)
        self.logger.info("Cliente registrado: %s", cliente.describir())

    def registrar_servicio(self, servicio: Servicio) -> None:
        if not isinstance(servicio, Servicio):
            raise ErrorReservaInvalida("Se esperaba un objeto Servicio.")
        if any(s.id == servicio.id for s in self.servicios):
            raise ErrorReservaInvalida(f"Ya existe el servicio {servicio.id}.")
        self.servicios.append(servicio)
        self.logger.info("Servicio registrado: %s", servicio.describir())

    def crear_reserva(self, reserva: Reserva) -> None:
        if any(r.id == reserva.id for r in self.reservas):
            raise ErrorReservaInvalida(f"Ya existe la reserva {reserva.id}.")
        if reserva.cliente not in self.clientes or reserva.servicio not in self.servicios:
            raise ErrorReservaInvalida("Cliente y servicio deben estar registrados previamente.")
        self.reservas.append(reserva)
        self.logger.info("Reserva creada: %s", reserva.describir())
