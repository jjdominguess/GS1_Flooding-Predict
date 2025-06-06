# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Nome do projeto

## Nome do grupo

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do integrante 1</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do integrante 2</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do integrante 3</a> 
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do integrante 4</a> 
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do integrante 5</a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do Tutor</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do Coordenador</a>


## 📜 Descrição

*Descreva seu projeto com base no texto do PBL (até 600 palavras)*


## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>.github</b>: Nesta pasta ficarão os arquivos de configuração específicos do GitHub que ajudam a gerenciar e automatizar processos no repositório.

- <b>assets</b>: aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como imagens.

- <b>config</b>: Posicione aqui arquivos de configuração que são usados para definir parâmetros e ajustes do projeto.

- <b>document</b>: aqui estão todos os documentos do projeto que as atividades poderão pedir. Na subpasta "other", adicione documentos complementares e menos importantes.

- <b>scripts</b>: Posicione aqui scripts auxiliares para tarefas específicas do seu projeto. Exemplo: deploy, migrações de banco de dados, backups.

- <b>src</b>: Todo o código fonte criado para o desenvolvimento do projeto ao longo das 7 fases.

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

## 🔧 Como executar o código

*Acrescentar as informações necessárias sobre pré-requisitos (IDEs, serviços, bibliotecas etc.) e instalação básica do projeto, descrevendo eventuais versões utilizadas. Colocar um passo a passo de como o leitor pode baixar o seu código e executá-lo a partir de sua máquina ou seu repositório. Considere a explicação organizada em fase.*


## 🗃 Histórico de lançamentos

* 0.5.0 - XX/XX/2024
    * 
* 0.4.0 - XX/XX/2024
    * 
* 0.3.0 - XX/XX/2024
    * 
* 0.2.0 - XX/XX/2024
    * 
* 0.1.0 - XX/XX/2024
    *

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>

# Global Solution 2025.1 – Previsão e Monitoramento de Enchentes

## Descrição do Projeto
Este projeto é um MVP funcional para a Global Solution FIAP 2025.1, focado em prever e monitorar enchentes utilizando sensores simulados (ESP32/Wokwi), Machine Learning em Python e integração via API. O sistema lê dados ambientais, processa e envia para um modelo de ML que retorna o risco de enchente em tempo real.

---

