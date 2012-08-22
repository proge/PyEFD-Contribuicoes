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

from Registro import RegistroX001, Registro
from RegistroX990 import RegistroX990
from util import Obrigatoriedade, Ocorrencia

'''Registro C001. Abertura do bloco C. (03/03/2011 11:57)'''
class RegistroC001(RegistroX001):

    def __init__(self):
        RegistroX001.__init__(self)
        self.REG_PAI = "0000"
        self.REG = "C001"
        self.nivel = 1
        self.ocorrencia = Ocorrencia.UM
        self.obrigatoriedade = Obrigatoriedade.O
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.IND_MOV,
            ))
        return linha + super(RegistroC001, self).gerar_linha()

'''Registro C010. Identificacao do estabelecimento.'''
class RegistroC010(Registro):

    def __init__(self):
        self.REG_PAI = "C001"
        self.REG = "C010"
        self.CNPJ = "22222222000191"
        self.IND_ESCRI = "2"
        self.nivel = 2
        self.ocorrencia = Ocorrencia.VARIOS
        self.obrigatoriedade = Obrigatoriedade.O_SE
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.CNPJ,
            self.IND_ESCRI,
            ))
        return linha + super(RegistroC010, self).gerar_linha()


'''
Registro C100. 
Documento - Nota Fiscal (Codigo 01), Nota Fiscal Avulsa (Codigo 1B), 
            Nota Fiscal de Produtor (Codigo 04) e NFe (Codigo 55).
'''
class RegistroC100(Registro):

    def __init__(self):
        self.REG_PAI = "C010"
        self.REG = "C100"
        self.IND_OPER = "0"
        self.IND_EMIT = "1"
        self.COD_PART = "122"
        self.COD_MOD = "55"
        self.COD_SIT = "00"
        self.SER = "2"
        self.NUM_DOC = "8038"
        self.CHV_NFE = ""
        self.DT_DOC = "03012011"
        self.DT_E_S = "03012011"
        self.VL_DOC = "316,00"
        self.IND_PGTO = "1"
        self.VL_DESC = "0,00"
        self.VL_ABAT_NT = "0,00"
        self.VL_MERC = "316,00"
        self.IND_FRT = "1"
        self.VL_FRT = "0,00"
        self.VL_SEG = "0,00"
        self.VL_OUT_DA = "0,00"
        self.VL_BC_ICMS = "0,00"
        self.VL_ICMS = "0,00"
        self.VL_BC_ICMS_ST = "316,00"
        self.VL_ICMS_ST = "316,00"
        self.VL_IPI = "0,00"
        self.VL_PIS = "2,61"
        self.VL_COFINS = "12,01"
        self.VL_PIS_ST = "0,00"
        self.VL_COFINS_ST = "0,00"
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.O_SE
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
            self.NUM_DOC,
            self.CHV_NFE,
            self.DT_DOC,
            self.DT_E_S,
            self.VL_DOC,
            self.IND_PGTO,
            self.VL_DESC,
            self.VL_ABAT_NT,
            self.VL_MERC,
            self.IND_FRT,
            self.VL_FRT,
            self.VL_SEG,
            self.VL_OUT_DA,
            self.VL_BC_ICMS,
            self.VL_ICMS,
            self.VL_BC_ICMS_ST,
            self.VL_ICMS_ST,
            self.VL_IPI,
            self.VL_PIS,
            self.VL_COFINS,
            self.VL_PIS_ST,
            self.VL_COFINS_ST,
            ))
        return linha + super(RegistroC100, self).gerar_linha()

'''
Registro C110. Complemento do documento - informacao complementar da nota fiscal
(codigos 01, 1B, 04 e 55). Layout para este registro encontra-se no ATO 
COTEPE/ICMS No 9, DE 18 DE ABRIL DE 2008 
(http://www.fazenda.gov.br/confaz/confaz/atos/atos_cotepe/2008/ac009_08.htm)'''
class RegistroC110(Registro):

    def __init__(self):
        self.REG_PAI = "C100"
        self.REG = "C110"
        self.COD_INF = ""
        self.TXT_COMPL = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_INF,
            self.TXT_COMPL,
            ))
        return linha + super(RegistroC110, self).gerar_linha()

