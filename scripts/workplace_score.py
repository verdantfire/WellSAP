import joblib
import math 
import statistics 

def emp_satisfaction(dict):
    age=joblib.load('C:\\Users\\Himanshu Ruhela\\WellSAP\\WellSAP\\scaler_and _encoder\\emp_satisfaction_age_encoder.pkl')
    dict['Age_Group']=age.transform([dict['Age_Group']])

    gender=joblib.load('C:\\Users\\Himanshu Ruhela\\WellSAP\\WellSAP\\scaler_and _encoder\\emp_satisfaction_gender_encoder.pkl')
    dict['Gender']=gender.transform([dict['Gender']])

    overtime_encoder=joblib.load('C:\\Users\\Himanshu Ruhela\\WellSAP\\WellSAP\\scaler_and _encoder\\emp_satisfaction_overtime_encoder.pkl')
    dict['OverTime']=overtime_encoder.transform([dict['OverTime']])

    scaler=joblib.load('C:\\Users\\Himanshu Ruhela\\WellSAP\\WellSAP\\scaler_and _encoder\\scaler_emp_satisfaction.pkl')
    columns = ['Absences', 'Salary', 'PercentSalaryHike', 'YearsAtCompany', 'YearsInCurrentRole', 'YearsSinceLastPromotion', 'YearsWithCurrManager', 'NumCompaniesWorked']
    scaler_f = [[dict[key] for key in columns]] 
    scaler_f=scaler.transform(scaler_f)
    for i in list(range(0,len(columns))):
        dict[columns[i]] = scaler_f[0][i]

    input_f = [[dict[key] for key in dict.keys()]]
    model=joblib.load('C:\\Users\\Himanshu Ruhela\\WellSAP\\WellSAP\\models\\workplace_wellbeing_emp_satisfaction.pkl')
    return int(model.predict(input_f)[0])

def env_satisfaction(dict):
    age=joblib.load('C:\\Users\\Himanshu Ruhela\\WellSAP\\WellSAP\\scaler_and _encoder\\env_age_encoder.pkl')
    dict['Age_Group']=age.transform([dict['Age_Group']])

    gender=joblib.load('C:\\Users\\Himanshu Ruhela\\WellSAP\\WellSAP\\scaler_and _encoder\\env_gender_encoder.pkl')
    dict['Gender']=gender.transform([dict['Gender']])

    job_diversity=joblib.load('C:\\Users\\Himanshu Ruhela\\WellSAP\\WellSAP\\scaler_and _encoder\\env_job_diversity_encoder.pkl')
    dict['FromDiversityJobFairID']=job_diversity.transform([dict['FromDiversityJobFairID']])

    citi_encoder=joblib.load('C:\\Users\\Himanshu Ruhela\\WellSAP\\WellSAP\\scaler_and _encoder\\env_citizendesc_encoder.pkl')
    dict['CitizenDesc']=citi_encoder.transform([dict['CitizenDesc']])

    his_encoder=joblib.load('C:\\Users\\Himanshu Ruhela\\WellSAP\\WellSAP\\scaler_and _encoder\\env_HispanicLatino_encoder.pkl')
    dict['HispanicLatino']=his_encoder.transform([dict['HispanicLatino']])

    race_encoder=joblib.load('C:\\Users\\Himanshu Ruhela\\WellSAP\\WellSAP\\scaler_and _encoder\\env_racedesc_encoder.pkl')
    dict['RaceDesc']=race_encoder.transform([dict['RaceDesc']])

    attri_encoder=joblib.load('C:\\Users\\Himanshu Ruhela\\WellSAP\\WellSAP\\scaler_and _encoder\\env_attri_encoder.pkl')
    dict['Attrition']=attri_encoder.transform([dict['Attrition']])

    busi_encoder=joblib.load('C:\\Users\\Himanshu Ruhela\\WellSAP\\WellSAP\\scaler_and _encoder\\env_busi_encoder.pkl')
    dict['BusinessTravel']=busi_encoder.transform([dict['BusinessTravel']])

    scaler=joblib.load('C:\\Users\\Himanshu Ruhela\\WellSAP\\WellSAP\\scaler_and _encoder\\env_minmax_scaler.pkl')
    columns = ['JobInvolvement','DistanceFromHome']
    scaler_f = [[dict[key] for key in columns]] 
    scaler_f=scaler.transform(scaler_f)
    for i in list(range(0,len(columns))):
        dict[columns[i]] = scaler_f[0][i]

    model=joblib.load('C:\\Users\\Himanshu Ruhela\\WellSAP\\WellSAP\\models\\workplace_wellbeing_env_satisfaction.pkl')
    input_f = [[dict[key] for key in dict.keys()]]
    return int(model.predict(input_f)[0])

def work_life_balance(data):
    gender_encoder = joblib.load('C:\\Users\\Himanshu Ruhela\\WellSAP\\WellSAP\\scaler_and _encoder\\work_balance_gender_encoder.pkl')
    data['Gender'] = gender_encoder.transform([data['Gender']])

    age_encoder = joblib.load('C:\\Users\\Himanshu Ruhela\\WellSAP\\WellSAP\\scaler_and _encoder\\work_balance_age_encoder.pkl')
    data['Age_Group'] = age_encoder.transform([data['Age_Group']])

    model = joblib.load('C:\\Users\\Himanshu Ruhela\\WellSAP\\WellSAP\\models\\workplace_wellbeing_balance_model.pkl')
    input_f = [[data[key] for key in data.keys()]]

    return int(model.predict(input_f)[0])

def workplace(emp,env,bal):
    if emp==0 or env==0 or bal==0:
        gm = (math.log(emp+1) + math.log(env+1) + math.log(bal+1)) / 3
        gm = math.pow(10,gm) - 1
        am = (emp+env+bal) / 3
        workplace_score = gm**2/am
    
    else:
        workplace_score = statistics.harmonic_mean([emp,env,bal])

    return workplace_score
    
