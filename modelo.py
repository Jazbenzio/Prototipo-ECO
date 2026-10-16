#parte dario
# modelo.py
# El Arquitecto del Modelo programa aquí
import random

class Perceptron:
    def __init__(self):
        # Inicializar el "cerebro" en blanco
        self.w1 = random.uniform(-1, 1)
        self.w2 = random.uniform(-1, 1)
        self.bias = random.uniform(-1, 1)
        self.tasa_aprendizaje = 0.1

    def predecir(self, x1, x2):
        # Suma matemática
        suma = (x1 * self.w1) + (x2 * self.w2) + self.bias
        # Función de activación (Escalón)
        return 1 if suma > 0 else 0

    def entrenar(self, entradas, respuestas_correctas, epocas=20):
        print("Iniciando entrenamiento de la IA...")
        for epoca in range(epocas):
            for i in range(len(entradas)):
                prediccion = self.predecir(entradas[i][0], entradas[i][1])
                error = respuestas_correctas[i] - prediccion
                
                # Ajustar pesos si hubo error
                self.w1 += error * entradas[i][0] * self.tasa_aprendizaje
                self.w2 += error * entradas[i][1] * self.tasa_aprendizaje
                self.bias += error * self.tasa_aprendizaje
        print("Entrenamiento completado.")
