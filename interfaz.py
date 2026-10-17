
# El Desarrollador de la Interfaz programa aquí

# Importamos el trabajo de los compañeros
from Guardado_de_datos import obtener_datos_entrenamiento
from modelo import Perceptron

def main():
    print("=== ASISTENTE VIRTUAL IA ===")
    
    # 1. Traemos los datos
    entradas, respuestas = obtener_datos_entrenamiento()
    
    # 2. Creamos la IA
    mi_ia = Perceptron()
    
    # 3. La entrenamos
    mi_ia.entrenar(entradas, respuestas)
    
    # 4. Menú interactivo
    while True:
        print("\nPrueba la IA. Ingresa dos números (0 o 1). Escribe 'salir' para terminar.")
        val1 = input("Primer valor: ")
        if val1.lower() == 'salir':
            break
            
        val2 = input("Segundo valor: ")
        
        try:
            x1 = int(val1)
            x2 = int(val2)
            resultado = mi_ia.predecir(x1, x2)
            print(f"--> La IA dice que el resultado es: {resultado}")
        except ValueError:
            print("Por favor, ingresa solo números (0 o 1).")

if __name__ == "__main__":
    main()