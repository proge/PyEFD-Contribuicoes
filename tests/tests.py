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

import sys
sys.path.append('..')

from pyefd_contribuicoes.RegistroRoot import RegistroRoot
from pyefd_contribuicoes.bloco0 import Registro0100
from pyefd_contribuicoes.bloco0 import Registro0110
from pyefd_contribuicoes.bloco0 import Registro0140
from pyefd_contribuicoes.bloco0 import Registro0150
from pyefd_contribuicoes.bloco0 import Registro0190
from pyefd_contribuicoes.bloco0 import Registro0200
from pyefd_contribuicoes.bloco0 import Registro0400
from pyefd_contribuicoes.blocoC import RegistroC010
from pyefd_contribuicoes.blocoC import RegistroC100
from pyefd_contribuicoes.blocoC import RegistroC170
from pyefd_contribuicoes.blocoM import RegistroM100
from pyefd_contribuicoes.blocoM import RegistroM105
from pyefd_contribuicoes.blocoM import RegistroM200
from pyefd_contribuicoes.blocoM import RegistroM500
from pyefd_contribuicoes.blocoM import RegistroM505
from pyefd_contribuicoes.blocoM import RegistroM600

'''
Gera um arquivo EFD-PIS/Cofins de exemplo simples que pelo menos
passa no validador PVA versao 1.0.0 Beta.
'''

def criar_fornecedor_teste():
    fornecedor = Registro0150()
    return fornecedor


def criar_cliente_teste():
    cliente = Registro0150()
    cliente.COD_PART = "1"
    cliente.BAIRRO = "BAIRRO"
    cliente.CNPJ = ""
    cliente.CPF = "17898468970" # Gerado pelo http:# www.geradorcpf.com/
    cliente.COD_MUN = "3550308"
    cliente.COD_PAIS = "01058"
    cliente.END = "RUA XXX"
    cliente.NUM = "99"
    cliente.NOME = "NOME PESSOA FISICA"
    return cliente


def criar_unidade_teste():
    unidade = Registro0190()
    return unidade


def criar_produto_teste():
    produto = Registro0200()
    return produto


def criar_cfop_teste():
    cfop = Registro0400()
    return cfop

# Ponto de partida / Registro Root
registro_root = RegistroRoot()

# Bloco 0

# Dados do contabilista
registro0100 = Registro0100()
registro0110 = Registro0110()
registro0140 = Registro0140()

# Bloco C

# Identificacao do estabelecimento
registroC010 = RegistroC010()
# Cabecalho da NFe
registroC100 = RegistroC100()
# Item da NFe
registroC170 = RegistroC170()

# Bloco M

# Credito de PIS/PASEP relativo ao periodo.
registroM100 = RegistroM100()
# Detalhamento da base de calculo do credito apurado no periodo PIS/PASEP.
registroM105 = RegistroM105()
registroM200 = RegistroM200()
# Credito de COFINS relativo ao periodo.
registroM500 = RegistroM500()
# Detalhamento da base de calculo do credito apurado no periodo - Cofins.
registroM505 = RegistroM505()
# TODO Registro M210 e obrigatorio ?
registroM600 = RegistroM600()
# TODO Registro M610 e obrigatorio ?

registro0001 = registro_root.registro0000.registro0001

registro0001.add_registro_filho(registro0100) # Dados do contabilista
registro0001.add_registro_filho(registro0110)
registro0001.add_registro_filho(registro0140)

# Registro0150 Cliente
registro0140.add_registro_filho(criar_cliente_teste())
# Registro0150 Fornecedor
registro0140.add_registro_filho(criar_fornecedor_teste())
# Registro0190 Unidade
registro0140.add_registro_filho(criar_unidade_teste())
# Registro0200 Produto
registro0140.add_registro_filho(criar_produto_teste())
# Registro0400 CFOP
registro0140.add_registro_filho(criar_cfop_teste())

registroC001 = registro_root.registro0000.registroC001

# Identificacao do estabelecimento
registroC001.add_registro_filho(registroC010)
# Cabecalho da NFe
registroC010.add_registro_filho(registroC100)
# Item da NFe
registroC100.add_registro_filho(registroC170)

registroM001 = registro_root.registro0000.registroM001

# Credito de PIS/PASEP relativo ao periodo.
registroM001.add_registro_filho(registroM100)
# Detalhamento da base de calc do credito apurado no periodo PIS/PASEP.
registroM100.add_registro_filho(registroM105)

registroM001.add_registro_filho(registroM200)
# FIXME: Registro M210 e obrigatorio ?
# Credito de COFINS relativo ao periodo.
registroM001.add_registro_filho(registroM500)
# Detalhamento da base de calc do credito apurado no periodo - Cofins.
registroM500.add_registro_filho(registroM505)

registroM001.add_registro_filho(registroM600)
# FIXME: Registro M610 e obrigatorio ?

caminho_padrao = 'efd.txt'
caminho = raw_input('Informe o caminho em que o arquivo será gerado [{}]: '.format(caminho_padrao))
if caminho == '':
    camiho = caminho_padrao

try :
    registro_root.gerar(caminho)
except:
    print("Ocorreu um erro ao tentar gerar arquivo ! \n\n"
            + "Verifique o caminho informado e tente novamente.")



