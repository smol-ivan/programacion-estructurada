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
    print(f"De ellas se sabe que:")
    print(f"{gusta_pizza_y_caminar} personas les gusta la pizza y caminar")
    print(f"{no_gusta_pizza_no_camina} personas no les gusta ni la pizza ni caminar")
    print(f"{gusta_pizza_no_camina} personas les gusta la pizza pero no caminan")
    print(f"{no_gusta_pizza_si_camina} personas no les gusta la pizza pero sí caminan")


max_personas = int(input("Ingrese el número de personas a entrevistar: "))
respuestas_aleatorias = aleatorizar_respuestas(max_personas)

analizar_respuestas(respuestas_aleatorias)