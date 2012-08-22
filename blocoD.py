# -*- coding: iso-8859-1 -*-

##############################################################################
#                                                                            #
#  Copyright (C) 2012 Proge Informática Ltda (<http://www.proge.com.br>).    #
#                                                                            #
#  Author Daniel Hartmann <daniel@proge.com.br>                              #
#                                                                            #
#  This program is free software: you can redistribute it and/or modify      #
#  it under the terms of the GNU Affero General Public License as            #
#  published by the Free Software Foundation, either version 3 of the        #
#  License, or (at your option) any later version.                           #
#                                                                            #
#  This program is distributed in the hope that it will be useful,           #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of            #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
#  GNU Affero General Public License for more details.                       #
#                                                                            #
#  You should have received a copy of the GNU Affero General Public License  #
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.     #
#                                                                            #
##############################################################################

from Registro import RegistroX001
from RegistroX990 import RegistroX990
from bloco9 import Registro
from util import Ocorrencia, Obrigatoriedade

'''Registro D001. Abertura do bloco D.'''
class RegistroD001(RegistroX001):

    def __init__(self):
        RegistroX001.__init__(self)
        self.REG_PAI = "0000"
        self.REG = "D001"
        self.nivel = 1
        self.ocorrencia = Ocorrencia.UM
        self.obrigatoriedade = Obrigatoriedade.O
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((self.REG, self.IND_MOV))
        return linha + super(RegistroD001, self).gerar_linha()


'''Registro D010. Identificacao do estabelecimento.@since 1.00.00 (15/03/2011 14:18)
 '''
class RegistroD010(Registro):

    def __init__(self):
        self.REG_PAI = "D001"
        self.REG = "D010"
        self.CNPJ = ""
        self.nivel = 2
        self.ocorrencia = Ocorrencia.VARIOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((self.REG, self.CNPJ))
        return linha + super(RegistroD010, self).gerar_linha()


'''
Registro D100. Aquisiscao de servicos de transporte - Nota fiscal de servico de 
transporte(codigo 07) e conhecimentos de transporte rodoviario de cargas (codigo
08),Conhecimento de transporte de cargas avulso (codigo 8B), aquaviario de 
cargas (codigo 09), aereo (codigo 10), ferroviario de cargas (codigo 11), 
multimodal de cargas (codigo 26), nota fiscal de transporte ferroviario decarga
(codigo 27) e conhecimento de transporte eletronico - CT-e (codigo 57).
 '''
class RegistroD100(Registro):

    def __init__(self):
        self.REG_PAI = "D010"
        self.REG = "D100"
        self.IND_OPER = ""
        self.IND_EMIT = ""
        self.COD_PART = ""
        self.COD_MOD = ""
        self.COD_SIT = ""
        self.SER = ""
        self.SUB = ""
        self.NUM_DOC = ""
        self.CHV_CTE = ""
        self.DT_DOC = ""
        self.DT_A_P = ""
        self.TP_CTE = ""
        self.CHV_CTE_REF = ""
        self.VL_DOC = ""
        self.VL_DESC = ""
        self.IND_FRT = ""
        self.VL_SERV = ""
        self.VL_BC_ICMS = ""
        self.VL_ICMS = ""
        self.VL_NT = ""
        self.COD_INF = ""
        self.COD_CTA = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.IND_OPER,
            self.IND_EMIT,
            self.COD_PART,
            self.COD_MOD,
            self.COD_SIT,
            self.SER,
            self.SUB,
            self.NUM_DOC,
            self.CHV_CTE,
            self.DT_DOC,
            self.DT_A_P,
            self.TP_CTE,
            self.CHV_CTE_REF,
            self.VL_DOC,
            self.VL_DESC,
            self.IND_FRT,
            self.VL_SERV,
            self.VL_BC_ICMS,
            self.VL_ICMS,
            self.VL_NT,
            self.COD_INF,
            self.COD_CTA,
            ))
        return linha + super(RegistroD100, self).gerar_linha()


