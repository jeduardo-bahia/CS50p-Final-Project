from brain import (
    calculate_summary,
    get_highest_entry_date,
    get_available_categories
)

# Dados fake para teste
sample_data = [
    {"data": "2025-01-01", "tipo": "entrada", "categoria": "APORTES", "valor": 1000},
    {"data": "2025-01-01", "tipo": "saida", "categoria": "MARKETING", "valor": 300},
    {"data": "2025-01-02", "tipo": "entrada", "categoria": "VENDAS", "valor": 2000},
    {"data": "2025-01-02", "tipo": "saida", "categoria": "SALARIOS", "valor": 500},
]


def test_calculate_summary():
    entradas, saidas = calculate_summary(sample_data)
    assert entradas == 3000
    assert saidas == 800


def test_get_highest_entry_date():
    date = get_highest_entry_date(sample_data)
    assert date == "2025-01-02"


def test_get_available_categories():
    categorias = get_available_categories(sample_data)
    assert "APORTES" in categorias
    assert "MARKETING" in categorias
    assert "VENDAS" in categorias
    assert "SALARIOS" in categorias