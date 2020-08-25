import webbrowser#pagia web
import os#URL ABSOLUTA
import os.path#SI EXISTE FICHERO
import json

#--
salir = True
url_lista=[]
atributos=[]
caracteristicas=[]

def seleccionando():
    atri_cara=[]
    for id_url in range(len(url_lista)):
        with open(url_lista[id_url],'r') as miarchivo:
                datos=miarchivo.read()
        objeto=json.loads(datos)
        for d in objeto:
        #SEPARA POR ATRIBUTOS: CARACTERISTICAS
            items = d.items()
            for id_item in items:
                atributos.append(id_item[0]), caracteristicas.append(id_item[1])#OBTIENE NOMBRE:"ALEX"  
                #keys = d.keys() obtiene los nombres,#values=d.values() obtiene los atributos,#print(keys,":::::::",values)
            #print(str(atributos),":::",str(caracteristicas))
    atri_cara.append(atributos)
    atri_cara.append(caracteristicas)
    return atri_cara

def atributoxxx(str):
    #TRANSFORMANDO
    ayuda=seleccionando()
    atri=ayuda[0]
    carac=ayuda[1]
    for i in range(len(atri)-1):#CICLO PARA NOMBRE:AXEL
        if atri[i]==str:
            if str=='nombre':
                print(str(atri[i]),'=','"',str(carac[i]),'"')
            else:
                print(str(atri[i]),'=',str(carac[i]))

while salir==True:
    print('Utilice los comandos diponibles')
    #comando = input().upper()#solictar comando
    comando = input().lower()#MINUSCULAS
    comando=comando+" "#AYUDA A QUE LA MATRIZ SE QUEDE EN 2 DE TAMAÑO, CAUSA ERROR
    separador_coma = ","
    seprador_espacio=" "
    sep_palabras_es= comando.split(seprador_espacio)#SEPARA COMANDO NOMBRE,HOLA,ET

    sep_palabras_coma = sep_palabras_es[1].split(separador_coma)#SEPARAR EN UNA LISTA LAS OPCIONES ELEGIADAS
    #print(sep_palabras_coma)
    
    if sep_palabras_es[0] == 'cargar':
        if len(sep_palabras_coma)==0:#NO HA SLECCIONADO NINGUN ARCHIVO
            print("No Ha Seleccionado Ningun Archivo")
        else:
            for id_urls in range(len(sep_palabras_coma)):
                sep_matriz=""#SEPARA LAS PALABRAS
                n_palabra=sep_matriz.join(sep_palabras_coma[id_urls])#UNE LA PALBRA Y LA SACA
                url=n_palabra+".json"#AGREGA LA EXTENSION
                my_path = os.path.abspath(os.path.dirname(__file__))#URL DE CADA ARCHIVO
                path_1 = os.path.join(my_path, '../Python-Html_1/',url)#URL ABSOLUTA
                if os.path.isfile(path_1)== True:#VALIDAR SI EXISTE EL ARCHIVO
                    url_lista.append(path_1)#AGREGA URLS DIRECTORIO
                    print("Url Agregada:", path_1)
                else:
                    print("Archivo No Existe: En Esta Carpeta")
                
            
    elif sep_palabras_es[0] == 'seleccionar*':
        #TRANSFORMANDO
        ayuda=seleccionando()
        atri=ayuda[0]
        carac=ayuda[1]
        #print("::",str(atri))
        #print("::",str(carac))
        for i in range(len(atri)-1):#CICLO PARA NOMBRE:AXEL  
            if str(atri[i]).lower()=='nombre':#NOMBRE ESTA EN MAYSUCULA
                print(str(atri[i]),'=','"',str(carac[i]),'"')#IMP EN PANTALLA NOMBRE="HOLA"
            else:
                print(str(atri[i]),'=',str(carac[i]))#IMP EDAD=15
    

    elif sep_palabras_es[0] == 'seleccionar':
        #TRANSFORMANDO
        for id in range(len(sep_palabras_coma)):
            if str(sep_palabras_coma[id])=='nombre':
                atributoxxx("nombre")
                print('nombre')
            elif str(sep_palabras_coma[id])=='edad':
                print('edad')
            elif str(sep_palabras_coma[id])=='activo':
                print('activo')
            elif str(sep_palabras_coma[id])=='promedio':
                print('promedio')
            
        print("xd...")


    elif sep_palabras_es[0] == 'maximo':
        print("Calculando Maximo...")


    elif sep_palabras_es[0] == 'minimo':
        print("Calculando Minimo...")


    elif sep_palabras_es[0] == 'suma':
        print("Sumando...")


    elif sep_palabras_es[0] == 'cuenta':
        print("Calculando Cuenta...")


    elif sep_palabras_es[0] == 'reportar':
        print("Generando Html...")


    elif sep_palabras_es[0] == 'salir':
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