'''
Registro D101. Complemento do documento de transporte (Codigos 07, 08, 8B, 09, 
10, 11, 26, 27 e 57) - PIS/PASEP.
'''
class RegistroD101(Registro):

    def __init__(self):
        self.REG_PAI = "D100"
        self.REG = "D101"
        self.IND_NAT_FRT = ""
        self.VL_ITEM = ""
        self.CST_PIS = ""
        self.NAT_BC_CRED = ""
        self.VL_BC_PIS = ""
        self.ALIQ_PIS = ""
        self.VL_PIS = ""
        self.COD_CTA = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.IND_NAT_FRT,
            self.VL_ITEM,
            self.CST_PIS,
            self.NAT_BC_CRED,
            self.VL_BC_PIS,
            self.ALIQ_PIS,
            self.VL_PIS,
            self.COD_CTA,
            ))
        return linha + super(RegistroD101, self).gerar_linha()


'''
Registro D105. Complemento do documento de transporte (Codigos 07, 08, 8B, 09,
10, 11, 26, 27 e 57) - Cofins.
'''
class RegistroD105(Registro):

    def __init__(self):
        self.REG_PAI = "D100"
        self.REG = "D105"
        self.IND_NAT_FRT = ""
        self.VL_ITEM = ""
        self.CST_COFINS = ""
        self.NAT_BC_CRED = ""
        self.VL_BC_COFINS = ""
        self.ALIQ_COFINS = ""
        self.VL_COFINS = ""
        self.COD_CTA = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.IND_NAT_FRT,
            self.VL_ITEM,
            self.CST_COFINS,
            self.NAT_BC_CRED,
            self.VL_BC_COFINS,
            self.ALIQ_COFINS,
            self.VL_COFINS,
            self.COD_CTA,
            ))
        return linha + super(RegistroD105, self).gerar_linha()


'''Registro D111. Processo referenciado.'''
class RegistroD111(Registro):

    def __init__(self):
        self.REG_PAI = "D100"
        self.REG = "D111"
        self.NUM_PROC = ""
        self.IND_PROC = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.NUM_PROC,
            self.IND_PROC,
            ))
        return linha + super(RegistroD111, self).gerar_linha()


'''
Registro D200. Resumo da escritura diaria - prestacao de servicos de transporte
Notafiscal de servico de transporte (codigo 07) e conhecimentos de transporte
rodoviario de cargas (codigo 08), Conhecimento de transporte de cargas avulso
(codigo 8B), aquaviario de cargas (codigo 09), aereo (codigo 10), ferroviario de
carga (codigo 27) e conhecimento de tranporte eletronico - CT-e (codigo 57).
'''
class RegistroD200(Registro):

    def __init__(self):
        self.REG_PAI = "D010"
        self.REG = "D200"
        self.COD_MOD = ""
        self.COD_SIT = ""
        self.SER = ""
        self.NUM_DOC_INI = ""
        self.NUM_DOC_FIN = ""
        self.CFOP = ""
        self.DT_REF = ""
        self.VL_DOC = ""
        self.VL_DESC = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_MOD,
            self.COD_SIT,
            self.SER,
            self.NUM_DOC_INI,
            self.NUM_DOC_FIN,
            self.CFOP,
            self.DT_REF,
            self.VL_DOC,
            self.VL_DESC,
            ))
        return linha + super(RegistroD200, self).gerar_linha()


'''Registro D201. Totalizacao do resumo diario - PIS/PASEP.'''
class RegistroD201(Registro):

    def __init__(self):
        self.REG_PAI = "D200"
        self.REG = "D201"
        self.CST_PIS = ""
        self.VL_ITEM = ""
        self.VL_BC_PIS = ""
        self.ALIQ_PIS = ""
        self.VL_PIS = ""
        self.COD_CTA = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.CST_PIS,
            self.VL_ITEM,
            self.VL_BC_PIS,
            self.ALIQ_PIS,
            self.VL_PIS,
            self.COD_CTA,
            ))
        return linha + super(RegistroD201, self).gerar_linha()


