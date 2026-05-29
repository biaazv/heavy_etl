import logging
import sys

def configurar_logging():
    """Configura o sistema de logging para o projeto."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )

    # Reduz o nível de log de bibliotecas externas se necessário
    logging.getLogger("sqlalchemy").setLevel(logging.WARNING)
