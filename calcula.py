# -*- coding: utf-8 -*-
def calcula(preco, porcentagem, quantidade):
    preco_venda = ((preco/100)*porcentagem+preco)
    lucro_unidade = ((preco_venda-preco)/quantidade)
    lucro_total = str(lucro_unidade*quantidade)
    lucro_unidade = str(lucro_unidade)
    preco_venda_unidade = str(preco_venda/quantidade)
    preco_venda = str(preco_venda)
    resultado = {"preco_venda": preco_venda, "preco_venda_unidade": preco_venda_unidade, "lucro_unidade": lucro_unidade, "lucro_total": lucro_total}
    return resultado
