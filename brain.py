def format_brl(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def detect_intent(message):
    message = message.lower()

    if "entrada" in message:
        return "total_entradas"
    elif "saida" in message:
        return "total_saidas"
    elif "saldo" in message:
        return "saldo"
    elif "maior gasto" in message:
        return "maior_gasto"
    else:
        return "unknown"


def calculate_summary(data):
    total_entradas = sum(t["valor"] for t in data if t["tipo"] == "entrada")
    total_saidas = sum(t["valor"] for t in data if t["tipo"] == "saida")
    return total_entradas, total_saidas


def get_category_totals(data, tipo):
    """Retorna um dicionário com o total por categoria para um tipo (entrada/saida)."""
    totals = {}
    for t in data:
        if t["tipo"] == tipo:
            categoria = t["categoria"]
            totals[categoria] = totals.get(categoria, 0) + t["valor"]
    return totals


def get_highest_expense_category(data):
    gastos = get_category_totals(data, "saida")
    if not gastos:
        return None
    return max(gastos, key=gastos.get)


def get_lowest_expense_category(data):
    gastos = get_category_totals(data, "saida")
    if not gastos:
        return None
    return min(gastos, key=gastos.get)


def get_highest_entry_category(data):
    entradas = get_category_totals(data, "entrada")
    if not entradas:
        return None
    return max(entradas, key=entradas.get)


def get_lowest_entry_category(data):
    entradas = get_category_totals(data, "entrada")
    if not entradas:
        return None
    return min(entradas, key=entradas.get)


def get_highest_entry_date(data):
    totals = {}
    for t in data:
        if t["tipo"] == "entrada":
            date = t["data"]
            totals[date] = totals.get(date, 0) + t["valor"]
    if not totals:
        return None
    return max(totals, key=totals.get)


def get_highest_exit_date(data):
    totals = {}
    for t in data:
        if t["tipo"] == "saida":
            date = t["data"]
            totals[date] = totals.get(date, 0) + t["valor"]
    if not totals:
        return None
    return max(totals, key=totals.get)


def get_top_category_by_date(data, date, tipo):
    totals = {}
    for t in data:
        if t["data"] == date and t["tipo"] == tipo:
            categoria = t["categoria"]
            totals[categoria] = totals.get(categoria, 0) + t["valor"]
    if not totals:
        return None
    return max(totals, key=totals.get)


def get_available_categories(data):
    categorias = set()
    for t in data:
        categorias.add(t["categoria"])
    return sorted(categorias)


def generate_response(intent, data, message=None):

    if not message:
        return "Pergunta inválida."

    message = message.lower()

    # AJUDA
    if "ajuda" in message:
        categorias = get_available_categories(data)
        if not categorias:
            return "Nenhum CSV carregado."
        lista = "\n".join(f"- {c}" for c in categorias)
        return (
            "Categorias disponíveis no CSV:\n"
            f"{lista}\n\n"
            "Você pode perguntar:\n"
            "• total de saida em CATEGORIA\n"
            "• total de entrada em CATEGORIA\n"
            "• maior saida por data\n"
            "• maior entrada por data\n"
            "• qual categoria teve maior saida\n"
            "• qual categoria teve menor saida\n"
            "• qual categoria teve maior entrada\n"
            "• qual categoria teve menor entrada\n"
            "• saldo"
        )

    # MAIOR/MENOR CATEGORIA DE SAÍDA
    if "categoria" in message and "saida" in message:
        totals = get_category_totals(data, "saida")
        if not totals:
            return "Não encontrei saídas."
        if "menor" in message:
            categoria = min(totals, key=totals.get)
            return f"Categoria com menor saída: {categoria} ({format_brl(totals[categoria])})"
        else:
            categoria = max(totals, key=totals.get)
            return f"Categoria com maior saída: {categoria} ({format_brl(totals[categoria])})"

    # MAIOR/MENOR CATEGORIA DE ENTRADA
    if "categoria" in message and "entrada" in message:
        totals = get_category_totals(data, "entrada")
        if not totals:
            return "Não encontrei entradas."
        if "menor" in message:
            categoria = min(totals, key=totals.get)
            return f"Categoria com menor entrada: {categoria} ({format_brl(totals[categoria])})"
        else:
            categoria = max(totals, key=totals.get)
            return f"Categoria com maior entrada: {categoria} ({format_brl(totals[categoria])})"

    # MAIOR ENTRADA POR DATA
    if "maior entrada por data" in message:
        date = get_highest_entry_date(data)
        if date:
            return f"A data com maior entrada foi {date}"
        return "Não encontrei entradas."

    # MAIOR SAÍDA POR DATA
    if "maior saida por data" in message:
        date = get_highest_exit_date(data)
        if date:
            return f"A data com maior saída foi {date}"
        return "Não encontrei saídas."

    # MAIOR CATEGORIA EM DATA ESPECÍFICA
    for t in data:
        if t["data"].lower() in message:
            date = t["data"]
            if "saida" in message:
                categoria = get_top_category_by_date(data, date, "saida")
                if categoria:
                    return f"Maior saída em {date}: {categoria}"
            if "entrada" in message:
                categoria = get_top_category_by_date(data, date, "entrada")
                if categoria:
                    return f"Maior entrada em {date}: {categoria}"

    # DETECTAR CATEGORIA NA PERGUNTA
    for t in data:
        categoria = t["categoria"].lower()
        if categoria in message:
            if "entrada" in message:
                total = sum(
                    x["valor"] for x in data
                    if x["categoria"].lower() == categoria and x["tipo"] == "entrada"
                )
                return f"Total de entradas em {categoria}: {format_brl(total)}"
            if "saida" in message:
                total = sum(
                    x["valor"] for x in data
                    if x["categoria"].lower() == categoria and x["tipo"] == "saida"
                )
                return f"Total de saídas em {categoria}: {format_brl(total)}"
            total = sum(
                x["valor"] for x in data
                if x["categoria"].lower() == categoria
            )
            return f"Total em {categoria}: {format_brl(total)}"

    # TOTAIS GERAIS
    total_entradas, total_saidas = calculate_summary(data)

    if intent == "total_entradas":
        return f"Total de entradas: {format_brl(total_entradas)}"

    if intent == "total_saidas":
        return f"Total de saídas: {format_brl(total_saidas)}"

    if intent == "saldo":
        saldo = total_entradas - total_saidas
        return f"Saldo atual: {format_brl(saldo)}"

    if intent == "maior_gasto":
        categoria = get_highest_expense_category(data)
        if categoria:
            return f"Categoria com maior gasto: {categoria}"
        return "Nenhuma despesa encontrada."

    return "Desculpe, não entendi sua pergunta."