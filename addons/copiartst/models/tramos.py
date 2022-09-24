import re
import pyperclip as clip
fee = 100
fee = input("\n-------------------------------------\nDefinir fee en USD oficial, por defecto es 100: ")

tst_amadeus = clip.paste()
retenc = [0]

route=re.findall(r'^\s{2}\d{1}\s{2}\w{2}.{55}',tst_amadeus, flags=re.M)

tramo = []
renglon = []
def RecorreRoute(renglon):
    for renglon in route:
        tramo.append(renglon)
        return(tramo)

RecorreRoute(route)
print(renglon)