'''Registro C111. Processo referenciado.'''
class RegistroC111(Registro):

    def __init__(self):
        self.REG_PAI = "C100"
        self.REG = "C111"
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
        return linha + super(RegistroC111, self).gerar_linha()


'''
Registro C120. Complemento do documento - operacoes de importacao (codigo 01).
Layout para este registro encontra-se no ATO COTEPE/ICMS No 9, DE 18 DE ABRIL 
DE 2008 
(http://www.fazenda.gov.br/confaz/confaz/atos/atos_cotepe/2008/ac009_08.htm).
'''
class RegistroC120(Registro):

    def __init__(self):
        self.REG_PAI = "C100"
        self.REG = "C120"
        self.COD_DOC_IMP = ""
        self.NUM_DOC_IMP = ""
        self.PIS_IMP = ""
        self.COFINS_IMP = ""
        self.NUM_ACDRAW = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.O_SE
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_DOC_IMP,
            self.NUM_DOC_IMP,
            self.PIS_IMP,
            self.COFINS_IMP,
            self.NUM_ACDRAW,
            ))
        return linha + super(RegistroC120, self).gerar_linha()


'''Registro C170. Complemento do documento - Itens do documento (codigos 01, 1B, 04 e 55). (03/03/2011 11:45)'''
class RegistroC170(Registro):

    def __init__(self):
        self.REG_PAI = "C100"
        self.REG = "C170"
        self.NUM_ITEM = "001"
        self.COD_ITEM = "1"
        self.DESCR_COMPL = ""
        self.QTD = "2,00000"
        self.UNID = "UN"
        self.VL_ITEM = "158,00"
        self.VL_DESC = "0,00"
        self.IND_MOV = "0"
        self.CST_ICMS = "060"
        self.CFOP = "1403"
        self.COD_NAT = "1403"
        self.VL_BC_ICMS = "158,00"
        self.ALIQ_ICMS = "18,00"
        self.VL_ICMS = "31,54"
        self.VL_BC_ICMS_ST = "0,00"
        self.ALIQ_ST = "0,00"
        self.VL_ICMS_ST = "0,00"
        self.IND_APUR = "0"
        self.CST_IPI = "02"
        self.COD_ENQ = ""
        self.VL_BC_IPI = "0,00"
        self.ALIQ_IPI = "0,00"
        self.VL_IPI = "0,00"
        self.CST_PIS = "50"
        self.VL_BC_PIS = "158,00"
        self.ALIQ_PIS_PERC = "1,65"
        self.QUANT_BC_PIS = ""
        self.ALIQ_PIS_REAIS = ""
        self.VL_PIS = "2,61"
        self.CST_COFINS = "50"
        self.VL_BC_COFINS = "158,00"
        self.ALIQ_COFINS_PERC = "7,60"
        self.QUANT_BC_COFINS = ""
        self.ALIQ_COFINS_REAIS = ""
        self.VL_COFINS = "12,01"
        self.COD_CTA = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.O_SE
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.NUM_ITEM,
            self.COD_ITEM,
            self.DESCR_COMPL,
            self.QTD,
            self.UNID,
            self.VL_ITEM,
            self.VL_DESC,
            self.IND_MOV,
            self.CST_ICMS,
            self.CFOP,
            self.COD_NAT,
            self.VL_BC_ICMS,
            self.ALIQ_ICMS,
            self.VL_ICMS,
            self.VL_BC_ICMS_ST,
            self.ALIQ_ST,
            self.VL_ICMS_ST,
            self.IND_APUR,
            self.CST_IPI,
            self.COD_ENQ,
            self.VL_BC_IPI,
            self.ALIQ_IPI,
            self.VL_IPI,
            self.CST_PIS,
            self.VL_BC_PIS,
            self.ALIQ_PIS_PERC,
            self.QUANT_BC_PIS,
            self.ALIQ_PIS_REAIS,
            self.VL_PIS,
            self.CST_COFINS,
            self.VL_BC_COFINS,
            self.ALIQ_COFINS_PERC,
            self.QUANT_BC_COFINS,
            self.ALIQ_COFINS_REAIS,
            self.VL_COFINS,
            self.COD_CTA,
            ))
        return linha + super(RegistroC170, self).gerar_linha()


