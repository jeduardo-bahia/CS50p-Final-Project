![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0-000000?style=flat&logo=flask&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-passing-brightgreen?style=flat&logo=pytest&logoColor=white)
![CSV](https://img.shields.io/badge/CSV-Data-orange?style=flat&logo=files&logoColor=white)
![CS50P](https://img.shields.io/badge/CS50P-Final%20Project-red?style=flat&logo=edx&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat)

# FinSight

### CS50P Final Project — by Jhonanthan Bahia

---

## 📌 Description / Descrição

**English:**
FinSight is a web-based financial chat assistant that allows users to upload a CSV file containing financial transactions and ask questions about their data in natural language (Portuguese). The application analyzes income, expenses, balances, and categories, returning formatted responses through a floating chat interface.

**Português:**
O FinSight é um assistente financeiro via chat que permite ao usuário carregar um arquivo CSV com transações financeiras e fazer perguntas sobre os dados em linguagem natural. A aplicação analisa entradas, saídas, saldos e categorias, retornando respostas formatadas através de uma interface de chat flutuante.

---

## 📁 Project Structure / Estrutura do Projeto

```
FINSIGHT/
├── static/
│   └── img/
│       └── avatar.png
├── templates/
│   └── index.html        # Chat interface / Interface do chat
├── brain.py              # Logic and intent engine / Lógica e motor de intenções
├── project.py            # Main Flask application / Aplicação Flask principal
├── test_project.py       # Pytest tests / Testes com pytest
├── requirements.txt      # Dependencies / Dependências
└── sample_data.csv       # Sample CSV for testing / CSV de exemplo
```

---

## ⚙️ How It Works / Como Funciona

**English:**
1. The user uploads a `.csv` file with columns: `data`, `tipo`, `categoria`, `valor`
2. The user types a question in the chat (e.g. *"total de entradas"*, *"saldo"*, *"maior gasto"*)
3. `brain.py` detects the intent of the message and generates a response based on the loaded data
4. The response is displayed in the floating chat interface

**Português:**
1. O usuário carrega um arquivo `.csv` com as colunas: `data`, `tipo`, `categoria`, `valor`
2. O usuário digita uma pergunta no chat (ex: *"total de entradas"*, *"saldo"*, *"maior gasto"*)
3. O `brain.py` detecta a intenção da mensagem e gera uma resposta com base nos dados carregados
4. A resposta é exibida na interface de chat flutuante

---

## 💬 Supported Questions / Perguntas Suportadas

| Question / Pergunta | Example / Exemplo |
|---|---|
| Total income | `total de entradas` |
| Total expenses | `total de saidas` |
| Current balance | `saldo` |
| Highest expense category | `maior gasto` |
| Total by category | `total de saida em logística` |
| Highest income date | `maior entrada por data` |
| Highest expense date | `maior saida por data` |
| Available categories | `ajuda` |

---

## ▶️ How to Run / Como Executar

```bash
# Install dependencies / Instalar dependências
pip install -r requirements.txt

# Run the application / Executar a aplicação
python project.py
```

The browser will open automatically at `http://127.0.0.1:5000`

---

## 🧪 Running Tests / Executando os Testes

```bash
pytest test_project.py
```

Tests cover / Os testes cobrem:
- `calculate_summary` — calculates total income and expenses
- `get_highest_entry_date` — finds the date with the highest income
- `get_available_categories` — lists all categories in the data

---

## 📦 Dependencies / Dependências

- `flask` — web framework
- `pytest` — testing framework

---

## 🎯 Design Decisions / Decisões de Design

**English:**
- `brain.py` was kept separate from `project.py` to isolate the logic from the web layer, making it easier to test and maintain.
- Intent detection uses simple keyword matching, which is efficient and easy to extend.
- A floating chat widget was chosen over a full-page layout to allow the dashboard to remain visible while chatting.
- The CSV format was kept simple (no database) to make the project accessible and easy to run locally.

**Português:**
- O `brain.py` foi mantido separado do `project.py` para isolar a lógica da camada web, facilitando os testes e a manutenção.
- A detecção de intenção usa correspondência simples de palavras-chave, sendo eficiente e fácil de expandir.
- Um chat flutuante foi escolhido em vez de uma página inteira para permitir que o dashboard permaneça visível durante a conversa.
- O formato CSV foi mantido simples (sem banco de dados) para tornar o projeto acessível e fácil de executar localmente.
