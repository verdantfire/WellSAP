import joblib

def personal(data):
    print(data)
    gender_encoder = joblib.load('C:\\Users\\Himanshu Ruhela\\WellSAP\\WellSAP\\scaler_and _encoder\\personal_gender_encoder.pkl')
    data['Gender'] = gender_encoder.transform([data['Gender']])

    age_encoder = joblib.load('C:\\Users\\Himanshu Ruhela\\WellSAP\\WellSAP\\scaler_and _encoder\\personal_age_encoder.pkl')
    data['Age_Group'] = age_encoder.transform([data['Age_Group']])

    model = joblib.load('C:\\Users\\Himanshu Ruhela\\WellSAP\\WellSAP\\models\\personal_wellbeing_model.pkl')
    input_f = [[data[key] for key in data.keys()]] 

    print(input_f)
    return model.predict(input_f)

def physical(data):
    model = joblib.load('C:\\Users\\Himanshu Ruhela\\WellSAP\\WellSAP\\models\\personal_wellbeing_model.pkl')
    coefs = model.coef_
    values = [data[key] for key in data.keys()]
    physical_var = [0,1,2,8,9,10]
    physical_score = 0
    for i in physical_var:
        physical_score += values[i]*coefs[0][i]
    return physical_score

def social(data):
    model = joblib.load('C:\\Users\\Himanshu Ruhela\\WellSAP\\WellSAP\\models\\personal_wellbeing_model.pkl')
    coefs = model.coef_
    values = [data[key] for key in data.keys()]
    social_var = [3,4,5,6,7,11,12,15]
    social_score = 0
    for i in social_var:
        social_score += values[i]*coefs[0][i]
    return social_score