'''Registro C180. Consolidacao de notas fiscais eletronicas emitidas pela pessoa juridica (codigo 55) - operacoes de vendas. (14/03/2011 11:08)'''
class RegistroC180(Registro):

    def __init__(self):
        self.REG_PAI = "C010"
        self.REG = "C180"
        self.COD_MOD = ""
        self.DT_DOC_INI = ""
        self.DT_DOC_FIN = ""
        self.COD_ITEM = ""
        self.COD_NCM = ""
        self.EX_IPI = ""
        self.VL_TOT_ITEM = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_MOD,
            self.DT_DOC_INI,
            self.DT_DOC_FIN,
            self.COD_ITEM,
            self.COD_NCM,
            self.EX_IPI,
            self.VL_TOT_ITEM,
            ))
        return linha + super(RegistroC180, self).gerar_linha()

'''Registro C181. Detalhamento da consolidacao - operacoes de vendas - PIS/PASEP. (14/03/2011 11:17)'''
class RegistroC181(Registro):

    def __init__(self):
        self.REG_PAI = "C180"
        self.REG = "C181"
        self.CST_PIS = ""
        self.CFOP = ""
        self.VL_ITEM = ""
        self.VL_DESC = ""
        self.VL_BC_PIS = ""
        self.ALIQ_PIS = ""
        self.QUANT_BC_PIS = ""
        self.ALIQ_PIS_QUANT = ""
        self.VL_PIS = ""
        self.COD_CTA = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.O_SE
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.CST_PIS,
            self.CFOP,
            self.VL_ITEM,
            self.VL_DESC,
            self.VL_BC_PIS,
            self.ALIQ_PIS,
            self.QUANT_BC_PIS,
            self.ALIQ_PIS_QUANT,
            self.VL_PIS,
            self.COD_CTA,
            ))
        return linha + super(RegistroC181, self).gerar_linha()

'''Registro C185. Detalhamento da consolidacao - operacoes de vendas - Cofins.'''
class RegistroC185(Registro):

    def __init__(self):
        self.REG_PAI = "C180"
        self.REG = "C185"
        self.CST_COFINS = ""
        self.CFOP = ""
        self.VL_ITEM = ""
        self.VL_DESC = ""
        self.VL_BC_COFINS = ""
        self.ALIQ_COFINS = ""
        self.QUANT_BC_COFINS = ""
        self.ALIQ_COFINS_QUANT = ""
        self.VL_COFINS = ""
        self.COD_CTA = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.O_SE
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.CST_COFINS,
            self.CFOP,
            self.VL_ITEM,
            self.VL_DESC,
            self.VL_BC_COFINS,
            self.ALIQ_COFINS,
            self.QUANT_BC_COFINS,
            self.ALIQ_COFINS_QUANT,
            self.VL_COFINS,
            self.COD_CTA,
            ))
        return linha + super(RegistroC185, self).gerar_linha()

'''Registro C188. Processo referenciado. (14/03/2011 11:28)'''
class RegistroC188(Registro):

    def __init__(self):
        self.REG_PAI = "C180"
        self.REG = "C188"
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
        return linha + super(RegistroC188, self).gerar_linha()


'''Registro C190. Consolidacao de notas fiscais eletronicas (codigo 55) - operacoes de aquisicao com direito a credito, e operacoes de devolucao de compras e vendas. (14/03/2011 11:31)'''
class RegistroC190(Registro):

    def __init__(self):
        self.REG_PAI = "C010"
        self.REG = "C190"
        self.COD_MOD = ""
        self.DT_REF_INI = ""
        self.DT_REF_FIN = ""
        self.COD_ITEM = ""
        self.COD_NCM = ""
        self.EX_IPI = ""
        self.VL_TOT_ITEM = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_MOD,
            self.DT_REF_INI,
            self.DT_REF_FIN,
            self.COD_ITEM,
            self.COD_NCM,
            self.EX_IPI,
            self.VL_TOT_ITEM,
            ))
        return linha + super(RegistroC190, self).gerar_linha()


