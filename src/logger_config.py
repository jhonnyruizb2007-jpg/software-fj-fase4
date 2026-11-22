"""Configuración centralizada de logging para archivo y consola."""
import logging
from pathlib import Path


def configurar_logger(nombre: str = "software_fj", archivo: str = "software_fj.log") -> logging.Logger:
    """Crea un logger sin duplicar manejadores al importar varias veces."""
    logger = logging.getLogger(nombre)
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        formato = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        ruta = Path(archivo)
        file_handler = logging.FileHandler(ruta, encoding="utf-8")
        file_handler.setFormatter(formato)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formato)
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    return logger
