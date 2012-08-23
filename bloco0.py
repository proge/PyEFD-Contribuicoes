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

from Registro import Registro, RegistroX001
from RegistroX990 import RegistroX990
from bloco1 import Registro1001, Registro1990
from bloco9 import Registro9990
from blocoA import RegistroA001, RegistroA990
from blocoC import RegistroC001, RegistroC990
from blocoD import RegistroD001, RegistroD990
from blocoF import RegistroF001, RegistroF990
from blocoM import RegistroM001, RegistroM990
from blocoP import RegistroP001, RegistroP990
from util import Ocorrencia, Obrigatoriedade

'''Registro 0001. Abertura do bloco 0.'''
class Registro0001(RegistroX001):

    def __init__(self):
        super(Registro0001, self).__init__()
        self.REG_PAI = "0000"
        self.REG = "0001"
        self.nivel = 1
        self.ocorrencia = Ocorrencia.UM
        self.obrigatoriedade = Obrigatoriedade.O
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((self.REG, self.IND_MOV))
        return linha + super(Registro0001, self).gerar_linha()

'''Registro 0990. Encerramento do Bloco 0.'''
class Registro0990(RegistroX990):

    def __init__(self):
        super(Registro0990, self).__init__()
        self.REG_PAI = "0000"
        self.REG = "0990"
        self.nivel = 1
        self.ocorrencia = Ocorrencia.UM
        self.obrigatoriedade = Obrigatoriedade.O

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((self.REG, self.QTD_LIN))
        return linha + super(Registro0990, self).gerar_linha()

