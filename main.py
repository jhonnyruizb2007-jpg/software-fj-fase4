"""Punto de entrada: ejecuta diez o más escenarios sin detener la aplicación."""
import logging
from src.logger_config import configurar_logger
from src.models import Cliente
from src.services import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from src.booking import Reserva, SistemaSoftwareFJ
from src.exceptions import ErrorSoftwareFJ

logger = configurar_logger()
sistema = SistemaSoftwareFJ(logger)


def ejecutar_prueba(numero, titulo, operacion):
    """Aísla cada simulación: registra éxito o error y permite continuar."""
    logger.info("SIMULACIÓN %02d - %s", numero, titulo)
    try:
        operacion()
    except ErrorSoftwareFJ as error:
        logger.exception("Error controlado en simulación %02d: %s", numero, error)
    except (TypeError, ValueError) as error:
        logger.exception("Error de datos en simulación %02d: %s", numero, error)
    except Exception:
        logger.exception("Error inesperado en simulación %02d", numero)
    else:
        logger.info("Simulación %02d finalizada correctamente.", numero)
    finally:
        logger.info("Fin del escenario %02d; el sistema continúa activo.", numero)


def caso_cliente_valido():
    cliente = Cliente("C001", "Ana Pérez", "ana@example.com", "3001234567")
    sistema.registrar_cliente(cliente)
    sistema.cliente_demo = cliente

def caso_cliente_invalido():
    Cliente("C002", "A", "correo-invalido", "12")

def caso_servicio_sala():
    servicio = ReservaSala("S001", "Sala Norte", 50000, 12)
    sistema.registrar_servicio(servicio)
    sistema.sala_demo = servicio

def caso_servicio_equipo():
    servicio = AlquilerEquipo("S002", "Portátil", 80000, 5)
    sistema.registrar_servicio(servicio)
    sistema.equipo_demo = servicio

def caso_servicio_asesoria():
    servicio = AsesoriaEspecializada("S003", "Consultoría TI", 100000, "Ciberseguridad")
    sistema.registrar_servicio(servicio)
    sistema.asesoria_demo = servicio

def caso_servicio_invalido():
    ReservaSala("S004", "Sala imposible", -10, 0)

def caso_reserva_exitosa():
    reserva = Reserva("R001", sistema.cliente_demo, sistema.sala_demo, 2)
    sistema.crear_reserva(reserva)
    reserva.confirmar()
    costo = reserva.procesar(descuento=0.10)
    logger.info("Costo final reserva R001: $%.2f", costo)

def caso_reserva_sin_confirmar():
    reserva = Reserva("R002", sistema.cliente_demo, sistema.equipo_demo, 1)
    sistema.crear_reserva(reserva)
    reserva.procesar()

def caso_servicio_no_disponible():
    servicio = ReservaSala("S005", "Sala fuera de servicio", 40000, 8, disponible=False)
    sistema.registrar_servicio(servicio)
    reserva = Reserva("R003", sistema.cliente_demo, servicio, 1)
    sistema.crear_reserva(reserva)
    reserva.confirmar()

def caso_cancelacion():
    reserva = Reserva("R004", sistema.cliente_demo, sistema.asesoria_demo, 1)
    sistema.crear_reserva(reserva)
    reserva.confirmar()
    reserva.cancelar()
    logger.info("Estado final R004: %s", reserva.estado)

def caso_calculo_invalido():
    sistema.sala_demo.calcular_costo(2, impuesto=2.5)

def caso_cancelar_procesada():
    reserva = Reserva("R005", sistema.cliente_demo, sistema.sala_demo, 1)
    sistema.crear_reserva(reserva)
    reserva.confirmar()
    reserva.procesar()
    reserva.cancelar()

def caso_calculo_polimorfico():
    for servicio in (sistema.sala_demo, sistema.equipo_demo, sistema.asesoria_demo):
        logger.info("%s | costo de una unidad: $%.2f", servicio.describir(), servicio.calcular_costo())

def main():
    """Ejecuta casos válidos e inválidos; cada uno está aislado."""
    pruebas = [
        ("Registro válido de cliente", caso_cliente_valido),
        ("Registro inválido de cliente", caso_cliente_invalido),
        ("Creación de sala", caso_servicio_sala),
        ("Creación de alquiler de equipo", caso_servicio_equipo),
        ("Creación de asesoría", caso_servicio_asesoria),
        ("Creación de servicio inválido", caso_servicio_invalido),
        ("Reserva, confirmación y procesamiento exitosos", caso_reserva_exitosa),
        ("Procesamiento sin confirmar", caso_reserva_sin_confirmar),
        ("Reserva de servicio no disponible", caso_servicio_no_disponible),
        ("Confirmación y cancelación", caso_cancelacion),
        ("Parámetros inconsistentes en cálculo", caso_calculo_invalido),
        ("Intento de cancelar reserva procesada", caso_cancelar_procesada),
        ("Cálculo polimórfico de los tres servicios", caso_calculo_polimorfico),
    ]
    logger.info("===== INICIO DE PRUEBAS SOFTWARE FJ =====")
    for numero, (titulo, operacion) in enumerate(pruebas, start=1):
        ejecutar_prueba(numero, titulo, operacion)
    logger.info("===== FIN DE PRUEBAS. Reservas en memoria: %d =====", len(sistema.reservas))

if __name__ == "__main__":
    main()
