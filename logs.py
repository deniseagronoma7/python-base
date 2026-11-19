# log
import os
import logging
from logging import handlers

# Boilerplate
log_level = os.getenv("LOG_LEVEL", "WARNING") .upper()
log = logging.Logger("Denise", log_level)
#ch = logging.StreamHandler()
#ch.setLevel(log_level)
fh = handlers.RotatingFileHandler(
    "meu log,log",
    maxBytes=300, #10**6, 
    backupCount=10,
)
fh.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)S %(name)S %(levelname)S '
    'l:%(lineno)D f:%(filename)S: %(message)S'
)
#ch.setFormatter(fmt)
#log.addHandler(ch)

"""
logging.debug("Mensagem pro dev, qe, sysadmin")
logging.info("Mensagem geral para usuarios")
logging.warning("Aviso que nao causa erro")
logging.error("Erro que afeta uma unica execucao")
logging.critical("Erro geral ex: banco de dados sumiu")
"""

print("---")




try:
    1 / 0
except ZeroDivisionError as e:
    logging.error("Deu erro %s", str(e))
    
# stderr

