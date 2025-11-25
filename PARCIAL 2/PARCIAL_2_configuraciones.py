import pygame as pg 
import pygame.mixer as mixer 
from PARCIAL_2_funciones import agregar_numeros_al_azar_v3
from PARCIAL_2_funciones import unir_matriz_general
from PARCIAL_2_funciones import limpiar_repetidos_horizontales
from PARCIAL_2_funciones import limpiar_repetidos_verticales
from PARCIAL_2_funciones import formatear_puntaje
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


pantalla_actual = "inicio" #esto controla los cambios de pantalla del menu 

#bandera de control de bucles de juego, se usa para reiniciar
jugando = False

#texto
fuente = pg.font.SysFont("Bernard MT Comprimida",50)
texto_prueba = fuente.render("cosas aca", True, (255,255,255))


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


#texto de palabra puntaje:
texto_de_palabra_puntaje = fuente.render("Puntaje:",True,(0,0,0))
rect_de_texto_de_palabra_puntaje = texto_de_palabra_puntaje.get_rect(topleft = (650,20))

#texto de numeros puntaje:
puntaje =  0000
puntaje_str = formatear_puntaje(puntaje)
texto_de_puntaje = fuente.render(puntaje_str,True,(0,0,0))
rect_de_puntaje = texto_de_puntaje.get_rect(topleft = (800,20))


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
celda_seleccionada = None



#MATRICES - son lo mismo, pero cambio los nombres para que los datos no se mezclen:
#vacias:

'MATRICES - Dificil'
matriz_sector_1 = [[0,0,0],[0,0,0],[0,0,0]]
matriz_sector_2 = [[0,0,0],[0,0,0],[0,0,0]]
matriz_sector_3 = [[0,0,0],[0,0,0],[0,0,0]]
matriz_sector_4 = [[0,0,0],[0,0,0],[0,0,0]]
matriz_sector_5 = [[0,0,0],[0,0,0],[0,0,0]]
matriz_sector_6 = [[0,0,0],[0,0,0],[0,0,0]]
matriz_sector_7 = [[0,0,0],[0,0,0],[0,0,0]]
matriz_sector_8 = [[0,0,0],[0,0,0],[0,0,0]]
matriz_sector_9 = [[0,0,0],[0,0,0],[0,0,0]]


#con numeros agregados:                        matriz | cantidad de numeros para agregar
numeros_sector1 = agregar_numeros_al_azar_v3(matriz_sector_1,3)
numeros_sector2 = agregar_numeros_al_azar_v3(matriz_sector_2,3)
numeros_sector3 = agregar_numeros_al_azar_v3(matriz_sector_3,3)
numeros_sector4 = agregar_numeros_al_azar_v3(matriz_sector_4,3)
numeros_sector5 = agregar_numeros_al_azar_v3(matriz_sector_5,3)
numeros_sector6 = agregar_numeros_al_azar_v3(matriz_sector_6,3)
numeros_sector7 = agregar_numeros_al_azar_v3(matriz_sector_7,3)
numeros_sector8 = agregar_numeros_al_azar_v3(matriz_sector_8,3)
numeros_sector9 = agregar_numeros_al_azar_v3(matriz_sector_9,3)

celda_seleccionada = None


matrices = [numeros_sector1,numeros_sector2,numeros_sector3,numeros_sector4,numeros_sector5,
            numeros_sector6,numeros_sector7,numeros_sector8,numeros_sector9]

matriz_general_a = unir_matriz_general(matrices)
matriz_general_b = limpiar_repetidos_verticales(matriz_general_a)
matriz_general_fin = limpiar_repetidos_horizontales(matriz_general_b)

   



'MATRICES - nivel medio'
#vacias:
matriz_sector_1_medio = [[0,0,0],[0,0,0],[0,0,0]]
matriz_sector_2_medio  = [[0,0,0],[0,0,0],[0,0,0]]
matriz_sector_3_medio  = [[0,0,0],[0,0,0],[0,0,0]]
matriz_sector_4_medio  = [[0,0,0],[0,0,0],[0,0,0]]
matriz_sector_5_medio  = [[0,0,0],[0,0,0],[0,0,0]]
matriz_sector_6_medio  = [[0,0,0],[0,0,0],[0,0,0]]
matriz_sector_7_medio  = [[0,0,0],[0,0,0],[0,0,0]]
matriz_sector_8_medio  = [[0,0,0],[0,0,0],[0,0,0]]
matriz_sector_9_medio  = [[0,0,0],[0,0,0],[0,0,0]]