'''Registro D205. Totalizacao do resumo diario - Cofins.'''
class RegistroD205(Registro):

    def __init__(self):
        self.REG_PAI = "D200"
        self.REG = "D205"
        self.CST_COFINS = ""
        self.VL_ITEM = ""
        self.VL_BC_COFINS = ""
        self.ALIQ_COFINS = ""
        self.VL_COFINS = ""
        self.COD_CTA = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.CST_COFINS,
            self.VL_ITEM,
            self.VL_BC_COFINS,
            self.ALIQ_COFINS,
            self.VL_COFINS,
            self.COD_CTA,
            ))
        return linha + super(RegistroD205, self).gerar_linha()


'''Registro D209. Processo referenciado.'''
class RegistroD209(Registro):

    def __init__(self):
        self.REG_PAI = "D200"
        self.REG = "D209"
        self.NUM_PROC = ""
        self.IND_PROC = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.NUM_PROC,
            self.IND_PROC,
            ))
        return linha + super(RegistroD209, self).gerar_linha()


'''
Registro D300. Resumo da escrituracao diaria - Bilhetes consolidados de passagem
rodoviario (codigo 13), de passagem aquaviario (codigo 14), de passagem e nota
de bagagem (codigo 15) e de passagem ferroviario (codigo 16).
'''
class RegistroD300(Registro):

    def __init__(self):
        self.REG_PAI = "D010"
        self.REG = "D300"
        self.COD_MOD = ""
        self.SER = ""
        self.SUB = ""
        self.NUM_DOC_INI = ""
        self.NUM_DOC_FIN = ""
        self.CFOP = ""
        self.DT_REF = ""
        self.VL_DOC = ""
        self.VL_DESC = ""
        self.CST_PIS = ""
        self.VL_BC_PIS = ""
        self.ALIQ_PIS = ""
        self.VL_PIS = ""
        self.CST_COFINS = ""
        self.VL_BC_COFINS = ""
        self.ALIQ_COFINS = ""
        self.VL_COFINS = ""
        self.COD_CTA = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_MOD,
            self.SER,
            self.SUB,
            self.NUM_DOC_INI,
            self.NUM_DOC_FIN,
            self.CFOP,
            self.DT_REF,
            self.VL_DOC,
            self.VL_DESC,
            self.CST_PIS,
            self.VL_BC_PIS,
            self.ALIQ_PIS,
            self.VL_PIS,
            self.CST_COFINS,
            self.VL_BC_COFINS,
            self.ALIQ_COFINS,
            self.VL_COFINS,
            self.COD_CTA,
            ))
        return linha + super(RegistroD300, self).gerar_linha()


'''Registro D309. Processo referenciado.@since 1.00.00 (21/03/2011 11:04)
 '''
class RegistroD309(Registro):

    def __init__(self):
        self.REG_PAI = "D300"
        self.REG = "D309"
        self.NUM_PROC = ""
        self.IND_PROC = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.NUM_PROC,
            self.IND_PROC,
            ))
        return linha + super(RegistroD309, self).gerar_linha()


'''
Registro D350. Resumo diario de cupom fiscal emitido por ECF - (codigos 2E, 13, 
14, 15, e 16).
'''
class RegistroD350(Registro):

    def __init__(self):
        self.REG_PAI = "D010"
        self.REG = "D350"
        self.COD_MOD = ""
        self.ECF_MOD = ""
        self.ECF_FAB = ""
        self.DT_DOC = ""
        self.CRO = ""
        self.CRZ = ""
        self.NUM_COO_FIN = ""
        self.GT_FIN = ""
        self.VL_BRT = ""
        self.CST_PIS = ""
        self.VL_BC_PIS = ""
        self.ALIQ_PIS = ""
        self.QUANT_BC_PIS = ""
        self.ALIQ_PIS_QUANT = ""
        self.VL_PIS = ""
        self.CST_COFINS = ""
        self.VL_BC_COFINS = ""
        self.ALIQ_COFINS = ""
        self.QUANT_BC_COFINS = ""
        self.ALIQ_COFINS_QUANT = ""
        self.VL_COFINS = ""
        self.COD_CTA = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_MOD,
            self.ECF_MOD,
            self.ECF_FAB,
            self.DT_DOC,
            self.CRO,
            self.CRZ,
            self.NUM_COO_FIN,
            self.GT_FIN,
            self.VL_BRT,
            self.CST_PIS,
            self.VL_BC_PIS,
            self.ALIQ_PIS,
            self.QUANT_BC_PIS,
            self.ALIQ_PIS_QUANT,
            self.VL_PIS,
            self.CST_COFINS,
            self.VL_BC_COFINS,
            self.ALIQ_COFINS,
            self.QUANT_BC_COFINS,
            self.ALIQ_COFINS_QUANT,
            self.VL_COFINS,
            self.COD_CTA,
            ))
        return linha + super(RegistroD350, self).gerar_linha()


