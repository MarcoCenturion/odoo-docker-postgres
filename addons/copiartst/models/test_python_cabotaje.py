import re
import pyperclip as clip
fee = 4000

fee = input("\n-------------------------------------\nDefinir fee en ARS oficial\nPor defecto es ARS4000: ")

tst_amadeus = clip.paste() #importar el contenido de amades
tst = tst_amadeus.splitlines()

cia = re.findall('BG CXR: (..) |CARRIER (..)', tst_amadeus)#[0]
cambio=re.findall('1USD=(......)', tst_amadeus)
route = re.findall(r'^\s{2}\d{1}\s{2}\w{2}.{53}',tst_amadeus, flags=re.M)
orig = re.findall('\n (\w{3})\n', tst_amadeus)[0]
fare_ars = re.findall('\nARS(\D{0,3}\d{1,6}.\d{2})', tst_amadeus)[0]
bagage = re.findall(' (0P|20|30|32|2B|PC|1P|2P|3P)\n', tst_amadeus)
ltd = re.findall('(DTE \d{2}\D{3}\d{2}/\d{2}:\d{2}|DTE \d{2}\D{3}\d{2})', tst_amadeus)[0]
date = re.findall(r'(?:[ |*][A-Z]{1}.)((?:\d{2}\D{3} ))', tst_amadeus)
ttl = re.findall('\n(ARS|AR|ARS )(\d{1,7}.\d{2})', tst_amadeus)[-1][-1]
ref = re.findall('\n(NONREF|NONEND|NON-END|NON-REF)', tst_amadeus)

'''
Definir funcion que recorra toda la lista route y arme una sola linea
compuesta por CIA VUELO TRAMO FECHA EQUIPO
'''

tramo=[]
contador = len(route)
for renglon in route:
    vuelo = renglon[5:12]
    fecha = renglon[14:20]
    orides = renglon[22:29]
    horarios = renglon[34:44]
    tramo.append(vuelo+fecha+orides+horarios)
    contador = contador-1
tramos="\n".join(tramo)


'''Funicion para aplicar markup selectivo
INCOMPLETO
def totalizar():
    if cambio=re.findall('1USD=(......)', tst_amadeus) == True():
        total=float(ttl)+(float(fee)*float(str(cambio[0])))
    elif:
        input("Definir tipo de cambio oficial" :,cambio)
'''
#
#total=float(ttl)+(float(fee)*float(str(cambio[0])))

total=float(ttl)+float(fee)

# Caso tkt internacional
texto =(f'Cotización Cabotaje:\n---------------------------\n* Cía Emisora: {str(cia)}\n* Origen: {str(orig)}\n* Cia/Vuelo|Fecha|Tramo|Sale|Llega: \n\n{str(tramos)}\n\n* Ultimo día para emitir: {str(ltd)}\n* Equipaje incluido: {str(bagage)}\n* Total con impuestos ARS: {str(total)}\n* Endosos y Devoluciones: {ref}\n----------------------------') 

print(texto)
clip.copy(texto)
