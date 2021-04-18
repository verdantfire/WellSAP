from numpy.core.arrayprint import array2string
import pandas as pd
import numpy as np
from scripts.score import score

hr_data = pd.read_csv('C:\\Users\\Himanshu Ruhela\\WellSAP\\WellSAP\\dataset\\hr_data.csv',header=0,index_col='Employee_ID')
attrition_data = pd.read_csv('C:\\Users\\Himanshu Ruhela\\WellSAP\\WellSAP\\dataset\\attrition_data.csv',header=0,index_col='Employee_ID')
lifestyle_data = pd.read_csv('C:\\Users\\Himanshu Ruhela\\WellSAP\\WellSAP\\dataset\\lifestyle_data_simplified.csv',header=0,index_col='Employee_ID')


def data_id(employee_id):
    data = {}
    
    #Basic Info
    data['employee_id'] = employee_id
    data['employee_name'] = hr_data.loc[employee_id, 'Employee_Name']
    data['Age_Group'] = attrition_data.loc[employee_id, 'Age_Group']
    data['Gender'] = attrition_data.loc[employee_id, 'Gender']


    #Personal Life
    data['FRUITS_VEGGIES'] = lifestyle_data.loc[employee_id, 'FRUITS_VEGGIES']    
    data['DAILY_STRESS'] = lifestyle_data.loc[employee_id, 'DAILY_STRESS']    
    data['BMI_RANGE'] = lifestyle_data.loc[employee_id, 'BMI_RANGE']    
    data['DONATION'] = lifestyle_data.loc[employee_id, 'DONATION']    
    data['PLACES_VISITED'] = lifestyle_data.loc[employee_id, 'PLACES_VISITED']    
    data['CORE_CIRCLE'] = lifestyle_data.loc[employee_id, 'CORE_CIRCLE']    
    data['SUPPORTING_OTHERS'] = lifestyle_data.loc[employee_id, 'SUPPORTING_OTHERS']    
    data['DAILY_STEPS'] = lifestyle_data.loc[employee_id, 'DAILY_STEPS']    
    data['SOCIAL_NETWORK'] = lifestyle_data.loc[employee_id, 'SOCIAL_NETWORK']    
    data['SLEEP_HOURS'] = lifestyle_data.loc[employee_id, 'SLEEP_HOURS']    
    data['WEEKLY_MEDITATION'] = lifestyle_data.loc[employee_id, 'WEEKLY_MEDITATION']    
    data['DAILY_SHOUTING'] = lifestyle_data.loc[employee_id, 'DAILY_SHOUTING']    
    data['MaritalStatusID'] = hr_data.loc[employee_id, 'MaritalStatusID']
    data['RelationshipSatisfaction'] = attrition_data.loc[employee_id, 'RelationshipSatisfaction']


    #Work Life
    data['TODO_COMPLETED'] = lifestyle_data.loc[employee_id, 'TODO_COMPLETED']
    data['LOST_VACATION'] = lifestyle_data.loc[employee_id, 'LOST_VACATION']
    data['TIME_FOR_PASSION'] = lifestyle_data.loc[employee_id, 'TIME_FOR_PASSION']
    data['FLOW'] = lifestyle_data.loc[employee_id, 'FLOW']

    data['PerfScoreID'] = hr_data.loc[employee_id, 'PerfScoreID']
    data['SpecialProjectsCount'] = hr_data.loc[employee_id, 'SpecialProjectsCount']
    data['DaysLateLast30'] = hr_data.loc[employee_id, 'DaysLateLast30']
    data['Absences'] = hr_data.loc[employee_id, 'Absences']
    data['Salary'] = hr_data.loc[employee_id, 'Salary']
    data['EngagementSurvey'] = hr_data.loc[employee_id, 'EngagementSurvey']
    data['PerformanceRating'] = attrition_data.loc[employee_id, 'PerformanceRating']
    data['YearsAtCompany'] = attrition_data.loc[employee_id, 'YearsAtCompany']
    data['YearsInCurrentRole'] = attrition_data.loc[employee_id, 'YearsInCurrentRole']
    data['YearsSinceLastPromotion'] = attrition_data.loc[employee_id, 'YearsSinceLastPromotion']
    data['YearsWithCurrManager'] = attrition_data.loc[employee_id, 'YearsWithCurrManager']
    data['PercentSalaryHike'] = attrition_data.loc[employee_id, 'PercentSalaryHike']
    data['JobSatisfaction'] = attrition_data.loc[employee_id, 'JobSatisfaction']
    data['StockOptionLevel'] = attrition_data.loc[employee_id, 'StockOptionLevel']
    data['TrainingTimesLastYear'] = attrition_data.loc[employee_id, 'TrainingTimesLastYear']
    data['JobLevel'] = attrition_data.loc[employee_id, 'JobLevel']
    data['OverTime'] = attrition_data.loc[employee_id, 'OverTime']
    data['NumCompaniesWorked'] = attrition_data.loc[employee_id, 'NumCompaniesWorked']

    data['FromDiversityJobFairID'] = hr_data.loc[employee_id, 'FromDiversityJobFairID']
    data['CitizenDesc'] = hr_data.loc[employee_id, 'CitizenDesc']
    data['HispanicLatino'] = hr_data.loc[employee_id, 'HispanicLatino']
    data['RaceDesc'] = hr_data.loc[employee_id, 'RaceDesc']
    data['Attrition'] = attrition_data.loc[employee_id, 'Attrition']
    data['BusinessTravel'] = attrition_data.loc[employee_id, 'BusinessTravel']
    data['DistanceFromHome'] = attrition_data.loc[employee_id, 'DistanceFromHome']
    data['JobInvolvement'] = attrition_data.loc[employee_id, 'JobInvolvement']


    #Subjective
    data['LIVE_VISION'] = lifestyle_data.loc[employee_id, 'LIVE_VISION']
    data['ACHIEVEMENT'] = lifestyle_data.loc[employee_id, 'ACHIEVEMENT']
    data['SUFFICIENT_INCOME'] = lifestyle_data.loc[employee_id, 'SUFFICIENT_INCOME']
    data['PERSONAL_AWARDS'] = lifestyle_data.loc[employee_id, 'PERSONAL_AWARDS']

    return score(data)