'''
Registro C191. Detalhamento da consolidacao - operacoes de aquisicao com direito
a credito, e operacoes de devolucao de compras e vendas - PIS/PASEP.
'''
class RegistroC191(Registro):

    def __init__(self):
        self.REG_PAI = "C190"
        self.REG = "C191"
        self.COD_PART = ""
        self.CST_PIS = ""
        self.CFOP = ""
        self.VL_ITEM = ""
        self.VL_DESC = ""
        self.VL_BC_PIS = ""
        self.ALIQ_PIS = ""
        self.QUANT_BC_PIS = ""
        self.ALIQ_PIS_QUANT = ""
        self.VL_PIS = ""
        self.COD_CTA = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.O_SE
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_PART,
            self.CST_PIS,
            self.CFOP,
            self.VL_ITEM,
            self.VL_DESC,
            self.VL_BC_PIS,
            self.ALIQ_PIS,
            self.QUANT_BC_PIS,
            self.ALIQ_PIS_QUANT,
            self.VL_PIS,
            self.COD_CTA,
            ))
        return linha + super(RegistroC191, self).gerar_linha()


'''
Registro C195. Detalhamento da consolidacao - operacoes de aquisicao com direito
a credito, e operacoes de devolucao de compras e vendas - Cofins.
'''
class RegistroC195(Registro):

    def __init__(self):
        self.REG_PAI = "C190"
        self.REG = "C195"
        self.COD_PART = ""
        self.CST_COFINS = ""
        self.CFOP = ""
        self.VL_ITEM = ""
        self.VL_DESC = ""
        self.VL_BC_COFINS = ""
        self.ALIQ_COFINS = ""
        self.QUANT_BC_COFINS = ""
        self.ALIQ_COFINS_QUANT = ""
        self.VL_COFINS = ""
        self.COD_CTA = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.O_SE
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_PART,
            self.CST_COFINS,
            self.CFOP,
            self.VL_ITEM,
            self.VL_DESC,
            self.VL_BC_COFINS,
            self.ALIQ_COFINS,
            self.QUANT_BC_COFINS,
            self.ALIQ_COFINS_QUANT,
            self.VL_COFINS,
            self.COD_CTA,
            ))
        return linha + super(RegistroC195, self).gerar_linha()

'''Registro C198. Processo referenciado.'''
class RegistroC198(Registro):

    def __init__(self):
        self.REG_PAI = "C190"
        self.REG = "C198"
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
        return linha + super(RegistroC198, self).gerar_linha()


'''
Registro C199. Complemento do documento - operacoes de importacao (codigos 55).
'''
class RegistroC199(Registro):

    def __init__(self):
        self.REG_PAI = "C190"
        self.REG = "C199"
        self.COD_DOC_IMP = ""
        self.NUM_DOC_IMP = ""
        self.VL_PIS_IMP = ""
        self.VL_COFINS_IMP = ""
        self.NUM_ACDRAW = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.O_SE
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_DOC_IMP,
            self.NUM_DOC_IMP,
            self.VL_PIS_IMP,
            self.VL_COFINS_IMP,
            self.NUM_ACDRAW,
            ))
        return linha + super(RegistroC199, self).gerar_linha()



'''
Registro C380. Nota fiscal de venda a consumidor (codigo 02) - consolidacao de 
documentos emitidos.
'''
class RegistroC380(Registro):

    def __init__(self):
        self.REG_PAI = "C010"
        self.REG = "C380"
        self.COD_MOD = ""
        self.DT_DOC_INI = ""
        self.DT_DOC_FIN = ""
        self.NUM_DOC_INI = ""
        self.NUM_DOC_FIN = ""
        self.VL_DOC = ""
        self.VL_DOC_CANC = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_MOD,
            self.DT_DOC_INI,
            self.DT_DOC_FIN,
            self.NUM_DOC_INI,
            self.NUM_DOC_FIN,
            self.VL_DOC,
            self.VL_DOC_CANC,
            ))
        return linha + super(RegistroC380, self).gerar_linha()


