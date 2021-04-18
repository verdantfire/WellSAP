import joblib

def personal(data):
    gender_encoder = joblib.load('./../scaler_and _encoder/personal_gender_encoder.pkl')
    data['Gender'] = gender_encoder.transform(data['Gender'])

    age_encoder = joblib.load('./../scaler_and _encoder/personal_age_encoder.pkl')
    data['Age_Group'] = age_encoder.transform(data['Age_Group'])

    data['BMI_RANGE'] = data['BMI_RANGE'].astype('category')
    data['DONATION'] = data['DONATION'].astype('category')
    data['MaritalStatusID'] = data['MaritalStatusID'].astype('category')
    data['Age_Group'] = data['Age_Group'].astype('category')
    data['Gender'] = data['Gender'].astype('category')
    data['RelationshipSatisfaction'] = data['RelationshipSatisfaction'].astype('category')

    model = joblib.load('./../models/personal_wellbeing_model.pkl')
    input_f = [[data[key] for key in data.keys()]] 

    return model.predict(input_f)

def physical(data):
    model = joblib.load('./../models/personal_wellbeing_model.pkl')
    coefs = model.coef_
    values = [data[key] for key in data.keys()]
    physical_var = [0,1,2,8,9,10]
    physical_score = 0
    for i in physical_var:
        physical_score += values[i]*coefs[i]
    return physical_score

def social(data):
    model = joblib.load('./../models/personal_wellbeing_model.pkl')
    coefs = model.coef_
    values = [data[key] for key in data.keys()]
    social_var = [3,4,5,6,7,11,12,15]
    social_score = 0
    for i in social_var:
        social_score += values[i]*coefs[i]
    return social_score