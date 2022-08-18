"""
Ubicándolo al final muestra por consola/pantalla cuando falta para el cierre 
"""

#LIBRERIAS
import time as TM

#DEFINICION
def contador(tm):
  for i in range(tm):
    print("Cerrando en "+str(tm))
    TM.sleep(1)
    #plog(str("Cerrando en "+str(tm)))  #Si se agrega el log y la función plog, también lo registra en el log.
    tm-=1
  print("Cerrado.")

#EJECUCIÓN
contador(5)
