# Software FJ – Fase 4 (Programación 213023)

Sistema de consola orientado a objetos para gestionar clientes, servicios y reservas. La información se conserva en listas y objetos en memoria; **no utiliza bases de datos ni archivos de datos**. El único archivo generado es `software_fj.log`, destinado al registro de eventos y errores.

## Requisitos
- Python 3.10 o superior.
- No requiere instalar paquetes externos.

## Estructura
```text
software_fj_fase4/
├── main.py
├── README.md
├── software_fj.log       # se crea al ejecutar
└── src/
    ├── __init__.py
    ├── exceptions.py
    ├── logger_config.py
    ├── models.py
    ├── services.py
    └── booking.py
```

## Ejecución
1. Descomprimir el proyecto.
2. Abrir una terminal en la carpeta `software_fj_fase4`.
3. Ejecutar `python main.py` (en algunos equipos: `python3 main.py`).
4. Revisar la salida de consola y el archivo `software_fj.log`.

## Diseño
- `Entidad` es la clase abstracta general.
- `Cliente` encapsula nombre, correo y teléfono con propiedades y validaciones.
- `Servicio` es abstracta. `ReservaSala`, `AlquilerEquipo` y `AsesoriaEspecializada` redefinen cálculo de subtotal y descripción.
- `Reserva` controla los estados PENDIENTE, CONFIRMADA, CANCELADA y PROCESADA.
- `SistemaSoftwareFJ` administra listas internas sin persistencia.
- `ErrorSoftwareFJ` y sus subclases representan errores del dominio.
- `configurar_logger` registra fecha, nivel y contexto en consola y archivo.

## Casos de prueba
El programa ejecuta 13 escenarios: altas válidas e inválidas, creación de servicios, reservas exitosas y fallidas, disponibilidad, cancelaciones y cálculos de costos. Cada escenario se aísla con `try/except/else/finally`, de modo que un fallo no impide ejecutar los siguientes.

## Decisiones y límites
La tarifa de sala y asesoría se interpreta por hora; la tarifa de equipo se interpreta por día. Para el ejemplo se usa IVA configurable del 19 % y un descuento opcional. Estos valores son supuestos de simulación, no tarifas oficiales de Software FJ. Los datos se pierden al cerrar el programa, tal como exige el almacenamiento en memoria.

## Git: secuencia sugerida de commits individuales
1. `chore: crear estructura inicial del proyecto`
2. `feat: implementar entidades y validación de clientes`
3. `feat: agregar servicios especializados y cálculo polimórfico`
4. `feat: implementar reservas y estados del proceso`
5. `feat: incorporar excepciones personalizadas y logging`
6. `test: agregar simulaciones válidas e inválidas`
7. `docs: documentar ejecución y arquitectura`

En la descripción del repositorio, explicar con transparencia que el desarrollo se realizó individualmente por las circunstancias del grupo. No crear ramas o pull requests ficticios para aparentar colaboración.
