from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np

# Carregar modelo
model = joblib.load('../model/flood_predictor.pkl')

# Inicializar a API Flask
app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Receber JSON
        data = request.get_json()

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
    app.run(debug=True)
