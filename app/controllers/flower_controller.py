from flask import Blueprint, render_template, request, jsonify
from app.services.flower_service import cargar_modelo, hacer_prediccion

flower = Blueprint('routes', __name__)

try:
    modelo = cargar_modelo()
except Exception as e:
    modelo = None
    print(f"Error al cargar el modelo: {e}")

@flower.route('/', methods=['GET'])
def index(name=None):
    try:
        return render_template('index.html')
    except Exception as e:
        return f"Error al cargar la web: {str(e)}", 500

@flower.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()  
        length_sepal = data['length_sepal']
        length_petal = data['length_petal']
        width_sepal = data['width_sepal']
        width_petal = data['width_petal']
        if modelo is None:
            return jsonify({'error': 'Modelo no cargado correctamente'}), 500
        
        prediccion = hacer_prediccion(modelo, length_sepal, length_petal, width_sepal, width_petal)
        
        if prediccion is None:
            return jsonify({'error': 'Error en la predicción'}), 500
        
        return jsonify({'prediction': prediccion})
    except Exception as e:
        return jsonify({'error': f'Error en la solicitud: {str(e)}'}), 400