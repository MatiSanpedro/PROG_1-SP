import pygame as pg 
import pygame.mixer as mixer 
from PARCIAL_2_funciones import *
import copy
import random



pg.init() #esto es para iniciar todos los modulos, fuente, musica, etc
reloj = pg.time.Clock()

#pantalla
ANCHO_PANTALLA = 900
ALTO_PANTALLA = 700
pantalla = pg.display.set_mode((ANCHO_PANTALLA,ALTO_PANTALLA))
azul = (0,0,150)
pantalla.fill((255, 235, 222))

#tamaño de cuadrado:
tamaño = 50

#imagen de fondo de inicio
fondo_pantalla = pg.image.load("sudoku2.jpg")
correccion_fondo_pantalla = pg.transform.scale(fondo_pantalla,(900,700))


pantalla_actual = "nombre" #esto controla los cambios de pantalla del menu 

#bandera de control de bucles de juego, se usa para reiniciar
jugando = False

#texto
fuente = pg.font.SysFont("Bernard MT Comprimida",50)
texto_prueba = fuente.render("cosas aca", True, (255,255,255))

#ingresar nombre de jugador: 
cuadrado_de_fondo = pg.Surface((400,100))
cuadrado_de_fondo.fill((110, 50, 38))
ingrese_nombre = fuente.render("ingrese su nombre",True, (250,250,250),(0,0,0))



'botones de MENU INICIO'
#Nivel | boton 1
nivel = pg.Surface((290,50))
nivel.fill((117, 83, 76))
fuente = pg.font.SysFont("Bernard MT Comprimida",50)
texto1 = fuente.render("Nivel",True, (250,250,250),(0,0,0)) #la segunda tupla es el color detras de las letras
boton1 = nivel.get_rect(topleft = (300, 100))


#jugar | boton 2 
jugar = pg.Surface((290,50))
jugar.fill((117, 83, 76))
texto_2 = fuente.render("Jugar",True,(250,250,250),(0,0,0))
boton2 = jugar.get_rect(topleft = (300,245))

#puntaje | boton 3 
boton_puntaje = pg.Surface((290,50))
boton_puntaje.fill((117, 83, 76))
texto_3 = fuente.render("Ver Puntaje",True,(250,250,250),(0,0,0))
boton3 = boton_puntaje.get_rect(topleft = (300,390))

modo_dificultad = " " #con esto controlo la seleccion de nivel, se guarda y recien ahi se ejecuta "jugar"


#salir | boton 4 
boton_salida = pg.Surface((290,50))
boton_salida.fill((117, 83, 76))
texto_4 = fuente.render("Salir",True,(250,250,250),(0,0,0))
boton4 = boton_salida.get_rect(topleft = (300,540))


'botones de "SELECCIONAR NIVEL"'
#facil | boton 1
nivel_nivel = pg.Surface((290,50))
nivel_nivel.fill((200,100,100))
fuente = pg.font.SysFont("Bernard MT Comprimida",50)
texto_facil = fuente.render("facil",True, (250,250,250))
boton1_nivel = nivel_nivel.get_rect(topleft = (290,50))

#medio | boton 2 
medio = pg.Surface((290,50))
medio.fill((50,0,0))
texto_medio = fuente.render("Medio",True,(250,250,250))
boton2_nivel = medio.get_rect(topleft = (250,150))

#Dificil | boton 3 
dificil = pg.Surface((290,50))
dificil.fill((0,0,0))
texto_dificil = fuente.render("Dificil",True,(250,250,250))
boton3_nivel = dificil.get_rect(topleft = (250,250))


#volver| boton 4 
volver = pg.Surface((290,50))
volver.fill((150,0,0))
texto_4_nivel = fuente.render("Volver",True,(250,250,250))
boton4_nivel = volver.get_rect(topleft = (250,350)) 

correccion_tamaño_nivel = pg.transform.scale(fondo_pantalla,(900,700))

#botons de comprobar celdas
fuente_validar_celda = pg.font.SysFont("Bernard MT Comprimida",30)
validar_celda = pg.Surface((200,50))
validar_celda.fill((110, 50, 38))
texto_validar_celda = fuente_validar_celda.render("validar", True, ((219, 97, 77)))
boton_validar_celda = validar_celda.get_rect(topleft = (600,200))


#boton de reiniciar juego:
reset_juego = pg.Surface((200,50))
reset_juego.fill((110, 50, 38))
texto_reiniciar_juego = fuente_validar_celda.render("Reiniciar Juego",True, (219, 97, 77))
boton_reiniciar_juego = reset_juego.get_rect(topleft = (650,400))


reiniciar_juego = False

#texto de palabra puntaje:
texto_de_palabra_puntaje = fuente.render("Puntaje:",True,(0,0,0))
rect_de_texto_de_palabra_puntaje = texto_de_palabra_puntaje.get_rect(topleft = (650,20))


#texto de numeros puntaje:
puntaje =  0000
puntaje_str = formatear_puntaje(puntaje)



#bandera de control de punto 4 "ver puntaje"
ver_ranking = False #esta se usa para que "leer json no se ejecute 700 veces "



#banderas de la funcion "validar matriz sector"

flag_sector_1 = False       
flag_sector_2 = False
flag_sector_3 = False
flag_sector_4 = False
flag_sector_4 = False
flag_sector_5 = False
flag_sector_6 = False
flag_sector_7 = False
flag_sector_8 = False
flag_sector_9 = False
#############

flag_filas_0_3 = False
flag_filas_3_6 = False
flag_filas_6_9 = False
#############

flag_columnas_0_3 = False 
flag_columnas_3_6 = False
flag_columnas_6_9 = False



#variables de input, solo se usan en una funcion 
cuadrado_seleccionado = False
#esto se usa para controlar la interaccion entre funcion "input numero" y "dibujar numero ingresado" en el case "jugar"



puntaje = 0
#MATRICES - cambio los nombres para que los datos no se mezclen:
'MATRICES - Dificil'

matriz_vacia = iniciar_matriz(9,9,0) #inicia matriz, | int1 = cantidad de filas| int2 = cantidad de columnas| int3 = numeros que contiene  
matriz_dificil = generar_matriz_completa_C(matriz_vacia) #llena la matriz vacia 
nuevita = agregar_ceros_final(matriz_dificil,6) #limpia ceros y repeticiones 
celda_seleccionada = None


'MATRICES - nivel medio'
matriz_vacia_medio = iniciar_matriz(9,9,0)
matriz_medio = generar_matriz_completa_C(matriz_vacia_medio) #llena la matriz vacia 
matriz_general_fin_medio = agregar_ceros_final(matriz_medio,5) #limpia ceros y repeticiones 

#esto se usa para controlar la interaccion entre funcion "input numero" y "dibujar numero ingresado" en el case "jugar"
celda_seleccionada_medio = None

'MATRICES - nivel facil'

matriz_vacia_facil = iniciar_matriz(9,9,0)
matriz_facil = generar_matriz_completa_C(matriz_vacia_facil) #llena la matriz vacia 
matriz_general_fin_facil = agregar_ceros_final(matriz_facil,4) #limpia ceros y repeticiones 
#esto se usa para controlar la interaccion entre funcion "input numero" y "dibujar numero ingresado" en el case "jugar"
celda_seleccionada_facil = None

reiniciar_juego = False


'''
nuevita_C = agregar_ceros_final(copy.deepcopy(matriz_dificil), 6)
matriz_general_fin_facil_C = (copy.deepcopy(matriz_general_fin_facil))
matriz_general_fin_medio_C = (copy.deepcopy(matriz_general_fin_medio))'''