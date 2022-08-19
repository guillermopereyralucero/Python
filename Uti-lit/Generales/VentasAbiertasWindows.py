"""
Para obtener todas las ventanas abiertas y medidas de ellas
"""

#LIBRERIAS
import pywinauto

#DEFINICION
def ventanasWindows(uiaOwin32):
  ventanasAbiertas = pywinauto.Desktop(backend=uiaOwin32).windows() # backend="uia" or backend="win32" by default
  for v in ventanasAbiertas:
      print(v.window_text(), v.rectangle())

#EJECUCIÓN
ventanasWindows('uia')


