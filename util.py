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

'''
<p>Indica a <strong>obrigatoriedade</strong> do Registro.</p>

<p><strong>O</strong> = O registro sempre e obrigatorio.</p>

<p><strong>OC</strong> = O registro e obrigatorio, se houver informacao 
                         a ser prestada.

        Ex.: Registro C100 so devera ser apresentado se houver 
             movimentacao ou operacoes utilizando os documentos de 
             codigos 01, 1B, 04 ou 55.</p>

<p><strong>O_SE</strong> = O(...) = O registro e obrigatorio se atentida 
                                    a condicao.

                   Ex.: Registro C191 O(Se existir C190) O registro e
                        obrigatorio sempre que houver o registro C190.

<p><strong>N</strong>= O registro nao deve ser informado. 

       Ex.: Registro C490 se for informado o Registro C400.</p>
'''
class Obrigatoriedade:
    O = 'O'
    OC = 'OC'
    O_SE = 'O_SE'
    N = 'N'


'''
<p>Indica a <strong>ocorrencia</strong> do Registro.</p>

<p><strong>UM</strong> = um por arquivo.</p>

<p><strong>VARIOS</strong> = varios por arquivo.</p>

<p><strong>UM_PARA_UM</strong> = devera haver um unico registro filho
                                 para respectivo registro pai.</p>

<p><strong>UM_PARA_MUITOS</strong> = pode haver varios registros filhos
                                     para respectivo registro pai.</p>

'''
class Ocorrencia:
    UM = 'UM'
    VARIOS = 'VARIOS'
    UM_PARA_UM = 'UM_PARA_UM'
    UM_PARA_MUITOS = 'UM_PARA_MUITOS'
