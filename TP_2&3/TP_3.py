from pila import Pila

def balde(tecla, paint, fila, columna):
    color = paint[fila][columna]
    pintar_balde(tecla, paint, fila, columna, color)

def pintar_balde(tecla, paint, fila, columna, color):
    diccionario_teclas={
        "w":"#ffffff",
        "n":"#000000",
        "b":"#0000ff",
        "y":"#ffff00",
        "r":"#ff0000",
        "g":"#00ff00",
    }
    if fila > len(paint)-1 or columna > len(paint[0])-1:
        return
    if paint[fila][columna] == color:
        if tecla not in diccionario_teclas:
            if len(tecla)!=6:
                return
            else:
                paint[fila][columna] = f'#{tecla}'
        else:
            paint[fila][columna] = diccionario_teclas[tecla]
        if not paint[fila][columna]==color:
            pintar_balde(tecla, paint, fila + 1, columna, color)
            pintar_balde(tecla, paint, fila - 1, columna, color)
            pintar_balde(tecla, paint, fila, columna + 1, color)
            pintar_balde(tecla, paint, fila, columna - 1, color)


def deshacer_paint(deshacer,rehacer):
    #Elimine la verificacion por si esta vacia y la deje en el main
    estado=deshacer.desapilar()
    rehacer.apilar(estado)
    return estado

def rehacer_paint(rehacer,deshacer):
    #Elimine la verificacion por si esta vacia y la deje en el main
    estado=rehacer.desapilar()
    deshacer.apilar(estado)
    return estado
