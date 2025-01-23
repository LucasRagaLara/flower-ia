import numpy as np
import tensorflow as tf

def cargar_modelo():
    try:
        model = tf.keras.models.load_model('./model/modelo_iris.keras')
        return model
    except Exception as e:
        print(f"Error al cargar el modelo: {e}")
        return None

flores = {
    0: "Setosa",
    1: "Versicolor",
    2: "Virginica"
}

def hacer_prediccion(modelo, length_sepal, length_petal, width_sepal, width_petal):
    try:
        input_data = np.array([[length_sepal, length_petal, width_sepal, width_petal]]) 
        pred = modelo.predict(input_data)
        print("Probabilidades:", pred)
        clase_predicha = np.argmax(pred, axis=1)[0]
        flor_predicha = flores[clase_predicha]
        return flor_predicha
    except Exception as e:
        print(f"Error en la predicción: {e}")
        return None