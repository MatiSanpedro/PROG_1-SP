import pygame as pg
import time
from PARCIAL_2_funciones import *
from PARCIAL_2_configuraciones import * 
import os

correccion_tamaño_menu = pg.transform.scale(pantalla, (900,700)) #esto corrige el tamaño del fondo 



#Bucle principal
while True:
    reloj.tick(60)
    
    
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            pg.quit()
            quit()

        match pantalla_actual:

            
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
                    
                    pantalla.fill((189, 162, 162))#color de fondo de pantalla durante el juego
                    pantalla.blit(validar_celda,(650,200)) #blit de validar celda
                    pantalla.blit(texto_validar_celda,(710,215))#blit de texto validar celda
                    pantalla.blit(texto_de_palabra_puntaje,rect_de_texto_de_palabra_puntaje)#blit de texto "puntaje" 
                    pantalla.blit(reset_juego,(650,400)) #blit de boton "reiniciar juego"
                    pantalla.blit(texto_reiniciar_juego,(667, 415)) #texto de "reiniciar juego "
                    pantalla.blit(texto_de_puntaje,rect_de_puntaje) #numeros del puntaje
                    pantalla_actual = pausar_juego(evento,pantalla_actual) #controlador de pantalla, #ESC = volver a inicio - pausar
                    
                    

                    #dibujos de celdas - cuadrados
                    celdas_sector_1 = dibujar_cuadrados(pantalla,50,3,3,150,150) #sector 1
                    celdas_sector_2 = dibujar_cuadrados(pantalla,50,3,3,300,150) #sector 2
                    celdas_sector_3 = dibujar_cuadrados(pantalla,50,3,3,450,150) #sector 3
                    celdas_sector_4 = dibujar_cuadrados(pantalla,50,3,3,150,300) #sector 4
                    celdas_sector_5 = dibujar_cuadrados(pantalla,50,3,3,300,300) #sector 5
                    celdas_sector_6 = dibujar_cuadrados(pantalla,50,3,3,450,300) #sector 6
                    celdas_sector_7 = dibujar_cuadrados(pantalla,50,3,3,150,450) #sector 7 
                    celdas_sector_8 = dibujar_cuadrados(pantalla,50,3,3,300,450) #sector 8
                    celdas_sector_9 = dibujar_cuadrados(pantalla,50,3,3,450,450) #sector 9 
                    
                    #union de matrices:
                    todas_las_celdas = (celdas_sector_1 + celdas_sector_2 + celdas_sector_3 +
                                        celdas_sector_4 + celdas_sector_5 + celdas_sector_6 +
                                        celdas_sector_7 + celdas_sector_8 + celdas_sector_9)

                    dibujar_lineas(pantalla) #son las 4 lineas que separan los 9 espacios de la cuadricula
                    
                    #Dibujar numeros:
                    matriz_general_dibujos = dibujar_numeros(pantalla,matriz_general_fin,tamaño, fuente,150,150)
                    
                    #Detector de colisiones:
                    if evento.type == pg.MOUSEBUTTONDOWN:
                        posicion = (evento.pos) #posicion
                        celda_seleccionada = detectar_celda(posicion,todas_las_celdas) #detecta celda seleccionada
                        dibujar_borde_verde(pantalla,celda_seleccionada) #dibuja un bordecito verde en la celda clickeada
                        if boton_reiniciar_juego.collidepoint(posicion): #detecta click en  boton "reiniciar juego"
                            
                            print("reiniciar presionado")

                        if boton_validar_celda.collidepoint(posicion):#detecta click en boton "validar celdas"
                            dibujar_todas_las_validaciones(pantalla,flag_sector_1,flag_sector_2,flag_sector_3,
                        flag_sector_4,flag_sector_5,flag_sector_6,flag_sector_7,flag_sector_8,flag_sector_9)
                            print("validar celda presionado")

                    #ingresar numero por teclado
                    if evento.type == pg.KEYDOWN and celda_seleccionada is not None:#verifico que sea evento de telclado y se haya clickeado una celda 
                        numero_ingresado = input_numero(evento,celda_seleccionada)
                        matriz_general_fin = borrar_numero_de_matriz(matriz_general_fin,evento,celda_seleccionada,tamaño,x_inicial=150, y_inicial=150) #funcion borrar numero
                        
                        if numero_ingresado is not None: #si numero es algo
                            
                            matriz_general_fin = ingresar_numero_a_matriz(matriz_general_fin,numero_ingresado,celda_seleccionada,tamaño) #ingresar numero 
                            #banderas de sectores 3x3 | 
                            flag_sector_1 = validar_matriz_sector_1(matriz_general_fin)
                            flag_sector_2 = validar_matriz_sector_2(matriz_general_fin)
                            flag_sector_3 = validar_matriz_sector_3(matriz_general_fin)
                            flag_sector_4 = validar_matriz_sector_4(matriz_general_fin)
                            flag_sector_5 = validar_matriz_sector_5(matriz_general_fin)
                            flag_sector_6 = validar_matriz_sector_6(matriz_general_fin)
                            flag_sector_7 = validar_matriz_sector_7(matriz_general_fin)
                            flag_sector_8 = validar_matriz_sector_8(matriz_general_fin)
                            flag_sector_9 = validar_matriz_sector_9(matriz_general_fin)

                            #banderas de filas
                            flag_filas_0_3 = verificar_por_filas_1(matriz_general_fin)
                            flag_filas_3_6 = verificar_por_filas_2(matriz_general_fin)
                            flag_filas_6_9 = verificar_por_filas_3(matriz_general_fin)
                            #banderas de columnas 
                            flag_columnas_0_3 = verificar_por_columnas_1(matriz_general_fin) 
                            flag_columnas_3_6 = verificar_por_columnas_2(matriz_general_fin)
                            flag_columnas_6_9 = verificar_por_columnas_3(matriz_general_fin)

                            print(matriz_general_fin)
                                    
                        
                        
                        
                if modo_dificultad == "medio":
                            
                            
                            pantalla.fill((189, 162, 162))#color de fondo de pantalla durante el juego
                            pantalla.blit(validar_celda,(650,200)) #blit de validar celda
                            pantalla.blit(texto_validar_celda,(710,215))#blit de texto validar celda
                            pantalla.blit(texto_de_palabra_puntaje,rect_de_texto_de_palabra_puntaje)#blit de texto "puntaje" 
                            pantalla.blit(reset_juego,(650,400)) #blit de boton "reiniciar juego"
                            pantalla.blit(texto_reiniciar_juego,(667, 415)) #texto de "reiniciar juego "
                            pantalla.blit(texto_de_puntaje,rect_de_puntaje) #numeros del puntaje
                            pantalla_actual = pausar_juego(evento,pantalla_actual) #controlador de pantalla, #ESC = volver a inicio - pausar
                            
                            

                            #dibujos de celdas - cuadrados
                            celdas_sector_1_medio = dibujar_cuadrados(pantalla,50,3,3,150,150) #sector 1
                            celdas_sector_2_medio = dibujar_cuadrados(pantalla,50,3,3,300,150) #sector 2
                            celdas_sector_3_medio = dibujar_cuadrados(pantalla,50,3,3,450,150) #sector 3
                            celdas_sector_4_medio = dibujar_cuadrados(pantalla,50,3,3,150,300) #sector 4
                            celdas_sector_5_medio = dibujar_cuadrados(pantalla,50,3,3,300,300) #sector 5
                            celdas_sector_6_medio = dibujar_cuadrados(pantalla,50,3,3,450,300) #sector 6
                            celdas_sector_7_medio = dibujar_cuadrados(pantalla,50,3,3,150,450) #sector 7 
                            celdas_sector_8_medio = dibujar_cuadrados(pantalla,50,3,3,300,450) #sector 8
                            celdas_sector_9_medio = dibujar_cuadrados(pantalla,50,3,3,450,450) #sector 9 
                            
                            #union de matrices:
                            todas_las_celdas_medio = (celdas_sector_1_medio + celdas_sector_2_medio + celdas_sector_3_medio +
                                                celdas_sector_4_medio + celdas_sector_5_medio + celdas_sector_6_medio +
                                                celdas_sector_7_medio + celdas_sector_8_medio + celdas_sector_9_medio)

                            dibujar_lineas(pantalla) #son las 4 lineas que separan los 9 espacios de la cuadricula
                            
                            #Dibujar numeros:
                            matriz_general_dibujos_medio = dibujar_numeros(pantalla,matriz_general_fin_medio,tamaño, fuente,150,150)
                            
                            #Detector de colisiones:
                            if evento.type == pg.MOUSEBUTTONDOWN:
                                posicion = (evento.pos) #posicion
                                celda_seleccionada_medio = detectar_celda(posicion,todas_las_celdas_medio) #detecta celda seleccionada
                                dibujar_borde_verde(pantalla,celda_seleccionada_medio) #dibuja un bordecito verde en la celda clickeada
                                if boton_reiniciar_juego.collidepoint(posicion): #detecta click en  boton "reiniciar juego"
                                   
                                    print("reiniciar presionado")
                                    
                                if boton_validar_celda.collidepoint(posicion):#detecta click en boton "validar celdas"
                                    dibujar_todas_las_validaciones(pantalla,flag_sector_1,flag_sector_2,flag_sector_3,
                                flag_sector_4,flag_sector_5,flag_sector_6,flag_sector_7,flag_sector_8,flag_sector_9,flag_filas_0_3,flag_filas_3_6)
                                    print("validar celda presionado")

                                    
                            
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

                                    #banderas de filas
                                    flag_filas_0_3 = verificar_por_filas_1(matriz_general_fin_medio)
                                    flag_filas_3_6 = verificar_por_filas_2(matriz_general_fin_medio)
                                    flag_filas_6_9 = verificar_por_filas_3(matriz_general_fin_medio)
                                    #banderas de columnas 
                                    flag_columnas_0_3 = verificar_por_columnas_1(matriz_general_fin_medio) 
                                    flag_columnas_3_6 = verificar_por_columnas_2(matriz_general_fin_medio)
                                    flag_columnas_6_9 = verificar_por_columnas_3(matriz_general_fin_medio)
                                    
                                    puntaje_mutable = descontar_puntaje(flag_sector_1,flag_sector_2,flag_sector_3,flag_sector_4,flag_sector_5,flag_sector_6,flag_sector_7,flag_sector_8,flag_sector_9)
                                    

                                    print(matriz_general_fin_medio)
                                
                                    
                        

                 #reinicio no hecho 
                 # -validacion esta a medias 
                 # - puntaje no hecho
                 #  - nickname no hecho     
                
                pg.display.update()
                
            case "ver puntaje":
                pass
                         
    

    pg.display.flip()