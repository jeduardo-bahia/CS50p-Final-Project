from flask import Flask, render_template, request, jsonify
import csv
import webbrowser
import threading
import time
from brain import detect_intent, generate_response, get_category_totals, format_brl

app = Flask(__name__)

DATA = []  # Dados carregados do CSV


def load_csv(file):
    transactions = []

    content = file.stream.read().decode("utf-8").splitlines()
    reader = csv.DictReader(content)

    for row in reader:
        transactions.append({
            "data": row["data"].strip(),
            "tipo": row["tipo"].strip().lower(),
            "categoria": row["categoria"].strip(),
            "valor": float(row["valor"])
        })

    return transactions


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    global DATA
    file = request.files["file"]
    DATA = load_csv(file)
    return jsonify({"message": "Arquivo carregado com sucesso!"})


@app.route("/chat", methods=["POST"])
def chat():
    message = request.json.get("message")

    if not DATA:
        return jsonify({"response": "Nenhum CSV carregado ainda."})

    intent = detect_intent(message)
    response = generate_response(intent, DATA, message)
    return jsonify({"response": response})


@app.route("/top_categories")
def top_categories():
    if not DATA:
        return jsonify({"top_saidas": [], "top_entradas": []})

    saidas = get_category_totals(DATA, "saida")
    entradas = get_category_totals(DATA, "entrada")

    top_saidas = sorted(saidas.items(), key=lambda x: x[1], reverse=True)[:5]
    top_entradas = sorted(entradas.items(), key=lambda x: x[1], reverse=True)[:5]

    # Formato: [categoria, valor_numerico, valor_formatado]
    top_saidas = [[cat, val, format_brl(val)] for cat, val in top_saidas]
    top_entradas = [[cat, val, format_brl(val)] for cat, val in top_entradas]

    return jsonify({"top_saidas": top_saidas, "top_entradas": top_entradas})


def open_browser():
    time.sleep(1)
    webbrowser.open("http://127.0.0.1:5000")


def main():
    threading.Thread(target=open_browser).start()
    app.run(debug=True, use_reloader=False)


if __name__ == "__main__":
    main()