'''
Registro 0000. 
Abertura do arquivo digital e identificacao da pessoa juridica.
'''
class Registro0000(Registro):

    # -- Registros de abertura e encerramento de bloco --

    # Bloco 0
    registro0001 = Registro0001()
    registro0990 = Registro0990()

    # Bloco A
    registroA001 = RegistroA001()
    registroA990 = RegistroA990()

    # Bloco C
    registroC001 = RegistroC001()
    registroC990 = RegistroC990()

    # Bloco D
    registroD001 = RegistroD001()
    registroD990 = RegistroD990()

    # Bloco F
    registroF001 = RegistroF001()
    registroF990 = RegistroF990()

    # Bloco M
    registroM001 = RegistroM001()
    registroM990 = RegistroM990()

    # Bloco P
    registroP001 = RegistroP001()
    registroP990 = RegistroP990()

    # Bloco 1
    registro1001 = Registro1001()
    registro1990 = Registro1990()

    # Bloco 9
    registro9001 = Registro.get_registro9001_static()
    registro9990 = Registro9990()


    def __init__(self):
        self.REG_PAI = "ROOT"
        self.REG = "0000"
        self.COD_VER = "002"
        self.TIPO_ESCRIT = "0"
        self.IND_SIT_ESP = ""
        self.NUM_REC_ANTERIOR = ""
        self.DT_INI = "01012011"
        self.DT_FIN = "31012011"
        self.NOME = "EMPRESA"
        self.CNPJ = "22222222000191"
        self.UF = "SP"
        self.COD_MUN = "3513801"
        self.SUFRAMA = ""
        self.IND_NAT_PJ = "00"
        self.IND_ATIV = "0"
        self.nivel = 0
        self.ocorrencia = Ocorrencia.UM
        self.obrigatoriedade = Obrigatoriedade.O
        self.registros_filhos = []
        self.adicionarTodosRegistrosDeAberturaEncerramentoDeBloco()

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_VER,
            self.TIPO_ESCRIT,
            self.IND_SIT_ESP,
            self.NUM_REC_ANTERIOR,
            self.DT_INI,
            self.DT_FIN,
            self.NOME,
            self.CNPJ,
            self.UF,
            self.COD_MUN,
            self.SUFRAMA,
            self.IND_NAT_PJ,
            self.IND_ATIV,
            ))
        return linha + super(Registro0000, self).gerar_linha()

    def add_registro_filho(self, registro):
        if isinstance(registro, RegistroX001) or isinstance(registro, RegistroX990):
            raise Exception('''Nao e permitido adicionar registros de abertura 
                    ou encerramento no registro 0000 !\nEsses registros serao 
                    criados e adicionados automaticamente !''')

        super(Registro0000, self).add_registro_filho(self.registro)

    def adicionarTodosRegistrosDeAberturaEncerramentoDeBloco(self):
        # Bloco 0
        super(Registro0000, self).add_registro_filho(self.registro0001)
        super(Registro0000, self).add_registro_filho(self.registro0990)
        # Bloco A
        super(Registro0000, self).add_registro_filho(self.registroA001)
        super(Registro0000, self).add_registro_filho(self.registroA990)
        # Bloco C
        super(Registro0000, self).add_registro_filho(self.registroC001)
        super(Registro0000, self).add_registro_filho(self.registroC990)
        # Bloco D
        super(Registro0000, self).add_registro_filho(self.registroD001)
        super(Registro0000, self).add_registro_filho(self.registroD990)
        # Bloco F
        super(Registro0000, self).add_registro_filho(self.registroF001)
        super(Registro0000, self).add_registro_filho(self.registroF990)
        # Bloco M
        super(Registro0000, self).add_registro_filho(self.registroM001)
        super(Registro0000, self).add_registro_filho(self.registroM990)
        # Bloco P
        super(Registro0000, self).add_registro_filho(self.registroP001)
        super(Registro0000, self).add_registro_filho(self.registroP990)
        # Bloco 1
        super(Registro0000, self).add_registro_filho(self.registro1001)
        super(Registro0000, self).add_registro_filho(self.registro1990)
        # Bloco 9
        super(Registro0000, self).add_registro_filho(self.registro9001)
        super(Registro0000, self).add_registro_filho(self.registro9990)


    def atualizar_quantidade_nos_registros_de_encerramento_de_bloco(self):
        # Registro0000 + Registro0001 + demais registros
        self.registro0990.QTD_LIN = \
                str(self.registro0001.get_quantidade_total_de_registros() + 2)

        self.registroA990.QTD_LIN = \
                str(self.registroA001.get_quantidade_total_de_registros() + 1)

        self.registroC990.QTD_LIN = \
                str(self.registroC001.get_quantidade_total_de_registros() + 1)

        self.registroD990.QTD_LIN = \
                str(self.registroD001.get_quantidade_total_de_registros() + 1)

        self.registroF990.QTD_LIN = \
                str(self.registroF001.get_quantidade_total_de_registros() + 1)

        self.registroM990.QTD_LIN = \
                str(self.registroM001.get_quantidade_total_de_registros() + 1)

        self.registro1990.QTD_LIN = \
                str(self.registro1001.get_quantidade_total_de_registros() + 1)

        # Registro9999 + Registro9001 + demais registros
        self.registro9990.QTD_LIN = \
                str(self.registro9001.get_quantidade_total_de_registros() + 2)


'''Registro 0100. Dados do contabilista.'''
class Registro0100(Registro):

    def __init__(self):
        self.REG_PAI = "0001"
        self.REG = "0100"
        self.NOME = "NOME DO CONTADOR"
        self.CPF = "84898524729"; # Gerado pelo http:# www.geradorcpf.com/
        self.CRC = "1SP123456/0-7"
        self.CNPJ = ""
        self.CEP = "00000000"
        self.END = "RUA XXX"
        self.NUM = "99"
        self.COMPL = "SALA 99"
        self.BAIRRO = "BAIRRO"
        self.FONE = "9912345678"
        self.FAX = "9912346789"
        self.EMAIL = "contador@empresa.com.br"
        self.COD_MUN = "3550308"
        self.nivel = 2
        self.ocorrencia = Ocorrencia.VARIOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.NOME,
            self.CPF,
            self.CRC,
            self.CNPJ,
            self.CEP,
            self.END,
            self.NUM,
            self.COMPL,
            self.BAIRRO,
            self.FONE,
            self.FAX,
            self.EMAIL,
            self.COD_MUN,
            ))
        return linha + super(Registro0100, self).gerar_linha()

