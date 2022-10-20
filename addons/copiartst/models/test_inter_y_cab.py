# Importamos las librerías necesarias para el funcionamiento 
import re
import pyperclip as clip
fee = 4000

def parsearcia():
    cia = re.findall('BG CXR: (..) |CARRIER (..)', tst_amadeus)#[0]
    return cia
def parsearruta():    
    route = re.findall(r'^\s{2}\d{1}\s{2}\w{2}.{53}',tst_amadeus, flags=re.M)
    # Recorre toda la lista de vuelos, la convierte en strins, saca lo que no sirve
    # La vuelve a convertir en Strins para despes recorrerlo y mostrar un vuelo
    # por renlon
    tramo=[]
    contador = len(route)
    for renglon in route:
        vuelo = renglon[5:12]
        fecha = renglon[14:20]
        orides = renglon[22:29]
        horarios = renglon[34:44]
        tramo.append(vuelo+fecha+orides+horarios)
        contador = contador-1
    return tramo
'''def parsearorigen():
    orig = re.findall('\n (\w{3})\n', tst_amadeus)[0]
    return orig'''
def parseartarifa():
    fare_ars = re.findall('\nARS(\D{0,3}\d{1,6}.\d{2})', tst_amadeus)[0]
    return fare_ars
def parsearequipaje():    
    bagage = re.findall('(0P|20|30|32|2B|PC|1P|2P|3P)\n', tst_amadeus)
    return bagage
def parsearltd():    
    ltd = re.findall('(DTE \d{2}\D{3}\d{2}/\d{2}:\d{2}|DTE \d{2}\D{3}\d{2})', tst_amadeus)[0]
    return ltd
def parseardate():
    date = re.findall(r'(?:[ |*][A-Z]{1}.)((?:\d{2}\D{3} ))', tst_amadeus)
    return date
def parseartotal():
    ttl = re.findall('\n(ARS|AR|ARS )(\d{1,7}.\d{2})', tst_amadeus)[-1][-1]
    return ttl
def parsearendoso():    
    ref = re.findall('\n(NONREF|NONEND|NON-END|NON-REF)', tst_amadeus)
    return ref
def parsearretenc():
    retenc = re.findall('(\d{0,6}.\d{2})(Q1 |-Q1 |Q1)', tst_amadeus)[0]
    return retenc
def parsearcambio():
    cambio=re.findall('1USD=(......)', tst_amadeus)
    return cambio
def parsearfare():
    fare_usd = re.findall('USD(\D{0,6}\d{1,6}.\d{2}) ', tst_amadeus)[0]
    return fare_usd
def totalizar():
    ttl = re.findall('\n(ARS|AR|ARS )(\d{1,7}.\d{2})', tst_amadeus)[-1][-1]
    total=float(ttl)+float(fee)
    return total
def copia():
    print(texto)
    clip.copy(texto)


while True: #Comienzo del bucle infinito para el programa
   print(
           '''
           \t:::COTIZACIONES AEREAS:::
           ---------------------------
           [1] Cabotaje
           [2] Internacional
           [3] Definir Fee por Defecto ARS
           [4] Volver al Menu
           [0] Salir
           '''
           )
   inter = int(input("Elegi la opción:  "))
   if inter == 1:
       tst_amadeus = clip.paste() # Importar el contenido de Amadeus
       texto=(f'Cotización Cabotaje:\n---------------------------\n* Cía Emisora: {parsearcia()}\n* Cia/Vuelo|Fecha|Tramo|Sale|Llega: \n\n{parsearruta()}\n\n* Ultimo día para emitir: {parsearltd()}\n* Equipaje incluido: {parsearequipaje()}\n* Total con impuestos ARS: {totalizar()}\n* Endosos y Devoluciones: {parsearendoso()}\n----------------------------')
       copia()
   elif inter == 2:
       tst_amadeus = clip.paste() # Importar el contenido de Amadeus
       texto =(f'Cotización Internacional:\n---------------------------\n* Cía Emisora: {parsearcia()}\n* Cia/Vuelo|Fecha|Tramo|Sale|Llega: \n\n{parsearruta()}\n\n* Ultimo día para emitir: {parsearltd()}\n* Equipaje incluido: {parsearequipaje()}\n* Tipo de Cambio oficial {parsearcambio()}\n* Anticipo ganancias a recuperar en AFIP ARS: {parsearretenc()} por pasajero \n* Total con impuestos ARS: {totalizar()}\n* Endosos y Devoluciones: {parsearendoso()}\n----------------------------')
       copia()
   elif inter == 3:
       fee = input("\n-------------------------------------\nDefinir fee en ARS oficial\nPor defecto es ARS4000: ")
   elif inter == 0:
       break
   else:
       print("Ingresa una opción válida: ")
       continue

