import random

import niveles
import unruly

#Funcion auxiliar para mostrar la grilla
def mostrar_grilla(grilla):
    for i in range(len(grilla)):
        for n in range(len(grilla[0])):
            print(grilla[i][n],end="|")
        print()

#Funcion auxiliar para verificar la columna
def verif_col(grilla,col):
    mensaje1="¡Valor incorrecto!"
    mensaje2="Gracias por jugar"
    if col=="salir":
        print(mensaje2)
        return "salir"
    elif col=="" or not col.isdigit() or int(col)>=len(grilla[0]):
        print(mensaje1)
        return False

#Funcion auxiliar para verificar la fila
def verif_fil(grilla,fil):
    mensaje1="¡Valor incorrecto!"
    mensaje2="Gracias por jugar"
    if fil=="salir":
        print(mensaje2)
        return "salir"
    elif fil=="" or not fil.isdigit() or int(fil)>=len(grilla):
        print(mensaje1)
        return False
    return True

#Funcion auxiliar para verificar el valor
def verif_num(num,grilla,col,fil,nivel):
    mensaje2="Gracias por jugar"
    if num=="salir":
        print(mensaje2)
        return "salir"
    if num=="1":
        grilla=unruly.cambiar_a_uno(grilla,col,fil)
        unruly.crear_grilla(nivel)
    if num=="0":
        grilla=unruly.cambiar_a_cero(grilla,col,fil)
        unruly.crear_grilla(nivel)
    if num==" ":
        grilla=unruly.cambiar_a_vacio(grilla,col,fil)
        unruly.crear_grilla(nivel)

def main():
    nivel = random.choice(niveles.NIVELES)
    grilla = unruly.crear_grilla(nivel)
    print("Para contar las filas o columnas, empiece desde cero")
    while unruly.grilla_terminada(grilla)==False:
        mostrar_grilla(grilla)

        #Ingresa una columna
        col=input("Ingrese columna:")
        res_col=verif_col(grilla,col)
        #Verificaciones de la columna
        if res_col=="salir":
            break
        elif res_col==False:
            continue
        col=int(col)

        #Ingresa una fila
        fil=input("Ingrese la fila:")
        res_fil=verif_fil(grilla,fil)
        #Verificaciones de la fila
        if res_fil=="salir":
            break
        elif res_fil==False:
            continue
        fil=int(fil)

        #Ingresa un numero
        num=input("Ingrese valor a cambiar:")
        #Verificaciones del numero
        verif_num(num,grilla,col,fil,nivel)
        if num=="salir":
            break

    #Verifica si completo el juego
    else:
        print("Juego completado!")
        mostrar_grilla(grilla)
        return grilla
main()
    