'''Registro D359. Processo referenciado.'''
class RegistroD359(Registro):

    def __init__(self):
        self.REG_PAI = "D350"
        self.REG = "D359"
        self.NUM_PROC = ""
        self.IND_PROC = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.NUM_PROC,
            self.IND_PROC,
            ))
        return linha + super(RegistroD359, self).gerar_linha()




'''
Registro D500Nota fiscal de servico de comunicacao (codigo 21) e nota fiscal de
servico de telecomunicacao (codigo 22) - documentos de aquisicao com direito a
credito.
'''
class RegistroD500(Registro):

    def __init__(self):
        self.REG_PAI = "D010"
        self.REG = "D500"
        self.IND_OPER = ""
        self.IND_EMIT = ""
        self.COD_PART = ""
        self.COD_MOD = ""
        self.COD_SIT = ""
        self.SER = ""
        self.SUB = ""
        self.NUM_DOC = ""
        self.DT_DOC = ""
        self.DT_A_P = ""
        self.VL_DOC = ""
        self.VL_DESC = ""
        self.VL_SERV = ""
        self.VL_SERV_NT = ""
        self.VL_TERC = ""
        self.VL_DA = ""
        self.VL_BC_ICMS = ""
        self.VL_ICMS = ""
        self.COD_INF = ""
        self.VL_PIS = ""
        self.VL_COFINS = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.IND_OPER,
            self.IND_EMIT,
            self.COD_PART,
            self.COD_MOD,
            self.COD_SIT,
            self.SER,
            self.SUB,
            self.NUM_DOC,
            self.DT_DOC,
            self.DT_A_P,
            self.VL_DOC,
            self.VL_DESC,
            self.VL_SERV,
            self.VL_SERV_NT,
            self.VL_TERC,
            self.VL_DA,
            self.VL_BC_ICMS,
            self.VL_ICMS,
            self.COD_INF,
            self.VL_PIS,
            self.VL_COFINS,
            ))
        return linha + super(RegistroD500, self).gerar_linha()



'''Registro D501Complemento da operacao (codigos 21 e 22) - PIS/PASEP.'''
class RegistroD501(Registro):

    def __init__(self):
        self.REG_PAI = "D500"
        self.REG = "D501"
        self.CST_PIS = ""
        self.VL_ITEM = ""
        self.NAT_BC_CRED = ""
        self.VL_BC_PIS = ""
        self.ALIQ_PIS = ""
        self.VL_PIS = ""
        self.COD_CTA = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.CST_PIS,
            self.VL_ITEM,
            self.NAT_BC_CRED,
            self.VL_BC_PIS,
            self.ALIQ_PIS,
            self.VL_PIS,
            self.COD_CTA,
            ))
        return linha + super(RegistroD501, self).gerar_linha()


'''Registro D505. Complemento da operacao (codigos 21 e 22) - Cofins'''
class RegistroD505(Registro):

    def __init__(self):
        self.REG_PAI = "D500"
        self.REG = "D505"
        self.CST_COFINS = ""
        self.VL_ITEM = ""
        self.NAT_BC_CRED = ""
        self.VL_BC_COFINS = ""
        self.ALIQ_COFINS = ""
        self.VL_COFINS = ""
        self.COD_CTA = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.CST_COFINS,
            self.VL_ITEM,
            self.NAT_BC_CRED,
            self.VL_BC_COFINS,
            self.ALIQ_COFINS,
            self.VL_COFINS,
            self.COD_CTA,
            ))
        return linha + super(RegistroD505, self).gerar_linha()


