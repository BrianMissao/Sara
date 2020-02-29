# -*- coding: latin-1 -*-
import wx
from calcula import calcula
from relatorio import relatorio
from wx.lib.intctrl import IntCtrl
class Interface(wx.Frame):
    def __init__(Self, title="Sara Leide", name = "Sara Leide"):
        wx.Frame.__init__(Self, None, title=title, name=name)
        Self.atribuirEventosAosBotoes()
        Self.montarEstruturaDoPainel()
        Self.montarEstruturaDeMenus()
        Self.tornarAEstruturaDeMenusVisivel()
        Self.atribuirEventosAosMenus()
        Self.Show()

    def atribuirEventosAosBotoes(Self):
        Self.Bind(wx.EVT_BUTTON, Self.coletarDadosDoProduto, id=wx.ID_OK)

    def montarEstruturaDoPainel(Self):
        painel = wx.Panel(Self, -1, name="Adicionar produto")
        botaoAdicionarParaCalculo = wx.Button(painel, wx.ID_OK, label="Adicionar produto")

    def montarEstruturaDeMenus(Self):
        Self.ajuda = wx.Menu()
        Self.ajuda.Append(5001, "&Sobre")
        Self.menuBarra = wx.MenuBar()
        Self.menuBarra.Append(Self.ajuda, "&Ajuda")

    def tornarAEstruturaDeMenusVisivel(Self):
        Self.SetMenuBar(Self.menuBarra)

    def atribuirEventosAosMenus(Self):
        Self.Bind(wx.EVT_MENU, Self.sobre, id=5001)

    def coletarDadosDoProduto(Self, v):
        produto = wx.Dialog(Self, -1, title="Adicionar produto para cálculo", name="Adicionar produto para cálculo")
        Self.texto_estatico_produto = wx.StaticText(produto, label="Digite o produto:")
        Self.formula_produto = wx.TextCtrl(produto, -1, name="Digite o produto:")
        Self.Texto_estatico_preco = wx.StaticText(produto, label="Digite o preço total do produto no formato real.Centavo:")
        Self.formula_preco = wx.TextCtrl(produto, -1, name="Digite o preço total do produto no formato real.centavo:")
        Self.texto_estatico_quantidade = wx.StaticText(produto, label="Digite a quantidade do produto:")
        Self.formula_quantidade = IntCtrl(produto, -1, name="Digite a quantidade do protudo:")
        Self.texto_estatico_porcentagem = wx.StaticText(produto, label="Digite a porcentagem que será a base para o seu lucro:")
        Self.formula_porcentagem = IntCtrl(produto, -1, name="Digite a porcentagem que será a base para o seu lucro:")
        botaoCalcular = wx.Button(produto, wx.ID_OK, label="Calcular preço")
        botaoCancelar = wx.Button(produto, wx.ID_CANCEL, label="Cancelar")
        informacoesProduto = produto.ShowModal()
        if informacoesProduto == wx.ID_OK:
            Self.tratarDadosDigitadosPeloUsuario()

    def tratarDadosDigitadosPeloUsuario(Self):
        Self.formula_produto = Self.formula_produto.GetValue()
        Self.formula_preco = str(Self.formula_preco.GetValue())
        Self.formula_quantidade = str(Self.formula_quantidade.GetValue())
        Self.formula_porcentagem = str(Self.formula_porcentagem.GetValue())
        tratamento = [len(Self.formula_produto), len(Self.formula_preco), len(Self.formula_quantidade), len(Self.formula_porcentagem)]
        if 0 in tratamento:
            tratamento = wx.MessageDialog(Self, "Não foi possível adicionar este produto. Verifique se não há algum campo em branco e tente novamente.", "Adicionar produto", wx.OK|wx.ICON_WARNING)
            tratamento.ShowModal()
        else:
            Self.tentarConverterAsRespostasParaOsDevidosTiposECalcular()

    def tentarConverterAsRespostasParaOsDevidosTiposECalcular(Self):
        try:
            Self.formula_preco = float(Self.formula_preco)
            Self.formula_porcentagem = int(Self.formula_porcentagem)
            Self.formula_quantidade = int(Self.formula_quantidade)
            resultado_calculo = calcula(Self.formula_preco, Self.formula_porcentagem, Self.formula_quantidade)
            relatorio(Self.formula_produto, Self.formula_preco, Self.formula_porcentagem, Self.formula_quantidade, resultado_calculo["preco_venda"], resultado_calculo["preco_venda_unidade"], resultado_calculo["lucro_unidade"], resultado_calculo["lucro_total"])
            informacoes_produto = 'Produto adicionado com sucesso!\nVocê deve vendê-lo a %2s.\nCada unidade deve ser vendida a %2s.\nO lucro por unidade será de %2s, totalizando o lucro de %2s.\nPara mais informações, por favor consulte o arquivo "Relatório_produtos.txt"' % (resultado_calculo["preco_venda"], resultado_calculo["preco_venda_unidade"], resultado_calculo["lucro_unidade"], resultado_calculo["lucro_total"])
            mostra_resultado = wx.MessageDialog(Self, informacoes_produto, "Adicionar produto", wx.OK | wx.ICON_INFORMATION)
            mostra_resultado.ShowModal()
        except:
            resultado = wx.MessageDialog(Self, "Erro ao obter o cálculo deste produto.\n Verifique as informações e tente novamente.", "Adicionar produto", wx.OK|wx.ICON_WARNING)
            resultado.ShowModal()
            resultado.Destroy()
    def sobre(Self, v):
        informacoes = wx.MessageDialog(Self, "Sara Leide\nVerção 1.1", "Sobre", wx.OK | wx.ICON_INFORMATION)
        informacoes.ShowModal()
ex = wx.App()
Interface()
ex.MainLoop()