#--------------------------crea pagina web
import webbrowser
#---------------------------carga n archivos
comando = input().upper()# entrada de teclado mayuscula
#print(comando)
#salir = true
if comando == 'CARGAR':
    print("cargando...")
elif comando == 'SELECCIONAR':
    print("seleccionando...")
else:
    print("NEL")

#f = open('holamundo.html','w')

import webbrowser

f = open('holamundo.html','w')
principio = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <link rel="stylesheet" href="css/css.css">
  <title>Document</title>
</head>
<body>"""

cuerpo= comando

final= """
</body>
</html>"""

f.write(principio)
f.write(cuerpo)
f.write(final)
f.close()
webbrowser.open_new_tab('holamundo.html')
