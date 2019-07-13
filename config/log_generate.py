import datetime, sys

## Time Config ##
date_time = datetime.datetime.now()
date = date_time.date()  # Retorna a data
time = date_time.time()  # Retorna a hora
horacomex = time.hour - 5# Retorna a horas atrasada
horas = time.hour        # Retorna a hora
minutos = time.minute    # Retorna os minutos
segundos = time.second   # Retorna os segundos
ano = date.year          # Retorna o ano
mes = date.month         # Retorna o mes
dia = date.day           # Retorna o dia

## Character Adjustment ##
mes = '{message:{fill}{align}{width}}'.format(
message = (mes) ,
fill='0',
align='>',
width=2,
)
dia = '{message:{fill}{align}{width}}'.format(
message = (dia) ,
fill='0',
align='>',
width=2,
)
horas = '{message:{fill}{align}{width}}'.format(
message = (horas) ,
fill='0',
align='>',
width=2,
)
minutos = '{message:{fill}{align}{width}}'.format(
message = (minutos) ,
fill='0',
align='>',
width=2,
)
segundos = '{message:{fill}{align}{width}}'.format(
message = (segundos) ,
fill='0',
align='>',
width=2,
)

## Full time and date config ##
datacompleta = str(ano)+str(mes)+str(dia)
datacompletabarra = str(ano)+'/'+str(mes)+'/'+str(dia)
horacompleta = str(horas)+str(minutos)+str(segundos)
horacompletaseparada = str(horas)+':'+str(minutos)+':'+str(segundos)

## Capture generated Country information ##
f = open('bin/country.log', 'r')
country = f.read()
f.close()

## Capture generated document type information ##
f = open('bin/document.log', 'r')
document = f.read()
f.close()

## Capture generated document type information ##
f = open('bin/folio.log', 'r')
folio = f.read()
f.close()

## Capture generated Company Code and Company Name ##
f = open('bin/companycode.log', 'r')
companycode = f.read()
f.close()

## Create, write and close the log ##
f = open('./logs/log_'+ str(datacompleta) +'.txt', 'a+')
f.write('A document was generated at '+ str(horacompletaseparada) +' on '+ str(datacompletabarra) +'\n')
f.write('       It was generated '+ str(document) +' ('+ str(country) +')\n')
f.write('       Folio: '+ str(folio))
f.write('       Company: '+ str(companycode) +'\n')
f.close()