'''Registro C381. Detalhamento da consolidacao - PIS/PASEP.'''
class RegistroC381(Registro):

    def __init__(self):
        self.REG_PAI = "C380"
        self.REG = "C381"
        self.CST_PIS = ""
        self.COD_ITEM = ""
        self.VL_ITEM = ""
        self.VL_BC_PIS = ""
        self.ALIQ_PIS = ""
        self.QUANT_BC_PIS = ""
        self.ALIQ_PIS_QUANT = ""
        self.VL_PIS = ""
        self.COD_CTA = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.O_SE
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.CST_PIS,
            self.COD_ITEM,
            self.VL_ITEM,
            self.VL_BC_PIS,
            self.ALIQ_PIS,
            self.QUANT_BC_PIS,
            self.ALIQ_PIS_QUANT,
            self.VL_PIS,
            self.COD_CTA,
            ))
        return linha + super(RegistroC381, self).gerar_linha()


'''Registro C385. Detalhamento da consolidacao - Cofins.'''
class RegistroC385(Registro):

    def __init__(self):
        self.REG_PAI = "C380"
        self.REG = "C385"
        self.CST_COFINS = ""
        self.COD_ITEM = ""
        self.VL_ITEM = ""
        self.VL_BC_COFINS = ""
        self.ALIQ_COFINS = ""
        self.QUANT_BC_COFINS = ""
        self.ALIQ_COFINS_QUANT = ""
        self.VL_COFINS = ""
        self.COD_CTA = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.O_SE
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.CST_COFINS,
            self.COD_ITEM,
            self.VL_ITEM,
            self.VL_BC_COFINS,
            self.ALIQ_COFINS,
            self.QUANT_BC_COFINS,
            self.ALIQ_COFINS_QUANT,
            self.VL_COFINS,
            self.COD_CTA,
            ))
        return linha + super(RegistroC385, self).gerar_linha()


'''Registro C395. Notas fiscais de venda a consumidor (codigos 02, 2D, 2E e 59) - aquisicoes/entradas com credito. (14/03/2011 12:02)'''
class RegistroC395(Registro):

    def __init__(self):
        self.REG_PAI = "C010"
        self.REG = "C395"
        self.COD_MOD = ""
        self.COD_PART = ""
        self.SER = ""
        self.SUB_SER = ""
        self.NUM_DOC = ""
        self.DT_DOC = ""
        self.VL_DOC = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_MOD,
            self.COD_PART,
            self.SER,
            self.SUB_SER,
            self.NUM_DOC,
            self.DT_DOC,
            self.VL_DOC,
            ))
        return linha + super(RegistroC395, self).gerar_linha()


'''Registro C396. Itens do documento (codigos 02, 2D, 2E e 59) - aquisicoes/entradas com credito. (14/03/2011 12:04)'''
class RegistroC396(Registro):

    def __init__(self):
        self.REG_PAI = "C395"
        self.REG = "C396"
        self.COD_ITEM = ""
        self.VL_ITEM = ""
        self.VL_DESC = ""
        self.NAT_BC_CRED = ""
        self.CST_PIS = ""
        self.VL_BC_PIS = ""
        self.ALIQ_PIS = ""
        self.VL_PIS = ""
        self.CST_COFINS = ""
        self.VL_BC_COFINS = ""
        self.ALIQ_COFINS = ""
        self.VL_COFINS = ""
        self.COD_CTA = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.O_SE
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_ITEM,
            self.VL_ITEM,
            self.VL_DESC,
            self.NAT_BC_CRED,
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
        return linha + super(RegistroC396, self).gerar_linha()


