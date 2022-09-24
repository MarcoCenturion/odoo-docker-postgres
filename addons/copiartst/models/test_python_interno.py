import re
import pyperclip as clip
#fee = '100'
fee = input("\n-------------------------------------\nDefinir fee en USD oficial, por defecto es 100: ")

tst_amadeus = clip.paste()
retenc = [0]

tst = tst_amadeus.splitlines()


cia=re.findall('BG CXR: (..) |CARRIER (..)', tst_amadeus)#[0]
cambio=re.findall('1USD=(......)', tst_amadeus)
route=re.findall(r'^\s{2}\d{1}\s{2}\w{2}.{55}',tst_amadeus, flags=re.M)
orig=re.findall('\n (\w{3})\n', tst_amadeus)[0]
fare_ars=re.findall('\nARS(\D{0,3}\d{1,6}.\d{2})', tst_amadeus)[0]
bagage=re.findall('(0P|20|30|32|2B|PC|1P|2P|3P)\n', tst_amadeus)
ltd=re.findall('(DTE \d{2}\D{3}\d{2}/\d{2}:\d{2}|DTE \d{2}\D{3}\d{2})', tst_amadeus)[0]
retenc=re.findall('(\d{1,6}.\d{2})(Q1|-Q1)', tst_amadeus)[0]
date=re.findall(r'(?:[ |*][A-Z]{1}.)((?:\d{2}\D{3} ))', tst_amadeus)
fare_usd=re.findall('USD(\D{0,6}\d{1,6}.\d{2}) ', tst_amadeus)[0]
ttl=re.findall('\n(ARS|AR|ARS )(\d{1,7}.\d{2})', tst_amadeus)[-1][-1]


tramo=[]
for renglon in route:
    #tramo.append(renglon[5:12],renglon[14:20],renglon[22:29],renglon[34:44])
    tramo.append(renglon)

total=float(ttl)+(float(fee)*float(str(cambio[0])))

# Caso tkt internacional
texto =(f'INTERNACIONAL\n---------------------------\n* Cía Emisora: {str(cia)}\n* Origen: {str(orig)}\n* Tramos: \n{str(tramo)}\n* Ultimo día para emitir: {str(ltd)}\n* Equipaje incluido: {str(bagage)}\n* Tipo de Cambio oricial {str(cambio)}\n* Anticipo ganancias a recuperar en AFIP ARS: {str(retenc)} por pasajero \n* Total con impuestos ARS: {str(total)}\n----------------------------') 

print(texto)
clip.copy(texto)

