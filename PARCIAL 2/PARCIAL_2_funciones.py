import pygame as pg 
import random 


#funcion volver atras
def pausar_juego(evento,pantalla_actual):
    if evento.type == pg.KEYDOWN:
        if evento.key == pg.K_ESCAPE:
            pantalla_actual = "inicio"
            print("Juego Pausado.")
    
    return pantalla_actual



#pausa - despausa
def pausar_despausar(evento):
    if evento.type == pg.KEYDOWN:
        if evento.key == pg.K_p: # P = pausa 
            pg.mixer.music.pause()
            print("sonido pausado")
        if evento.key == pg.K_o: #O = despausa
            pg.mixer.music.unpause()
            print("Sonido reanudado")


'DIBUJOS EN PANTALLA'


#esto usa de parametros:
#1 Pantalla principal 
#2 tamaño de los cuadrados 
#3 cantidad de columnas
#4 cantidad de filas
#5  X desde donde comienza a dibujarse
#6 Y desde donde comienza a dibujarse

#dibuja los cuadraditos: 
def dibujar_cuadrados(pantalla:pg.Surface, tamaño:int, columna:int, fila:int, x_inicial:int, y_inicial:int)->list:
    'recibe surface,int tamaño, int columna(cantidad),int fila (cantidad), int X inicial, int Y inicial'     
    lista_retorno_de_cuadrados = []

    for filass in range(fila):
        for columnass in range(columna):
            rectangulo_azul = pg.Rect(x_inicial + columnass * tamaño, y_inicial + filass * tamaño,tamaño,
                tamaño 
                )
            pg.draw.rect(pantalla, (255, 234, 227), rectangulo_azul)      # cuadrados azules
            pg.draw.rect(pantalla, (0, 0, 0), rectangulo_azul, 1)     # bordes negros

            lista_retorno_de_cuadrados.append(rectangulo_azul)
            #retorna los cuadrados para usarlos despues en .collidepoint


    return lista_retorno_de_cuadrados




#lineas separadoras:
def dibujar_lineas(pantalla):
    #verticales             #color     #inicio     #fin
    pg.draw.line(pantalla, (0, 0, 0), (450, 150), (450,600), 6)
    pg.draw.line(pantalla, (0, 0, 0), (300, 150), (300,600), 6)
    
    #horizontales
    pg.draw.line(pantalla, (0, 0, 0), (150,300), (600,300), 6)
    pg.draw.line(pantalla, (0, 0, 0), (150,450), (600,450), 6)




#dibujar todo
def dibujar_todos_los_cuadrados(pantalla):
    
    celdas_sector_1 = dibujar_cuadrados(pantalla,50,3,3,150,150) #sector 1
    celdas_sector_2 = dibujar_cuadrados(pantalla,50,3,3,300,150) #sector 2
    celdas_sector_3 = dibujar_cuadrados(pantalla,50,3,3,450,150) #sector 3
    celdas_sector_4 = dibujar_cuadrados(pantalla,50,3,3,150,300) #sector 4
    celdas_sector_5 = dibujar_cuadrados(pantalla,50,3,3,300,300) #sector 5
    celdas_sector_6 = dibujar_cuadrados(pantalla,50,3,3,450,300) #sector 6
    celdas_sector_7 = dibujar_cuadrados(pantalla,50,3,3,150,450) #sector 7 
    celdas_sector_8 = dibujar_cuadrados(pantalla,50,3,3,300,450) #sector 8
    celdas_sector_9 = dibujar_cuadrados(pantalla,50,3,3,450,450) #sector 9 


#detecta las colisiones dentro de los cuadrados 
#recibe el evento del mouse, la posicion y una tupla para iterar con enumerate

def detectar_colisiones_simple(posicion,cuadrados):
    # Detectar clic en cuadrado
    for i, rect in enumerate(cuadrados):
        if rect.collidepoint(posicion):
            print(f"Hiciste clic en la celda número {i} en posición {rect.topleft}")
            


