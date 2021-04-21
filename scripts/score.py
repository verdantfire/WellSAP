import math
import statistics
import math

from scripts.personal_score import personal
from scripts.personal_score import physical
from scripts.personal_score import social
from scripts.workplace_score import emp_satisfaction
from scripts.workplace_score import env_satisfaction
from scripts.workplace_score import work_life_balance
from scripts.workplace_score import workplace
from scripts.subjective_score import subjective

def score(data):

    #print(data)
    personal_keys = ['FRUITS_VEGGIES', 'DAILY_STRESS', 'BMI_RANGE', 'DONATION', 'PLACES_VISITED', 'CORE_CIRCLE', 'SUPPORTING_OTHERS', 'DAILY_STEPS','SOCIAL_NETWORK', 'SLEEP_HOURS', 'WEEKLY_MEDITATION', 'DAILY_SHOUTING', 'MaritalStatusID', 'Age_Group', 'Gender', 'RelationshipSatisfaction']
    personal_score = (personal({key: data[key] for key in personal_keys}))*100/7
    physical_score = (physical({key: data[key] for key in personal_keys}))*100/7
    social_score = (social({key: data[key] for key in personal_keys}))*100/7
    
    emp_satisfaction_keys = ['Age_Group', 'PerfScoreID', 'SpecialProjectsCount', 'DaysLateLast30', 'Absences', 'Salary', 'EngagementSurvey', 'Gender', 'PercentSalaryHike', 'PerformanceRating', 'YearsAtCompany', 'YearsInCurrentRole', 'YearsSinceLastPromotion', 'YearsWithCurrManager', 'JobSatisfaction', 'StockOptionLevel', 'TrainingTimesLastYear', 'JobLevel', 'OverTime', 'NumCompaniesWorked']
    emp_satisfaction_score = emp_satisfaction({key: data[key] for key in emp_satisfaction_keys})*100/5   
    
    env_satisfaction_keys = ['Age_Group', 'FromDiversityJobFairID', 'CitizenDesc', 'HispanicLatino', 'RaceDesc', 'Gender', 'Attrition', 'BusinessTravel', 'DistanceFromHome', 'JobInvolvement']
    env_satisfaction_score = env_satisfaction({key: data[key] for key in env_satisfaction_keys})*100/4
    
    work_life_balance_keys = ['TODO_COMPLETED', 'LOST_VACATION', 'TIME_FOR_PASSION', 'FLOW', 'Age_Group', 'Gender']
    work_life_balance_score = work_life_balance({key: data[key] for key in work_life_balance_keys})*100/4
    
    workplace_score = workplace(emp_satisfaction_score, env_satisfaction_score, work_life_balance_score)

    subjective_keys = ['LIVE_VISION', 'ACHIEVEMENT', 'SUFFICIENT_INCOME', 'PERSONAL_AWARDS']
    subjective_score = subjective({key: data[key] for key in subjective_keys})

    if personal_score == 0 or workplace_score == 0 or subjective_score == 0:
        gm = (math.log(personal_score+1) + math.log(workplace_score+1) + math.log(subjective_score+1)) / 3
        gm = math.pow(10,gm) - 1
        am = (personal_score + workplace_score + subjective_score) / 3
        final_score = gm**2/am
    
    else:
        final_score = statistics.harmonic_mean([personal_score, workplace_score, subjective_score])

    return {"Employee Name": data['employee_name'],
            "Employee ID": data['employee_id'],
            "Age": data['Age_Group'],
            "Gender": data['Gender'],
            "Wellness score": final_score,
            "Personal Wellness Score": personal_score,
            "Workplace Wellness Score": workplace_score,
            "Subjective Wellness Score": subjective_score,
            "Physical Wellness Score": physical_score,
            "Social Wellness Score": social_score,
            "Employee Satisfaction": emp_satisfaction_score,
            "Environment Satisfaction": env_satisfaction_score,
            "Work Life Balance": work_life_balance_score}
