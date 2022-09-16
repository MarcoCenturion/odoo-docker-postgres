import re
import pyperclip as clip
fee = input("definir fee en usd (oficial): ")
tst_amadeus = clip.paste()

#print(tst_amadeus)

cia=re.findall('BG CXR: (..) |CARRIER (..)', tst_amadeus)#[0]
cambio=re.findall('1USD=(......)', tst_amadeus)
route=re.findall('\n \w{3}\v \w{3} \w{2}\n\w|\n([ |X]\w{3} ..)', tst_amadeus)
orig=re.findall('\n (\w{3})\n', tst_amadeus)[0]
fare_ars=re.findall('\nARS(\D{0,3}\d{1,6}.\d{2})', tst_amadeus)[0]
bagage=re.findall('(0P|20|30|32|2B|PC|1P|2P|3P)\n', tst_amadeus)
ltd=re.findall('(DTE \d{2}\D{3}\d{2}/\d{2}:\d{2}|DTE \d{2}\D{3}\d{2})', tst_amadeus)[0]
retenc=re.findall('(\d{1,6}.\d{2})(Q1|-Q1)', tst_amadeus)[0]
date=re.findall(r'(?:[ |*][A-Z]{1}.)((?:\d{2}\D{3} ))', tst_amadeus)
fare_usd=re.findall('USD(\D{0,6}\d{1,6}.\d{2}) ', tst_amadeus)[0]
ttl=re.findall('\n(ARS|AR|ARS )(\d{1,7}.\d{2})', tst_amadeus)[-1][-1]


cia=list(cia)
#print(cia)
for i in cia:
     if i != '':
          cia = i
'''

print("Cotización aéreo")
print("--------------------------------------------------------------")
print("Ruta completa",route)
:print("Origen",orig)
print("Tarifa en pesos ARS",fare_ars)
print("Equipaje permitido ",bagage)
print("Ultimo día para emitir",ltd)
print("Retención Ganancias ARS",retenc)
print("Tarifa orifinal USD",fare_usd)
print("Cia aérea emisora ",cia)
print("Tipo de cambio 1USD = ARS",cambio)
print("--------------------------------------------------------------")
print("Total con impuestos ARS ",float(ttl)+float(fee))
print("--------------------------------------------------------------")
'''
#print("Cía Emisora ",cia,"\n Origen ",orig, "Ruta ", route,"\nUltimo día para emitir",ltd,"\nEquipaje ",bagage,"\nA recuperar en AFIP ARS ",retenc,"\nTotal c/tax ",float(ttl)+float(fee))

total=float(ttl)+(float(fee)*float(str(cambio[0])))
#total=float(ttl)+float(fee)

print(f'---------------------------\n* Cía Emisora: {str(cia)}\n* Origen: {str(orig)}\n* Ruta: {str(route)}\n* Ultimo día para emitir: {str(ltd)}\n* Equipaje incluido: {str(bagage)}\n* Tipo de Cambio oficial {str(cambio)}\n* Anticipo ganancias a recuperar en AFIP ARS: {str(retenc)} por pasajero \n* Total con impuestos ARS: {str(total)}\n----------------------------') 

#print(f'{float(str(cambio[0]))}')


clip.copy(f'---------------------------\n* Cía Emisora: {str(cia)}\n* Origen: {str(orig)}\n* Ruta: {str(route)}\n* Ultimo día para emitir: {str(ltd)}\n* Equipaje incluido: {str(bagage)}\n* Tipo de Cambio oficial {str(cambio)}\n* Anticipo ganancias a recuperar en AFIP ARS: {str(retenc)} por pasajero \n* Total con impuestos ARS: {str(total)}\n----------------------------') 
