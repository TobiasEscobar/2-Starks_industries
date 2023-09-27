from data_stark import lista_personajes

#A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB
def mostrar_nombres_nb(lista:list):
    '''
    Brief:
    - Muestra por terminal todos los nombres del genero "NB" que se encuentren en una lista
    Param:
    - lista: La lista de donde debe iterar en busca de los nombres
    Return: 
    - No tiene return
    '''
    for heroe in lista:
        if heroe["genero"] == "NB":
            nombre_heroe = heroe["nombre"]
            print(f"{nombre_heroe}\n")

#B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
#C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
def heroe_mas_alto(lista:list, genero:str)->list:
    '''
    Brief:
    - Muestra por terminal el heroe mas alto (dependiendo de su genero) que este en la lista
    Param:
    - lista: La lista de donde debe iterar para encontrar al mas alto dependiendo de su genero
    - genero: Dependiendo de cual se elija (M, F o NB) tomara a diferentes heroes   
    Return: 
    - Devuelve una lista con el nombre del heroe mas alto del genero elegido
    '''
    primera_flag = True
    for heroe in lista:
        altura_float = float(heroe["altura"])
        if heroe["genero"] == genero:
            if primera_flag == True or altura_float > mayor_altura:
                mayor_altura = altura_float
                nombre_heroe = heroe["nombre"]
                primera_flag = False
    heroe_alto = nombre_heroe
    return heroe_alto

#D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
#E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
def heroe_mas_debil(lista:list, genero:str)->list:
    '''
    Brief:
    - Muestra por terminal el heroe mas debil (dependiendo de su genero) que este en la lista
    Param:
    - lista: La lista de donde debe iterar para encontrar al mas debil dependiendo de su genero
    - genero: Dependiendo de cual se elija (M, F o NB) tomara a diferentes heroes   
    Return: 
    - Devuelve una lista con el nombre del heroe mas debil del genero elegido
    '''
    primera_flag = True
    for heroe in lista:
        fuerza_float = float(heroe["fuerza"])
        if heroe["genero"] == genero:
            if primera_flag == True or fuerza_float < menor_fuerza:
                menor_fuerza = fuerza_float
                nombre_heroe = heroe["nombre"]
                primera_flag = False
    heroe_debil = nombre_heroe
    return heroe_debil

def calcular_promedio(numero_1, numero_2)->float:
    '''
    Brief:
    - Divide dos numeros que se les pase por parametro y lo devuelve
    Param:
    - numero_1: el dividendo
    - numero_2: el divisor
    Return: 
    - Devuelve el resultado de la division
    '''
    if numero_2 == 0:
        print("No se puede dividir por 0")
    else:
        promedio = numero_1 / numero_2
        return promedio

#F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB
def promedio_fuerza_nb(lista:list, genero:str)->str:
    '''
    Brief:
    - Muestra por terminal el promedio de fuerzaz de los heroes del genero NB
    Param:
    - lista: La lista de donde debe iterar para encontrar la fuerza de los heroes del genero NB
    Return: 
    - Devuelve una lista con el promedio de fuerza de heroes del genero NB
    '''
    acumulador_fuerza = 0
    contar_heroes = 0
    for heroe in lista:
        if heroe["genero"] == genero:
            fuerza_float = float(heroe["fuerza"])
            contar_heroes += 0
            acumulador_fuerza += fuerza_float
    promedio = calcular_promedio(acumulador_fuerza, contar_heroes)
    if promedio:
        mensaje = print(f"El promedio de fuerza entre los generos NB es de: {promedio}")
        return mensaje
    else:
        mensaje = print("No se pudo conseguir el promedio porque no existe los heroes o sus datos son de 0")
        return mensaje

#G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
#H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
def tipo_de_color(lista:list, tipo:str)->dict:
    '''
    Brief:
    - Determina cuantos heroes hay con cada tipo de color de ojos o pelo.
    Param:
    - lista: La lista de donde debe iterar para encontrar los tipos de color de ojos o de pelo de los heroes
    - tipo: key de diccionario para determinar si la funcion contara los tipos de color de ojos o de pelo
    Return:
    - Devuelve un diccionario con la suma de cada tipo de color de ojos o de pelo
    '''
    conteo_color = {}
    for heroe in lista:
        caracteristica = heroe[tipo].lower()
        if caracteristica and caracteristica != "no hair":
            if caracteristica in conteo_color:
                conteo_color[caracteristica] += 1
            else:
                conteo_color[caracteristica] = 1
    return conteo_color


#I. Listar todos los superhéroes agrupados por color de ojos.
#J. Listar todos los superhéroes agrupados por tipo de inteligencia
def agrupar_por_caracteristica(lista:list, tipo:str)->dict:
    '''
    Brief:
    - Agrupa a todos los heroes dependiendo de su color de ojos o de su tipo de inteligencia
    Param:
    - lista: La lista de donde debe iterar para encontrar los colores de ojos o el tipo de inteligencia
    - tipo: key de diccionario para determinar si la funcion agrupara por colores de ojos o por tipos de inteligencia
    Return:
    - Devuelve un diccionario con los heroes agrupados en su respectivo color o tipo de inteligencia 
    '''
    heroes_por_caracteristicas = {}
    for heroe in lista:
        caracteristica = heroe[tipo].lower()
        if caracteristica:
            if caracteristica in heroes_por_caracteristicas:
                heroes_por_caracteristicas[caracteristica].append(heroe["nombre"])
            else:
                heroes_por_caracteristicas[caracteristica] = [heroe["nombre"]]
    return heroes_por_caracteristicas