def dibujar_numeros(pantalla, matriz: list, tamaño, fuente, posicion_x, posicion_y):
    lista_de_numeros = []

    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):

            valor = matriz[fila][columna]
            if valor != 0:  # Solo dibujo si no es cero

                # Calcular posición de la celda actual
                x = posicion_x + columna * tamaño
                y = posicion_y + fila * tamaño

                # Dibujar borde de celda (opcional)
                rect = pg.Rect(x, y, tamaño, tamaño)
                #pg.draw.rect(pantalla, (0, 0, 0), rect, 1)

                # Renderizar el número
                texto = fuente.render(str(valor), True, (158, 108, 100))
                
                # Centrar el número dentro de la celda
                texto_rect = texto.get_rect(center=(x + tamaño // 2, y + tamaño // 2))
                pantalla.blit(texto, texto_rect)

                lista_de_numeros.append(rect)

    return lista_de_numeros




#          parametros:     matriz | #cantidad de numeros para agregar
def agregar_numeros_al_azar(matriz, cantidad):
    #agrega numeros al azar, en lugares al azar en una matriz

    filas = len(matriz)
    columnas = len(matriz[0])
    contador = 0 #contador del bucle
    usados = set() #set de numeros ya usados

    while contador < cantidad: #definida por parametro 
        fila_al_azar = random.randrange(filas)  # fila al azar 
        columna_al_azar = random.randrange(columnas) #columna al azar 
        numero_al_azar = random.randint(1, 9) #numero al azar dentro de 1 y 9

        # si el lugar ya tiene un número distinto de 0, saltar
        if matriz[fila_al_azar][columna_al_azar] != 0:#esto es para no perder numeros en el contador y que al final agregue algo distinto de la cantidad que quiero
            continue
        #si el numero esta dentro de la lista de usados lo salto 
        if numero_al_azar in usados:
            continue

        # verifico que el numero no este en las filas
        if numero_al_azar in matriz[fila_al_azar]:
            continue

        # verifico que el numero no esté en la posicion "j", [0,1,2]
        repetido = False
        for j in range(filas): 
            if matriz[j][columna_al_azar] == numero_al_azar: # mira uno por uno dentro de la lista pequeña [0,1,2]
                repetido = True #si esta, freno
                break
        if repetido:
            continue #salto ese numero 

        # Si pasa todo esto, lo incluyo 
        matriz[fila_al_azar][columna_al_azar] = numero_al_azar
        contador += 1 #sumo 1 al contador y continua el bucle 
        usados.add(numero_al_azar)
    return matriz



   


def mouse_de_inicio(boton1:pg.rect,boton2:pg.rect,boton3:pg.rect,boton4:pg.rect,evento:pg.event,posicion:tuple):
    if evento.type == pg.MOUSEBUTTONDOWN:
        if evento.button ==1:
            print("  ")

        if boton1.collidepoint(posicion):                
            pantalla_actual = "nivel"

        elif boton2.collidepoint(posicion):
            pantalla_actual = "jugar"
            
        elif boton3.collidepoint(posicion):
            pantalla_actual = "ver puntaje"

        elif boton4.collidepoint(posicion):
            pg.quit()
            quit()


        return pantalla_actual




'DIBUJOS EN PANTALLA'


#esto usa de parametros:
#1 Pantalla principal 
#2 tamaño de los cuadrados 
#3 cantidad de columnas
#4 cantidad de filas
#5  X desde donde comienza a dibujarse
#6 Y desde donde comienza a dibujarse

#dibuja los cuadraditos: 
def dibujar_cuadrados(pantalla:pg.surface, tamaño:int, columna:int, fila:int, x_inicial:int, y_inicial:int)->dict: 
    'recibe surface, tamaño de los cuadrados, cantidad de filas, cantidad de columnas , posicion X y posicion Y. Dibuja cuadrados multiplicando '   
    lista_retorno_de_cuadrados = []

    for filass in range(fila):
        for columnass in range(columna): 

            #los valores son x inicial (ejem 150) + indice(ejem 0) * tamaño (ejem 50) 
            # cada vez que el indice avanza una posicion, 
            # el inicio donde voy a dibujar el cuadrado siguiente avanza exactamente una anchura de cuadrado 
            #  X = 150 + (columnass=0) × 50 = 150  Rect = (150, 150, 50, 50),
            # X = 150 + (columnass=1) x 50 = 200   
            # X =  150 +  (columnass=2) x50 = 250  
 
            rectangulo_azul = pg.Rect(x_inicial + columnass * tamaño, y_inicial + filass * tamaño,tamaño,
                tamaño 
                )
            pg.draw.rect(pantalla, (255, 234, 227), rectangulo_azul)      # cuadrados azules
            pg.draw.rect(pantalla, (0, 0, 0), rectangulo_azul, 1)     # bordes negros
            
            #esto no tiene blits porque usa pg.draw 

            #retorna los cuadrados para usarlos despues en "detectar celda"
            #y otras funciones que requieran la posicion
            lista_retorno_de_cuadrados.append(({
            "rect": rectangulo_azul,
            "fila": filass,
            "columna": columnass
        }))
    

    
    return lista_retorno_de_cuadrados



#lineas separadoras:
def dibujar_lineas(pantalla:pg.surface):
    'recibe un surface pantalla, dibuja 4 lineas en la pantalla para separar los 9 sectores del juego'
    #verticales             #color     #inicio     #fin
    pg.draw.line(pantalla, (0, 0, 0), (450, 150), (450,600), 6)
    pg.draw.line(pantalla, (0, 0, 0), (300, 150), (300,600), 6)
    
    #horizontales
    pg.draw.line(pantalla, (0, 0, 0), (150,300), (600,300), 6)
    pg.draw.line(pantalla, (0, 0, 0), (150,450), (600,450), 6)

    #esto no tiene blits porque usa pg.draw.line


#dibuja el borde verde de la celda clickeada:
def dibujar_borde_verde(pantalla:pg.Surface,celda_seleccionada:dict):
    'recibe pantalla(surface) y un dict de los datos de la celda seleccionada, dibuja un bordecito verde al clickear la celda'
    if celda_seleccionada is not None: #verifico que celda sea algo, si no es asi, cuando de click fuera de la cuadricula se rompe el juego 
        rect = celda_seleccionada["rect"]
        pg.draw.rect(pantalla,(0,200,0),rect,3)


                  #NO USADO 
#dibujar todo
def dibujar_todos_los_cuadrados(pantalla:pg.surface):
    'recibe surface pantalla, esta funcion repite 9 veces "dibujar_cuadrados"'
    celdas_sector_1 = dibujar_cuadrados(pantalla,50,3,3,150,150) #sector 1
    celdas_sector_2 = dibujar_cuadrados(pantalla,50,3,3,300,150) #sector 2
    celdas_sector_3 = dibujar_cuadrados(pantalla,50,3,3,450,150) #sector 3
    celdas_sector_4 = dibujar_cuadrados(pantalla,50,3,3,150,300) #sector 4
    celdas_sector_5 = dibujar_cuadrados(pantalla,50,3,3,300,300) #sector 5
    celdas_sector_6 = dibujar_cuadrados(pantalla,50,3,3,450,300) #sector 6
    celdas_sector_7 = dibujar_cuadrados(pantalla,50,3,3,150,450) #sector 7 
    celdas_sector_8 = dibujar_cuadrados(pantalla,50,3,3,300,450) #sector 8
    celdas_sector_9 = dibujar_cuadrados(pantalla,50,3,3,450,450) #sector 9 


#detecta las colisiones dentro de los cuadrados 
#recibe el evento del mouse, la posicion y una tupla para iterar con enumerate

def detectar_colisiones_simple(posicion:tuple,cuadrados:list):
    'recibe la posicion y una lista de rect, detecta las colisiones,clicks en los rect'
    # Detectar clic en cuadrado
    for i, rect in enumerate(cuadrados):
        if rect.collidepoint(posicion):
            print(f"Hiciste clic en la celda número {i} en posición {rect.topleft}")
            

def detectar_todas_las_colisiones(posicion:tuple,celdas_sector_1:list,celdas_sector_2:list,celdas_sector_3:list,celdas_sector_4:list,celdas_sector_5:list,celdas_sector_6:list,celdas_sector_7:list,celdas_sector_8:list,celdas_sector_9:list):
    'recibe la posicion del mouse y 9 listas, detecta las colisiones del click y todos los rect dibujados, no retorna'
    detectar_colisiones_simple(posicion,celdas_sector_1)
    detectar_colisiones_simple(posicion,celdas_sector_2)
    detectar_colisiones_simple(posicion,celdas_sector_3)
    detectar_colisiones_simple(posicion,celdas_sector_4)
    detectar_colisiones_simple(posicion,celdas_sector_5)
    detectar_colisiones_simple(posicion,celdas_sector_6)
    detectar_colisiones_simple(posicion,celdas_sector_7)
    detectar_colisiones_simple(posicion,celdas_sector_8)
    detectar_colisiones_simple(posicion,celdas_sector_9)



#probar esto,      NO USADO EN EL JUEGO 
'modificar esto para que funcione, solo dibuja pero no modifica la matriz '
def ingresar_texto(evento,cuadrados,cuadrado_seleccionado,fuente,pantalla):
    #condicion: si se presiona una tecla y hay una celda seleccionada
    if evento.type == pg.KEYDOWN and cuadrado_seleccionado is not None:
        if evento.key == pg.K_BACKSPACE: #tecla borrar
            numero_ingresado = ""
        elif evento.unicode.isdigit():
            numero_ingresado = evento.unicode
            if numero_ingresado < "1" or numero_ingresado > "9": #valido que sean solo numeros 
                numero_ingresado = ""

        #dibujar el número en pantalla
        if numero_ingresado:
            rect = cuadrados[cuadrado_seleccionado]
            x, y = rect.center
            texto = fuente.render(numero_ingresado, True, (0, 0, 0))
            texto_rect = texto.get_rect(center=(x, y))
            pantalla.blit(texto, texto_rect)



def detectar_celda(pos:tuple, cuadrados:list)->dict:
    'recibe la tupla posicion y una lista con los rect dibujados, retorna indice, datos del rect, fila, columna, y tupla posicion, retorna None, si no detecta nada'
    for i, celda in enumerate(cuadrados):
        rect = celda["rect"]

        if rect.collidepoint(pos):
            print(f"clic en la celda numero {i}, posicion {rect.topleft}")
            return {
                "indice": i,
                "rect": rect,
                "fila": celda["fila"],
                "columna": celda["columna"],
                "pos_mouse": pos
            }

    return None   # no hubo clic en ninguna celda


def input_numero(evento: pg.event, cuadrado_seleccionado: dict) -> int:
    'recibe evento pg, el diccionario con la ubicacion del cuadrado seleccionado, detecta el ingreso SOLAMENTE DE NUMEROS por teclado.'
    if evento.type != pg.KEYDOWN: #solo evento de teclado 
        return None

    if cuadrado_seleccionado["indice"] is None: #retorna none si no se selecciona ninguna celda 
        return None

    # si la tecla no es número devuelve none, sin este punto tira error el juego entero xD
    if evento.unicode.isdigit() == False:
        return None

    numero = int(evento.unicode) 

    # valido rango 1-9
    if numero < 1 or numero > 9:
           numero = 0  #si es cero, la funcion "dibujar numeros" no lo dibuja 

    return numero




def agregar_numero_a_matriz(evento:pg.event,numero_ingresado:int,celda_seleccionada:dict,matriz_grande): 
    'recibe evento.pg, un int, un dict de celda seleccionada y una lista, extrae del diccionario las coordenadas para usar en la matriz, añade el numero a la matriz' 
    fila = celda_seleccionada["fila"]
    columna = celda_seleccionada["columna"]
    rect = celda_seleccionada["rect"]

    if evento == pg.KEYDOWN:
        if evento.unicode.isdigit():
            numero_ingresado = int(evento.unicode)

            matriz_grande[fila][columna] = numero_ingresado
            



def dibujar_numeros(pantalla:pg.surface, matriz: list, tamaño:int, fuente:pg.font, posicion_x:int, posicion_y:int):
    ''' esta funcion dibuja numeros,todos excepto el 0, en un surface(pantalla) tomandolos de una matriz. Retorna una lista de rect '''
    lista_de_numeros = []

    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):

            valor = matriz[fila][columna]
            if valor != 0:  # solo dibujo si no es cero

                # calcular posición de la celda usando x e y de inicio 
                x = posicion_x + columna * tamaño
                y = posicion_y + fila * tamaño

                #dibujar borde de celda 
                rect = pg.Rect(x, y, tamaño, tamaño)
                #pg.draw.rect(pantalla, (0, 0, 0), rect, 1)

                #   Renderiza el numero, castea a str porque sino tira error 
                numero = fuente.render(str(valor), True, (158, 108, 100))
                
                # centrar el numero dentro de la celda  (opcional, estetico)
                texto_rect = numero.get_rect(center=(x + tamaño // 2, y + tamaño // 2))
                pantalla.blit(numero, texto_rect)

                lista_de_numeros.append(rect)

    return lista_de_numeros





# Probar estas funciones, no se si sirven 
def unir_matriz_general(matriz_general):
    """Une las 9 matrices 3x3 en una sola 9x9."""
    matriz_9x9 = []
    for fila_entera in range(3):  # cada bloque de 3 filas
        for fila_interna in range(3):
            fila_completa = []
            for col_bloque in range(3):
                fila_completa += matriz_general[fila_entera * 3 + col_bloque][fila_interna]
            matriz_9x9.append(fila_completa)
    return matriz_9x9



def limpiar_repetidos_horizontales(matriz_grande:list)->list:
    'recibe una matriz, inspecciona la matriz en busca de repetidos, si encuentra un numero repetido lo reemplaza por un numero al azar que no este en la lista. '
    for i in range(len(matriz_grande)):
        numero_random1 = random.randrange(1,10) #numero random1
        numero_random2 = random.randrange(1,10) #numero random2
        numero_random3 = random.randrange(1,10) #numero random3
        numero_random4 = random.randrange(1,10) #numero random4
        repetidos = set() #set de repetidos
        vistos = set() #set de numeros vistos 

        for j in range(len(matriz_grande[i])):
            numero_inspeccionado = matriz_grande[i][j] #numero inspeccionado 

            if numero_inspeccionado in vistos: #si veo un mismo numero, mas de una vez, esta repetido
                repetidos.add(numero_inspeccionado)

                if numero_inspeccionado in repetidos: # si el numero esta en repetidos
                    if numero_random1 in matriz_grande[i]:   #verifico si random1 esta en la fila 

                        if numero_random2 in matriz_grande[i]:  #verifico si random2 esta en la fila

                            if numero_random3 in matriz_grande[i]: #verifico si random3 esta en la fila

                                if numero_random4 in matriz_grande[i]: ##verifico si random2 esta en la fila
                                    matriz_grande[i][j] = 0   # si estan todos repetidos reemplazo el repetido por 0 
                                else:
                                    matriz_grande[i][j] = numero_random4  #reemplazo el repetido por random4

                            else:
                                matriz_grande[i][j] = numero_random3  #reemplazo el repetido por random3
                        else:
                            matriz_grande[i][j] = numero_random2 #reemplazo el repetido por random2
                    else:
                        matriz_grande[i][j] = numero_random1 #reemplazo el repetido por random1
            
            if matriz_grande[i][j] != 0: #distinto de cero
                vistos.add(numero_inspeccionado) # agrego a la lista de vistos 

    return matriz_grande




def limpiar_repetidos_verticales(matriz_grande:list)->list:
    'recibe una matriz, crea una columna e intenta reeemplazar los numeros repetidos por otros generados al azar'
    for i in range(len(matriz_grande[0])):  
        numero_random1 = random.randrange(1,10) #numero random1
        numero_random2 = random.randrange(1,10) #numero random2
        numero_random3 = random.randrange(1,10) #numero random3
        numero_random4 = random.randrange(1,10) #numero random4
        repetidos = set()  #set de numeros repetidos 
        vistos = set() #set de numeros ya vistos 

       
        columna_fabricada = [] 
        for fila in range(9): #solo necesito 9 lugares
            columna_fabricada.append(matriz_grande[fila][i]) #fabrico 1 columna para revisarla lugar por lugar con for 

        for j in range(len(matriz_grande)):  # filas
            numero_inspeccionado = matriz_grande[j][i]

            if numero_inspeccionado in vistos:  
                repetidos.add(numero_inspeccionado)

                if numero_inspeccionado in repetidos:

                    # verifico los numeros en la columna fabricada
                    if numero_random1 in columna_fabricada:

                        if numero_random2 in columna_fabricada:

                            if numero_random3 in columna_fabricada:

                                if numero_random4 in columna_fabricada:
                                    matriz_grande[j][i] = 0
                                else:
                                    matriz_grande[j][i] = numero_random4
                                    columna_fabricada[j] = numero_random4  #agrego el numero a la columna fabricada porque estoy comparando con esta misma lista
                            else:
                                matriz_grande[j][i] = numero_random3
                                columna_fabricada[j] = numero_random3
                        else:
                            matriz_grande[j][i] = numero_random2
                            columna_fabricada[j] = numero_random2
                    else:
                        matriz_grande[j][i] = numero_random1
                        columna_fabricada[j] = numero_random1

            if matriz_grande[j][i] != 0:
                vistos.add(numero_inspeccionado)

    return matriz_grande





def ingresar_numero_a_matriz(matriz_general_fin:list,numero:int,celda_seleccionada:dict,tamaño:int,x_inicial=150, y_inicial=150)->list:
    'recibe la matriz general, el numero ingresado por teclado, un diccionario con datos de la celda clickeada, tamaño(50), x inicial de los rect, y inicial de los rect . retorna una matriz grande'

    #indice = celda_seleccionada["indice"] #indice 
    mouse_x,mouse_y = celda_seleccionada["pos_mouse"] #extraigo la tupla posicion del mouse 
        
    columna = (mouse_x - x_inicial) // tamaño #convierto la x en indices: posicion_mouse_x menos x_inicial(150) dividido tamaño(50) 
    columna = int(columna) #redondeo por si acaso 
        
    fila = (mouse_y - y_inicial) // tamaño #mismo caso
    fila = int(fila)
    
    if columna < 0 or fila < 0: #si alguno es menor a cero es click fuera del area
        return matriz_general_fin  # clic fuera del area, no hacer nada

    # evito exceder los limites, fila o columna mayor o igual al largo de la matriz 
    if fila >= len(matriz_general_fin) or columna >= len(matriz_general_fin[0]):
        return matriz_general_fin  # click fuera, ignorar

    matriz_general_fin[fila][columna] = numero
    
    return matriz_general_fin

    
def borrar_numero_de_matriz(matriz_general_fin:list,evento:pg.event,celda_seleccionada:dict,tamaño:int,x_inicial=150, y_inicial=150)->list:
    'recibe la matriz general,evento, un diccionario con datos de la celda clickeada, tamaño(50),x inicial de los rect, y inicial de los rect. Borra un numero de una casilla seleccionada. Retorna una matriz grande'

    indice = celda_seleccionada["indice"] #indice 
    mouse_x,mouse_y = celda_seleccionada["pos_mouse"]
        
    columna = (mouse_x - x_inicial) // tamaño #convierto la x en indices: posicion_mouse_x menos x_inicial(150) dividido tamaño(50) 
    columna = int(columna) #redondeo por si acaso 
        
    fila = (mouse_y - y_inicial) // tamaño #mismo caso
    fila = int(fila)
    
    
        
    if columna < 0 or fila < 0: #si alguno es menor a cero es click fuera del area
        return matriz_general_fin  # clic fuera del area, no hacer nada

    # evito exceder los limites, fila o columna mayor o igual al largo de la matriz 
    if fila >= len(matriz_general_fin) or columna >= len(matriz_general_fin[0]):
        return matriz_general_fin  # click fuera, ignorar
    
    if evento.type == pg.KEYDOWN:
        if evento.key == pg.K_BACKSPACE:
            matriz_general_fin[fila][columna] = 0
        if evento.key == pg.K_DELETE:
            matriz_general_fin[fila][columna] = 0

    return matriz_general_fin


def validar_matriz_sector_1(matriz_general_fin:list)->bool:
    'recibe matriz general. recorre un segmento 3x3 de la matriz(ejemplo sector1 = 0-3,0-3) y verifica si hay numeros repetidos. Retorna bool, False si hay repetidos, True si no los hay'
    bandera = None   #bandera de retorno
    repetidos = set() #set de repetidos
    vistos = set() #set de numeros vistos 
    hay_ceros = False #bandera que comprueba si existen ceros 

    for i in range(0,3): 
        
        for j in range(0,3):
            numero_inspeccionado = matriz_general_fin[i][j] 

            if numero_inspeccionado == 0: #verifica ceros en la matriz 
                hay_ceros = True

            if numero_inspeccionado in vistos: #  si esta en vistos, esta repetido 
                repetidos.add(numero_inspeccionado)
            
            if matriz_general_fin[i][j] != 0: #solo me interesan los numeros que no sean cero 
                vistos.add(numero_inspeccionado)

    if len(repetidos) == 0 and not hay_ceros: # si el largo de repetidos es 0 y a la vez no hay ceros en la matriz(osea espacios en blanco)
        bandera = True
    else:
        bandera = False
    
    return bandera

def validar_matriz_sector_2(matriz_general_fin:list)->bool:
    'recibe matriz general. recorre un segmento 3x3 de la matriz(ejemplo sector1 = 0-3,0-3) y verifica si hay numeros repetidos. Retorna bool, False si hay repetidos, True si no los hay'
    bandera = None   #bandera de retorno
    repetidos = set() #set de repetidos
    vistos = set() #set de numeros vistos 
    hay_ceros = False #bandera que comprueba si existen ceros 

    for i in range(0,3): 
        
        for j in range(3,6):
            numero_inspeccionado = matriz_general_fin[i][j] 

            if numero_inspeccionado == 0: #verifica ceros en la matriz 
                hay_ceros = True

            if numero_inspeccionado in vistos: #  si esta en vistos, esta repetido 
                repetidos.add(numero_inspeccionado)
            
            if matriz_general_fin[i][j] != 0: #solo me interesan los numeros que no sean cero 
                vistos.add(numero_inspeccionado)

    if len(repetidos) == 0 and not hay_ceros: # si el largo de repetidos es 0 y a la vez no hay ceros en la matriz(osea espacios en blanco)
        bandera = True
    else:
        bandera = False
    
    return bandera


def validar_matriz_sector_3(matriz_general_fin:list)->bool:
    'recibe matriz general. recorre un segmento 3x3 de la matriz(ejemplo sector1 = 0-3,0-3) y verifica si hay numeros repetidos. Retorna bool, False si hay repetidos, True si no los hay'
    bandera = None   #bandera de retorno
    repetidos = set() #set de repetidos
    vistos = set() #set de numeros vistos 
    hay_ceros = False #bandera que comprueba si existen ceros 

    for i in range(0,3): 
        
        for j in range(6,9):
            numero_inspeccionado = matriz_general_fin[i][j] 

            if numero_inspeccionado == 0: #verifica ceros en la matriz 
                hay_ceros = True

            if numero_inspeccionado in vistos: #  si esta en vistos, esta repetido 
                repetidos.add(numero_inspeccionado)
            
            if matriz_general_fin[i][j] != 0: #solo me interesan los numeros que no sean cero 
                vistos.add(numero_inspeccionado)

    if len(repetidos) == 0 and not hay_ceros: # si el largo de repetidos es 0 y a la vez no hay ceros en la matriz(osea espacios en blanco)
        bandera = True
    else:
        bandera = False
    
    return bandera


def validar_matriz_sector_4(matriz_general_fin:list)->bool:
    'recibe matriz general. recorre un segmento 3x3 de la matriz(ejemplo sector1 = 0-3,0-3) y verifica si hay numeros repetidos. Retorna bool, False si hay repetidos, True si no los hay'
    bandera = None   #bandera de retorno
    repetidos = set() #set de repetidos
    vistos = set() #set de numeros vistos 
    hay_ceros = False #bandera que comprueba si existen ceros 

    for i in range(3,6): 
        
        for j in range(0,3):
            numero_inspeccionado = matriz_general_fin[i][j] 

            if numero_inspeccionado == 0: #verifica ceros en la matriz 
                hay_ceros = True

            if numero_inspeccionado in vistos: #  si esta en vistos, esta repetido 
                repetidos.add(numero_inspeccionado)
            
            if matriz_general_fin[i][j] != 0: #solo me interesan los numeros que no sean cero 
                vistos.add(numero_inspeccionado)

    if len(repetidos) == 0 and not hay_ceros: # si el largo de repetidos es 0 y a la vez no hay ceros en la matriz(osea espacios en blanco)
        bandera = True
    else:
        bandera = False
    
    return bandera


def validar_matriz_sector_5(matriz_general_fin:list)->bool:
    'recibe matriz general. recorre un segmento 3x3 de la matriz(ejemplo sector1 = 0-3,0-3) y verifica si hay numeros repetidos. Retorna bool, False si hay repetidos, True si no los hay'
    bandera = None   #bandera de retorno
    repetidos = set() #set de repetidos
    vistos = set() #set de numeros vistos 
    hay_ceros = False #bandera que comprueba si existen ceros 

    for i in range(3,6): 
        
        for j in range(3,6):
            numero_inspeccionado = matriz_general_fin[i][j] 

            if numero_inspeccionado == 0: #verifica ceros en la matriz 
                hay_ceros = True

            if numero_inspeccionado in vistos: #  si esta en vistos, esta repetido 
                repetidos.add(numero_inspeccionado)
            
            if matriz_general_fin[i][j] != 0: #solo me interesan los numeros que no sean cero 
                vistos.add(numero_inspeccionado)

    if len(repetidos) == 0 and not hay_ceros: # si el largo de repetidos es 0 y a la vez no hay ceros en la matriz(osea espacios en blanco)
        bandera = True
    else:
        bandera = False
    
    return bandera


def validar_matriz_sector_6(matriz_general_fin:list)->bool:
    'recibe matriz general. recorre un segmento 3x3 de la matriz(ejemplo sector1 = 0-3,0-3) y verifica si hay numeros repetidos. Retorna bool, False si hay repetidos, True si no los hay'
    bandera = None   #bandera de retorno
    repetidos = set() #set de repetidos
    vistos = set() #set de numeros vistos 
    hay_ceros = False #bandera que comprueba si existen ceros 

    for i in range(3,6): 
        
        for j in range(6,9):
            numero_inspeccionado = matriz_general_fin[i][j] 

            if numero_inspeccionado == 0: #verifica ceros en la matriz 
                hay_ceros = True

            if numero_inspeccionado in vistos: #  si esta en vistos, esta repetido 
                repetidos.add(numero_inspeccionado)
            
            if matriz_general_fin[i][j] != 0: #solo me interesan los numeros que no sean cero 
                vistos.add(numero_inspeccionado)

    if len(repetidos) == 0 and not hay_ceros: # si el largo de repetidos es 0 y a la vez no hay ceros en la matriz(osea espacios en blanco)
        bandera = True
    else:
        bandera = False
    
    return bandera

def validar_matriz_sector_7(matriz_general_fin:list)->bool:
    'recibe matriz general. recorre un segmento 3x3 de la matriz(ejemplo sector1 = 0-3,0-3) y verifica si hay numeros repetidos. Retorna bool, False si hay repetidos, True si no los hay'
    bandera = None   #bandera de retorno
    repetidos = set() #set de repetidos
    vistos = set() #set de numeros vistos 
    hay_ceros = False #bandera que comprueba si existen ceros 

    for i in range(6,9): 
        
        for j in range(0,3):
            numero_inspeccionado = matriz_general_fin[i][j] 

            if numero_inspeccionado == 0: #verifica ceros en la matriz 
                hay_ceros = True

            if numero_inspeccionado in vistos: #  si esta en vistos, esta repetido 
                repetidos.add(numero_inspeccionado)
            
            if matriz_general_fin[i][j] != 0: #solo me interesan los numeros que no sean cero 
                vistos.add(numero_inspeccionado)

    if len(repetidos) == 0 and not hay_ceros: # si el largo de repetidos es 0 y a la vez no hay ceros en la matriz(osea espacios en blanco)
        bandera = True
    else:
        bandera = False
    
    return bandera


def validar_matriz_sector_8(matriz_general_fin:list)->bool:
    'recibe matriz general. recorre un segmento 3x3 de la matriz(ejemplo sector1 = 0-3,0-3) y verifica si hay numeros repetidos. Retorna bool, False si hay repetidos, True si no los hay'
    bandera = None   #bandera de retorno
    repetidos = set() #set de repetidos
    vistos = set() #set de numeros vistos 
    hay_ceros = False #bandera que comprueba si existen ceros 

    for i in range(6,9): 
        
        for j in range(3,6):
            numero_inspeccionado = matriz_general_fin[i][j] 

            if numero_inspeccionado == 0: #verifica ceros en la matriz 
                hay_ceros = True

            if numero_inspeccionado in vistos: #  si esta en vistos, esta repetido 
                repetidos.add(numero_inspeccionado)
            
            if matriz_general_fin[i][j] != 0: #solo me interesan los numeros que no sean cero 
                vistos.add(numero_inspeccionado)

    if len(repetidos) == 0 and not hay_ceros: # si el largo de repetidos es 0 y a la vez no hay ceros en la matriz(osea espacios en blanco)
        bandera = True
    else:
        bandera = False
    
    return bandera


def validar_matriz_sector_9(matriz_general_fin:list)->bool:
    'recibe matriz general. recorre un segmento 3x3 de la matriz(ejemplo sector1 = 0-3,0-3) y verifica si hay numeros repetidos. Retorna bool, False si hay repetidos, True si no los hay'
    bandera = None   #bandera de retorno
    repetidos = set() #set de repetidos
    vistos = set() #set de numeros vistos 
    hay_ceros = False #bandera que comprueba si existen ceros 

    for i in range(6,9): 
        
        for j in range(6,9):
            numero_inspeccionado = matriz_general_fin[i][j] 

            if numero_inspeccionado == 0: #verifica ceros en la matriz 
                hay_ceros = True

            if numero_inspeccionado in vistos: #  si esta en vistos, esta repetido 
                repetidos.add(numero_inspeccionado)
            
            if matriz_general_fin[i][j] != 0: #solo me interesan los numeros que no sean cero 
                vistos.add(numero_inspeccionado)

    if len(repetidos) == 0 and not hay_ceros: # si el largo de repetidos es 0 y a la vez no hay ceros en la matriz(osea espacios en blanco)
        bandera = True
    else:
        bandera = False
    
    return bandera



def dibujar_validacion_sector1(pantalla:pg.Surface,bandera_sector1:bool):
    'recibe pantalla(surface) y un bool, dibuja un bordecito verde si el bool es verdadero o rojo si es falso '
    rect = pg.Rect(150,150,150,150)
    if bandera_sector1 :
        pg.draw.rect(pantalla,(0,150,0),rect,3)
    else:
        pg.draw.rect(pantalla,(150,0,0),rect,3)

def dibujar_validacion_sector2(pantalla:pg.Surface,bandera_sector1:bool):
    'recibe pantalla(surface) y un bool, dibuja un bordecito verde si el bool es verdadero o rojo si es falso '
    rect = pg.Rect(300,150,150,150)
    if bandera_sector1 :
        pg.draw.rect(pantalla,(0,150,0),rect,3)
    else:
        pg.draw.rect(pantalla,(150,0,0),rect,3)

def dibujar_validacion_sector3(pantalla:pg.Surface,bandera_sector1:bool):
    'recibe pantalla(surface) y un bool, dibuja un bordecito verde si el bool es verdadero o rojo si es falso '
    rect = pg.Rect(450,150,150,150)
    if bandera_sector1 :
        pg.draw.rect(pantalla,(0,150,0),rect,3)
    else:
        pg.draw.rect(pantalla,(150,0,0),rect,3)


def dibujar_validacion_sector4(pantalla:pg.Surface,bandera_sector1:bool):
    'recibe pantalla(surface) y un bool, dibuja un bordecito verde si el bool es verdadero o rojo si es falso '
    rect = pg.Rect(150,300,150,150)
    if bandera_sector1 :
        pg.draw.rect(pantalla,(0,150,0),rect,3)
    else:
        pg.draw.rect(pantalla,(150,0,0),rect,3)

def dibujar_validacion_sector5(pantalla:pg.Surface,bandera_sector1:bool):
    'recibe pantalla(surface) y un bool, dibuja un bordecito verde si el bool es verdadero o rojo si es falso '
    rect = pg.Rect(300,300,150,150)
    if bandera_sector1 :
        pg.draw.rect(pantalla,(0,150,0),rect,3)
    else:
        pg.draw.rect(pantalla,(150,0,0),rect,3)

def dibujar_validacion_sector6(pantalla:pg.Surface,bandera_sector1:bool):
    'recibe pantalla(surface) y un bool, dibuja un bordecito verde si el bool es verdadero o rojo si es falso '
    rect = pg.Rect(450,300,150,150)
    if bandera_sector1 :
        pg.draw.rect(pantalla,(0,150,0),rect,3)
    else:
        pg.draw.rect(pantalla,(150,0,0),rect,3)

def dibujar_validacion_sector7(pantalla:pg.Surface,bandera_sector1:bool):
    'recibe pantalla(surface) y un bool, dibuja un bordecito verde si el bool es verdadero o rojo si es falso '
    rect = pg.Rect(150,450,150,150)
    if bandera_sector1 :
        pg.draw.rect(pantalla,(0,150,0),rect,3)
    else:
        pg.draw.rect(pantalla,(150,0,0),rect,3)

def dibujar_validacion_sector8(pantalla:pg.Surface,bandera_sector1:bool):
    'recibe pantalla(surface) y un bool, dibuja un bordecito verde si el bool es verdadero o rojo si es falso '
    rect = pg.Rect(300,450,150,150)
    if bandera_sector1 :
        pg.draw.rect(pantalla,(0,150,0),rect,3)
    else:
        pg.draw.rect(pantalla,(150,0,0),rect,3)

def dibujar_validacion_sector9(pantalla:pg.Surface,bandera_sector1:bool):
    'recibe pantalla(surface) y un bool, dibuja un bordecito verde si el bool es verdadero o rojo si es falso '
    rect = pg.Rect(450,450,150,150)
    if bandera_sector1 :
        pg.draw.rect(pantalla,(0,150,0),rect,3)
    else:
        pg.draw.rect(pantalla,(150,0,0),rect,3)



def dibujar_todas_las_validaciones(pantalla:pg.Surface,bandera_sector1:bool,bandera_sector2:bool,bandera_sector3:bool,
                    bandera_sector4:bool,bandera_sector5:bool,bandera_sector6:bool,bandera_sector7:bool,bandera_sector8:bool,bandera_sector9:bool,flag_filas_0_3:bool,flag_filas_3_6:bool):
    'recibe pantalla y 9 bool dibuja los 9 cuadrados segun si bandera es falso o verdadero '
    dibujar_validacion_sector1(pantalla,bandera_sector1)
    dibujar_validacion_sector2(pantalla,bandera_sector2)
    dibujar_validacion_sector3(pantalla,bandera_sector3)
    dibujar_validacion_sector4(pantalla,bandera_sector4)
    dibujar_validacion_sector5(pantalla,bandera_sector5)
    dibujar_validacion_sector6(pantalla,bandera_sector6)
    dibujar_validacion_sector7(pantalla,bandera_sector7)
    dibujar_validacion_sector8(pantalla,bandera_sector8)
    dibujar_validacion_sector9(pantalla,bandera_sector9)
    dibujar_validacion_sectores123(pantalla,flag_filas_0_3)
    dibujar_validacion_sectores456(pantalla,flag_filas_3_6)


#fuente.render no permite int, y no permite castearlo a str si es un numero con ceros adelante. Tuve que hacer esto
def formatear_puntaje(puntaje:int) -> str:
    'recibe int, convierte a string, retorna string'
    return f"{puntaje:04d}" #llenar con 4 ceros 




def verificar_por_filas_1(matriz)->bool:
    'verifica las filas 0, 1, 2 y arroja True si no hay repetidos, false si hay repetidos'
    bandera = False
    hay_repetidos = False
    for fila in range(0,3):
        vistos = set()
        repetidos = set()
        for columna in range(0,9):

            numero_inspeccionado = (matriz[fila][columna])
            
            if numero_inspeccionado in vistos: #  si esta en vistos, esta repetido 
               repetidos.add(numero_inspeccionado)
               hay_repetidos = True
            if matriz[fila][columna] != 0: #solo me interesan los numeros que no sean cero 
                vistos.add(numero_inspeccionado)
                
    if len(repetidos) == 0 and not hay_repetidos:
        bandera = True
    else: bandera = False
    print("repetidos en filas 0-3 encontrados")
    return bandera
                



           
def verificar_por_filas_2(matriz)->bool:
    'verifica las filas y arroja True si no hay repetidos, false si hay repetidos'
    bandera = False
    hay_repetidos = False
    
    for fila in range(3,6):
        vistos = set()
        repetidos = set()
        for columna in range(0,9):

            numero_inspeccionado = (matriz[fila][columna])
            
            if numero_inspeccionado in vistos: #  si esta en vistos, esta repetido 
               repetidos.add(numero_inspeccionado)
               hay_repetidos = True
            if matriz[fila][columna] != 0: #solo me interesan los numeros que no sean cero 
                vistos.add(numero_inspeccionado)
                
    if len(repetidos) == 0 and not hay_repetidos:
        bandera = True
    else: bandera = False
    print("repetidos en filas 3-6 encontrados")
    return bandera
                

def verificar_por_filas_3(matriz)->bool:
    bandera = False
    hay_repetidos = False
    
    for fila in range(6,9):
        vistos = set()
        repetidos = set()
        for columna in range(0,9):

            numero_inspeccionado = (matriz[fila][columna])
            
            if numero_inspeccionado in vistos: #  si esta en vistos, esta repetido 
               repetidos.add(numero_inspeccionado)
               hay_repetidos = True
            if matriz[fila][columna] != 0: #solo me interesan los numeros que no sean cero 
                vistos.add(numero_inspeccionado)
                
    if len(repetidos) == 0 and not hay_repetidos:
        bandera = True
    else: bandera = False 
    print("repetidos en filas 6-9 encontrados")

    return bandera
                


def verificar_por_columnas_1(matriz)->bool:
    'recibe matriz, itera 3 columnas buscando repetidos, True si no hay repetidos, False si hay. Retorna bool'
    bandera = False
    hay_repetidos = False
    
    for columna in range(0,3):
        vistos = set()
        repetidos = set()
        for fila in range(0,9):

            numero_inspeccionado = (matriz[fila][columna])
            
            if numero_inspeccionado in vistos: #  si esta en vistos, esta repetido 
               repetidos.add(numero_inspeccionado)
               hay_repetidos = True
            if matriz[fila][columna] != 0: #solo me interesan los numeros que no sean cero 
                vistos.add(numero_inspeccionado)
                
    if len(repetidos) == 0 and not hay_repetidos:
        bandera = True
    else: bandera = False 
    print("repetidos en columnas 0,3 encontrados")
    
    return bandera
    




def verificar_por_columnas_2(matriz)->bool:
    'recibe matriz, itera 3 columnas buscando repetidos, True si no hay repetidos, False si hay. Retorna bool'
    bandera = False
    hay_repetidos = False
    
    for columna in range(3,6):
        vistos = set()
        repetidos = set()
        for fila in range(0,9):

            numero_inspeccionado = (matriz[fila][columna])
            
            if numero_inspeccionado in vistos: #  si esta en vistos, esta repetido 
               repetidos.add(numero_inspeccionado)
               hay_repetidos = True
            if matriz[fila][columna] != 0: #solo me interesan los numeros que no sean cero 
                vistos.add(numero_inspeccionado)
                
    if len(repetidos) == 0 and not hay_repetidos:
        bandera = True
    else: bandera = False 
    print("repetidos en columnas 3,6 encontrados")
    
    return bandera



def verificar_por_columnas_3(matriz)->bool:
    'recibe matriz, itera 3 columnas buscando repetidos, True si no hay repetidos, False si hay. Retorna bool'
    bandera = False
    hay_repetidos = False
    
    for columna in range(6,9):
        vistos = set()
        repetidos = set()
        for fila in range(0,9):

            numero_inspeccionado = (matriz[fila][columna])
            
            if numero_inspeccionado in vistos: #  si esta en vistos, esta repetido 
               repetidos.add(numero_inspeccionado)
               hay_repetidos = True
            if matriz[fila][columna] != 0: #solo me interesan los numeros que no sean cero 
                vistos.add(numero_inspeccionado)
                
    if len(repetidos) == 0 and not hay_repetidos:
        bandera = True
    else: bandera = False 
    print("repetidos en columnas 6,9 encontrados")
    
    return bandera



def agregar_numeros_al_azar_v3(matriz:list, cantidad:int) -> list:
    '''recibe una matriz y un numero, agrega numeros al azar, en lugares al azar en una matriz. Retorna una matriz'''
    filas = len(matriz)
    columnas = len(matriz[0])
    contador = 0

    while contador < cantidad:

        fila = random.randrange(filas)
        columna = random.randrange(columnas)
        numero = random.randint(1, 9)

        # si el lugar ya tiene un número distinto de 0, saltar
        if matriz[fila][columna] != 0:
            continue

        #si el num ya esta en la fila
        if numero in matriz[fila]:
            continue

        # si el numero ya esta en la columna
        repetido_columna = False
        for f in range(filas):
            if matriz[f][columna] == numero:
                repetido_columna = True
                break
        if repetido_columna:
            continue

        #si pasa todo esto lo coloca
        matriz[fila][columna] = numero
        contador += 1

    return matriz

#validacion por filas de los primeros 3 sectores 
def dibujar_validacion_sectores123(pantalla:pg.Surface,flag_filas_0_3:bool):
    'recibe pantalla(surface) y un bool, dibuja un bordecito verde si el bool es verdadero o rojo si es falso '
    rect = pg.Rect(150,150,450,150)
    
    if flag_filas_0_3 :
        pg.draw.rect(pantalla,(0,150,0),rect,7)
    else:
        pg.draw.rect(pantalla,(110,0,0),rect,7)

#validacion por filas de los sectores 4,5,6:

def dibujar_validacion_sectores456(pantalla:pg.Surface,flag_filas_3_6:bool):
    'recibe pantalla(surface) y un bool, dibuja un bordecito verde si el bool es verdadero o rojo si es falso '
    rect = pg.Rect(150,300,450,150)
    
    if flag_filas_3_6 :
        pg.draw.rect(pantalla,(0,150,0),rect,7)
    else:
        pg.draw.rect(pantalla,(110,0,0),rect,7)





def descontar_puntaje(bandera1:bool,bandera2:bool,bandera3:bool,bandera4:bool,bandera5:bool,bandera6:bool,bandera7:bool,bandera8:bool,bandera9:bool)->int:
    'recibe 9 bool, suma 9 por cada bandera verdadera, resta 1 por cada bandera falsa, retorna (int)'
    todas = [bandera1,bandera2,bandera3,bandera4,bandera5,bandera6,bandera7,bandera8,bandera9]
    puntaje = 0000

    for i in range(9):
        bandera_inspeccionada =  todas[i]
        if bandera_inspeccionada:
            puntaje +=9
        else:
            puntaje +=1
    str(puntaje)
    
    return puntaje

