"""Servicios especializados con herencia, polimorfismo y costos flexibles."""
from abc import abstractmethod
from .models import Entidad
from .exceptions import ErrorServicioNoDisponible, ErrorCalculoCosto

class Servicio(Entidad):
    """Contrato abstracto para cualquier servicio comercial."""
    def __init__(self, identificador: str, nombre: str, tarifa_base: float, disponible: bool = True):
        super().__init__(identificador)
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del servicio es obligatorio.")
        if isinstance(tarifa_base, bool) or not isinstance(tarifa_base, (int, float)) or tarifa_base <= 0:
            raise ValueError("La tarifa base debe ser un número positivo.")
        self.nombre = nombre.strip()
        self.tarifa_base = float(tarifa_base)
        self.disponible = bool(disponible)

    def validar_disponibilidad(self) -> None:
        if not self.disponible:
            raise ErrorServicioNoDisponible(f"El servicio '{self.nombre}' no está disponible.")

    def calcular_costo(self, unidades: float = 1, *, impuesto: float = 0.19, descuento: float = 0) -> float:
        """Variante flexible: unidades, impuesto y descuento son opcionales."""
        try:
            if isinstance(unidades, bool) or unidades <= 0:
                raise ValueError("Las unidades deben ser positivas.")
            if not (0 <= impuesto <= 1) or not (0 <= descuento <= 1):
                raise ValueError("Impuesto y descuento deben estar entre 0 y 1.")
            subtotal = self._costo_base(float(unidades))
            total = subtotal * (1 - descuento) * (1 + impuesto)
            if total <= 0:
                raise ValueError("El costo calculado no es positivo.")
            return round(total, 2)
        except (TypeError, ValueError) as causa:
            raise ErrorCalculoCosto(f"No se pudo calcular el costo de {self.nombre}.") from causa

    @abstractmethod
    def _costo_base(self, unidades: float) -> float:
        """Calcula el subtotal específico del servicio."""

    @abstractmethod
    def describir(self) -> str:
        """Describe las condiciones del servicio."""

class ReservaSala(Servicio):
    """Alquiler de una sala por horas."""
    def __init__(self, identificador: str, nombre: str, tarifa_hora: float, capacidad: int, disponible: bool = True):
        super().__init__(identificador, nombre, tarifa_hora, disponible)
        if not isinstance(capacidad, int) or capacidad < 1:
            raise ValueError("La capacidad debe ser un entero positivo.")
        self.capacidad = capacidad

    def _costo_base(self, unidades: float) -> float:
        return self.tarifa_base * unidades

    def describir(self) -> str:
        return f"Sala '{self.nombre}', capacidad {self.capacidad}, tarifa/hora ${self.tarifa_base:.2f}"

class AlquilerEquipo(Servicio):
    """Alquiler de equipos por día; la cantidad representa días."""
    def __init__(self, identificador: str, nombre: str, tarifa_dia: float, unidades_disponibles: int, disponible: bool = True):
        super().__init__(identificador, nombre, tarifa_dia, disponible)
        if not isinstance(unidades_disponibles, int) or unidades_disponibles < 1:
            raise ValueError("Las unidades disponibles deben ser un entero positivo.")
        self.unidades_disponibles = unidades_disponibles

    def _costo_base(self, unidades: float) -> float:
        if unidades > self.unidades_disponibles:
            raise ValueError("La cantidad solicitada supera las unidades disponibles.")
        return self.tarifa_base * unidades

    def describir(self) -> str:
        return f"Equipo '{self.nombre}', unidades disponibles {self.unidades_disponibles}, tarifa/día ${self.tarifa_base:.2f}"

class AsesoriaEspecializada(Servicio):
    """Asesoría facturada por hora con recargo por especialidad."""
    def __init__(self, identificador: str, nombre: str, tarifa_hora: float, especialidad: str, recargo: float = 0.15, disponible: bool = True):
        super().__init__(identificador, nombre, tarifa_hora, disponible)
        if not isinstance(especialidad, str) or not especialidad.strip():
            raise ValueError("La especialidad es obligatoria.")
        if not 0 <= recargo <= 1:
            raise ValueError("El recargo debe estar entre 0 y 1.")
        self.especialidad = especialidad.strip()
        self.recargo = recargo

    def _costo_base(self, unidades: float) -> float:
        return self.tarifa_base * unidades * (1 + self.recargo)

    def describir(self) -> str:
        return f"Asesoría en {self.especialidad}: ${self.tarifa_base:.2f}/hora + recargo {self.recargo:.0%}"