'''
Regimes de apuracao da contribuicao social e de apropriacao de credito.
'''
class Registro0110(Registro):

    def __init__(self):
        self.REG_PAI = "0001"
        self.REG = "0110"
        self.COD_INC_TRIB = "1"
        self.IND_APRO_CRED = "1"
        self.COD_TIPO_CONT = "1"
        self.nivel = 2
        self.ocorrencia = Ocorrencia.UM
        self.obrigatoriedade = Obrigatoriedade.O
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_INC_TRIB,
            self.IND_APRO_CRED,
            self.COD_TIPO_CONT,
            ))
        return linha + super(Registro0110, self).gerar_linha()


'''Registro 0140. Tabela de cadastro de estabelecimento.'''
class Registro0140(Registro):

    def __init__(self):
        self.REG_PAI = "0001"
        self.REG = "0140"
        self.COD_EST = "1"
        self.NOME = "EMPRESA"
        self.CNPJ = "22222222000191"
        self.UF = "SP"
        self.IE = ""
        self.COD_MUN = "3513801"
        self.IM = ""
        self.SUFRAMA = ""
        self.nivel = 2
        self.ocorrencia = Ocorrencia.VARIOS
        self.obrigatoriedade = Obrigatoriedade.O
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_EST,
            self.NOME,
            self.CNPJ,
            self.UF,
            self.IE,
            self.COD_MUN,
            self.IM,
            self.SUFRAMA,
            ))
        return linha + super(Registro0140, self).gerar_linha()


'''Regime de Apuração da Contribuição Previdenciária sobre a Receita Bruta'''
class Registro0145(Registro):

    def __init__(self):
        self.REG_PAI = "0140"
        self.REG = "0145"
        self.COD_INC_TRIB = ''
        self.VL_REC_TOT = ''
        self.VL_REC_ATIV = ''
        self.VL_REC_DEMAIS_ATIV = ''
        self.INFO_COMPL = ''
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_UM
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_INC_TRIB,
            self.VL_REC_TOT,
            self.VL_REC_ATIV,
            self.VL_REC_DEMAIS_ATIV,
            self.INFO_COMPL,
            ))
        return linha + super(Registro0145, self).gerar_linha()


'''Registro 0150. Tabela de cadastro do participante.'''
class Registro0150(Registro):

    def __init__(self):
        self.REG_PAI = "0140"
        self.REG = "0150"
        self.COD_PART = "122"
        self.NOME = "FORNECEDOR TESTE"
        self.COD_PAIS = "01058"
        self.CNPJ = "22222222000191"
        self.CPF = ""
        self.IE = ""
        self.COD_MUN = "3513801"
        self.SUFRAMA = ""
        self.END = "SP"
        self.NUM = "99"
        self.COMPL = ""
        self.BAIRRO = "BAIRRO"
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_PART,
            self.NOME,
            self.COD_PAIS,
            self.CNPJ,
            self.CPF,
            self.IE,
            self.COD_MUN,
            self.SUFRAMA,
            self.END,
            self.NUM,
            self.COMPL,
            self.BAIRRO,
            ))
        return linha + super(Registro0150, self).gerar_linha()


'''Registro 0190. Identificacao das unidades de medida.'''
class Registro0190(Registro):

    def __init__(self):
        self.REG_PAI = "0140"
        self.REG = "0190"
        self.UNID = "UN"
        self.DESC = "UNIDADE"
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.UNID,
            self.DESC,
            ))
        return linha + super(Registro0190, self).gerar_linha()