#con numeros agregados:                        matriz | cantidad de numeros para agregar
numeros_sector1_medio  = agregar_numeros_al_azar_v3(matriz_sector_1_medio ,4)
numeros_sector2_medio  = agregar_numeros_al_azar_v3(matriz_sector_2_medio ,4)
numeros_sector3_medio  = agregar_numeros_al_azar_v3(matriz_sector_3_medio ,4)
numeros_sector4_medio  = agregar_numeros_al_azar_v3(matriz_sector_4_medio ,4)
numeros_sector5_medio  = agregar_numeros_al_azar_v3(matriz_sector_5_medio ,4)
numeros_sector6_medio  = agregar_numeros_al_azar_v3(matriz_sector_6_medio ,4)
numeros_sector7_medio  = agregar_numeros_al_azar_v3(matriz_sector_7_medio ,4)
numeros_sector8_medio  = agregar_numeros_al_azar_v3(matriz_sector_8_medio ,4)
numeros_sector9_medio  = agregar_numeros_al_azar_v3(matriz_sector_9_medio ,4)


matrices_medio  = [numeros_sector1_medio ,numeros_sector2_medio ,numeros_sector3_medio  ,numeros_sector4_medio ,numeros_sector5_medio ,
            numeros_sector6_medio ,numeros_sector7_medio ,numeros_sector8_medio ,numeros_sector9_medio ]

#esto se usa para controlar la interaccion entre funcion "input numero" y "dibujar numero ingresado" en el case "jugar"
celda_seleccionada_medio = None

matriz_general_a_medio  = unir_matriz_general(matrices_medio )
matriz_general_b_medio  = limpiar_repetidos_verticales(matriz_general_a_medio )
matriz_general_fin_medio  = limpiar_repetidos_horizontales(matriz_general_b_medio )




'MATRICES - nivel facil'
#vacias:
matriz_sector_1_facil = [[0,0,0],[0,0,0],[0,0,0]]
matriz_sector_2_facil  = [[0,0,0],[0,0,0],[0,0,0]]
matriz_sector_3_facil  = [[0,0,0],[0,0,0],[0,0,0]]
matriz_sector_4_facil  = [[0,0,0],[0,0,0],[0,0,0]]
matriz_sector_5_facil  = [[0,0,0],[0,0,0],[0,0,0]]
matriz_sector_6_facil  = [[0,0,0],[0,0,0],[0,0,0]]
matriz_sector_7_facil  = [[0,0,0],[0,0,0],[0,0,0]]
matriz_sector_8_facil  = [[0,0,0],[0,0,0],[0,0,0]]
matriz_sector_9_facil  = [[0,0,0],[0,0,0],[0,0,0]]


#con numeros agregados:                        matriz | cantidad de numeros para agregar
numeros_sector1_facil  = agregar_numeros_al_azar_v3(matriz_sector_1_facil ,5)
numeros_sector2_facil  = agregar_numeros_al_azar_v3(matriz_sector_2_facil ,5)
numeros_sector3_facil  = agregar_numeros_al_azar_v3(matriz_sector_3_facil ,5)
numeros_sector4_facil  = agregar_numeros_al_azar_v3(matriz_sector_4_facil ,5)
numeros_sector5_facil  = agregar_numeros_al_azar_v3(matriz_sector_5_facil ,5)
numeros_sector6_facil  = agregar_numeros_al_azar_v3(matriz_sector_6_facil ,5)
numeros_sector7_facil  = agregar_numeros_al_azar_v3(matriz_sector_7_facil ,5)
numeros_sector8_facil  = agregar_numeros_al_azar_v3(matriz_sector_8_facil ,5)
numeros_sector9_facil  = agregar_numeros_al_azar_v3(matriz_sector_9_facil ,5)


matrices_facil  = [numeros_sector1_facil ,numeros_sector2_facil ,numeros_sector3_facil  ,numeros_sector4_facil ,numeros_sector5_facil ,
            numeros_sector6_facil ,numeros_sector7_facil ,numeros_sector8_facil ,numeros_sector9_facil ]

#esto se usa para controlar la interaccion entre funcion "input numero" y "dibujar numero ingresado" en el case "jugar"
celda_seleccionada = None

matriz_general_a_facil  = unir_matriz_general(matrices_facil )
matriz_general_b_facil  = limpiar_repetidos_verticales(matriz_general_a_facil )
matriz_general_fin_facil  = limpiar_repetidos_horizontales(matriz_general_b_facil )