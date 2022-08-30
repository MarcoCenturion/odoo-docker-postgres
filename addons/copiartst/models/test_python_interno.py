import re
tst_amadeus = '''

FXR

01 CENTURION/JULIE*
ITINERARY REBOOKED
LAST TKT DTE 02AUG21/23:59 LT in POS - SEE ADV PURCHASE
------------------------------------------------------------
     AL FLGT  BK T DATE  TIME  FARE BASIS      NVB  NVA   BG
 BUE
 MIA AA   900 Y *Y 01SEP 2050  Y                          1P
 NYC AA   309 V *V 12SEP 0608  V0AHZNN1                   1P
 LAX AA     1 G  G 20SEP 0800  G7AKZNN1                   1P
 LAS      S U R F A C E
XMIA AA   659 Y *Y 03OCT 0015  Y                          1P
 BUE AA   931 Y *Y 03OCT 2045  Y                          1P

USD  6193.00      01SEP21BUE AA MIA Q150.00 2765.00AA NYC
ARS630138.00      161.86AA LAX200.93/-LAS AA X/MIA AA BUE Q
ARS 44109.70-AR   150.00 M2765.00NUC6192.79END ROE1.000000
ARS189041.40-O5   XT ARS 220548.30-Q1 ARS 1017.50-QO ARS
ARS235388.60-XT   814.00-TQ ARS 5799.80-XR ARS 1139.60-AY
AR1098677.70      ARS 1943.40-US ARS 1943.40-US ARS 402.90
>                                                 PAGE  2/ 3

>

m

                  -XA ARS 712.30-XY ARS 609.50-YC ARS 457.90                    
                  -XF MIA4.50                                                   
RATE USED 1USD=101.75000ARS                                                     
FARE FAMILIES:    (ENTER FQFN FOR DETAILS, FXY FOR UPSELL)                      
FARE FAMILY:FC1:1:MAINFL                                                        
FARE FAMILY:FC2:5-6:MAINFL                                                      
FARE FAMILY:FC3:2:MAIN                                                          
FARE FAMILY:FC4:3:MAIN                                                          
FXU/TS TO UPSELL MAINFL-MAINFL-MAINFL-MAIN* FOR 238362.80ARS                    
BG CXR: AA                                                                      
PRICED WITH VALIDATING CARRIER AA - REPRICE IF DIFFERENT VC                     
FARE VALID FOR E TICKET ONLY                                                    
TICKETS ARE NON-REFUNDABLE                                                      
ENDOS /C2-3 NONREF/FAREDIF/ CXL BY FLT TIME OR NOVALUE -BG:A                    
      A                                                                         
ATTN                  ***                                                       
>                                                 PAGE  3/ 3                    
                                                                                


                                                                                
'''
rate = re.findall('\n \w{3}\v \w{3} \w{2}\n\w|\n([ |X]\w{3} ..)', tst_amadeus)

print(rate)

rate=list(rate)
print(rate)
for i in rate:
     if i != '':
          rate = i
          print(rate)
