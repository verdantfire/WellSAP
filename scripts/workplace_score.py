import joblib
import pandas  as pd
import math 
import statistics 

def emp_satisfaction(dict):
    age=joblib.load(open('./../scaler_and _encoder/emp_satisfaction_age_encoder.pkl'))
    dict['Age_Group']=age.transform(dict['Age_Group']).astype('category')

    gender=joblib.load(open('./../scaler_and _encoder/emp_satisfaction_gender_encoder.pkl'))
    dict['Gender']=gender.transform(dict['Gender']).astype('category')

    overtime_encoder=joblib.load(open('./../scaler_and _encoder/emp_satisfaction_overtime_encoder.pkl'))
    dict['OverTime']=overtime_encoder.transform(dict['OverTime']).astype('category')

    scaler=joblib.load(open('./../scaler_and _encoder/scaler_emp_satisfaction.pkl'))
    input_f = [[dict[key] for key in dict.keys()]]
    input_f=scaler.tranform(input_f)
    model=joblib.load(open('./../models/workplace_wellbeing_emp_satisfaction.pkl'))
    return model.predict(input_f)

def env_satisfaction(dict):
    age=joblib.load(open('./../scaler_and _encoder/env_age_encoder.pkl'))
    dict['Age_Group']=age.transform(dict['Age_Group']).astype('category')

    gender=joblib.load(open('./../scaler_and _encoder/env_gender_encoder.pkl'))
    dict['Gender']=gender.transform(dict['Gender']).astype('category')

    job_diversity=joblib.load(open('./../scaler_and _encoder/env_job_diversity_encoder.pkl'))
    dict['FromDiversityJobFairID']=job_diversity.transform(dict['FromDiversityJobFairID']).astype('category')

    citi_encoder=joblib.load(open('./../scaler_and _encoder/env_citizendesc_encoder.pkl'))
    dict['CitizenDesc']=citi_encoder.transform(dict['CitizenDesc']).astype('category')

    his_encoder=joblib.load(open('./../scaler_and _encoder/env_HispanicLatino_encoder.pkl'))
    dict['HispanicLatino']=his_encoder.tranform(dict['HispanicLatino']).astype('category')

    race_encoder=joblib.load(open('./../scaler_and _encoder/env_racedesc_encoder.pkl'))
    dict['RaceDesc']=race_encoder.tranform(dict['RaceDesc']).astype('category')

    attri_encoder=joblib.load(open('./../scaler_and _encoder/env_attri_encoder.pkl'))
    dict['Attrition']=attri_encoder.transform(dict['Attrition']).astype('category')

    busi_encoder=joblib.load(open('./../scaler_and _encoder/env_busi_encoder.pkl'))
    dict['BusinessTravel']=busi_encoder.transfrom(dict['BusinessTravel']).astype('category')

    scaler=joblib.load(open('./../scaler_and _encoder/env_minmax_scaler.pkl'))
    [dict['JobInvolvement'],dict['DistanceFromHome']]=scaler.tranform([dict['JobInvolvement'],dict['DistanceFromHome']])
    model=joblib.load(open('./../models/workplace_wellbeing_env_satisfaction.pkl'))
    input_f = [[dict[key] for key in dict.keys()]]
    return model.predict(input_f)

def work_life_balance(data):
    gender_encoder = joblib.load('./../scaler_and _encoder/work_balance_gender_encoder.pkl')
    data['Gender'] = gender_encoder.transform(data['Gender']).astype('category')

    age_encoder = joblib.load('./../scaler_and _encoder/work_balance_age_encoder.pkl')
    data['Age_Group'] = age_encoder.transform(data['Age_Group']).astype('category')

    model = joblib.load('./../models/workplace_wellbeing_balance_model.pkl')
    input_f = [[data[key] for key in data.keys()]]

    return model.predict(input_f)

def workplace_score(emp,env,bal):
    if emp==0 or env==0 or bal==0:
        emp_gm = math.log(emp+1)
        env_gm = math.log(env+1)
        bal_gm = math.log(bal+1)
        gm = (emp_gm + env_gm + bal_gm) / 3
        gm = math.pow(10,gm) - 1
        am = (emp+env+bal) / 3
        workplace_score = gm**2/am
    
    else:
        workplace_score = statistics.harmonic_mean([emp,env,bal])

    return workplace_score
    
