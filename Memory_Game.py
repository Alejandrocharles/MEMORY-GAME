# ALEJANDRO CHARLES GONZALEZ
# A00835903
# INGENIERIA EN TECNOLOGIAS COMPUTACIONALES
# PROYECTO - MEMORAMA - TEMATICA
# Grupo 404

# se importan paquetes
import random, os
from colorama import init, Fore, Back, Style

#Se definen los colores
colores = [Fore.BLACK, Fore.BLUE , Fore.CYAN , Fore.GREEN, Fore.LIGHTBLACK_EX, Fore.WHITE,
           Fore.LIGHTBLACK_EX , Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore. LIGHTGREEN_EX,
           Fore.LIGHTMAGENTA_EX , Fore.LIGHTRED_EX , Fore.LIGHTWHITE_EX, Fore.LIGHTYELLOW_EX,
           Fore.MAGENTA, Fore.RED, Fore.RESET, Fore.WHITE , Fore.YELLOW ]

fondo = [  Back.BLACK, Back.BLUE, Back.CYAN, Back.GREEN,Back.LIGHTBLACK_EX, Back.LIGHTBLUE_EX, Back.LIGHTCYAN_EX,
           Back.LIGHTGREEN_EX, Back.LIGHTMAGENTA_EX, Back.LIGHTRED_EX, Back.LIGHTWHITE_EX, Back.LIGHTYELLOW_EX,
           Back.MAGENTA, Back.RED, Back.RESET, Back.WHITE , Back.YELLOW ]


#Se define la funcion pares
def pares():
    pars =    """26 + 34
60
12 x 7 
84
45 - 27 
18 
8 x 7
56
12 x 6 
72
66 ÷ 6 
11
28 + 47 
75
37 x 2 
74
13 + 58 
71
13 x 13 
169
12 x 12 
144
14 x 5
70
32 + 69 
101
6 x 7 
42
15 x 15 
225
2 x 79 
158
28 ÷ 4
7
27 + 28 
55"""

# creamos lista de pares
    lista = pars.split("\n")
    print(colores[-2]+ "Longitud = ", len(lista))
    for elemento in lista:
        print(elemento)
    
    return lista


def limpia():
    ''' Función que limpia a pantalla sin importar el sistema operativo
      de la máquina donde esté corriendo '''
    
    if os.name == 'nt': #Windows
        os.system('cls')
        
    else:  #'posix'
        os.system('clear') #Mac/linux


def llena_tablero():
    '''Llena el tablero con los pares volteados '''
    matriz = []
    
    for r in range(6):
        renglon = []
        
        for c in range(6):
            # Agrega un emoji de signo de interrogacion en con el código unicode
            renglon.append('\U00002753')
        matriz.append(renglon)
        
    return matriz


def despliega_matriz(tablero, r1 = None, c1 = None, r2 = None, c2 = None):
    ''' Despliega a pantalla la matriz que se recibe en forma de tabla
     desplegando una cuadricula '''
    
    renglones = len(tablero)
    columnas = len(tablero[0])
    
    # Despliega el marco de arriba del tablero con el numero de renglones 
    print(colores[-2],"==============="*renglones)
    print(colores[-2],f'1'.center(20),f'2'.center(6),f'3'.center(20),f'4'.center(5),f'5'.center(22),f'6'.center(3), end="")
    print(colores[-2], '\n'+"==============="*renglones)
    
    # Despliega el tablero, y se eligen los colores de letra 
    print(colores[-2],"===============" * renglones)
    
    for r in range(renglones):
        print(colores[-2], r + 1,"|", end="")
        for c in range(columnas):
            
            # Centra el elemento en un espacio de 9 - se elige el color de fondo y de letra.
            print(fondo[-4],colores[0]+ f'{tablero[r][c]}'.center(9), Back.RESET, end="")
            print(colores[-2],"|" + Back.RESET, end="")
            
        print('\n' + "==============="* renglones)
        
        
def llena_escondida(lista):
    ''' Llena una matriz de operaciones aritmeticas, para que el niño aprenda
        sobre matematicas '''
    matriz=[]
    
    #mezcla los elementos de la lista, para el memorama
    (lista)
    
    for r in range(6):
        renglon=[]
        for c in range(6):
             # Agrega cada elemento de la lista
            renglon.append(lista.pop(0))
        matriz.append(renglon)
       
    return matriz


