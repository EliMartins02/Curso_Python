class TabelaIR():
    def __init__(self):
        self.tabela = [
        {"faixa": (0, 1903.98), "aliquota": 0, "deducao": 0},
        {"faixa": (1903.99, 2826.65), "aliquota": 7.5, "deducao": 142.80}, # sempre usa o ponto para nº
        {"faixa": (2826.66, 3751.05), "aliquota": 15, "deducao": 344.80},
        {"faixa": (3751.06, 4664.68), "aliquota": 22.5, "deducao": 630.80},
        {"faixa": (4664.69, float("inf")), "aliquota": 27.5, "deducao": 860.80} #inf=infinito
    ]
        
class CalculadoraIR():
    def __init__(self, salario_bruto, tabela_ir):#init so no começo para iniciar
        self.salario_bruto = salario_bruto
        self. tabela_ir = tabela_ir

    def calcular(self):
        impsoto = 0
        for faixa in self. tabela_ir.tabela
          