# consulta_folio = open('folio.txt', 'r')
# folio = consulta_folio.read()
# print(folio)
# consulta_folio.close()

## Calcula folio + 1 ##
f = open('folio.txt', 'r+')
folio = f.read()
folio = int(folio) + 1

f.close()

## Salva novo folio no TXT ##
f = open('folio.txt', 'w')
print(folio, file=f)
f.close()
