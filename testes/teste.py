# consulta_folio = open('folio.txt', 'r')
# folio = consulta_folio.read()
# print(folio)
# consulta_folio.close()


f = open('folio.txt', 'r+')
folio = f.read()
folio = int(folio) + 1
print(folio)
f.close()