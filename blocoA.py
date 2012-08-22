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
from util import Ocorrencia, Obrigatoriedade

'''Registro A001. Abertura do bloco A.'''
class RegistroA001(RegistroX001):

    def __init__(self):
        RegistroX001.__init__(self)
        self.REG_PAI = "0000"
        self.REG = "A001"
        self.nivel = 1
        self.ocorrencia = Ocorrencia.UM
        self.obrigatoriedade = Obrigatoriedade.O
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.IND_MOV,
            ))
        return linha + super(RegistroA001, self).gerar_linha()



'''Registro A010. Identificacao do estabelecimento.'''
class RegistroA010(Registro):

    def __init__(self):
        self.REG_PAI = "A001"
        self.REG = "A010"
        self.CNPJ = ""
        self.nivel = 2
        self.ocorrencia = Ocorrencia.VARIOS
        self.obrigatoriedade = Obrigatoriedade.O_SE
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.CNPJ,
            ))
        return linha + super(RegistroA010, self).gerar_linha()


'''Registro A100. Documento - nota fiscal de servico.'''
class RegistroA100(Registro):

    def __init__(self):
        self.REG_PAI = "A010"
        self.REG = "A100"
        self.IND_OPER = ""
        self.IND_EMIT = ""
        self.COD_PART = ""
        self.COD_SIT = ""
        self.SER = ""
        self.SUB = ""
        self.NUM_DOC = ""
        self.CHV_NFSE = ""
        self.DT_DOC = ""
        self.DT_EXE_SERV = ""
        self.VL_DOC = ""
        self.IND_PGTO = ""
        self.VL_DESC = ""
        self.VL_BC_PIS = ""
        self.VL_PIS = ""
        self.VL_BC_COFINS = ""
        self.VL_COFINS = ""
        self.VL_PIS_RET = ""
        self.VL_COFINS_RET = ""
        self.VL_ISS = ""
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
            self.COD_SIT,
            self.SER,
            self.SUB,
            self.NUM_DOC,
            self.CHV_NFSE,
            self.DT_DOC,
            self.DT_EXE_SERV,
            self.VL_DOC,
            self.IND_PGTO,
            self.VL_DESC,
            self.VL_BC_PIS,
            self.VL_PIS,
            self.VL_BC_COFINS,
            self.VL_COFINS,
            self.VL_PIS_RET,
            self.VL_COFINS_RET,
            self.VL_ISS,
            ))
        return linha + super(RegistroA100, self).gerar_linha()


'''
 * Registro A110. 
 * Complemento do documento - informacao complementar da NF.
 * 
 * @author Leonardo Ono (ono.leo@gmail.com)
 * @since 1.00.00 (13/03/2011 20:31)
 '''
class RegistroA110(Registro):

    def __init__(self):
        self.REG_PAI = "A100"
        self.REG = "A110"
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
        return linha + super(RegistroA110, self).gerar_linha()




'''
 * Registro A111. 
 * Processo referenciado.
 '''
class RegistroA111(Registro):

    def __init__(self):
        self.REG_PAI = "A100"
        self.REG = "A111"
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
        return linha + super(RegistroA111, self).gerar_linha()




'''
 * Registro A120. 
 * Informacao complementar - operacoes de importacao.
 '''
class RegistroA120(Registro):

    def __init__(self):
        self.REG_PAI = "A100"
        self.REG = "A120"
        self.VL_TOT_SERV = ""
        self.VL_BC_PIS = ""
        self.VL_PIS_IMP = ""
        self.DT_PAG_PIS = ""
        self.VL_BC_COFINS = ""
        self.VL_COFINS_IMP = ""
        self.DT_PAG_COFINS = ""
        self.LOC_EXE_SERV = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.VL_TOT_SERV,
            self.VL_BC_PIS,
            self.VL_PIS_IMP,
            self.DT_PAG_PIS,
            self.VL_BC_COFINS,
            self.VL_COFINS_IMP,
            self.DT_PAG_COFINS,
            self.LOC_EXE_SERV,
            ))
        return linha + super(RegistroA120, self).gerar_linha()




'''Registro A170. Complemento do documento - itens do documento.'''
class RegistroA170(Registro):

    def __init__(self):
        self.REG_PAI = "A100"
        self.REG = "A170"
        self.NUM_ITEM = ""
        self.COD_ITEM = ""
        self.DESCR_COMPL = ""
        self.VL_ITEM = ""
        self.VL_DESC = ""
        self.NAT_BC_CRED = ""
        self.IND_ORIG_CRED = ""
        self.CST_PIS = ""
        self.VL_BC_PIS = ""
        self.ALIQ_PIS = ""
        self.VL_PIS = ""
        self.CST_COFINS = ""
        self.VL_BC_COFINS = ""
        self.ALIQ_COFINS = ""
        self.VL_COFINS = ""
        self.COD_CTA = ""
        self.COD_CCUS = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.NUM_ITEM,
            self.COD_ITEM,
            self.DESCR_COMPL,
            self.VL_ITEM,
            self.VL_DESC,
            self.NAT_BC_CRED,
            self.IND_ORIG_CRED,
            self.CST_PIS,
            self.VL_BC_PIS,
            self.ALIQ_PIS,
            self.VL_PIS,
            self.CST_COFINS,
            self.VL_BC_COFINS,
            self.ALIQ_COFINS,
            self.VL_COFINS,
            self.COD_CTA,
            self.COD_CCUS,
            ))
        return linha + super(RegistroA170, self).gerar_linha()


'''Registro A990. Encerramento do bloco A.'''
class RegistroA990(RegistroX990):

    def __init__(self):
        RegistroX990.__init__(self)
        self.REG_PAI = "0000"
        self.REG = "A990"
        self.nivel = 1
        self.ocorrencia = Ocorrencia.UM
        self.obrigatoriedade = Obrigatoriedade.O
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.QTD_LIN,
            ))
        return linha + super(RegistroA990, self).gerar_linha()



