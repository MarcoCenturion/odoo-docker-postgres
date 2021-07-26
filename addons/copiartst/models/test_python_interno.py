import re
tst_amadeus = '''


FXR

01 CENTURION/MARCO*
ITINERARY REBOOKED
LAST TKT DTE 13JUL21/23:59 LT in POS - SEE ADV PURCHASE
------------------------------------------------------------
     AL FLGT  BK T DATE  TIME  FARE BASIS      NVB  NVA   BG
 BUE
 MIA AA   900 B *B 10NOV 2214  NLN5NZB1        10NOV10NOV 0P
 BUE AA   907 B *B 20NOV 1940  VLN4NSB1        20NOV20NOV 0P

USD   752.00      10NOV21BUE AA MIA290.00AA BUE Q150.00
ARS 75952.00      312.00NUC752.00END ROE1.000000
ARS  5316.60-AR   XT ARS 26583.20-Q1 ARS 1010.00-QO ARS
ARS 22785.60-O5   808.00-TQ ARS 5757.00-XR ARS 565.60-AY ARS
ARS 40748.50-XT   1929.10-US ARS 1929.10-US ARS 400.00-XA
ARS144802.70      ARS 707.00-XY ARS 605.00-YC ARS 454.50-XF
                  MIA4.50
RATE USED 1USD=101.00000ARS
NO BAG INCLUDED FOR AT LEAST ONE FLIGHT
FARE FAMILIES:    (ENTER FQFn FOR DETAILS, FXY FOR UPSELL)
>                                                 PAGE  2/ 3

>

m

FARE FAMILY:FC1:1:BASIC                                                         
FARE FAMILY:FC2:2:BASIC                                                         
FXU/TS TO UPSELL MAIN-MAIN FOR 22583.60ARS                                      
TICKET STOCK RESTRICTION                                                        
BG CXR: AA                                                                      
PRICED WITH VALIDATING CARRIER AA - REPRICE IF DIFFERENT VC                     
FARE VALID FOR E TICKET ONLY                                                    
TICKETS ARE NON-REFUNDABLE                                                      
ENDOS /C1-2 NONREF/NOCHG/BASIC -BG:AA                                           
>                                                 PAGE  3/ 3                    
                                                                                

                  
                                                                                
'''
retenc = re.findall('ARS (\D{0,3}\d{1,6}.\d{2})(Q1|-Q1)', tst_amadeus)[0][0]

print(retenc)
'''
retenc=list(retenc)
print(retenc)
for i in retenc:
	if i != '':
		retenc = i
		print(retenc)
'''