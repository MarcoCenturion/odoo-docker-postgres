import re
tst_amadeus = '''


FQQ10

10 SLN5NSM1   *          * 1          * 152098.90  *RB    *Y

LAST TKT DTE 26JUL21 - SEE ADV PURCHASE
------------------------------------------------------------
     AL FLGT  BK T DATE  TIME  FARE BASIS      NVB  NVA   BG
 BUE
 MIA AA       S  S 12NOV       SLN5NSM1                   1P
 NYC AA       S  S 20NOV       SLN5NSM1                   1P
XMIA AA       S  S 24NOV       SLN5NSM1        21NOV      1P
 BUE AA       S  S             SLN5NSM1        21NOV      1P

USD   800.00      12NOV21BUE AA MIA Q150.00AA NYC M BUEMIA
ARS 81200.00      255.00AA X/MIA AA BUE Q150.00 M245.00NUC
ARS  5684.00-AR   800.00END ROE1.000000
AR                                            
                                                                                
'''
rate = re.findall('\n (\w{3})\n', tst_amadeus)

print(rate)

rate=list(rate)
print(rate)
for i in rate:
     if i != '':
          rate = i
          print(rate)
