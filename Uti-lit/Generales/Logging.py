"""
Log de errores que escribe en archivo y muestra por consola/pantalla.
"""

#LIBRERIAS
import os
import datetime
import logging
import time as TM

#DEFINICION

#LOG - Para errores e información importante
def log(ruta):
  global logger
  log=ruta+f'_{datetime.datetime.now().strftime("%Y-%m-%d")}.txt'
  print(f'Log en archivo: {log}')
  check=os.makedirs(os.path.dirname(log),exist_ok=True)
  logger=logging.getLogger(__name__)
  logger.setLevel(logging.DEBUG)
  file_handler=logging.FileHandler(log)
  file_handler.setFormatter(logging.Formatter('\n%(asctime)s - %(levelname)s - at line: %(lineno)d - %(message)s'))
  stream_handler=logging.StreamHandler()
  stream_handler.setFormatter(logging.Formatter('\n%(asctime)s - %(levelname)s - at line: %(lineno)d - %(message)s'))
  logger.addHandler(file_handler) #Escritura en archivo log
  logger.addHandler(stream_handler) #Salida por pantalla/consola


#EJECUCIÓN
log('C:/Users/pereyragu/OneDrive - Telefonica/AutoPython/Desarrollo/Logs/AS2')  #Ruta Ejemplo
logger.debug("123")
