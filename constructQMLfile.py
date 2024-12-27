import time
import re

pitchupFile = open("pitch up.qml", "rb")
pitchupCode = pitchupFile.read()
pitchupFile.close()

pitchdowntemplateFile = open("qml-templates/pitch down template.qmltemplate", "rb")
pitchdowntemplateCode = pitchdowntemplateFile.read()
pitchdowntemplateFile.close()

pitchdownCode = pitchdowntemplateCode



tunenedotemplateFile = open("qml-templates/tune n-edo template.qmltemplate", "rb")
tunenedotemplateCode = tunenedotemplateFile.read()
tunenedotemplateFile.close()

tunenedoCode = tunenedotemplateCode

pos = pitchupCode.find(b"n convertAccidentalTextToAccidentalType")

curlybrackets = 0


codes = {"a":b"", "first_curly_close": False, "curlybrackets": 0}

while not codes["first_curly_close"]:
    if pitchupCode[pos] == 123:
        codes["curlybrackets"] += 1
    if pitchupCode[pos] == 125:
        codes["curlybrackets"] -= 1 
        if codes["curlybrackets"] == 0:
            codes["first_curly_close"] = True
    if pitchupCode[pos] == 125 or codes["curlybrackets"]>=1:
        codes["a"] += chr(pitchupCode[pos]).encode("utf-8")
    pos += 1

print("parsed method convertAccidentalTextToAccidentalType")
pitchdownCode = pitchdownCode.replace(b"/* template CATTAT */", codes["a"])
print(codes["a"])

pos = pitchupCode.find(b"function convertAccidentalTypeToSteps(a")

codes["first_curly_close"] = False
codes["curlybrackets"] = 0
codes["a"] = b""

while not codes["first_curly_close"]:
    if pitchupCode[pos] == 123:
        codes["curlybrackets"] += 1
    if pitchupCode[pos] == 125:
        codes["curlybrackets"] -= 1 
        if codes["curlybrackets"] == 0:
            codes["first_curly_close"] = True
    if pitchupCode[pos] == 125 or codes["curlybrackets"]>=1:
        codes["a"] += chr(pitchupCode[pos]).encode("utf-8")
    pos += 1


print("parsed method convertAccidentalTypeToSteps")
pitchdownCode = pitchdownCode.replace(b"/* template CATTS */", codes["a"])



pos = pitchupCode.find(b"function constructAccidental(numSharps, numArro")

codes["first_curly_close"] = False
codes["curlybrackets"] = 0
codes["a"] = b""

while not codes["first_curly_close"]:
    if pitchupCode[pos] == 123:
        codes["curlybrackets"] += 1
    if pitchupCode[pos] == 125:
        codes["curlybrackets"] -= 1 
        if codes["curlybrackets"] == 0:
            codes["first_curly_close"] = True
    if pitchupCode[pos] == 125 or codes["curlybrackets"]>=1:
        codes["a"] += chr(pitchupCode[pos]).encode("utf-8")
    pos += 1


print("parsed method constructAccidental")
pitchdownCode = pitchdownCode.replace(b"/* template CA */", codes["a"])



pos = pitchupCode.find(b"function deconstructAccidental(acc) ")

codes["first_curly_close"] = False
codes["curlybrackets"] = 0
codes["a"] = b""

while not codes["first_curly_close"]:
    if pitchupCode[pos] == 123:
        codes["curlybrackets"] += 1
    if pitchupCode[pos] == 125:
        codes["curlybrackets"] -= 1 
        if codes["curlybrackets"] == 0:
            codes["first_curly_close"] = True
    if pitchupCode[pos] == 125 or codes["curlybrackets"]>=1:
        codes["a"] += chr(pitchupCode[pos]).encode("utf-8")
    pos += 1


print("parsed method deconstructAccidental")
pitchdownCode = pitchdownCode.replace(b"/* template dCA */", codes["a"])



pos = pitchupCode.find(b"function convertStepsToAccidentalType(steps, edo)")

codes["first_curly_close"] = False
codes["curlybrackets"] = 0
codes["a"] = b""

while not codes["first_curly_close"]:
    if pitchupCode[pos] == 123:
        codes["curlybrackets"] += 1
    if pitchupCode[pos] == 125:
        codes["curlybrackets"] -= 1 
        if codes["curlybrackets"] == 0:
            codes["first_curly_close"] = True
    if pitchupCode[pos] == 125 or codes["curlybrackets"]>=1:
        codes["a"] += chr(pitchupCode[pos]).encode("utf-8")
    pos += 1




print("parsed method convertStepsToAccidentalType")
pitchdownCode = pitchdownCode.replace(b"/* template CSTAT */", codes["a"].replace(b"useFlatSide = sharpValue >= 0",b"useFlatSide = sharpValue <= 0"))



pos = pitchupCode.find(b"function convertAccidentalTypeToName(accTy")

codes["first_curly_close"] = False
codes["curlybrackets"] = 0
codes["a"] = b""

while not codes["first_curly_close"]:
    if pitchupCode[pos] == 123:
        codes["curlybrackets"] += 1
    if pitchupCode[pos] == 125:
        codes["curlybrackets"] -= 1 
        if codes["curlybrackets"] == 0:
            codes["first_curly_close"] = True
    if pitchupCode[pos] == 125 or codes["curlybrackets"]>=1:
        codes["a"] += chr(pitchupCode[pos]).encode("utf-8")
    pos += 1




print("parsed method convertAccidentalTypeToName")
pitchdownCode = pitchdownCode.replace(b"/* template CATTN */", codes["a"])