'''Registro C400. Equipamento ECF (codigos 02 e 2D). (14/03/2011 12:09)'''
class RegistroC400(Registro):

    def __init__(self):
        self.REG_PAI = "C010"
        self.REG = "C400"
        self.COD_MOD = ""
        self.ECF_MOD = ""
        self.ECF_FAB = ""
        self.ECF_CX = ""
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
            self.ECF_CX,
            ))
        return linha + super(RegistroC400, self).gerar_linha()

    def preencher_valores_dos_campos_pela_linha(self, linha):
        valores = linha.split("\\|")
        self.COD_MOD = valores[2]
        self.ECF_MOD = valores[3]
        self.ECF_FAB = valores[4]
        self.ECF_CX = valores[5];


'''Registro C405. Reducao Z (codigos 02 e 2D). (14/03/2011 12:12)'''
class RegistroC405(Registro):

    def __init__(self):
        self.REG_PAI = "C400"
        self.REG = "C405"
        self.DT_DOC = ""
        self.CRO = ""
        self.CRZ = ""
        self.NUM_COO_FIN = ""
        self.GT_FIN = ""
        self.VL_BRT = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.O_SE
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.DT_DOC,
            self.CRO,
            self.CRZ,
            self.NUM_COO_FIN,
            self.GT_FIN,
            self.VL_BRT,
            ))
        return linha + super(RegistroC405, self).gerar_linha()


'''Registro C481. Resumo diario de documentos emitidos por ECF - PIS/PASEP (codigos 02 e 2D). (14/03/2011 12:15)'''
class RegistroC481(Registro):

    def __init__(self):
        self.REG_PAI = "C405"
        self.REG = "C481"
        self.CST_PIS = ""
        self.VL_ITEM = ""
        self.VL_BC_PIS = ""
        self.ALIQ_PIS = ""
        self.QUANT_BC_PIS = ""
        self.ALIQ_PIS_QUANT = ""
        self.VL_PIS = ""
        self.COD_ITEM = ""
        self.COD_CTA = ""
        self.nivel = 5
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
            self.QUANT_BC_PIS,
            self.ALIQ_PIS_QUANT,
            self.VL_PIS,
            self.COD_ITEM,
            self.COD_CTA,
            ))
        return linha + super(RegistroC481, self).gerar_linha()


'''Registro C485. Resumo diario de documentos emitidos por ECF - Cofins (codigos 02 e 2D). (14/03/2011 12:20)'''
class RegistroC485(Registro):

    def __init__(self):
        self.REG_PAI = "C405"
        self.REG = "C485"
        self.CST_COFINS = ""
        self.VL_ITEM = ""
        self.VL_BC_COFINS = ""
        self.ALIQ_COFINS = ""
        self.QUANT_BC_COFINS = ""
        self.ALIQ_COFINS_QUANT = ""
        self.VL_COFINS = ""
        self.COD_ITEM = ""
        self.COD_CTA = ""
        self.nivel = 5
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
            self.QUANT_BC_COFINS,
            self.ALIQ_COFINS_QUANT,
            self.VL_COFINS,
            self.COD_ITEM,
            self.COD_CTA,
            ))
        return linha + super(RegistroC485, self).gerar_linha()


'''Registro C489 Processo referenciado. (14/03/2011 12:22)'''
class RegistroC489(Registro):

    def __init__(self):
        self.REG_PAI = "C400"
        self.REG = "C489"
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
        return linha + super(RegistroC489, self).gerar_linha()


'''Registro C490. Consolidacao de documentos emitidos por ECF (codigos 02, 2D e 59). (14/03/2011 12:24)'''
class RegistroC490(Registro):

    def __init__(self):
        self.REG_PAI = "C010"
        self.REG = "C490"
        self.DT_DOC_INI = ""
        self.DT_DOC_FIN = ""
        self.COD_MOD = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.DT_DOC_INI,
            self.DT_DOC_FIN,
            self.COD_MOD,
            ))
        return linha + super(RegistroC490, self).gerar_linha()



