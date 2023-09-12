import gamelib
import png
import diseño
import TP_3
from pila import Pila

ANCHO_GRILLA=400
ALTO_GRILLA=500

def paint_nuevo(ancho, alto):
    '''inicializa el deshacer del programa con una imagen vacía de ancho x alto'''
    paint=[]
    for i in range(alto):
        fila=[]
        for j in range(ancho):
            fila.append("#FFFFFF")
        paint.append(fila)
    return paint

def copiar_paint(paint):
    paint_copia=paint_nuevo(len(paint[0]),len(paint))
    for i in range(len(paint)):
        for j in range(len(paint[0])):
            paint_copia[i][j]=paint[i][j]
    return paint_copia

def png_aux(paint):
    contador=6
    colores={
        "#FFFFFF":0,
        "#000000":1,
        "#0000FF":2,
        "#FFFF00":3,
        "#FF0000":4,
        "#00FF00":5
    }
    paleta = [
    (255, 255, 255),
    (0, 0, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255,0,0),
    (0,255,0)
    ]
    paint_aux=paint_nuevo(len(paint[0]),len(paint))
    for i in range(len(paint)):
        for j in range(len(paint[0])):
            if paint[i][j] in colores:
                paint_aux[i][j]=colores[paint[i][j]]
            else:
                colores[paint[i][j]]=contador
                contador+=1
                r,g,b=int(paint[i][j][1:3],16),int(paint[i][j][3:5],16),int(paint[i][j][5:7],16)
                paleta.append((r,g,b))
                paint_aux[i][j]=colores[paint[i][j]]
    return paint_aux,paleta

def guardar_png(paint):
    ruta=gamelib.input("¿Como quiere guardar la imagen?")
    paint_aux,paleta=png_aux(paint)
    png.escribir(f"{ruta}.png",paleta,paint_aux)


def guardar_ppm(paint):
    alto=len(paint)
    ancho=len(paint[0])
    while True:
        ruta = gamelib.input("Ingrese ruta")
        if ruta is None or ".ppm" not in ruta:
            gamelib.say("El archivo no es un PPM")
        else:
            break
    try:
        with open(ruta,"w")as arch:
            arch.write("P3"+"\n")
            arch.write(f'{alto} {ancho}'+"\n")
            arch.write("255"+"\n")
            for i in range(alto):
                for j in range(ancho):
                    arch.write(f'{int(paint[i][j][1:3],16)} {int(paint[i][j][3:5],16)} {int(paint[i][j][5:7],16)}'+"\n")
    except FileNotFoundError:
        gamelib.say("No existe el archivo")
    except TypeError:
        pass


def cargar_ppm(paint,deshacer,rehacer):
    while True:
        ruta = gamelib.input("Ingrese ruta")
        if not ruta is None and ".ppm" not in ruta :
            gamelib.say("El archivo no es un PPM")
            continue
        else:
            break
    try:
        with open(ruta, "r") as arch:
            next(arch)
            alto, ancho = arch.readline().split(" ")
            alto = int(alto)
            ancho = int(ancho)
            paint=paint_nuevo(ancho,alto)
            next(arch)
            for i in range(alto):
                for j in range(ancho):
                    colores = arch.readline().split()
                    r, g, b = f'{int(colores[0]):02x}',f'{int(colores[1]):02x}',f'{int(colores[2]):02x}'
                    paint[i][j]=f'#{r+g+b}'
    except FileNotFoundError:
        gamelib.say("No existe el archivo")
    except TypeError:
        pass
    while not rehacer.esta_vacia():
        rehacer.desapilar()
    while not deshacer.esta_vacia():
        deshacer.desapilar()
    #Elimine la apilacion en esta funcion
    return paint



def botones(paint,ev,deshacer,rehacer):
    if 450<=ev.y<=470 and 30<=ev.x<=120:
        gamelib.draw_rectangle(29,449,121,471,fill="black")
        diseño.boton_PNG()
        guardar_png(paint)
    elif 450<=ev.y<=470 and 150<=ev.x<=240:
        gamelib.draw_rectangle(149,449,241,471,fill="black")
        diseño.boton_gppm()
        guardar_ppm(paint)
    elif 450<=ev.y<=470 and 270<=ev.x<=360:
        gamelib.draw_rectangle(269,449,361,471,fill="black")
        diseño.boton_cppm()
        paint=cargar_ppm(paint,deshacer,rehacer)
    elif 410<=ev.y<=430 and 240<=ev.x<=260: #Nueva funcion
        #Agregue un mensaje para cuando el usuario apreta sobre el balde
        gamelib.say("Para utilizar el balde, utilice la rueda del raton")
    return paint

def verificar_color():
    hexadecimal="abcdefABCDEF0123456789"
    while True:
        color=gamelib.input("Ingrese color:")
        if color==None or len(color)!=6 or any(car not in hexadecimal for car in color):
            gamelib.say("Color incorrecto")
            continue
        else:
            break
    return color

def copiar_color(paint,fila,columna):
    return paint[fila][columna][1:]

def main():
    gamelib.title("AlgoPaint")
    gamelib.resize(ANCHO_GRILLA,ALTO_GRILLA)
    paint=paint_nuevo(4,4)
    color="ffffff"
    tecla="n"
    deshacer=Pila()
    rehacer=Pila()
    #Aca habia una apilacion que elimine 
    while gamelib.loop(fps=15):
        diseño.paint_mostrar(paint)
        diseño.color_seleccionado(tecla,color)
        diseño.cuadros_colores(color)
        for ev in gamelib.get_events():
            if ev.type == gamelib.EventType.KeyPress:
                tecla=ev.key
                if tecla=="e":
                    color=verificar_color()
                    tecla=color
                elif tecla=="c":
                    tecla=color
                elif tecla=="z":
                    if not deshacer.esta_vacia():
                        paint=TP_3.deshacer_paint(deshacer,rehacer)
                #Agrego la tecla "n", para que el usuario pueda volver a pintar por lo menos con el color negro
                    tecla="n"
                elif tecla=="x":
                #Evite usar la tecla "y" para hacer rehacer. Era la misma que para el color amarillo
                    if not rehacer.esta_vacia():
                        paint=TP_3.rehacer_paint(rehacer,deshacer)
                    tecla="n"
            if ev.type == gamelib.EventType.ButtonPress:
                fila = ev.y // (400//len(paint))
                columna = ev.x // (400//len(paint[0]))
                if 0 <= fila < len(paint) and 0 <= columna < len(paint[0]) and ev.y<=400:
                    if ev.mouse_button==1:
                        #Vacio pila de rehacer y cambio el orden en donde apilo
                        while not rehacer.esta_vacia():
                            rehacer.desapilar()
                        paint_copia=copiar_paint(paint)
                        deshacer.apilar(paint_copia)
                        diseño.pintar(tecla,paint,fila,columna,color)
                    if ev.mouse_button==2: #El balde ahora es un evento de tipo 2 (rueda del mouse)
                        #Vacio pila de rehacer y cambio el orden en donde apilo
                        while not rehacer.esta_vacia():
                            rehacer.desapilar()
                        paint_copia=copiar_paint(paint)
                        deshacer.apilar(paint_copia)
                        TP_3.balde(tecla,paint,fila,columna)
                    if ev.mouse_button==3:
                        color=copiar_color(paint,fila,columna)
                        tecla=color
                paint=botones(paint,ev,deshacer,rehacer)

gamelib.init(main)