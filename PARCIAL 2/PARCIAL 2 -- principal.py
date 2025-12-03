import pygame as pg
import time
from PARCIAL_2_funciones import *
from PARCIAL_2_configuraciones import *
import json
import os

fin = False
correccion_tamaño_menu = pg.transform.scale(pantalla, (900,700)) #esto corrige el tamaño del fondo 
texto_para_ingresar = "" #aca va el nickname del jugador 


#Bucle principal
while True:
    reloj.tick(60)
    
    
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            pg.quit()
            quit()

        match pantalla_actual: 

            case "nombre":  #desde este case se guarda el nombre del jugador, al presionar enter salta hacia el menu de inicio

                pantalla.blit(correccion_fondo_pantalla,(0,0)) #fondo de pantalla
                renderencio = fuente.render(texto_para_ingresar,True, (255,255,255)) #render del texto usado para blitear
                pantalla.blit(renderencio,(300,300)) 
                pantalla.blit(ingrese_nombre,(300,250))

                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_BACKSPACE: #tecla borrar 
                        texto_para_ingresar = texto_para_ingresar[0:-1] #texto para ingresar = lo que el usuario escribio 
                    elif evento.key == pg.K_RETURN: #tecla enter 
                        guardar_nombre_puntaje_json(texto_para_ingresar) #guardo json
                        pantalla_actual = "inicio" #cambia hacia pantalla de inicio 
                        print("ingresado correctamente")
                    else:
                        texto_para_ingresar += evento.unicode
                        
            
            case "inicio": #este case es la pantalla principal del menu
            
                pantalla.blit(correccion_fondo_pantalla,(0,0)) #fondo de pantalla

                pantalla.blit(nivel,(300,100)) #boton 1 
                pantalla.blit(texto1,(390, 100)) #texto 1

                pantalla.blit(jugar,(300,245))#boton2
                pantalla.blit(texto_2,(390,245))#texto2

                pantalla.blit(boton_puntaje,(300,390))#boton3
                pantalla.blit(texto_3,(354, 390))#texto3
                
                pantalla.blit(boton_salida,(300,540)) #boton4
                pantalla.blit(texto_4,(360,540))#texto4 
                
                #eventos del mouse - pantalla de inicio: 
                if evento.type == pg.MOUSEBUTTONDOWN: 
                    if evento.button == 1: #click derecho 
                        posicion = evento.pos   #posicion del click
                        print(f"click en {posicion}")

                        if boton1.collidepoint(posicion):#click boton1 "Nivel"                
                            pantalla_actual = "nivel"
                            print("Nivel Presionado")

                        elif boton2.collidepoint(posicion):#click boton2 "Jugar"
                            pantalla_actual = "jugar"
                            print("Jugar presionado")


                        elif boton3.collidepoint(posicion): #click boton3 "Ver Puntaje"
                            pantalla_actual = "ver puntaje"
                            print("Puntaje presionado")
                        
                        elif boton4.collidepoint(posicion): #click boton4 "Salir"
                            print("saliendo del juego.")
                            pg.quit()
                            quit()


            
            case "nivel":

                #blits de los rect de los botones 
                pantalla.blit(correccion_tamaño_nivel,(0, 0))  #corrector de tamaño de fondo
                pantalla.blit(nivel_nivel ,(250,50)) #rectangulo 1
                pantalla.blit(texto_facil,(250,50)) #texto 1 

                pantalla.blit(medio,(250,150)) #rectangulo 2 
                pantalla.blit(texto_medio ,(250,150)) #texto 2 

                pantalla.blit(dificil,(250,250)) #rectangulo 3 
                pantalla.blit(texto_dificil,(250,250)) #texto 3

                pantalla.blit(volver, (250, 350)) #rectangulo volver
                pantalla.blit(texto_4_nivel,(250,350)) #texto volver
                
                
                #mouse:
                if evento.type == pg.MOUSEBUTTONDOWN: 
                        posicion = (evento.pos)


                        if evento.button ==1:
                            print(" ")

                        if boton1_nivel.collidepoint(posicion):         
                            modo_dificultad = "facil"    #dificultad
                            pantalla_actual = "inicio"   #vuelvo a inicio automaticamente en todos los casos
                            print("modo facil seleccionado")


                        elif boton2_nivel.collidepoint(posicion):
                            modo_dificultad = "medio"
                            pantalla_actual = "inicio"
                            print("modo medio seleccionado")


                        elif boton3_nivel.collidepoint(posicion):
                            modo_dificultad = "dificil"
                            pantalla_actual = "inicio"
                            print("modo dificil seleccionado")


                        elif boton4_nivel.collidepoint(posicion):
                            pantalla_actual = "inicio"

                
            case "jugar":
                
                if modo_dificultad == "dificil":
                    
                    texto_de_puntaje = fuente.render(str(puntaje), True, (0,0,0))
                    rect_de_puntaje = texto_de_puntaje.get_rect(topleft=(800,20))
                    pantalla.blit(texto_de_puntaje, rect_de_puntaje)
                    
                    pantalla.fill((189, 162, 162))#color de fondo de pantalla durante el juego
                    pantalla.blit(validar_celda,(650,200)) #blit de validar celda
                    pantalla.blit(texto_validar_celda,(710,215))#blit de texto validar celda
                    pantalla.blit(texto_de_palabra_puntaje,rect_de_texto_de_palabra_puntaje)#blit de texto "puntaje" 
                    pantalla.blit(reset_juego,(650,400)) #blit de boton "reiniciar juego"
                    pantalla.blit(texto_reiniciar_juego,(667, 415)) #texto de "reiniciar juego "
                    pantalla.blit(texto_de_puntaje,rect_de_puntaje) #numeros del puntaje
                    pantalla_actual = pausar_juego(evento,pantalla_actual) #controlador de pantalla, #ESC = volver a inicio - pausar
                    

                    #dibujos de celdas - cuadrados
                    celdas_sector_1 = dibujar_cuadrados(pantalla,50,3,3,150,150)
                    celdas_sector_2 = dibujar_cuadrados(pantalla,50,3,3,300,150)
                    celdas_sector_3 = dibujar_cuadrados(pantalla,50,3,3,450,150)
                    celdas_sector_4 = dibujar_cuadrados(pantalla,50,3,3,150,300)
                    celdas_sector_5 = dibujar_cuadrados(pantalla,50,3,3,300,300)
                    celdas_sector_6 = dibujar_cuadrados(pantalla,50,3,3,450,300)
                    celdas_sector_7 = dibujar_cuadrados(pantalla,50,3,3,150,450)
                    celdas_sector_8 = dibujar_cuadrados(pantalla,50,3,3,300,450)
                    celdas_sector_9 = dibujar_cuadrados(pantalla,50,3,3,450,450)

                    #union de celdas:
                    todas_las_celdas = (
                        celdas_sector_1 + celdas_sector_2 + celdas_sector_3 +
                        celdas_sector_4 + celdas_sector_5 + celdas_sector_6 +
                        celdas_sector_7 + celdas_sector_8 + celdas_sector_9)

                    dibujar_lineas(pantalla) #son las 4 lineas que separan los 9 espacios de la cuadricula
                    
                    #Dibujar numeros:
                    matriz_general_dibujos = dibujar_numeros(pantalla,nuevita,tamaño, fuente,150,150)
                    
                    #ingresar numero por teclado
                    if evento.type == pg.KEYDOWN and celda_seleccionada is not None:#verifico que sea evento de telclado y se haya clickeado una celda 
                        numero_ingresado = input_numero(evento,celda_seleccionada)
                        nuevita = borrar_numero_de_matriz(nuevita,evento,celda_seleccionada,tamaño,x_inicial=150, y_inicial=150) #funcion borrar numero
                        
                        if numero_ingresado is not None: #si numero es algo
                            
                            nuevita = ingresar_numero_a_matriz(nuevita,numero_ingresado,celda_seleccionada,tamaño) #ingresar numero 
                            #banderas de sectores 3x3 | 
                            flag_sector_1 = validar_matriz_sector_1(nuevita)
                            flag_sector_2 = validar_matriz_sector_2(nuevita)
                            flag_sector_3 = validar_matriz_sector_3(nuevita)
                            flag_sector_4 = validar_matriz_sector_4(nuevita)
                            flag_sector_5 = validar_matriz_sector_5(nuevita)
                            flag_sector_6 = validar_matriz_sector_6(nuevita)
                            flag_sector_7 = validar_matriz_sector_7(nuevita)
                            flag_sector_8 = validar_matriz_sector_8(nuevita)
                            flag_sector_9 = validar_matriz_sector_9(nuevita)

                            
                            
                            lista_de_banderas = [flag_sector_1,flag_sector_2,flag_sector_3,flag_sector_4,flag_sector_5,flag_sector_6,flag_sector_7,flag_sector_8,flag_sector_9]
                            #aca deberia ir la funcion de descontar puntos 
                            print(nuevita)
                            
                            #Detector de colisiones:
                    if evento.type == pg.MOUSEBUTTONDOWN:
                        posicion = (evento.pos) #posicion
                        celda_seleccionada = detectar_celda(posicion,todas_las_celdas) #detecta celda seleccionada
                        dibujar_borde_verde(pantalla,celda_seleccionada) #dibuja un bordecito verde en la celda clickeada
                        
                        #validar celda
                        if boton_validar_celda.collidepoint(posicion):#detecta click en boton "validar celdas"
                            dibujar_todas_las_validaciones(pantalla,flag_sector_1,flag_sector_2,flag_sector_3,
                            flag_sector_4,flag_sector_5,flag_sector_6,flag_sector_7,flag_sector_8,flag_sector_9,flag_filas_0_3,flag_filas_3_6)
                            
                            puntaje = sumar_restar_puntaje(lista_de_banderas,puntaje)
                            bandera_final = validar_final(lista_de_banderas)
                            if bandera_final:
                                fin = True
                                actualizar_puntaje_json(texto_para_ingresar,puntaje)

                            print(f"puntaje: {puntaje}")
                            print("validar celda presionado")

                        #reiniciar
                        if boton_reiniciar_juego.collidepoint(posicion): #detecta click en  boton "reiniciar juego"
                            reiniciar_juego = True
                            if reiniciar_juego == True:
                                matriz_vacia = iniciar_matriz(9,9,0) #inicia matriz, | int1 = cantidad de filas| int2 = cantidad de columnas| int3 = numeros que contiene  
                                matriz_dificil = generar_matriz_completa_C(matriz_vacia) #llena la matriz vacia 
                                nuevita = agregar_ceros_final(matriz_dificil,6) #limpia ceros y repeticiones 
                                celda_seleccionada = None
                                puntaje = 0
                                reiniciar_juego = False
                                print("reiniciar presionado")


                        
                        
                if modo_dificultad == "medio":
                        texto_de_puntaje = fuente.render(str(puntaje), True, (0,0,0))
                        rect_de_puntaje = texto_de_puntaje.get_rect(topleft=(800,20))
                        pantalla.blit(texto_de_puntaje, rect_de_puntaje)
                    
                        pantalla.fill((189, 162, 162))#color de fondo de pantalla durante el juego
                        pantalla.blit(validar_celda,(650,200)) #blit de validar celda
                        pantalla.blit(texto_validar_celda,(710,215))#blit de texto validar celda
                        pantalla.blit(texto_de_palabra_puntaje,rect_de_texto_de_palabra_puntaje)#blit de texto "puntaje" 
                        pantalla.blit(reset_juego,(650,400)) #blit de boton "reiniciar juego"
                        pantalla.blit(texto_reiniciar_juego,(667, 415)) #texto de "reiniciar juego "
                        pantalla.blit(texto_de_puntaje,rect_de_puntaje) #numeros del puntaje
                        pantalla_actual = pausar_juego(evento,pantalla_actual) #controlador de pantalla, #ESC = volver a inicio - pausar
                    

                        #dibujos de celdas - cuadrados
                        celdas_sector_1_medio = dibujar_cuadrados(pantalla,50,3,3,150,150)
                        celdas_sector_2_medio = dibujar_cuadrados(pantalla,50,3,3,300,150)
                        celdas_sector_3_medio = dibujar_cuadrados(pantalla,50,3,3,450,150)
                        celdas_sector_4_medio = dibujar_cuadrados(pantalla,50,3,3,150,300)
                        celdas_sector_5_medio = dibujar_cuadrados(pantalla,50,3,3,300,300)
                        celdas_sector_6_medio = dibujar_cuadrados(pantalla,50,3,3,450,300)
                        celdas_sector_7_medio = dibujar_cuadrados(pantalla,50,3,3,150,450)
                        celdas_sector_8_medio = dibujar_cuadrados(pantalla,50,3,3,300,450)
                        celdas_sector_9_medio = dibujar_cuadrados(pantalla,50,3,3,450,450)

                        #union de celdas:
                        todas_las_celdas_medio = (
                            celdas_sector_1_medio + celdas_sector_2_medio + celdas_sector_3_medio +
                            celdas_sector_4_medio + celdas_sector_5_medio + celdas_sector_6_medio +
                            celdas_sector_7_medio + celdas_sector_8_medio + celdas_sector_9_medio)

                        dibujar_lineas(pantalla) #son las 4 lineas que separan los 9 espacios de la cuadricula
                        
                        #Dibujar numeros:
                        matriz_general_dibujos_medio = dibujar_numeros(pantalla,matriz_general_fin_medio,tamaño, fuente,150,150)
                        
                        #ingresar numero por teclado
                        if evento.type == pg.KEYDOWN and celda_seleccionada_medio is not None:#verifico que sea evento de telclado y se haya clickeado una celda 
                            numero_ingresado = input_numero(evento,celda_seleccionada_medio)
                            matriz_general_fin_medio = borrar_numero_de_matriz(matriz_general_fin_medio,evento,celda_seleccionada_medio,tamaño,x_inicial=150, y_inicial=150) #funcion borrar numero
                            
                            if numero_ingresado is not None: #si numero es algo
                                
                                matriz_general_fin_medio = ingresar_numero_a_matriz(matriz_general_fin_medio,numero_ingresado,celda_seleccionada_medio,tamaño) #ingresar numero 
                                #banderas de sectores 3x3 | 
                                flag_sector_1 = validar_matriz_sector_1(matriz_general_fin_medio)
                                flag_sector_2 = validar_matriz_sector_2(matriz_general_fin_medio)
                                flag_sector_3 = validar_matriz_sector_3(matriz_general_fin_medio)
                                flag_sector_4 = validar_matriz_sector_4(matriz_general_fin_medio)
                                flag_sector_5 = validar_matriz_sector_5(matriz_general_fin_medio)
                                flag_sector_6 = validar_matriz_sector_6(matriz_general_fin_medio)
                                flag_sector_7 = validar_matriz_sector_7(matriz_general_fin_medio)
                                flag_sector_8 = validar_matriz_sector_8(matriz_general_fin_medio)
                                flag_sector_9 = validar_matriz_sector_9(matriz_general_fin_medio)

                                
                                
                                lista_de_banderas = [flag_sector_1,flag_sector_2,flag_sector_3,flag_sector_4,flag_sector_5,flag_sector_6,flag_sector_7,flag_sector_8,flag_sector_9]
                                #aca deberia ir la funcion de descontar puntos 
                                
                                
                                #Detector de colisiones:
                        if evento.type == pg.MOUSEBUTTONDOWN:
                            posicion = (evento.pos) #posicion
                            celda_seleccionada_medio = detectar_celda(posicion,todas_las_celdas_medio) #detecta celda seleccionada
                            dibujar_borde_verde(pantalla,celda_seleccionada_medio) #dibuja un bordecito verde en la celda clickeada
                            
                                
                            if boton_validar_celda.collidepoint(posicion):#detecta click en boton "validar celdas"
                                dibujar_todas_las_validaciones(pantalla,flag_sector_1,flag_sector_2,flag_sector_3,
                                flag_sector_4,flag_sector_5,flag_sector_6,flag_sector_7,flag_sector_8,flag_sector_9,flag_filas_0_3,flag_filas_3_6)
                                
                                puntaje = sumar_restar_puntaje(lista_de_banderas,puntaje)
                                bandera_final = validar_final(lista_de_banderas)
                                if bandera_final:
                                    fin = True
                                    actualizar_puntaje_json(texto_para_ingresar,puntaje)
                                    print(f"puntaje: {puntaje}")
                                    print("validar celda presionado")
                             
                            if boton_reiniciar_juego.collidepoint(posicion): #boton reiniciar
                                reiniciar_juego = True
                                if reiniciar_juego == True:
                                    matriz_vacia_medio = iniciar_matriz(9,9,0)
                                    matriz_medio = generar_matriz_completa_C(matriz_vacia_medio) #llena la matriz vacia 
                                    matriz_general_fin_medio = agregar_ceros_final(matriz_medio,5) #limpia ceros y repeticiones 

                                
                                    celda_seleccionada_medio = None
                                    puntaje = 0
                                    reiniciar_juego = False
                                    print("reiniciar presionado")
                            
                                    

                # facil
                if modo_dificultad == "facil":
                    

                    texto_de_puntaje = fuente.render(str(puntaje), True, (0,0,0))
                    rect_de_puntaje = texto_de_puntaje.get_rect(topleft=(800,20))
                    pantalla.blit(texto_de_puntaje, rect_de_puntaje)
                    
                    pantalla.fill((189, 162, 162))#color de fondo de pantalla durante el juego
                    pantalla.blit(validar_celda,(650,200)) #blit de validar celda
                    pantalla.blit(texto_validar_celda,(710,215))#blit de texto validar celda
                    pantalla.blit(texto_de_palabra_puntaje,rect_de_texto_de_palabra_puntaje)#blit de texto "puntaje" 
                    pantalla.blit(reset_juego,(650,400)) #blit de boton "reiniciar juego"
                    pantalla.blit(texto_reiniciar_juego,(667, 415)) #texto de "reiniciar juego "
                    pantalla.blit(texto_de_puntaje,rect_de_puntaje) #numeros del puntaje
                    pantalla_actual = pausar_juego(evento,pantalla_actual) #controlador de pantalla, #ESC = volver a inicio - pausar
                    

                    #dibujos de celdas - cuadrados
                    celdas_sector_1_facil = dibujar_cuadrados(pantalla,50,3,3,150,150)
                    celdas_sector_2_facil = dibujar_cuadrados(pantalla,50,3,3,300,150)
                    celdas_sector_3_facil = dibujar_cuadrados(pantalla,50,3,3,450,150)
                    celdas_sector_4_facil = dibujar_cuadrados(pantalla,50,3,3,150,300)
                    celdas_sector_5_facil = dibujar_cuadrados(pantalla,50,3,3,300,300)
                    celdas_sector_6_facil = dibujar_cuadrados(pantalla,50,3,3,450,300)
                    celdas_sector_7_facil = dibujar_cuadrados(pantalla,50,3,3,150,450)
                    celdas_sector_8_facil = dibujar_cuadrados(pantalla,50,3,3,300,450)
                    celdas_sector_9_facil = dibujar_cuadrados(pantalla,50,3,3,450,450)

                    #union de celdas:
                    todas_las_celdas_facil = (
                        celdas_sector_1_facil + celdas_sector_2_facil + celdas_sector_3_facil +
                        celdas_sector_4_facil + celdas_sector_5_facil + celdas_sector_6_facil +
                        celdas_sector_7_facil + celdas_sector_8_facil + celdas_sector_9_facil)

                    dibujar_lineas(pantalla) #son las 4 lineas que separan los 9 espacios de la cuadricula
                    
                    #Dibujar numeros:
                    matriz_general_dibujos_facil = dibujar_numeros(pantalla,matriz_general_fin_facil,tamaño, fuente,150,150)
                    
                    #ingresar numero por teclado
                    if evento.type == pg.KEYDOWN and celda_seleccionada_facil is not None:#verifico que sea evento de telclado y se haya clickeado una celda 
                        numero_ingresado = input_numero(evento,celda_seleccionada_facil)
                        matriz_general_fin_facil = borrar_numero_de_matriz(matriz_general_fin_facil,evento,celda_seleccionada_facil,tamaño,x_inicial=150, y_inicial=150) #funcion borrar numero
                        
                        if numero_ingresado is not None: #si numero es algo
                            
                            matriz_general_fin_facil = ingresar_numero_a_matriz(matriz_general_fin_facil,numero_ingresado,celda_seleccionada_facil,tamaño) #ingresar numero 
                            #banderas de sectores 3x3 | 
                            flag_sector_1 = validar_matriz_sector_1(matriz_general_fin_facil)
                            flag_sector_2 = validar_matriz_sector_2(matriz_general_fin_facil)
                            flag_sector_3 = validar_matriz_sector_3(matriz_general_fin_facil)
                            flag_sector_4 = validar_matriz_sector_4(matriz_general_fin_facil)
                            flag_sector_5 = validar_matriz_sector_5(matriz_general_fin_facil)
                            flag_sector_6 = validar_matriz_sector_6(matriz_general_fin_facil)
                            flag_sector_7 = validar_matriz_sector_7(matriz_general_fin_facil)
                            flag_sector_8 = validar_matriz_sector_8(matriz_general_fin_facil)
                            flag_sector_9 = validar_matriz_sector_9(matriz_general_fin_facil)

                            
                            
                            lista_de_banderas = [flag_sector_1,flag_sector_2,flag_sector_3,flag_sector_4,flag_sector_5,flag_sector_6,flag_sector_7,flag_sector_8,flag_sector_9]
                            #aca deberia ir la funcion de descontar puntos 
                            
                            
                            #Detector de colisiones:
                    if evento.type == pg.MOUSEBUTTONDOWN:
                        posicion = (evento.pos) #posicion
                        celda_seleccionada_facil = detectar_celda(posicion,todas_las_celdas_facil) #detecta celda seleccionada
                        dibujar_borde_verde(pantalla,celda_seleccionada_facil) #dibuja un bordecito verde en la celda clickeada
                        
                        
                            
                        if boton_validar_celda.collidepoint(posicion):#detecta click en boton "validar celdas"
                            dibujar_todas_las_validaciones(pantalla,flag_sector_1,flag_sector_2,flag_sector_3,
                            flag_sector_4,flag_sector_5,flag_sector_6,flag_sector_7,flag_sector_8,flag_sector_9,flag_filas_0_3,flag_filas_3_6)
                            
                            puntaje = sumar_restar_puntaje(lista_de_banderas,puntaje)
                            bandera_final = validar_final(lista_de_banderas)
                            if bandera_final:
                                    fin = True
                                    actualizar_puntaje_json(texto_para_ingresar,puntaje)

                            print(f"puntaje: {puntaje}")
                            print("validar celda presionado")
                             
                        if boton_reiniciar_juego.collidepoint(posicion): #detecta click en  boton "reiniciar juego"
                            reiniciar_juego = True
                            if reiniciar_juego == True:
                                matriz_vacia_facil = iniciar_matriz(9,9,0)
                                matriz_facil = generar_matriz_completa_C(matriz_vacia_facil) #llena la matriz vacia 
                                matriz_general_fin_facil = agregar_ceros_final(matriz_facil,4) #limpia ceros y repeticiones 
                                #esto se usa para controlar la interaccion entre funcion "input numero" y "dibujar numero ingresado" en el case "jugar"
                                celda_seleccionada_facil = None
                                puntaje = 0
                                reiniciar_juego = False
                            print("reiniciar presionado")
                            
                         
                        
                        # musica no hecha  
                        
                           
                       
             
                    
            case "ver puntaje":
                    
                    if not ver_ranking: #uso esta bandera porque de lo contrario la funcion "leer json" se llama mil veces seguidas
                        nombre_y_puntaje = leer_json("nombres_puntaje.json")
                        ver_ranking = True 
                    if pantalla_actual != "ver puntaje": #cuando cierro el "case", la bandera vuelve a ser false"
                        ver_ranking = False


                    pantalla.blit(correccion_fondo_pantalla, (0, 0))#blit de fondo de pantalla
                    ultimos_4 = nombre_y_puntaje[-5:][::-1] #[-5] significa, desde el ultimo elemento, 5 hacia atras 
                    #[::-1] es lo mismo que sort=reverse, pero escrito en numeros, ordena a la inversa 
                    y = 250  # posicion vertical inicial, se mueve +40 dentro del for 

                    for jugador in ultimos_4: #necesito este for para ver los ultimos 4 casos 
                        ambos_datos = f"{jugador['nombre']} - {jugador['puntaje']}" #extraigo datos del dict, lo paso a string 
                        surface_ambos_datos = fuente.render(ambos_datos, True, (255, 255, 255),(0,0,0))  #render para texto 
                        pantalla.blit(surface_ambos_datos, (300, y)) #blit de ambos datos 
                        y += 40 # uso esto para mover las impresiones cada vez que se mueve el for 

                #teclas para volver atras
                    if evento.type == pg.KEYDOWN: # tecla presionada 
                        if evento.key == pg.K_ESCAPE: #ESC
                            pantalla_actual = "inicio" 
                        if evento.key == pg.K_SPACE:#ESPACIO
                            pantalla_actual = "inicio"
                
                
                    
                

                
                         
    

    pg.display.flip()