def validar_carta(tablero,r1,c1,r2 = None,c2 = None):
 
      
    # verifica que carta voy a validar
    if r2 is None and c2 is None:
        
        # validar la carta 1
        while r1 < 1 or r1 > 6 or c1 < 1 or c1 > 6 or tablero [r1-1][c1-1] != "\U00002753":
            r1 = int(input("\nError,Ingresa de nuevo la posicion de la carta 1\nRenglon: "))
            c1 = int(input("Columna: "))
                    
        # retornar el valor como debe ser ( si ingreso 1, , regreso 0 ,0 )    
        return r1 - 1 ,c1 - 1
    
    else: # Validar la carta 2
        while r2 < 1 or r2 > 6 or c2 < 1 or c2 > 6 or tablero [r2-1][c2-1] != "\U00002753":
            r2 = int(input("\nError,Ingresa de nuevo la posicion de la carta 2\nRenglon: "))
            c2 = int(input("Columna: "))
            
        return r2 - 1,c2 - 1
 
        # retorna el valor como debe de ser

       
def validar_carta_computadora(tablero,r1,c1,r2 = None,c2 = None):    
    
    # verifica que carta voy a validar
    if r2 is None and c2 is None:
        # validar carta 1 - volver a generar un valor random
        while tablero [r1 - 1][c1 - 1] != "\U00002753":
            r1 = random.randint(1,6)
            c1 = random.randint(1,6)
        # retornar el valor definitivo de la carta 1 de la computadora( si ingreso 1, , regreso 0 ,0 )    
        return r1 - 1, c1 - 1
    
    else: # Validar la carta 2
        while tablero [r2 - 1][c2 - 1] != "\U00002753":
            r2 = random.randint(1,6)
            c2 = random.randint(1,6)
        return r2 - 1, c2 - 1
       
      
def son_pares(tablero, escondida, lista_pares, lista_impares,r1,c1,r2,c2):     

    # Poner visible la carta 1 y carta 2
    tablero[r1][c1] = escondida[r1][c1]
    tablero[r2][c2] = escondida[r2][c2]
    
    #desplegar el tablero
    limpia()
    tablero[r1][c1] = escondida[r1][c1]
    tablero[r2][c2] = escondida[r2][c2]
    
    # valor inicial a gano - se limpia el tablero y se despliega la matriz
    gano = 0
    limpia()
    despliega_matriz(escondida)
    despliega_matriz(tablero)
    
    # Verificamos si son pares o impares y desplegamos el mensaje 
    if escondida[r1][c1] in lista_pares:
        posicion = lista_pares.index(escondida[r1][c1])
        
        # Verifica si son pares
        if escondida[r2][c2] == lista_impares[posicion]:
            print(" ¡¡¡ FELICIDADES ES PAR !!! ")
            gano = 1
            
        else:
            print(" NO ES PAR :( ")
            # esconder de nuevo las cartas que no fueron par
            tablero[r1][c1] = "\U00002753"
            tablero[r2][c2] = "\U00002753"
            
    elif escondida[r1][c1] in lista_impares:
        posicion = lista_impares.index(escondida[r1][c1])
        
        #verificar si lo que esta en la lista de pares es igual a la carta 2
        if escondida[r2][c2] == lista_pares[posicion]: #es par
            print("¡¡¡ FELICIDADES ES PAR !!!")
            gano = 1
            
        else:
            print(" NO ES PAR :( ")
            # esconder de nuevo las cartas
            tablero[r1][c1] = "\U00002753"
            tablero[r2][c2] = "\U00002753"
    return gano
     
   
