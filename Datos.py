# datos.py
# El Ingeniero de Datos programa aquí

def obtener_datos_entrenamiento():
    """
    Devuelve los datos de entrada y las respuestas correctas.
    En el futuro, esto leerá un archivo CSV con Pandas.
    """
    # Entradas: [0,0], [0,1], [1,0], [1,1]
    entradas = [[0, 0], [0, 1], [1, 0], [1, 1]]
    
    # Respuestas que la IA debe aprender a predecir (Compuerta OR)
    respuestas_correctas = [0, 1, 1, 1]
    
    return entradas, respuestas_correctas