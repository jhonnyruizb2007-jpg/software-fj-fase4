# Universidad Nacional Abierta y a Distancia – UNAD
## Fase 4 – Componente práctico: prácticas simuladas
**Curso:** Programación (213023)  
**Programa:** Ingeniería de Sistemas  
**Estudiante:** [Nombre completo]  
**Código:** [Código del estudiante]  
**Tutor:** [Nombre del tutor]  
**Fecha:** [Fecha de entrega]

## Introducción
El presente trabajo desarrolla un sistema de consola para Software FJ, orientado a la gestión de clientes, servicios y reservas. La solución aplica programación orientada a objetos mediante abstracción, encapsulación, herencia y polimorfismo. También incorpora excepciones personalizadas y logging para controlar y registrar situaciones válidas e inválidas. La información se administra mediante objetos y listas en memoria, sin utilizar bases de datos; el archivo de log se emplea exclusivamente para registrar eventos y errores.

## Enlace del repositorio en GitHub
[PEGAR AQUÍ LA URL PÚBLICA DEL REPOSITORIO]

## Descripción breve de la solución
El sistema contiene una entidad abstracta, la clase Cliente, una jerarquía de servicios con tres especializaciones, una clase Reserva y una clase administradora con listas internas. El punto de entrada ejecuta trece simulaciones aisladas y registra sus resultados en consola y en `software_fj.log`.

## Conclusiones
1. La abstracción y la herencia permiten definir contratos comunes y especializar los servicios sin duplicar toda la lógica.
2. La encapsulación y las propiedades protegen los datos del cliente mediante validaciones centralizadas.
3. Las excepciones personalizadas y el registro de eventos permiten identificar fallos y mantener la ejecución de los escenarios posteriores.
4. El uso de listas y objetos en memoria cumple la restricción de no utilizar bases de datos, aunque implica que los datos desaparecen al cerrar la aplicación.

## Referencias
Cuevas Álvarez, A. (2016). *Python 3: curso práctico*. RA-MA Editorial. https://elibro.bibliotecavirtual.unad.edu.co/es/ereader/unad/106404?page=373

Romano, F., Baka, B., & Phillips, D. (2019). *Getting started with Python: Understand key data structures and use Python in object-oriented programming*. Packt Publishing. https://research-ebsco-com.bibliotecavirtual.unad.edu.co/linkprocessor/plink?id=b41fd66a-1134-3dcd-8dba-90f36451f08d

Silva, F. D. (2025). *Basics of using GitHub* [Objeto virtual de información (OVI)]. Repositorio Institucional UNAD. https://repository.unad.edu.co/handle/10596/75882

Van Rossum, G., & Drake, F. L., Jr. (2024). *El tutorial de Python*. Python Software Foundation. https://docs.python.org/es/3.12/tutorial/errors.html

Zambrano, J. P. (2025). *Introducción al uso de GitHub* [Objeto virtual de información (OVI)]. Repositorio Institucional UNAD. https://repository.unad.edu.co/handle/10596/75876
