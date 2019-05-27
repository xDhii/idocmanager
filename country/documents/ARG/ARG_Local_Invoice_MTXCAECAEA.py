﻿## Navegar ate a pasta de selecao da data e importar o arquivo ##
import os, sys
sys.path.insert(0, './config')
import datareal
sys.path.insert(0, './select')
import data_select
## Navegar ate a pasta de selecao e importar os arquivos ##
from ARG import empresas_arg, nota_select_arg

f = open('idoc/outbound.idoc', 'w', encoding='utf-8-sig')
print('EDI_DC40  8000000000003262818740 3012  /KFBCLA/AR_FE                                               /KFBCLA/AR_FE                                    SAPKFQ    LS  KFQCLNT800                                                                                           TFC04     LS  TFC04                                                                                                '+ str(data_select.ano) + str(data_select.mes) + str(data_select.dia) +'163959                                                                                                                '+ str(data_select.ano) + str(data_select.mes) + str(data_select.dia) +'163958      ', file=f)
print('/KFBCLA/AR_FE_CAEREQUEST000   800000000000326281800000100000001001       7500 00000015        '+ str(data_select.ano) +'-'+ str(data_select.mes) +'-'+ str(data_select.dia) +'                                                  80        30526143813          90.00            0.00            0.00           90.00            0.00          108.90 PES                     1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 01                                                                                                                                                                                                                                                            ', file=f)
print('/KFBCLA/AR_FE_ITEM000         800000000000326281800000200000102000012    8710103783336  0000000000020       Product 20                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                1.000 07                  90.00                 05                   18.9           108.9 000010                                                                                                                                                                                                                                                                                                                                                 ', file=f)
print('/KFBCLA/AR_FE_ITEMEXT000      800000000000326281800000300000203BATCH                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         000010                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ', file=f)
print('/KFBCLA/AR_FE_SUBTOTALESIVA00080000000000032628180000040000010205                  18.90                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ', file=f)
print('/KFBCLA/AR_FE_CAB000          800000000000326281800000500000102'+ str(empresas_arg.cuit) +'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             ', file=f)
print('/KFBCLA/AR_FE_EXTENCIONES000  800000000000326281800000600000102CUIT                          '+ str(empresas_arg.cuit) +'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ', file=f)
print('/KFBCLA/AR_FE_EXTENCIONES000  800000000000326281800000700000102DATA_INICIO                   01011993                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ', file=f)
print('/KFBCLA/AR_FE_EXTENCIONES000  800000000000326281800000800000102INVOICE                       CAEA'+ str(nota_select_arg.cuit) +'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       ', file=f)
print('/KFBCLA/AR_FE_EXTENCIONES000  800000000000326281800000900000102INVOICE                       CAEA'+ str(nota_select_arg.cuit) +'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       ', file=f)
print('/KFBCLA/AR_FE_EXTENCIONES000  800000000000326281800001000000102NOME_EMISSOR                  IDES Argentina Andreas Blachmann,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         ', file=f)
print('/KFBCLA/AR_FE_EXTENCIONES000  800000000000326281800001100000102ENDERECO_EMISSOR              Alem , 855                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ', file=f)
print('/KFBCLA/AR_FE_EXTENCIONES000  800000000000326281800001200000102ENDERECO_EMISSOR2             Capital Federal                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           ', file=f)
print('/KFBCLA/AR_FE_EXTENCIONES000  800000000000326281800001300000102ENDERECO_EMISSOR3             Tel.: 4891-3000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           ', file=f)
print('/KFBCLA/AR_FE_EXTENCIONES000  800000000000326281800001400000102NOME_BILLTO                   CL301                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ', file=f)
print('/KFBCLA/AR_FE_EXTENCIONES000  800000000000326281800001500000102ENDERECO_BILLTO               Avenida Bustillo , 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      ', file=f)
print('/KFBCLA/AR_FE_EXTENCIONES000  800000000000326281800001600000102ENDERECO_BILLTO2              Bariloche                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ', file=f)
print('/KFBCLA/AR_FE_EXTENCIONES000  800000000000326281800001700000102ENDERECO_BILLTO3              Argentina                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ', file=f)
print('/KFBCLA/AR_FE_EXTENCIONES000  800000000000326281800001800000102RUC_BILLTO                    30526143813                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ', file=f)
print('/KFBCLA/AR_FE_EXTENCIONES000  800000000000326281800001900000102NOME_SHIPTO                   CL301                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ', file=f)
print('/KFBCLA/AR_FE_EXTENCIONES000  800000000000326281800002000000102ENDERECO_SHIPTO               Avenida Bustillo , 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      ', file=f)
print('/KFBCLA/AR_FE_EXTENCIONES000  800000000000326281800002100000102ENDERECO_SHIPTO2              Bariloche                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ', file=f)
print('/KFBCLA/AR_FE_EXTENCIONES000  800000000000326281800002200000102ENDERECO_SHIPTO3              Argentina                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ', file=f)
print('/KFBCLA/AR_FE_EXTENCIONES000  800000000000326281800002300000102NOME_CONS                     CL301                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ', file=f)
print('/KFBCLA/AR_FE_EXTENCIONES000  800000000000326281800002400000102ENDERECO_CONS                 Avenida Bustillo , 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      ', file=f)
print('/KFBCLA/AR_FE_EXTENCIONES000  800000000000326281800002500000102ENDERECO_CONS2                Bariloche                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ', file=f)
print('/KFBCLA/AR_FE_EXTENCIONES000  800000000000326281800002600000102ENDERECO_CONS3                Argentina                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ', file=f)
print('/KFBCLA/AR_FE_EXTENCIONES000  800000000000326281800002700000102MOEDA                         ARS-Peso argentino                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ', file=f)
print('/KFBCLA/AR_FE_EXTENCIONES000  800000000000326281800002800000102DELIVERY_TERMS                FH                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ', file=f)
f.close()