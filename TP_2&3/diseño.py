import gamelib
ANCHO_PAINT=400
ALTO_PAINT=400

def paint_mostrar(paint):
    '''dibuja la interfaz de la aplicación en la ventana'''
    gamelib.draw_begin()
    gamelib.draw_rectangle(0,0,ANCHO_PAINT,ALTO_PAINT,fill="#FFFFFF")
    gamelib.draw_rectangle(0,ALTO_PAINT,ANCHO_PAINT,500,fill="#C0C0C0")
    boton_PNG()
    boton_gppm()
    boton_cppm()
    flechas() #Nueva funcion
    alto=len(paint)
    ancho=len(paint[0])
    valor_y=ANCHO_PAINT//alto
    valor_x=ANCHO_PAINT//ancho
    for i in range(alto):
        if i*valor_y<=ALTO_PAINT:
            gamelib.draw_line(0,i*valor_y,ANCHO_PAINT,i*valor_y,fill="#000000")
        for j in range(ancho):
            gamelib.draw_line(j*valor_x,0,j*valor_x,ALTO_PAINT,fill="#000000")
            colores(paint,i,j)
    gamelib.draw_end()


def colores(paint,i,j):
    valor_x=ANCHO_PAINT//len(paint[0])
    valor_y=ANCHO_PAINT//(len(paint))
    x=j*valor_x+valor_x//2
    y=i*valor_y+valor_y//2
    dim_x=valor_x//2
    dim_y=valor_y//2
    gamelib.draw_rectangle(x-dim_x,y-dim_y,x+dim_x,y+dim_y,fill=f'{paint[i][j]}')
            

def pintar(tecla,paint,fila,columna,color):
    diccionario_teclas={
        "w":"#FFFFFF",
        "n":"#000000",
        "b":"#0000FF",
        "y":"#FFFF00",
        "r":"#FF0000",
        "g":"#00FF00",
    }
    if tecla==color:
        paint[fila][columna]=f'#{color}'
    if tecla in diccionario_teclas:
        paint[fila][columna] = diccionario_teclas[tecla]
        


def color_seleccionado(tecla,color):
    colores={
        "w":(19,409,41,431),
        "n":(48,408,72,432),
        "r":(79,409,101,431),
        "g":(109,409,131,431),
        "b":(139,409,161,431),
        "y":(169,409,191,431),
        color:(199,409,221,431)
    }
    if tecla in colores:
        x1,y1,x2,y2=colores[tecla]
        if tecla=="n":
            gamelib.draw_rectangle(x1,y1,x2,y2,fill="#FFFFFF")
        else:
            gamelib.draw_rectangle(x1,y1,x2,y2)


def cuadros_colores(color):
    gamelib.draw_rectangle(20,410,40,430,outline="#FFFFFF",fill="#FFFFFF")
    gamelib.draw_text("W",30,420,fill="#000000")
    gamelib.draw_rectangle(50,410,70,430,fill="#000000",outline="#000000")
    gamelib.draw_text("N",60,420,fill="#FFFFFF")
    gamelib.draw_rectangle(80,410,100,430,fill="#FF0000",outline="#FF0000")
    gamelib.draw_text("R",90,420)
    gamelib.draw_rectangle(110,410,130,430,fill="#00FF00",outline="#00FF00")
    gamelib.draw_text("G",120,420)
    gamelib.draw_rectangle(140,410,160,430,fill="#0000FF",outline="#0000FF")
    gamelib.draw_text("B",150,420)
    gamelib.draw_rectangle(170,410,190,430,fill="#FFFF00",outline="#FFFF00")
    gamelib.draw_text("Y",180,420,fill="#000000")
    gamelib.draw_rectangle(200,410,220,430,fill=f'#{color}',outline=f'#{color}')
    if color!="FFFFFF":
        gamelib.draw_text("C",210,420,fill="#000000")
    else:
        gamelib.draw_text("E",210,420,fill="#000000")
        

def boton_PNG():
    gamelib.draw_rectangle(30,450,120,470)
    gamelib.draw_text("Guardar PNG",75,460,size=9,fill="#000000")

def boton_gppm():
    gamelib.draw_rectangle(150,450,240,470)
    gamelib.draw_text("Guardar PPM",195,460,size=9,fill="#000000")

def boton_cppm():
    gamelib.draw_rectangle(270,450,360,470)
    gamelib.draw_text("Cargar PPM",315,460,size=9,fill="#000000")

def flechas():
    #Muestras flechas para rehacer y deshacer
    gamelib.draw_text("<-- Z",300,420,fill="black")
    gamelib.draw_text("X -->",350,420,fill="black")
    #Agrego un baldecito con un mensaje como indicacion
    gamelib.draw_image("balde.gif",240,410)
    gamelib.draw_text("!",250,420,fill="#000000",size=25)