'''Registro 0200. Tabela de identificacao do item (Produtos e Servicos).'''
class Registro0200(Registro):

    def __init__(self):
        self.REG_PAI = "0140"
        self.REG = "0200"
        self.COD_ITEM = "1"
        self.DESCR_ITEM = "PRODUTO TESTE"
        self.COD_BARRA = ""
        self.COD_ANT_ITEM = ""
        self.UNID_INV = "UN"
        self.TIPO_ITEM = "00"
        self.COD_NCM = "61000000" # Pelo visto, e obrigatorio conforme o TIPO_ITEM
        self.EX_IPI = ""
        self.COD_GEN = "61"
        self.COD_LST = ""
        self.ALIQ_ICMS = "18,00"
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_ITEM,
            self.DESCR_ITEM,
            self.COD_BARRA,
            self.COD_ANT_ITEM,
            self.UNID_INV,
            self.TIPO_ITEM,
            self.COD_NCM,
            self.EX_IPI,
            self.COD_GEN,
            self.COD_LST,
            self.ALIQ_ICMS,
            ))
        return linha + super(Registro0200, self).gerar_linha()

'''Registro 0205. Alteracao do item.'''
class Registro0205(Registro):

    def __init__(self):
        self.REG_PAI = "0200"
        self.REG = "0205"
        self.DESCR_ANT_ITEM = ""
        self.DT_INI = ""
        self.DT_FIM = ""
        self.COD_ANT_ITEM = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.DESCR_ANT_ITEM,
            self.DT_INI,
            self.DT_FIM,
            self.COD_ANT_ITEM,
            ))
        return linha + super(Registro0205, self).gerar_linha()


'''Registro 0206. Codigo de produto conforme tabela ANP (combustiveis).'''
class Registro0206(Registro):

    def __init__(self):
        self.REG_PAI = "0200"
        self.REG = "0206"
        self.COD_COMB = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_UM
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((self.REG, self.COD_COMB))
        return linha + super(Registro0206, self).gerar_linha()


'''Registro 0208. Codigo de grupos por marca comercial - refri (bebidas frias).'''
class Registro0208(Registro):

    def __init__(self):
        self.REG_PAI = "0200"
        self.REG = "0208"
        self.COD_TAB = ""
        self.COD_GRU = ""
        self.MARCA_COM = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_UM
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_TAB,
            self.COD_GRU,
            self.MARCA_COM,
            ))
        return linha + super(Registro0208, self).gerar_linha()

'''Registro 0400. Tabela de natureza da operacao/prestacao'''
class Registro0400(Registro):

    def __init__(self):
        self.REG_PAI = "0140"
        self.REG = "0400"
        self.COD_NAT = "1403"
        self.DESCR_NAT = "VENDA"
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_NAT,
            self.DESCR_NAT,
            ))
        return linha + super(Registro0400, self).gerar_linha()


'''Registro 0450. Tabela de informacao complementar do documento fiscal.'''
class Registro0450(Registro):

    def __init__(self):
        self.REG_PAI = "0140"
        self.REG = "0450"
        self.COD_INF = ""
        self.TXT = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.COD_INF,
            self.TXT,
            ))
        return linha + super(Registro0450, self).gerar_linha()


'''Registro 0500. Plano de contas contabeis.'''
class Registro0500(Registro):

    def __init__(self):
        self.REG_PAI = "0001"
        self.REG = "0500"
        self.DT_ALT = ""
        self.COD_NAT_CC = ""
        self.IND_CTA = ""
        self.NIVEL = ""
        self.COD_CTA = ""
        self.NOME_CTA = ""
        self.COD_CTA_REF = ""
        self.CNPJ_EST = ""
        self.nivel = 2
        self.ocorrencia = Ocorrencia.VARIOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.DT_ALT,
            self.COD_NAT_CC,
            self.IND_CTA,
            self.NIVEL,
            self.COD_CTA,
            self.NOME_CTA,
            self.COD_CTA_REF,
            self.CNPJ_EST,
            ))
        return linha + super(Registro0500, self).gerar_linha()


'''Registro 0600. Centro de custos'''
class Registro0600(Registro):

    def __init__(self):
        self.REG_PAI = "0001"
        self.REG = "0600"
        self.DT_ALT = ""
        self.COD_CCUS = ""
        self.CCUS = ""
        self.nivel = 2
        self.ocorrencia = Ocorrencia.VARIOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.DT_ALT,
            self.COD_CCUS,
            self.CCUS,
            ))
        return linha + super(Registro0600, self).gerar_linha()

