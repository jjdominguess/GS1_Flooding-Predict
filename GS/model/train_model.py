import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report
import joblib
import os

# Caminhos
INPUT_PATH = '../data/processed/arquivo_pronto.csv'
MODEL_PATH = 'model/flood_predictor.pkl'

# Carregar os dados
df = pd.read_csv(INPUT_PATH)

# Separar X (features) e y (target)
X = df.drop(columns=['Data', 'enchente'])  # 'Data' não é uma feature útil
y = df['enchente']

# Separar treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Treinar modelo
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Avaliar
y_pred = model.predict(X_test)
print("Matriz de Confusão:")
print(confusion_matrix(y_test, y_pred))
print("\nRelatório de Classificação:")
print(classification_report(y_test, y_pred))

os.makedirs('model', exist_ok=True)
# Salvar modelo treinado
joblib.dump(model, MODEL_PATH)
print(f"\nModelo salvo em: {MODEL_PATH}")
