"""def respuestas_preguntas(max):
    auth = False
    preguntas = banco_preguntas
    respustas = {}
    while not auth:
        for i in range(max):


def banco_preguntas():
    banco = {1: 'Le gusta la pizza con piña?', 
            2: 'Le gustan los corridos tumbados?',
            3: 'Se encuentra soltero/a?'}
    
    return banco"""
"""
def respuestas_preguntas(max):
    preguntas = banco_preguntas()
    respuestas = {}
    
    for i in range(1, max + 1):
        respuestas_persona = {}
        print(f'Persona {i}')
        for pregunta_id, pregunta_texto in preguntas.items():
            clave_pregunta = f"p{pregunta_id}"
            auth = False
            while not auth:
                respuesta = input(f"Pregunta {pregunta_id}: {pregunta_texto} ")
                if respuesta.lower() in ['si', 'no']:
                    respuestas_persona[clave_pregunta] = respuesta
                    auth = True
                else:
                    print("Respuesta inválida. Por favor, ingrese 'si' o 'no'.")
        respuestas[i] = respuestas_persona
    return respuestas

def banco_preguntas():
    banco = {
        1: '¿Le gusta la pizza con piña?',
        2: '¿Le gustan los corridos tumbados?',
        3: '¿Se encuentra soltero/a?'
    }
    
    return banco

max_personas = 2
respuestas = respuestas_preguntas(max_personas)

print(respuestas)
"""


def aleatorizar_respuestas(max):
    import random
    respuetas = []
    for i in range(max):
        persona = []
        for key, value in banco_preguntas().items():
            opciones = value['opciones']
            respueta_aleatoria = random.choices(opciones)[0]
            persona.append(respueta_aleatoria)
        respuetas.append(persona)
    return respuetas


def banco_preguntas():
    banco = {
        1: {'pregunta': '¿Le gusta la pizza con piña?', 'opciones': ['sí', 'no']},
        2: {'pregunta': '¿Le gustan los corridos tumbados?', 'opciones': ['sí', 'no']}
    }
    return banco

def analizar_respuestas(respuestas):
    total_personas = len(respuestas)

    gusta_pizza = 0
    gusta_caminar = 0
    gusta_pizza_y_caminar = 0
    no_gusta_pizza_no_camina = 0

    for persona_respuestas in respuestas:
        if persona_respuestas[0] == 'sí':
            gusta_pizza += 1
        if persona_respuestas[1] == 'sí':
            gusta_caminar += 1
        if persona_respuestas[0] == 'sí' and persona_respuestas[1] == 'sí':
            gusta_pizza_y_caminar += 1
        if persona_respuestas[0] == 'no' and persona_respuestas[1] == 'no':
            no_gusta_pizza_no_camina += 1

    no_gusta_pizza_si_camina = gusta_caminar - gusta_pizza_y_caminar
    gusta_pizza_no_camina = gusta_pizza - gusta_pizza_y_caminar

    print(f"De una encuesta a {total_personas} personas se obtuvo lo siguiente:")
    print(f"A {gusta_pizza} personas les gusta la pizza")
    print(f"A {gusta_caminar} personas les gusta caminar")
    print(f"De ellas se sabe que:")
    print(f"{gusta_pizza_y_caminar} personas les gusta la pizza y caminar")
    print(f"{no_gusta_pizza_no_camina} personas no les gusta ni la pizza ni caminar")
    print(f"{gusta_pizza_no_camina} personas les gusta la pizza pero no caminan")
    print(f"{no_gusta_pizza_si_camina} personas no les gusta la pizza pero sí caminan")


max_personas = int(input("Ingrese el número de personas a entrevistar: "))
respuestas_aleatorias = aleatorizar_respuestas(max_personas)

print("Respuestas aleatorias:")
print(respuestas_aleatorias)

analizar_respuestas(respuestas_aleatorias)

"""def leer_respuestas(respuestas):
    personas = len(respuestas)
    preguntas = len(respuestas[0])
    
    respuestas_dict = {}
    
    for i in range(personas):
        persona_respuestas = {}
        for j in range(preguntas):
            pregunta_id = j + 1
            clave_pregunta = f"p{pregunta_id}"
            respuesta = respuestas[i][j]
            persona_respuestas[clave_pregunta] = respuesta
        
        respuestas_dict[i+1] = persona_respuestas
    
    return respuestas_dict


max_personas = int(input("Ingrese el número de personas a entrevistar: "))
respuestas_aleatorias = aleatorizar_respuestas(max_personas)

print("Respuestas aleatorias:")
print(respuestas_aleatorias)

respuestas_dict = leer_respuestas(respuestas_aleatorias)

print("\nRespuestas en formato de diccionario:")
print(respuestas_dict)

# Ejemplo de análisis de respuestas
pregunta1_respuestas = [respuestas_dict[i]['p1'] for i in respuestas_dict]
pregunta2_respuestas = [respuestas_dict[i]['p2'] for i in respuestas_dict]

# Verificamos si las respuestas son iguales para cada pregunta y solo consideramos esas personas para la intersección
personas_misma_respuesta = [i for i in respuestas_dict if respuestas_dict[i]['p1'] == respuestas_dict[i]['p2']]
interseccion = [respuestas_dict[i]['p1'] for i in personas_misma_respuesta]
union = set(pregunta1_respuestas).union(pregunta2_respuestas)

contador_interseccion_si = interseccion.count('sí')
contador_interseccion_no = interseccion.count('no')

print("\nAnálisis de respuestas:")
print(f"Intersección de respuestas entre pregunta 1 y pregunta 2: {interseccion}")
print(f"Número de personas que respondieron 'sí' en la intersección: {contador_interseccion_si}")
print(f"Número de personas que respondieron 'no' en la intersección: {contador_interseccion_no}")
print(f"Número total de personas en la intersección: {len(personas_misma_respuesta)}")
print(f"Unión de respuestas entre pregunta 1 y pregunta 2: {union}")"""