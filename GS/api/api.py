from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np
import os

# Carregar modelo
model_path = os.path.join(os.path.dirname(__file__), '..', 'model', 'flood_predictor.pkl')
model = joblib.load(os.path.abspath(model_path))

# Inicializar a API Flask
app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Receber JSON
        data = request.get_json()
        print(f"[LOG] Dados recebidos no /predict: {data}")  # Log dos dados recebidos

        # Criar DataFrame com uma linha
        df = pd.DataFrame([data])

        # Verificar se as colunas estão na ordem correta
        expected_cols = ['Chuva_mm', 'Umidade_%', 'Temperatura_C', 'Nivel_rio_m']
        if not all(col in df.columns for col in expected_cols):
            return jsonify({'error': 'JSON incompleto. Esperado: ' + str(expected_cols)}), 400

        # Fazer a predição
        prediction = model.predict(df)[0]

        return jsonify({'enchente': int(prediction)})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Rodar localmente
if __name__ == '__main__':
    app.run(debug=True, host = "0.0.0.0", port=5000)
