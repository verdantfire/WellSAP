import pandas  as pd
from statistics import harmonic_mean
import math

def subjective(dict):

    dict['LIVE_VISION']=(dict['LIVE_VISION']/10)*100
    dict['SUFFICIENT_INCOME']=((dict['SUFFICIENT_INCOME']-1))*50+50
    dict['ACHIEVEMENT']=(dict['ACHIEVEMENT']/10)*100
    dict['PERSONAL_AWARDS']=(dict['PERSONAL_AWARDS']/10)*100

    if(dict['LIVE_VISION']==0 or dict['SUFFICIENT_INCOME']==0 or dict['ACHIEVEMENT']==0 or dict['PERSONAL_AWARDS']==0):
        dict['LIVE_VISION']=dict['LIVE_VISION']+1
        dict['SUFFICIENT_INCOME']=dict['SUFFICIENT_INCOME']+1
        dict['ACHIEVEMENT']=dict['ACHIEVEMENT']+1
        dict['PERSONAL_AWARDS']=dict['PERSONAL_AWARDS']+1
        sum=math.log10(dict['LIVE_VISION']) + math.log10(dict['SUFFICIENT_INCOME']) + math.log10(dict['ACHIEVEMENT'])+ math.log10(dict['PERSONAL_AWARDS'])       
        gm=sum/4
        gm=math.pow(10,gm)-1
        am=(dict['LIVE_VISION']+dict['SUFFICIENT_INCOME']+dict['ACHIEVEMENT']+dict['PERSONAL_AWARDS'])/4
        hm=(gm*gm)/am
    else:
       hm=harmonic_mean([dict['LIVE_VISION'],dict['SUFFICIENT_INCOME'],dict['ACHIEVEMENT'],dict['PERSONAL_AWARDS']])    
    return hm


