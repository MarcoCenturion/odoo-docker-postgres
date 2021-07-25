import re
tst_amadeus = '''


FXR

01 P1
ITINERARY REBOOKED
LAST TKT DTE 28JUL21/23:59 LT in POS - SEE ADV PURCHASE
------------------------------------------------------------
     AL FLGT  BK T DATE  TIME  FARE BASIS      NVB  NVA   BG
 BUE
 MAD UX    42 Z  Z 01NOV 1330  ZYYR0L          01NOV01NOV 0P
 BUE UX    41 Z *Z 15NOV 2355  ZYYR0L          15NOV15NOV 0P

USD    45.00      01NOV21BUE UX MAD22.50UX BUE22.50NUC45.00
ARS  4568.00      END ROE1.000000
ARS  3744.40-AR   XT ARS 16047.30-O5 ARS 18721.90-Q1 ARS
ARS 48923.00-YQ   1015.00-QO ARS 812.00-TQ ARS 5785.50-XR
ARS 45355.90-XT   ARS 2495.60-JD ARS 74.20-OG ARS 404.40-QV
ARS102591.30
RATE USED 1USD=101.50000ARS
NO BAG INCLUDED FOR AT LEAST ONE FLIGHT
FARE FAMILIES:    (ENTER FQFn FOR DETAILS, FXY FOR UPSELL)
FARE FAMILY:FC1:1:LITE
>                                                 PAGE  2/ 3

>

m

FARE FAMILY:FC2:2:LITE                                                          
FXU/TS TO UPSELL LITE-STANDARD FOR 7855.20ARS                                   
TICKET STOCK RESTRICTION                                                        
BG CXR: UX/UX                                                                   
PRICED WITH VALIDATING CARRIER UX - REPRICE IF DIFFERENT VC                     
TICKETS ARE NON-REFUNDABLE                                                      
ENDOS CHGS AND REF RESTRICTED                                                   
PAYMT RESTRICTIONS APPLY                                                        
>                                                 PAGE  3/ 3     
                                                                    
'''
cia = ''.join(re.findall('BG CXR: (..) |CARRIER (..)', tst_amadeus)[0])
#cia=''.join(cia)

print(cia)
'''
retenc=list(retenc)
print(retenc)
for i in retenc:
	if i != '':
		retenc = i
		print(retenc)
'''