def main():
    # Llamamos a las funciones que llenan las matrices
    # Llamar a la funcion pares() - retorna una lista de 36 elementos 
    lista = pares()
    
    #separar los pares
    lista_pares = lista[0::2]
    lista_impares = lista[1::2]
    
    tablero = llena_tablero()
    escondida = llena_escondida(lista)
    
    #iniciamos el número de caidas y de oportunidades
    pares1 = 0
    pares2 = 0
    
    #se ejecuta mientras ninguno de los jugadores no gane
    while pares1 + pares2 < 2:
        
        limpia()
        despliega_matriz(escondida)
        despliega_matriz(tablero)
        
        
        # Empieza el turno del jugador 
        print("\n==========EMPIEZA EL TURNO DEL JUGADOR==========")
        
        print('** Escribe las posiciónes que quieres destapar **')
        
        # Crear una función para validar - elegir diferentes posiciones
        # que no esten destapadas - que este dentro del rango"""
        
        # Seleccionamos la primera carta a voltear
        
        #Validamos que el jugador elija un numero, para evitar errores
        while True:
            try:               
                r1 = int(input('\nIngresa la posicion de la Carta 1\nRenglón: '))
                c1 = int(input('Columna: '))
                # se llama la funcion validar_carta
                
                break

            except ValueError:
                print("\nDebes escribir un numero.")
                         
        #Seleccionamos la 2a carta - validando su valor 
        while True:
            try:       
                r2 = int(input('\nIngresa la posicion de la Carta 2\nRenglón: '))
                c2 = int(input('Columna: '))
                if (r1 == r2) and (c1 == c2):
                    while (r1 == r2) and (c1 == c2):
                        print("\nEscogiste el mismo par, elige de nuevo")
                        r1 = int(input('\nIngresa la posicion de la Carta 1\nRenglón: '))
                        c1 = int(input('Columna: '))  
                        r2 = int(input('\nIngresa la posicion de la Carta 2\nRenglón: '))
                        c2 = int(input('Columna: '))
                        
                #Se llama la funcion validar_carta
                r1, c1 = validar_carta(tablero,r1,c1)
                r2, c2 = validar_carta(tablero,r1,c1,r2,c2)
                break

            except ValueError:
                print("\nDebes escribir un numero.")
                
     
        # Actualizar el contador del jugador 1
        pares1 += son_pares(tablero, escondida, lista_pares, lista_impares,r1,c1,r2,c2)
        
        # Se despliegan los pares de cada jugador 
        print("\nPares del jugador =", pares1)
        print("Pares de la Computadora = ", pares2)
        
        # Empieza a jugar la computadora
        if pares1 + pares2 < 2:
            print("\n==========EMPIEZA A JUGAR LA COMPUTADORA==========")
            
            # Generar la carta 1 de la computadora
            r1 = random.randint(1,6)
            c1 = random.randint(1,6)
            
            
            # Generar la carta 2 de la computadora
            r2 = random.randint(1,6)
            c2 = random.randint(1,6)
            
            # Validar que no escoja el mismo par la computadora
            if (r1 == r2) and (c1 == c2):
                while (r1 == r2) or (c1 == c2):
                    r1 = random.randint(1,6)
                    c1 = random.randint(1,6)
                    
                    r2 = random.randint(1,6)
                    c2 = random.randint(1,6)
                    
                r1,c1 = validar_carta_computadora(tablero,r1,c1)
                r2,c2 = validar_carta_computadora(tablero,r2,c2)
            else:
                r1,c1 = validar_carta_computadora(tablero,r1,c1)
                r2,c2 = validar_carta_computadora(tablero,r2,c2)
                
                
            # DESPLEGAR EL TIRO ELEGIDO POR LA COMPUTADORA
            print("La computadora eligio la carta 1: [", r1 +1 , "]","[",c1 +1,"]")
            print("La computadora eligio la carta 2: [", r2 +1 , "]","[",c2 +1,"]")
            # Crear una pausa
            input('\nEnter para continuar')
        
        # Actualizar el contador del jugador 2
        pares2 += son_pares(tablero, escondida, lista_pares, lista_impares,r1,c1,r2,c2)
        # Se despliegan los pares de cada jugador 
        print("Pares del jugador =", pares1)
        print("Pares de la Computadora = ", pares2)
        
        # Crear una pausa
        input('\nEnter para continuar')
    # Limpiamos tablero y se despliega la matriz
    
    limpia()
    despliega_matriz(tablero)
    
    # Definimos quien gano el juego (EMPATE, GANASTE, PERDISTE)
    
    # CASO DE EMPATE - SE AGREGAN COLORES DE LETRA Y FONDO
    if pares1 == pares2:
        salida = fondo[-6] + colores[6] + " ********** EMPATE ********** " + Fore.RESET + Back.RESET
        print(salida.center(80))
        
    # GANASTE - SE AGREGAN COLORES DE LETRA Y FONDO
    elif pares1 > pares2:
        salida = fondo[-6] + colores[6] + " ********** ¡¡GANASTE, FELICIDADES!! ********** " + Back.RESET + Fore.RESET
        print(salida.center(80))
        
    # PERDISTE - SE AGREGAN COLORES DE LETRA Y FONDO
    else:
        salida = fondo[-6] + colores[6] + " ********** PERDISTE :( ********** " + Back.RESET + Fore.RESET 
        print(salida.center(80))

main()