'''
Registro C491. Detalhamento da consolidacao de documentos emitidos por ECF
(codigos 02, 2D e 59) - PIS/PASEP.
'''
class RegistroC491(Registro):

    def __init__(self):
        self.REG_PAI = "C490"
        self.REG = "C491"
        self.COD_ITEM = ""
        self.CST_PIS = ""
        self.CFOP = ""
        self.VL_ITEM = ""
        self.VL_BC_PIS = ""
        self.ALIQ_PIS = ""
        self.QUANT_BC_PIS = ""
        self.ALIQ_PIS_QUANT = ""
        self.VL_PIS = ""
        self.COD_CTA = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_ITEM,
            self.CST_PIS,
            self.CFOP,
            self.VL_ITEM,
            self.VL_BC_PIS,
            self.ALIQ_PIS,
            self.QUANT_BC_PIS,
            self.ALIQ_PIS_QUANT,
            self.VL_PIS,
            self.COD_CTA,
            ))
        return linha + super(RegistroC491, self).gerar_linha()



'''
Registro C495. Detalhamento da consolidacao de documentos emitidos por ECF
(codigos 02, 2D e 59) - Cofins.
'''
class RegistroC495(Registro):

    def __init__(self):
        self.REG_PAI = "C490"
        self.REG = "C495"
        self.COD_ITEM = ""
        self.CST_COFINS = ""
        self.CFOP = ""
        self.VL_ITEM = ""
        self.VL_BC_COFINS = ""
        self.ALIQ_COFINS = ""
        self.QUANT_BC_COFINS = ""
        self.ALIQ_COFINS_QUANT = ""
        self.VL_COFINS = ""
        self.COD_CTA = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_ITEM,
            self.CST_COFINS,
            self.CFOP,
            self.VL_ITEM,
            self.VL_BC_COFINS,
            self.ALIQ_COFINS,
            self.QUANT_BC_COFINS,
            self.ALIQ_COFINS_QUANT,
            self.VL_COFINS,
            self.COD_CTA,
            ))
        return linha + super(RegistroC495, self).gerar_linha()

'''Registro C499. Processo referenciado. (14/03/2011 12:39)'''
class RegistroC499(Registro):

    def __init__(self):
        self.REG_PAI = "C490"
        self.REG = "C499"
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
        return linha + super(RegistroC499, self).gerar_linha()


'''
Registro C500. Nota fiscal/conta de energia eletrica (codigo 06), nota
fiscal/conta de fornecimento d'agua canalizada (codigo 29) e nota fiscal consumo
fornecimento de gas (codigo 28) - documentos de entrada/aquisicao com credito.
'''
class RegistroC500(Registro):

    def __init__(self):
        self.REG_PAI = "C010"
        self.REG = "C500"
        self.COD_PART = ""
        self.COD_MOD = ""
        self.COD_SIT = ""
        self.SER = ""
        self.SUB = ""
        self.NUM_DOC = ""
        self.DT_DOC = ""
        self.DT_ENT = ""
        self.VL_DOC = ""
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
            self.COD_PART,
            self.COD_MOD,
            self.COD_SIT,
            self.SER,
            self.SUB,
            self.NUM_DOC,
            self.DT_DOC,
            self.DT_ENT,
            self.VL_DOC,
            self.VL_ICMS,
            self.COD_INF,
            self.VL_PIS,
            self.VL_COFINS,
            ))
        return linha + super(RegistroC500, self).gerar_linha()



'''Registro C501. Complemento da operacao (codigos 06, 28 e 29) - PIS/PASEP.'''
class RegistroC501(Registro):

    def __init__(self):
        self.REG_PAI = "C500"
        self.REG = "C501"
        self.CST_PIS = ""
        self.VL_ITEM = ""
        self.NAT_BC_CRED = ""
        self.VL_BC_PIS = ""
        self.ALIQ_PIS = ""
        self.VL_PIS = ""
        self.COD_CTA = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.O_SE
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
        return linha + super(RegistroC501, self).gerar_linha()


'''Registro C505. Complemento da operacao (codigos 06, 28 e 29) - Cofins (14/03/2011 12:50)'''
class RegistroC505(Registro):

    def __init__(self):
        self.REG_PAI = "C500"
        self.REG = "C505"
        self.CST_COFINS = ""
        self.VL_ITEM = ""
        self.NAT_BC_CRED = ""
        self.VL_BC_COFINS = ""
        self.ALIQ_COFINS = ""
        self.VL_COFINS = ""
        self.COD_CTA = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.O_SE
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
        return linha + super(RegistroC505, self).gerar_linha()


