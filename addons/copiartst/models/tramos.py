import re
import pyperclip as clip
fee = 100
fee = input("\n-------------------------------------\nDefinir fee en USD oficial, por defecto es 100: ")

tst_amadeus = clip.paste()
retenc = [0]

route=re.findall(r'^\s{2}\d{1}\s{2}\w{2}.{55}',tst_amadeus, flags=re.M)

'''def RecorreRoute():
'''

Tramos = 'Tramo'
contador = 0
for renglon in route:
    contador =+ 1
    print(renglon[5:12],renglon[14:20],renglon[22:29],renglon[34:44])
    #Tramos = str(renglon[5:12])+str(renglon[14:20])+str(renglon[22:29])+str(renglon[34:44])

#RecorreRoute(route)

print(renglon)
print(type(renglon))
print(Tramos)
print(type(Tramos))
