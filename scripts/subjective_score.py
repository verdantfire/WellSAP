import pandas  as pd
from statistics import harmonic_mean
import math

def subjective(dict):

    dict['LIVE_VISION']=(dict['LIVE_VISION']/10)*100
    dict['SUFFICIENT_INCOME']=(dict['SUFFICIENT_INCOME']/2)*100
    dict['ACHIEVEMENT']=(dict['ACHIEVEMENT']/10)*100
    dict['PERSONAL_AWARDS']=(dict['PERSONAL_AWARDS']/10)*100

    if(dict['LIVE_VISION']==0 or dict['SUFFICIENT_INCOME']==0 or dict['ACHIEVEMENT']==0 or dict['PERSONAL_AWARDS']==0):
        sum=(math.log(dict['LIVE_VISION']+1) + math.log(dict['SUFFICIENT_INCOME']+1) + math.log(dict['ACHIEVEMENT']+1)+ math.log(dict['PERSONAL_AWARDS']+1))/4
        gm=math.pow(10,sum)-1
        am=(dict['LIVE_VISION']+dict['SUFFICIENT_INCOME']+dict['ACHIEVEMENT']+dict['PERSONAL_AWARDS'])/4
        hm=gm**2/am
    else:
       hm=harmonic_mean([dict['LIVE_VISION'],dict['SUFFICIENT_INCOME'],dict['ACHIEVEMENT'],dict['PERSONAL_AWARDS']])    
    return hm


