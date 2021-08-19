import re
tst_amadeus = '''



LAST TKT DTE 02JUL21/09:31 LT in POS - SEE ADV PURCHASE
------------------------------------------------------------
     AL FLGT  BK T DATE  TIME  FARE BASIS      NVB  NVA   BG
 BUE
 MIA AR  1302 V  V 10NOV 2300  VLDVNEB                    0P
 BUE AR  1303 N  N 01DEC 1740  NLXBVNEB        14NOV      0P

USD   945.00      10NOV21BUE AR MIA Q150.00 302.00AR BUE Q
ARS 94973.00      150.00 342.50NUC944.50END ROE1.000000
ARS  6648.10-AR   XT ARS 33240.60-Q1 ARS 1005.00-QO ARS
ARS 28491.90-O5   804.00-TQ ARS 5728.50-XR ARS 562.80-AY ARS
ARS 47335.90-XT   1919.60-US ARS 1919.60-US ARS 398.00-XA
ARS177448.90      ARS 703.50-XY ARS 602.00-YC ARS 452.30-XF
                  MIA4.50
RATE USED 1USD=100.50000ARS
NO BAG INCLUDED FOR AT LEAST ONE FLIGHT
FARE FAMILIES:    (ENTER FQFn FOR DETAILS, FXY FOR UPSELL)
FARE FAMILY:FC1:1:EB                                                            
FARE FAMILY:FC2:2:EB                                                            
FXU/TS TO UPSELL EB-EP FOR 7777.90ARS                                           
BG CXR: AR                                                                      
PRICED WITH VALIDATING CARRIER AR - REPRICE IF DIFFERENT VC                     
ENDOS NONREF/NONEND -BG:AR

self.cia=''.join(re.findall('BG CXR: (..) |CARRIER (..)', self.tst_amadeus)[0])
                                                                                
'''
rate = re.findall('1USD=(......)', tst_amadeus)

print(rate)

rate=list(rate)
print(rate)
for i in rate:
     if i != '':
          rate = i
          print(rate)

'''


sale_order_new.write({
'order_line': [
(0,0, {
'order_id': sale_order.id,
'product_id': 2003,
'price_unit': 3000.0,
'product_uom_qty': 2.0,
'name': ''
})
]
})
'''