'''Registro D509.Processo referenciado.'''
class RegistroD509(Registro):

    def __init__(self):
        self.REG_PAI = "D500"
        self.REG = "D509"
        self.NUM_PROC = ""
        self.IND_PROC = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.NUM_PROC,
            self.IND_PROC,
            ))
        return linha + super(RegistroD509, self).gerar_linha()


'''
Registro D600. Consolidacao da prestacao de servicos - Notas de servico de
comunicacao(codigo 21) e de servico de telecomunicacao (codigo 22).
'''
class RegistroD600(Registro):

    def __init__(self):
        self.REG_PAI = "D010"
        self.REG = "D600"
        self.COD_MOD = ""
        self.COD_MUN = ""
        self.SER = ""
        self.SUB = ""
        self.IND_REC = ""
        self.QTD_CONS = ""
        self.DT_DOC_INI = ""
        self.DT_DOC_FIN = ""
        self.VL_DOC = ""
        self.VL_DESC = ""
        self.VL_SERV = ""
        self.VL_SERV_NT = ""
        self.VL_TERC = ""
        self.VL_DA = ""
        self.VL_BC_ICMS = ""
        self.VL_ICMS = ""
        self.VL_PIS = ""
        self.VL_COFINS = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_MOD,
            self.COD_MUN,
            self.SER,
            self.SUB,
            self.IND_REC,
            self.QTD_CONS,
            self.DT_DOC_INI,
            self.DT_DOC_FIN,
            self.VL_DOC,
            self.VL_DESC,
            self.VL_SERV,
            self.VL_SERV_NT,
            self.VL_TERC,
            self.VL_DA,
            self.VL_BC_ICMS,
            self.VL_ICMS,
            self.VL_PIS,
            self.VL_COFINS,
            ))
        return linha + super(RegistroD600, self).gerar_linha()


'''
Registro D601. Complemento da consolidacao da prestacao de servicos (codigos 21
e 22) - PIS/PASEP.
'''
class RegistroD601(Registro):

    def __init__(self):
        self.REG_PAI = "D600"
        self.REG = "D601"
        self.COD_CLASS = ""
        self.VL_ITEM = ""
        self.VL_DESC = ""
        self.CST_PIS = ""
        self.VL_BC_PIS = ""
        self.ALIQ_PIS = ""
        self.VL_PIS = ""
        self.COD_CTA = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_CLASS,
            self.VL_ITEM,
            self.VL_DESC,
            self.CST_PIS,
            self.VL_BC_PIS,
            self.ALIQ_PIS,
            self.VL_PIS,
            self.COD_CTA,
            ))
        return linha + super(RegistroD601, self).gerar_linha()


'''
Registro D605. Complemento da consolidacao da prestacao de servicos (codigos 21
e 22) - Cofins.
'''
class RegistroD605(Registro):

    def __init__(self):
        self.REG_PAI = "D600"
        self.REG = "D605"
        self.COD_CLASS = ""
        self.VL_ITEM = ""
        self.VL_DESC = ""
        self.CST_COFINS = ""
        self.VL_BC_COFINS = ""
        self.ALIQ_COFINS = ""
        self.VL_COFINS = ""
        self.COD_CTA = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_CLASS,
            self.VL_ITEM,
            self.VL_DESC,
            self.CST_COFINS,
            self.VL_BC_COFINS,
            self.ALIQ_COFINS,
            self.VL_COFINS,
            self.COD_CTA,
            ))
        return linha + super(RegistroD605, self).gerar_linha()


'''Registro D609.Processo referenciado.'''
class RegistroD609(Registro):

    def __init__(self):
        self.REG_PAI = "D600"
        self.REG = "D609"
        self.NUM_PROC = ""
        self.IND_PROC = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.NUM_PROC,
            self.IND_PROC,
            ))
        return linha + super(RegistroD609, self).gerar_linha()


'''Registro D990.Encerramento do bloco D.'''
class RegistroD990(RegistroX990):

    def __init__(self):
        RegistroX990.__init__(self)
        self.REG_PAI = "0000"
        self.REG = "D990"
        self.nivel = 1
        self.ocorrencia = Ocorrencia.UM
        self.obrigatoriedade = Obrigatoriedade.O
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((self.REG, self.QTD_LIN))
        return linha + super(RegistroD990, self).gerar_linha()

