import numpy as np
import tensorflow as tf
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import random

def get_datos():
    # Cargar el dataset Iris
    iris = load_iris()
    x = iris.data  # Características
    y = iris.target  # Etiquetas

    # Dividir los datos en entrenamiento y validación (80% entrenamiento, 20% validación)
    x_entrenamiento, x_validacion, y_entrenamiento, y_validacion = train_test_split(x, y, test_size=0.2, random_state=42)
    
    return x_entrenamiento, y_entrenamiento, x_validacion, y_validacion

def compile_fit(capas, x, y, epochs, activation, x_validacion, y_validacion):
    np.random.seed(5)
    tf.random.set_seed(5)
    random.seed(5)  
    model = tf.keras.Sequential()
    for index, neuronas_capa in enumerate(capas):
        if index == 0:  # Primera capa
            model.add(tf.keras.layers.Dense(neuronas_capa, activation=activation, input_dim=x.shape[1]))
        else:  # Capas ocultas
            model.add(tf.keras.layers.Dense(neuronas_capa, activation=activation))
    # Capa de salida
    model.add(tf.keras.layers.Dense(3, activation='softmax'))  # 3 clases en el dataset Iris
    # Compilar el modelo
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    # Entrenar el modelo
    history = model.fit(x, y, epochs=epochs, verbose=1, validation_data=(x_validacion, y_validacion))
    
    return model, history

def graficar_perdida(history):
    plt.plot(history.history['loss'], label='Pérdida Entrenamiento')
    plt.plot(history.history['val_loss'], label='Pérdida Validación')
    plt.title('Pérdida durante el entrenamiento')
    plt.xlabel('Épocas')
    plt.ylabel('Pérdida')
    plt.legend()
    plt.show()


# Obtener los datos
x_entrenamiento, y_entrenamiento, x_validacion, y_validacion = get_datos()

redes_neuronales = [
    [16],  
    [32],
    [16],  
]

# Entrenar los modelos y mostrar los resultados
for index, capas in enumerate(redes_neuronales):
    # print(f"\nEntrenando el modelo {index + 1} con la configuración: {capas}")
    
    modelo, historial = compile_fit(capas, x_entrenamiento, y_entrenamiento, epochs=40, activation='selu', x_validacion=x_validacion, y_validacion=y_validacion)
    # Evaluar el modelo
    perdida, precision = modelo.evaluate(x_validacion, y_validacion, verbose=0)
    print(f"Pérdida: {perdida:.4f}, Precisión: {precision:.4f}")
    
    
graficar_perdida(historial)
# Guardar el modelo
modelo.save('modelo_iris.keras')