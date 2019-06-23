﻿## Navegar ate a pasta de selecao da data e importar o arquivo ##
import os, sys
sys.path.insert(0, './config')
import datareal
sys.path.insert(0, './select')
import data_select
## Navegar ate a pasta de selecao e importar os arquivos ##
from MEX import empresas_mex, nota_select_mex

f = open('idoc/outbound.idoc', 'w', encoding='utf-8-sig')
print('EDI_DC40  1150000000029020882750 3012  ZKFBC_MX_INVOICE                                            ZKFBC_MX_OUT                                     SAPKFQ    LS  Z100                                                                                                 ZKFBC00001LS  TFCLIENT                                                                                             '+ str(datareal.datacompleta) +'194654                                                                                                                '+ str(datareal.datacompleta) +'194653      ', file=f)
print('ZKFBC_MEX_HEADER000           115000000002902088200000100000001'+ str(nota_select_mex.folio) + str(datareal.datacompletaseparada) +'T'+ str(datareal.horacompletacomex) +'                                                                                                                                0                                                  XXX0                P                                                                       PG350000140891232019                                                                                                                        44630                                                                                                                                                                                                                                                                                                           3.3  PAG                                                                                                                                                                                                                                                      ', file=f)
print('ZKFBC_MEX_EMISSOR000          115000000002902088200000200000001'+ str(empresas_mex.rfc) + str(empresas_mex.xnome) +'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ', file=f)
print('ZKFBC_MEX_EMISSOR_DF000       115000000002902088200000300000202Av. de las Americas                                              1545                                                                                                                                                                                                         Guadalajara                                                      JAL                                                              M xico                                                           44630                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ', file=f)
print('ZKFBC_MEX_EMISSOR_EX000       115000000002902088200000400000202Av. de las Americas                                              1545                                                                                                                                                                                                         Guadalajara                                                      JAL                                                              M xico                                                           44630                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ', file=f)
print('ZKFBC_MEX_REGIMENFISCAL000    115000000002902088200000500000202601                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ', file=f)
print('ZKFBC_MEX_RECEPTOR000         115000000002902088200000600000001PCZ071128UM9        PRODUCTOS DE CONSUMO Z SA DE CV                                                                                                                                                                                                                                                                                                                                                                                 P01                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ', file=f)
print('ZKFBC_MEX_RECEPTOR_DF000      115000000002902088200000700000602                                                                                                                   EJIDO  LOS RANCHITOS                                                                                                                                       TLAQUEPAQUE                                                      JAL                                                              M xico                                                           45590                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ', file=f)
print('ZKFBC_MEX_ITEM000             1150000000029020882000008000000021                                                       Pago                                                                                                                    0                0                                       ACT84111506                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ', file=f)
print('ZKFBC_MEX_CABEXT000           115000000002902088200000900000002REGIMENFISCAL                                                                                                                                                                                                                                              REGIMEN GENERAL DE LA LEY DE PERSONAS MORALES                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ', file=f)
print('ZKFBC_MEX_CABEXT000           115000000002902088200001000000002USOCFDI                                                                                                                                                                                                                                                    P01 POR DEFINIR                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              ', file=f)
print('ZKFBC_MEX_CABEXT000           115000000002902088200001100000002REGIMENFIS                                                                                                                                                                                                                                                 601 REGIMEN GENERAL DE LA LEY DE PERSONAS MORALES                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ', file=f)
print('ZKFBC_MEX_COMPR_PAGO000       115000000002902088200001200000002                                  2018-09-1203 MXN                                65059.73                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     2019-02-12T23:00:00                                                                                                                                                                                                                                                                                                      ', file=f)
print('ZKFBC_MEX_COMPR_DOC_REL000    11500000000290208820000130000120381512c22-a5b3-41db-a648-7ef3a15b0b09                                       3900091368                              MXN                        PPD         1         65059.73         65059.73 0.00                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      ', file=f)
f.close()
