import random

# 1. Datos de entrenamiento (Compuerta OR)
# Entradas: [0,0], [0,1], [1,0], [1,1]
datos = [[0, 0], [0, 1], [1, 0], [1, 1]]
# Respuestas que la IA debe aprender a predecir
respuestas_correctas = [0, 1, 1, 1]

# 2. Inicializar el "cerebro" en blanco (Valores aleatorios)
w1 = random.uniform(-1, 1)
w2 = random.uniform(-1, 1)
bias = random.uniform(-1, 1)
tasa_aprendizaje = 0.1  # Qué tan rápido ajusta sus errores

def predecir(x1, x2):
    # Suma matemática de las entradas multiplicadas por sus pesos
    suma = (x1 * w1) + (x2 * w2) + bias
    # Función de activación (Escalón: devuelve 1 si es positivo, 0 si no)
    return 1 if suma > 0 else 0

# 3. Ciclo de Entrenamiento (La IA aprende de sus errores)
epocas = 20 # Veces que repasará los datos completos
for epoca in range(epocas):
    for i in range(4):
        prediccion = predecir(datos[i][0], datos[i][1])
        error = respuestas_correctas[i] - prediccion
        
        # 4. Ajustar pesos si hubo error (Aprendizaje)
        w1 += error * datos[i][0] * tasa_aprendizaje
        w2 += error * datos[i][1] * tasa_aprendizaje
        bias += error * tasa_aprendizaje

# Prueba final para comprobar si aprendió
print("¡Entrenamiento terminado! Comprobando memoria de la IA:")
for i in range(4):
    print(f"Entradas {datos[i]} -> Predicción de la IA: {predecir(datos[i][0], datos[i][1])}")