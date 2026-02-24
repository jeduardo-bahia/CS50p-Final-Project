![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0-000000?style=flat&logo=flask&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-passing-brightgreen?style=flat&logo=pytest&logoColor=white)
![CSV](https://img.shields.io/badge/CSV-Data-orange?style=flat&logo=files&logoColor=white)
![CS50P](https://img.shields.io/badge/CS50P-Final%20Project-red?style=flat&logo=edx&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat)

# 💰 EduFin — Analisador Financeiro

> *Sistema de chat financeiro que lê arquivos CSV e responde perguntas em linguagem natural.*

---

## 📌 Sobre o Projeto

O **EduFin** é um assistente financeiro inteligente desenvolvido em Python com Flask. Ele permite que o usuário carregue um arquivo CSV com transações financeiras e faça perguntas em português para obter análises detalhadas dos dados — sem precisar de fórmulas ou planilhas complexas.

---

## ⚙️ Funcionalidades

- 📂 Upload de arquivos CSV com transações financeiras
- 💬 Chat em linguagem natural para consulta dos dados
- 📊 Dashboard com resumo financeiro atualizado automaticamente
- 🏆 Top 5 categorias com maiores entradas e saídas
- 🔍 Consulta por categoria, data e tipo de transação
- 💲 Valores formatados em Real Brasileiro (R$)

---

## 💬 Perguntas Suportadas

| Pergunta | Exemplo |
|---|---|
| Total de entradas | `total de entradas` |
| Total de saídas | `total de saidas` |
| Saldo atual | `saldo` |
| Maior gasto | `maior gasto` |
| Categoria com maior saída | `qual categoria teve maior saida` |
| Categoria com menor saída | `qual categoria teve menor saida` |
| Categoria com maior entrada | `qual categoria teve maior entrada` |
| Categoria com menor entrada | `qual categoria teve menor entrada` |
| Total por categoria | `total de saida em logística` |
| Data com maior entrada | `maior entrada por data` |
| Data com maior saída | `maior saida por data` |
| Categorias disponíveis | `ajuda` |

---

## 🗂️ Estrutura do Projeto

```
INTENT_ENGINE/
├── static/
│   └── img/
│       └── avatar.png
├── templates/
│   └── index.html          # Interface do chat
├── brain.py                # Lógica e motor de intenções
├── project.py              # Aplicação Flask principal
├── test_project.py         # Testes automatizados com pytest
├── requirements.txt        # Dependências
└── sample_data.csv         # CSV de exemplo
```

---

## 🚀 Como Executar

**1. Clone o repositório**
```bash
git clone https://github.com/jeduardo-bahia/CS50p-Final-Project.git
cd CS50p-Final-Project
```

**2. Instale as dependências**
```bash
pip install -r requirements.txt
```

**3. Execute o projeto**
```bash
python project.py
```

O navegador abrirá automaticamente em `http://127.0.0.1:5000` 🎉

---

## 🧪 Testes

```bash
pytest test_project.py
```

Funções testadas:
- `calculate_summary` — calcula o total de entradas e saídas
- `get_highest_entry_date` — encontra a data com maior entrada
- `get_available_categories` — lista todas as categorias do CSV

---

## 📦 Dependências

```
flask
pytest
```

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Uso |
|---|---|
| Python | Linguagem principal |
| Flask | Framework web |
| CSV Module | Leitura e parsing de arquivos |
| HTML5 / CSS3 | Estrutura e estilo |
| JavaScript | Interações e dashboard |
| Pytest | Testes automatizados |
| Google Fonts | Tipografia (Syne + DM Mono) |

---

## 🎯 Decisões de Design

- O `brain.py` foi separado do `project.py` para isolar a lógica da camada web, facilitando os testes e a manutenção.
- A detecção de intenção usa correspondência de palavras-chave, sendo simples, eficiente e fácil de expandir.
- O chat flutuante foi escolhido para que o dashboard permaneça visível durante a conversa.
- O formato CSV foi mantido simples (sem banco de dados) para facilitar o uso local.

---

## 👨‍💻 Autor

**Jhonanthan E. C. Bahia** — CS50P Final Project — 2026

[![GitHub](https://img.shields.io/badge/GitHub-jeduardo--bahia-181717?style=flat&logo=github)](https://github.com/jeduardo-bahia)

---

> *"Stop drowning in spreadsheets. Just ask EduFin."*
