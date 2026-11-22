"""Entidades generales y clientes del sistema."""
from abc import ABC, abstractmethod
from datetime import datetime
from .exceptions import ErrorValidacionCliente

class Entidad(ABC):
    """Clase abstracta común: toda entidad posee identificador y fecha de creación."""
    def __init__(self, identificador: str):
        if not isinstance(identificador, str) or not identificador.strip():
            raise ValueError("El identificador es obligatorio.")
        self._id = identificador.strip()
        self._creado_en = datetime.now()

    @property
    def id(self) -> str:
        return self._id

    @property
    def creado_en(self) -> datetime:
        return self._creado_en

    @abstractmethod
    def describir(self) -> str:
        """Devuelve una descripción legible de la entidad."""

class Cliente(Entidad):
    """Cliente con atributos encapsulados y validación en propiedades."""
    def __init__(self, identificador: str, nombre: str, correo: str, telefono: str):
        super().__init__(identificador)
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not isinstance(valor, str) or len(valor.strip()) < 2:
            raise ErrorValidacionCliente("El nombre debe tener al menos dos caracteres.")
        self._nombre = valor.strip().title()

    @property
    def correo(self) -> str:
        return self._correo

    @correo.setter
    def correo(self, valor: str) -> None:
        if not isinstance(valor, str) or valor.count("@") != 1 or "." not in valor.split("@")[-1]:
            raise ErrorValidacionCliente("El correo electrónico no tiene un formato válido.")
        self._correo = valor.strip().lower()

    @property
    def telefono(self) -> str:
        return self._telefono

    @telefono.setter
    def telefono(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.isdigit() or not (7 <= len(valor) <= 15):
            raise ErrorValidacionCliente("El teléfono debe contener entre 7 y 15 dígitos.")
        self._telefono = valor

    def describir(self) -> str:
        return f"Cliente {self.nombre} | {self.correo} | {self.telefono}"
