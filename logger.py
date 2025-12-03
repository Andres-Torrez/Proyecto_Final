import logging

# Configuracion de logger
logging.basicConfig(

    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s -- %(message)s",
    encoding="utf-8"
)

def log_info(msg):
    logging.info(msg)

def log_warning(msg):
    logging.warning(msg)

def log_error(msg):
    logging.error(msg)

