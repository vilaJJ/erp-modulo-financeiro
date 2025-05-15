def moeda_para_float(valor_formatado: str) -> float:
    if not valor_formatado:
        return 0.0

    valor_limpo = valor_formatado.replace("R$", "").replace(".", "").replace(",", ".").strip()

    try:
        return float(valor_limpo)
    except ValueError:
        return 0.0