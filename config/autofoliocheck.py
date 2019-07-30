## Check Folio Argentina
try:
    f = open('./select/ARG/folio.txt')
    f.close()
    print('File found!')
except FileNotFoundError:
    f = open('./select/ARG/folio.txt', 'w')
    f.write('0')
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
    f.write('0')
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
    f.write('0')
    f.close()
    print("File not found!")
    print("A new file was created")
## Check Folio Chile
try:
    f = open('./select/CHL/folio.txt')
    f.close()
    print('File found!')
except FileNotFoundError:
    f = open('./select/CHL/folio.txt', 'w')
    f.write('0')
    f.close()
    print("File not found!")
    print("A new file was created")
## Check Folio Ecuador
try:
    f = open('./select/ECU/folio.txt')
    f.close()
    print('File found!')
except FileNotFoundError:
    f = open('./select/ECU/folio.txt', 'w')
    f.write('0')
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
    f.write('0')
    f.close()
    print("File not found!")
    print("A new file was created")
## Check Folio PER ##
try:
    f = open('./select/PER/folio.txt')
    f.close()
    print('File found!')
except FileNotFoundError:
    f = open('./select/PER/folio.txt', 'w')
    f.write('0')
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
    f.write('0')
    f.close()
    print("File not found!")
    print("A new file was created")
