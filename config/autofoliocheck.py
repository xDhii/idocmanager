## Check Folio Argentina
try:
    f = open('./select/ARG/folio.txt')
    f.close()
    print('File found!')
except FileNotFoundError:
    f = open('./select/ARG/folio.txt', 'w')
    print('0', file=f)
    f.close()
    print("File not found!")
    print("A new file was created")
## Check Folio Brazil
try:
    f = open('./select/BRA/folio.txt')
    f.close()
    print('File found!')
except FileNotFoundError:
    f = open('./select/BRA/folio.txt', 'w')
    print('0', file=f)
    f.close()
    print("File not found!")
    print("A new file was created")
## Check RPS Brazil
try:
    f = open('./select/BRA/rps.txt')
    f.close()
    print('File found!')
except FileNotFoundError:
    f = open('./select/BRA/rps.txt', 'w')
    print('0', file=f)
    f.close()
    print("File not found!")
    print("A new file was created")
## Check Folio MEX ##
try:
    f = open('./select/MEX/folio.txt')
    f.close()
    print('File found!')
except FileNotFoundError:
    f = open('./select/MEX/folio.txt', 'w')
    print('0', file=f)
    f.close()
    print("File not found!")
    print("A new file was created")
## Check Folio URY ##
try:
    f = open('./select/URY/folio.txt')
    f.close()
    print('File found!')
except FileNotFoundError:
    f = open('./select/URY/folio.txt', 'w')
    print('0', file=f)
    f.close()
    print("File not found!")
    print("A new file was created")