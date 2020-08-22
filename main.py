import webbrowser#pagia web
import os

salir = True
url_lista=[]
while salir==True:
    print('Utilice los comandos diponibles')
    #comando = input().upper()#solictar comando
    comando = input().lower()#MINUSCULAS
    separador = ","
    sep_palabras = comando.split(separador)#SEPARAR EN UNA LISTA
    if sep_palabras[0] == 'cargar':
        if len(sep_palabras)==1:#NO HA SLECCIONADO NINGUN ARCHIVO
            print("No Ha Seleccionado Ningun Archivo")
        else:
            i=1
            for i in range(len(sep_palabras)-1):
                str1=""#SEPARA LAS PALABRAS
                n_palabra=str1.join(sep_palabras[i+1])#UNE LA PALBRA Y LA SACA
                url=n_palabra+".json"#AGREGA LA EXTENSION
                my_path = os.path.abspath(os.path.dirname(__file__))#URL DE CADA ARCHIVO
                path_1 = os.path.join(my_path, '..\\Python-Html_1\\',url)#URL ABSOLUTA
                print(path_1)
            print("cargando...")


    elif sep_palabras[0] == 'seleccionar':
        print("seleccionando...")
    elif sep_palabras[0] == 'maximo':
        print("Calculando Maximo...")
    elif sep_palabras[0] == 'minimo':
        print("Calculando Minimo...")
    elif sep_palabras[0] == 'suma':
        print("Sumando...")
    elif sep_palabras[0] == 'cuenta':
        print("Calculando Cuenta...")
    elif sep_palabras[0] == 'reportar':
        print("Generando Html...")
    elif sep_palabras[0] == 'salir':
        salir = False
    else:
        print("Otras Opciones")



f = open('holamundo.html','w')#nombre documento pagina web

principal = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <link rel="stylesheet" href="css/css.css">
  <title>Document</title>
</head><body>"""
cuerpo= comando
fin= """
</body>
</html>"""

f.write(principal)#inicio
f.write(cuerpo)#medio
f.write(fin)#final
f.close()#cerar
webbrowser.open_new_tab('holamundo.html')#generar
