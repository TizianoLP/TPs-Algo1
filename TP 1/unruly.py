"""Lógica del juego Unruly"""

from typing import List, Tuple, Any

Grilla = Any


def crear_grilla(desc: List[str]) -> Grilla:
    """Crea una grilla a partir de la descripción del estado inicial.

    La descripción es una lista de cadenas, cada cadena representa una
    fila y cada caracter una celda. Se puede asumir que la cantidad de las
    filas y columnas son múltiplo de dos. **No** se puede asumir que la
    cantidad de filas y columnas son las mismas.
    Los caracteres pueden ser los siguientes:

    Caracter  Contenido de la celda
    --------  ---------------------
         ' '  Vacío
         '1'  Casillero ocupado por un 1
         '0'  Casillero ocupado por un 0

    Ejemplo:

    >>> crear_grilla([
        '  1 1 ',
        '  1   ',
        ' 1  1 ',
        '  1  0',
    ])
    """
    grilla=[]
    for fila in desc:
        grilla.append(list(fila))
    return grilla

def dimensiones(grilla: Grilla) -> Tuple[int, int]:
    """Devuelve la cantidad de columnas y la cantidad de filas de la grilla
    respectivamente (ancho, alto)"""
    ancho=len(grilla[0])
    alto=len(grilla)
    return ancho,alto
def posicion_es_vacia(grilla: Grilla, col: int, fil: int) -> bool:
    """Devuelve un booleano indicando si la posición de la grilla dada por las
    coordenadas `col` y `fil` está vacía"""
    return grilla[fil][col]==" "

def posicion_hay_uno(grilla: Grilla, col: int, fil: int) -> bool:
    """Devuelve un booleano indicando si la posición de la grilla dada por las
    coordenadas `col` y `fil` está el valor 1"""
    return grilla[fil][col]=="1"

def posicion_hay_cero(grilla: Grilla, col: int, fil: int) -> bool:
    """Devuelve un booleano indicando si la posición de la grilla dada por las
    coordenadas `col` y `fil` está el valor 0"""
    return grilla[fil][col]=="0"


def cambiar_a_uno(grilla: Grilla, col: int, fil: int):
    """Modifica la grilla, colocando el valor 1 en la posición de la grilla
    dada por las coordenadas `col` y `fil`"""
    grilla[fil][col]="1"



def cambiar_a_cero(grilla: Grilla, col: int, fil: int):
    """Modifica la grilla, colocando el valor 0 en la posición de la grilla
    dada por las coordenadas `col` y `fil`"""
    #Misma logica que el de arriba
    grilla[fil][col]="0"


def cambiar_a_vacio(grilla: Grilla, col: int, fil: int):
    """Modifica la grilla, eliminando el valor de la posición de la grilla
    dada por las coordenadas `col` y `fil`"""
    #Misma logica que el de arriba
    grilla[fil][col]=" "


def fila_es_valida(grilla: Grilla, fil: int) -> bool:
    """Devuelve un booleano indicando si la fila de la grilla denotada por el
    índice `fil` es considerada válida.

    Una fila válida cuando se cumplen todas estas condiciones:
        - La fila no tiene vacíos
        - La fila tiene la misma cantidad de unos y ceros
        - La fila no contiene tres casilleros consecutivos del mismo valor
    """
    res0=0
    res1=0
    for n in grilla[fil]:
        if n=="1":
            res1+=1
        elif n==" ":
            return False
        else:
            res0+=1
    #Verifica que haya la misma cantidad de 0 que 1
    if res0!=res1:
        return False
    #Verifica que no haya 3 o mas numeros iguales seguidos
    if "111" in "".join(grilla[fil]) or "000" in "".join(grilla[fil]):
        return False
    else:
        return True
    

def columna_es_valida(grilla: Grilla, col: int) -> bool:
    """Devuelve un booleano indicando si la columna de la grilla denotada por
    el índice `col` es considerada válida.

    Las condiciones para que una columna sea válida son las mismas que las
    condiciones de las filas."""
    res0=0
    res1=0
    cont=" "
    for fil in range(len(grilla[0])):
        for col in range(len(grilla)):
            cont+=grilla[col][fil]
            n=grilla[col][fil]
            if n=="1":
                res1+=1
            elif n==" ":
                return False
            else:
                res0+=1
        cont+=" "
        if res0!=res1:
            return False
    if "111" in cont or "000" in cont:
        return False
    else:
        return True


def grilla_terminada(grilla: Grilla) -> bool:
    """Devuelve un booleano indicando si la grilla se encuentra terminada.

    Una grilla se considera terminada si todas sus filas y columnas son
    válidas."""
    for fil in range(len(grilla)):
        #Si las filas son validas...
        if fila_es_valida(grilla,fil)!=True:
            return False
    for col in range(len(grilla[0])):
        #Y las columnas tambien...
        if columna_es_valida(grilla,col)!=True:
            return False
    else:
        #Devuelve True, porque esta todo correcto
        return True