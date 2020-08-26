import webbrowser#pagia web
import os#URL ABSOLUTA
import os.path#SI EXISTE FICHERO
import json

#--
salir = True
url_lista=[]


def seleccionando():
    atri_cara=[]#RETORNAR
    atributos=[]#NOMBRE,PROEMDIO
    caracteristicas=[]#AXEL,95
    for id_url in range(len(url_lista)):#OBTIENE EL URL DE UNA MATRIZ CON URLS
        with open(url_lista[id_url],'r') as miarchivo:#ABRE EL URL
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
    atri_cara=[]#RETORNAR
    atribuos=[]#NOMBRE,PROEMDIO
    caracteristicas=[]#AXEL,95
    #TRANSFORMANDO
    ayuda=seleccionando()
    atri=ayuda[0]
    carac=ayuda[1]
    for i in range(len(atri)):#CICLO PARA NOMBRE:AXEL
        if atri[i]==str:
            atribuos.append(atri[i]), caracteristicas.append(carac[i])#MATRIZ
            #IMPRIME LAS OPCIONES
            #if str=='nombre':
                #print(atri[i],'=','"',carac[i],'"')
            #else:
                #print(atri[i],'=',carac[i])
    atri_cara.append(atribuos), atri_cara.append(caracteristicas)
    return atri_cara#RETORNA LA MATRIZ

while salir==True:
    print('Utilice los comandos diponibles')
    #comando = input().upper()#solictar comando
    comando = input().lower()#MINUSCULAS
    comando=comando+" "#AYUDA A QUE LA MATRIZ SE QUEDE EN 2 DE TAMAÑO, CAUSA ERROR
    separador_coma = ","#AYUDASEPARA LAS OPCIONES CON COMAS
    seprador_espacio=" "#AYUDASEPARA EL COMANDO CON LAS OPCIONES
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
                ayuda=atributoxxx("nombre")#FUNCION PARA OBTENER LOS DATOS:DATOS
                #DIVIDIR EN 2 MATRICES
                Atributos=ayuda[0]
                Caracteristica=ayuda[1]
                for a in range(len( Atributos)):#CICLO IMPRIME
                    print(Atributos[a],'=','"',Caracteristica[a],'"')

            elif str(sep_palabras_coma[id])=='edad':
                ayuda=atributoxxx("edad")
                #DIVIDIR EN 2 MATRICES
                Atributos=ayuda[0]
                Caracteristica=ayuda[1]
                for a in range(len( Atributos)):#CICLO IMPRIME
                    print(Atributos[a],'=',Caracteristica[a])

            elif str(sep_palabras_coma[id])=='activo':
                ayuda=atributoxxx("activo")
                #DIVIDIR EN 2 MATRICES
                Atributos=ayuda[0]
                Caracteristica=ayuda[1]
                for a in range(len( Atributos)):#CICLO IMPRIME
                    print(Atributos[a],'=',Caracteristica[a])

            elif str(sep_palabras_coma[id])=='promedio':
                ayuda=atributoxxx("promedio")
                #DIVIDIR EN 2 MATRICES
                Atributos=ayuda[0]
                Caracteristica=ayuda[1]
                for a in range(len( Atributos)):#CICLO IMPRIME
                    print(Atributos[a],'=',Caracteristica[a])

    elif sep_palabras_es[0] == 'maximo':
        if str(sep_palabras_coma[0])=='edad':
            ayuda=atributoxxx("edad")#FUNCION PARA OBTENER LOS DATOS:DATOS
            #DIVIDIR EN 2 MATRICES
            Caracteristica=ayuda[1]
            Caracteristica.sort()
            print('edad = ',Caracteristica[len(Caracteristica)-1])
        #--------------------
    elif str(sep_palabras_coma[0])=='promedio':
            ayuda=atributoxxx("promedio")#FUNCION PARA OBTENER LOS DATOS:DATOS
            #DIVIDIR EN 2 MATRICES
            Caracteristica=ayuda[1]
            Caracteristica.sort()
            print('promedio = ',Caracteristica[len(Caracteristica)-1])

    elif sep_palabras_es[0] == 'minimo':
        if str(sep_palabras_coma[0])=='edad':
            ayuda=atributoxxx("edad")#FUNCION PARA OBTENER LOS DATOS:DATOS
            #DIVIDIR EN 2 MATRICES
            Caracteristica=ayuda[1]
            Caracteristica.sort()
            print('edad = ',Caracteristica[0])
        #--------------------
    elif str(sep_palabras_coma[0])=='promedio':
            ayuda=atributoxxx("promedio")#FUNCION PARA OBTENER LOS DATOS:DATOS
            #DIVIDIR EN 2 MATRICES
            Caracteristica=ayuda[1]
            Caracteristica.sort()
            print('promedio = ',Caracteristica[0])

    elif sep_palabras_es[0] == 'suma':
        if str(sep_palabras_coma[0])=='edad':
            suma=0
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