print("parsed method getNextAccidental")
pitchdownCode = pitchdownCode.replace(b"/* template GNA */", pitchupCode[pitchupCode.find(b"/* template GNA start */"):pitchupCode.find(b"/* template GNA end */")+22])



pos = pitchupCode.find(b"function convertAccidentalToStepsOrNull")

codes["first_curly_close"] = False
codes["curlybrackets"] = 0
codes["a"] = b""

while not codes["first_curly_close"]:
    if pitchupCode[pos] == 123:
        codes["curlybrackets"] += 1
    if pitchupCode[pos] == 125:
        codes["curlybrackets"] -= 1 
        if codes["curlybrackets"] == 0:
            codes["first_curly_close"] = True
    if pitchupCode[pos] == 125 or codes["curlybrackets"]>=1:
        codes["a"] += chr(pitchupCode[pos]).encode("utf-8")
    pos += 1


print("parsed method convertAccidentalToStepsOrNull")
tunenedoCode = tunenedoCode.replace(b"/* template CATSON */", codes["a"])

symbols = []
for symbol_group in re.findall("Accidental\\.([A-Z]{0,}[1-9]{0,}(_[A-Z]{0,}[1-9]{0,}){0,})" ,pitchupCode.decode("utf-8")):
    symbols.append(b"\"" + symbol_group[0].encode("utf-8") + b"\"")

symbols = list(set(symbols))

tunenedoCode = tunenedoCode.replace(b"/* template symbols */", b",".join(symbols))

print("parsed accidentals")


print("parsed tune n-edo switch")
tunenedoCode = tunenedoCode.replace(b" /* template tune n-edo switch */", pitchupCode[pitchupCode.find(b"/* template tune n-edo case start */"):pitchupCode.find(b"/* template tune n-edo case end */")+36])





pitchdowntemplateFile = open("pitch down.qml", "wb")
pitchdowntemplateFile.write(pitchdownCode)
pitchdowntemplateFile.close()

pitchdowntemplateFile = open("tune n-edo.qml", "wb")
pitchdowntemplateFile.write(tunenedoCode)
pitchdowntemplateFile.close()


pitchdowntemplateFile = open("pitch up no dt.qml", "wb")
pitchdowntemplateFile.write(pitchupCode.replace(b"\r\n",b"\n").replace(
b"""// <NO DT VARIANT CHECKPOINT>\n          else if (acc.numArrows == 1/2 * sharpValue && acc.numSharps < 2)\n            return constructAccidental(acc.numSharps + 0.5, 0);\n          else if (acc.numArrows == -1/2 * sharpValue && acc.numSharps > -2)\n            return constructAccidental(acc.numSharps - 0.5, 0);\n          else if (acc.numArrows == 3/2 * sharpValue && acc.numSharps < 1)\n            return constructAccidental(acc.numSharps + 1.5, 0);\n          else if (acc.numArrows == -3/2 * sharpValue && acc.numSharps > -1)\n            return constructAccidental(acc.numSharps - 1.5, 0);""", 
b"""// <NO DT VARIANT CHECKPOINT>\n          else if (acc.numArrows == 1/2 * sharpValue && acc.numSharps < 2 && sharpValue >= 8)\n            return constructAccidental(acc.numSharps + 0.5, 0);\n          else if (acc.numArrows == -1/2 * sharpValue && acc.numSharps > -2 && sharpValue >= 8)\n            return constructAccidental(acc.numSharps - 0.5, 0);\n          else if (acc.numArrows == 3/2 * sharpValue && acc.numSharps < 1 && sharpValue >= 8)\n            return constructAccidental(acc.numSharps + 1.5, 0);\n          else if (acc.numArrows == -3/2 * sharpValue && acc.numSharps > -1 && sharpValue >= 8)\n            return constructAccidental(acc.numSharps - 1.5, 0);"""
))
pitchdowntemplateFile.close()

pitchdowntemplateFile = open("pitch down no dt.qml", "wb")
pitchdowntemplateFile.write(pitchdownCode.replace(b"\r\n",b"\n").replace(
b"""// <NO DT VARIANT CHECKPOINT>\n          else if (acc.numArrows == 1/2 * sharpValue && acc.numSharps < 2)\n            return constructAccidental(acc.numSharps + 0.5, 0);\n          else if (acc.numArrows == -1/2 * sharpValue && acc.numSharps > -2)\n            return constructAccidental(acc.numSharps - 0.5, 0);\n          else if (acc.numArrows == 3/2 * sharpValue && acc.numSharps < 1)\n            return constructAccidental(acc.numSharps + 1.5, 0);\n          else if (acc.numArrows == -3/2 * sharpValue && acc.numSharps > -1)\n            return constructAccidental(acc.numSharps - 1.5, 0);""", 
b"""// <NO DT VARIANT CHECKPOINT>\n          else if (acc.numArrows == 1/2 * sharpValue && acc.numSharps < 2 && sharpValue >= 8)\n            return constructAccidental(acc.numSharps + 0.5, 0);\n          else if (acc.numArrows == -1/2 * sharpValue && acc.numSharps > -2 && sharpValue >= 8)\n            return constructAccidental(acc.numSharps - 0.5, 0);\n          else if (acc.numArrows == 3/2 * sharpValue && acc.numSharps < 1 && sharpValue >= 8)\n            return constructAccidental(acc.numSharps + 1.5, 0);\n          else if (acc.numArrows == -3/2 * sharpValue && acc.numSharps > -1 && sharpValue >= 8)\n            return constructAccidental(acc.numSharps - 1.5, 0);"""
))
pitchdowntemplateFile.close()
