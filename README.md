# Sistema Software FJ – Fase 4

## Descripción del proyecto

Software FJ es una aplicación desarrollada en Python para la gestión de clientes, servicios y reservas. Su implementación aplica principios de programación orientada a objetos y mecanismos de manejo de excepciones para controlar errores y mantener la continuidad de las operaciones.

El sistema permite registrar clientes, administrar diferentes tipos de servicios y gestionar reservas mediante operaciones de creación, confirmación, cancelación y procesamiento.

## Funcionalidades principales

- **Gestión de clientes:** creación de clientes y validación de sus datos.
- **Administración de servicios:** manejo de reservas de salas, alquiler de equipos y asesorías especializadas.
- **Gestión de reservas:** creación y control de los estados de las reservas.
- **Manejo de excepciones:** implementación de excepciones personalizadas para controlar situaciones inválidas y errores durante la ejecución.
- **Registro de eventos:** almacenamiento de eventos y errores en un archivo de logs.
- **Pruebas de funcionamiento:** simulación de operaciones válidas e inválidas para verificar el comportamiento del sistema.

## Estructura del proyecto

```text
software_fj_fase4/
│
├── main.py
├── README.md
├── software_fj.log
│
└── src/
    ├── exceptions.py
    ├── logger_config.py
    ├── models.py
    ├── services.py
    └── booking.py
```

## Tecnologías utilizadas

- Python 3.
- Programación orientada a objetos.
- Manejo de excepciones.
- Módulo `logging` para el registro de eventos.
- Git y GitHub para el control de versiones y alojamiento del código fuente.

## Ejecución del proyecto

Para ejecutar la aplicación, es necesario tener Python 3 instalado.

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/jhonnyruizb2007-jpg/software-fj-fase4.git
   ```

2. Ingresar a la carpeta del proyecto:

   ```bash
   cd software-fj-fase4
   ```

3. Ejecutar el programa principal:

   ```bash
   python main.py
   ```

Durante la ejecución se realizan diferentes simulaciones que permiten observar el funcionamiento de las clases, las validaciones y el manejo de excepciones. Los eventos y errores registrados pueden consultarse en el archivo `software_fj.log`.

## Consideraciones

La aplicación utiliza estructuras de datos en memoria para gestionar la información. No requiere conexión a una base de datos. El archivo de logs se utiliza para registrar eventos y errores durante la ejecución.