'''Registro C509. Processo referenciado.'''
class RegistroC509(Registro):

    def __init__(self):
        self.REG_PAI = "C500"
        self.REG = "C509"
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
        return linha + super(RegistroC509, self).gerar_linha()


'''
Registro C600. Consolidacao diaria de notas fiscais/contas emitidas de energia
eletrica (codigo 06), nota fiscal/conta de fornecimento d'agua canalizada
(codigo 29) e nota fiscal/conta de fornecimento de gas (codigo 28) (empresas
obrigadas ou nao ao CONVENIO ICMS 115/03) - documentos de saida.
'''
class RegistroC600(Registro):

    def __init__(self):
        self.REG_PAI = "C010"
        self.REG = "C600"
        self.COD_MOD = ""
        self.COD_MUN = ""
        self.SER = ""
        self.SUB = ""
        self.COD_CONS = ""
        self.QTD_CONS = ""
        self.QTD_CANC = ""
        self.DT_DOC = ""
        self.VL_DOC = ""
        self.VL_DESC = ""
        self.CONS = ""
        self.VL_FORN = ""
        self.VL_SERV_NT = ""
        self.VL_TERC = ""
        self.VL_DA = ""
        self.VL_BC_ICMS = ""
        self.VL_ICMS = ""
        self.VL_BC_ICMS_ST = ""
        self.VL_ICMS_ST = ""
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
            self.COD_CONS,
            self.QTD_CONS,
            self.QTD_CANC,
            self.DT_DOC,
            self.VL_DOC,
            self.VL_DESC,
            self.CONS,
            self.VL_FORN,
            self.VL_SERV_NT,
            self.VL_TERC,
            self.VL_DA,
            self.VL_BC_ICMS,
            self.VL_ICMS,
            self.VL_BC_ICMS_ST,
            self.VL_ICMS_ST,
            self.VL_PIS,
            self.VL_COFINS,
            ))
        return linha + super(RegistroC600, self).gerar_linha()

'''Registro C601. Complemento da consolidacao diaria (codigos 06, 28 e 29) - documentos de saidas - PIS/PASEP. '''
class RegistroC601(Registro):

    def __init__(self):
        self.REG_PAI = "C600"
        self.REG = "C601"
        self.CST_PIS = ""
        self.VL_ITEM = ""
        self.VL_BC_PIS = ""
        self.ALIQ_PIS = ""
        self.VL_PIS = ""
        self.COD_CTA = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.O_SE
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
        return linha + super(RegistroC601, self).gerar_linha()


'''Registro C605. Complemento da consolidacao diaria (codigos 06, 28 e 29) - documentos de saidas - Cofins. '''
class RegistroC605(Registro):

    def __init__(self):
        self.REG_PAI = "C600"
        self.REG = "C605"
        self.CST_COFINS = ""
        self.VL_ITEM = ""
        self.VL_BC_COFINS = ""
        self.ALIQ_COFINS = ""
        self.VL_COFINS = ""
        self.COD_CTA = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.O_SE
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
        return linha + super(RegistroC605, self).gerar_linha()

'''Registro C609. Processo referenciado.'''
class RegistroC609(Registro):

    def __init__(self):
        self.REG_PAI = "C600"
        self.REG = "C609"
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
        return linha + super(RegistroC609, self).gerar_linha()



'''Registro C990. Encerramento do bloco C.'''
class RegistroC990(RegistroX990):

    def __init__(self):
        RegistroX990.__init__(self)
        self.REG_PAI = "0000"
        self.REG = "C990"
        self.nivel = 1
        self.ocorrencia = Ocorrencia.UM
        self.obrigatoriedade = Obrigatoriedade.O
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((self.REG, self.QTD_LIN))
        return linha + super(RegistroC990, self).gerar_linha()