## Estrutura do Projeto
- **wokwi/**: Simulação do protótipo ESP32 com sensores (HC-SR04 e DHT22) no Wokwi.
- **GS/api/**: API Flask para receber dados dos sensores e retornar predição do modelo.
- **GS/model/**: Scripts de tratamento de dados, treinamento e modelo salvo.
- **GS/data/**: Dados brutos e processados.
- **GS/dashboard/**: (Opcional) Dashboard para visualização dos dados e predições.

---

## 1. Simulação do ESP32 no Wokwi
- O arquivo `wokwi/src/prog.ino` simula um ESP32 lendo sensores de nível de rio (HC-SR04) e clima (DHT22).
- O ESP32 conecta-se ao WiFi simulado (`Wokwi-GUEST`) e envia os dados via HTTP POST para a API Flask.
- O arquivo `wokwi.toml` faz o forward da porta 5000 para permitir que o ESP32 acesse a API local usando `host.docker.internal`.
- Para rodar:
  1. Execute o Wokwi IoT Bridge na sua máquina.
  2. Rode a API Flask localmente.
  3. Dê play no Wokwi.

---

## 2. Tratamento de Dados
- Os dados brutos de enchentes são armazenados em `GS/data/raw/dados_enchente.csv`.
- O script `GS/model/preprocess_data.py` faz:
  - Leitura dos dados brutos.
  - Limpeza, tratamento de valores ausentes, conversão de tipos e normalização.
  - Geração do arquivo processado `GS/data/processed/arquivo_pronto.csv`.
- O pipeline garante que os dados estejam prontos para o treinamento do modelo.

---

## 3. Treinamento do Algoritmo de Machine Learning
- O script `GS/model/train_model.py`:
  - Lê os dados processados.
  - Separa features e target.
  - Treina um modelo de ML (ex: RandomForest, DecisionTree, etc.) para prever risco de enchente.
  - Salva o modelo treinado em `GS/model/flood_predictor.pkl`.
- O modelo é carregado pela API para predições em tempo real.

---

## 4. API Flask
- O arquivo `GS/api/api.py` implementa uma API REST com endpoint `/predict`.
- Recebe dados dos sensores via POST, aplica o modelo de ML e retorna o resultado (risco de enchente).
- Exemplo de payload esperado:
```json
{
  "Chuva_mm": 40,
  "Umidade_%": 85,
  "Temperatura_C": 22,
  "Nivel_rio_m": 2.2
}
```

---

## 5. Dashboard (Opcional)
- O diretório `GS/dashboard/` pode conter scripts para visualização dos dados e predições em tempo real (ex: Streamlit, Dash, Jupyter Notebook).

---

## 6. Como rodar o projeto
1. **Pré-requisitos:**
   - Python 3.10+
   - Bibliotecas: flask, joblib, pandas, numpy, scikit-learn, requests
   - Wokwi IoT Bridge instalado
2. **Tratamento e treinamento:**
   ```powershell
   python GS/model/preprocess_data.py
   python GS/model/train_model.py
   ```
3. **Rodar a API:**
   ```powershell
   python GS/api/api.py
   ```
4. **Rodar o Wokwi IoT Bridge**
   - Execute o `wokwi-io-bridge.exe` e deixe aberto.
5. **Simular o ESP32 no Wokwi**
   - Abra o projeto no Wokwi, dê play no `diagram.json`.
6. **(Opcional) Rodar o dashboard:**
   ```powershell
   python GS/dashboard/dashboard.py
   ```

---

## 7. Observações
- O projeto pode ser facilmente adaptado para uso com ESP32 físico.
- O pipeline de dados é modular e pode ser expandido para outros eventos extremos.
- Para dúvidas ou sugestões, consulte o código-fonte e os comentários nos scripts.

---

## 8. Créditos
- Projeto desenvolvido para a Global Solution FIAP 2025.1
- Integrantes: [Adicione os nomes aqui]
- Orientador: [Adicione o nome do professor, se desejar]

---

# Como Executar o Projeto – Global Solution 2025.1

## Pré-requisitos
- Python 3.10 ou superior
- Pip (gerenciador de pacotes Python)
- Bibliotecas Python: flask, joblib, pandas, numpy, scikit-learn, requests
- Wokwi IoT Bridge instalado (para integração ESP32/API)
- (Opcional) PlatformIO ou Arduino IDE para simulação local do ESP32

---

## Passo a Passo para Rodar o Projeto

### 1. Instale as dependências Python
Abra o terminal na pasta do projeto e execute:
```powershell
pip install flask joblib pandas numpy scikit-learn requests
```

### 2. (Opcional) Prepare os dados e treine o modelo
Se quiser refazer o pipeline de dados e o treinamento:
```powershell
python GS/model/preprocess_data.py
python GS/model/train_model.py
```

### 3. Rode a API Flask
No terminal, execute:
```powershell
python GS/api/api.py
```
A API estará disponível em http://localhost:5000/predict

### 4. Rode o Wokwi IoT Bridge
Baixe e execute o `wokwi-io-bridge.exe` (deixe a janela aberta).

### 5. Simule o ESP32 no Wokwi
- Abra o projeto no [wokwi.com](https://wokwi.com/)
- Importe o arquivo `diagram.json` e o código `src/prog.ino`
- Dê play no simulador
- O ESP32 irá conectar ao WiFi simulado e enviar dados para a API Flask

### 6. (Opcional) Rode o dashboard
Se desejar visualizar os dados/predições em tempo real:
```powershell
python GS/dashboard/dashboard.py
```

---

## Observações Importantes
- O arquivo `wokwi/wokwi.toml` já está configurado para o forward da porta 5000.
- O ESP32 simulado usa o WiFi `Wokwi-GUEST` e envia dados para `host.docker.internal:5000/predict`.
- Certifique-se de que a API Flask e o Wokwi IoT Bridge estejam rodando antes de dar play no Wokwi.
- Para dúvidas, consulte os comentários nos scripts e o README detalhado.

---

## Exemplo de Fluxo Completo
1. Rode a API Flask
2. Rode o Wokwi IoT Bridge
3. Dê play no Wokwi
4. Veja os dados chegando na API e os logs no monitor serial

---

## Créditos
Projeto desenvolvido para a Global Solution FIAP 2025.1