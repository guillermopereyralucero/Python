"""
Permite verificar si se está ejecutando un proceso (por PID o por NOMBRE) en cualquier equipo de la red. 
"""

#LIBRERIAS
import os

#DEFINICION
def controlProcesos(proceso):
  procesos=['FTTH.exe','VOIP.exe']
  for i in range(len(procesos)):
    comando=r'TASKLIST /S HOSTNAME /u USER /p PASS /nh /fi "IMAGENAME eq '+procesos[i]+'"'   #Comando CMD para buscar proceso       
    resultado=os.popen(comando)   #Manda comando por CMD
    datos=str(resultado.readlines())   #Lee resultado
    print(datos)
    if datos.startswith("['\\n', '"+str(procesos[i])):
      print("Proceso '{}' ejecutandose con normalidad.".format(procesos[i]))
    else:
      if datos.startswith("['INFORMAC"):
        print(asunto_proc_sin_ini)
      else:
        print("Error. Verificar servidor CGTECVM y que el proceso '{}' esté ejecutandose.".format(procesos[i]))

      

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
