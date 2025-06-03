import streamlit as st
import requests

# Configuração inicial
st.set_page_config(page_title="Predição de Enchentes", layout="centered")
st.title("🌧️ Dashboard de Predição de Enchentes via API")

st.markdown("Insira os dados climáticos abaixo para prever o risco de enchente:")

# Interface para entrada de dados
chuva = st.number_input("Chuva (mm)", min_value=0.0, max_value=500.0, value=30.0)
umidade = st.number_input("Umidade (%)", min_value=0.0, max_value=100.0, value=80.0)
temperatura = st.number_input("Temperatura (°C)", min_value=-10.0, max_value=50.0, value=25.0)
nivel_rio = st.number_input("Nível do Rio (m)", min_value=0.0, max_value=10.0, value=2.5)

# Quando clicar no botão
if st.button("🔍 Verificar risco de enchente"):
    payload = {
        "Chuva_mm": chuva,
        "Umidade_%": umidade,
        "Temperatura_C": temperatura,
        "Nivel_rio_m": nivel_rio
    }

    try:
        response = requests.post("http://127.0.0.1:5000/predict", json=payload)

        if response.status_code == 200:
            resultado = response.json()
            if resultado['enchente'] == 1:
                st.error("⚠️ Risco de ENCHENTE detectado!")
            else:
                st.success("✅ Sem risco de enchente.")
        else:
            st.warning("Erro ao consultar a API. Verifique se ela está rodando.")

    except Exception as e:
        st.error(f"Erro de conexão com a API: {e}")
