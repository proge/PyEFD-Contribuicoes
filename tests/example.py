#!/usr/bin/env python
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
from pyefd_contribuicoes.bloco0 import Registro0110, Registro0140
from pyefd_contribuicoes.blocoC import RegistroC010
from pyefd_contribuicoes.blocoM import RegistroM200, RegistroM600

'''
Tutorial passo-a-passo de como utilizar este projeto para geracao do arquivo
EFD-PIS/Cofins.

Ao executar, o código desta classe ira gerar um arquivo EFD-PIS/Cofins de 
exemplo simples que passa no validador PVA versao 1.0.0 Beta.
'''
registroRoot = RegistroRoot()


'''
Ao instanciar um novo RegistroRoot, os registros de nível 0, ou seja, os
registros 0000 e 9999 tambem ja sao criados e adicionados automaticamente e
podem ser acessados através do código abaixo:
'''
registro0000 = registroRoot.registro0000
registro9999 = registroRoot.registro9999

'''
Ao instanciar um novo RegistroRoot, os registros de nível 1, ou seja, os
registros de abertura e encerramento de bloco tambem já são criados e
adicionados automaticamente no registro 0000 e podem ser acessados conforme 
código abaixo:
'''

# Registros de abertura de bloco
registro0001 = registro0000.registro0001
registroA001 = registro0000.registroA001
registroC001 = registro0000.registroC001
registroD001 = registro0000.registroD001
registroF001 = registro0000.registroF001
registroM001 = registro0000.registroM001
registroP001 = registro0000.registroP001
registro1001 = registro0000.registro1001
registro9001 = registro0000.registro9001

# Registros de encerramento de bloco
registro0990 = registro0000.registro0990
registroA990 = registro0000.registroA990
registroC990 = registro0000.registroC990
registroD990 = registro0000.registroD990
registroF990 = registro0000.registroF990
registroM990 = registro0000.registroM990
registroP990 = registro0000.registroP990
registro1990 = registro0000.registro1990
registro9990 = registro0000.registro9990

'''
Apartir disso, os demais registros de nivel maior ou igual a 2 devem ser criados
e adicionados manualmente no seu respectivo registro PAI.

Exemplo: Cria o registro 0110 (regime de apuração) e adiciona ao registro 0001
(que é o registro PAI de 0110).
'''
registro0110 = Registro0110()
registro0001.add_registro_filho(registro0110)

'''
Cria o registro 0140 (tabela de cadastro de estabelecimento) e adiciona ao
registro 0001 (que é o registro PAI de 0140).
'''
registro0140 = Registro0140()
registro0001.add_registro_filho(registro0140)

'''
Cria o registro C010 (identificação do estabelecimento) e adiciona ao registro
C001 (que é o registro PAI de C010).
'''
registroC010 = RegistroC010()
registroC010.CNPJ = "22222222000191"
registroC010.IND_ESCRI = "2"

registroC001.add_registro_filho(registroC010)

'''
Cria o registro M200 (consolidação da contribuição PIS/PASEP do período) e
adiciona ao registro M001 (que é o registro PAI de M200).
'''
registroM200 = RegistroM200()
registroM001.add_registro_filho(registroM200)

'''
Cria o registro M600 (consolidação da contribuicao Cofins do período) e adiciona
ao registro M001 (que é o registro PAI de M600).
'''
registroM600 = RegistroM600()
registroM001.add_registro_filho(registroM600)

'''
Depois que todos os registros de seu interesse foram adicionados, basta utilizar
o método gerar() da classe RegistroRoot conforme código abaixo:
'''
registroRoot.gerar("teste_efd_pis_cofins.txt")

