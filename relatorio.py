# -*- coding: utf-8 -*-
from os import path
def relatorio(produto, preco, porcentagem, quantidade, preco_venda, preco_venda_unidade, lucro_unidade, lucro_total):
    relatorio_produto = "*"+produto+"\nPreço pago pelo lote do produto: %2s\nQuantidade em estoque: %s\nPorcentagem base para o lucro: %s\nPreço de revenda: %2s\nLucro por unidade: %s\nLucro total da venda do estoque: %s" % (preco, quantidade, porcentagem, preco_venda, lucro_unidade, lucro_total)
    if not path.exists("relatório_produtos.txt"):
        f = open("Relatório_produtos.txt", "w")
        f.write(relatorio_produto)
    else:
        f = open("Relatório_produtos.txt", "a")
        f.write("\n\n")
        f.write(relatorio_produto)
    f.close()