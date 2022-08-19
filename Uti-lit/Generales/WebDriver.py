"""
Para instalar y manipular controlador web Chrome
"""

#LIBRERIAS
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#DEFINICION
def webDriver(wait):
  control=webdriver.Chrome(ChromeDriverManager().install()) #Abre y/o instala webdriver
  control.implicitly_wait(wait) #Cuando algo no aparece, prueba cada 1 seg. durante 40 seg. 
  control.delete_all_cookies()
  print(" Iniciando navegador Web.")
  control.get('https://movistar.com.ar')    #URL A AUTOMATIZAR
  control.maximize_window()
  #busca=control.find_element(By.ID,'ACA VA EL ID').send_keys('ACA VA LO QUE SE QUIERA ESCRIBIR')

#EJECUCIÓN
webDriver(40)
