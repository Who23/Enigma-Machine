from machine import Machine

enigma = Machine()
final = ""

readFile = open("encode.txt", "r")
File = readFile.read()
readFile.close()

File = str(File)
File = File.upper()


for x in File:
    if x != " ":
        final = final + enigma.returnOutput(x)
    else:
        final = final + " "

readFile = open("encode.txt", "w")
readFile.write(final)
readFile.close()
