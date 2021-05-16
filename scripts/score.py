import math
import statistics

from scripts.personal_score import personal
from scripts.personal_score import physical
from scripts.personal_score import social
from scripts.workplace_score import emp_satisfaction
from scripts.workplace_score import env_satisfaction
from scripts.workplace_score import work_life_balance
from scripts.workplace_score import workplace
from scripts.subjective_score import subjective
from scripts.programs import wellness_programs

def score(data):

    result = {"Employee Name": data['employee_name'],
            "Age": data['Age_Group'],
            "Gender": data['Gender']}

    personal_keys = ['FRUITS_VEGGIES', 'DAILY_STRESS', 'BMI_RANGE', 'DONATION', 'PLACES_VISITED', 'CORE_CIRCLE', 'SUPPORTING_OTHERS', 'DAILY_STEPS','SOCIAL_NETWORK', 'SLEEP_HOURS', 'WEEKLY_MEDITATION', 'DAILY_SHOUTING', 'MaritalStatusID', 'Age_Group', 'Gender', 'RelationshipSatisfaction']
    personal_score = round((personal({key: data[key] for key in personal_keys}))*100/7,3)
    result["Personal Wellness Score"] = personal_score
    physical_score = round((physical({key: data[key] for key in personal_keys}))*100/7,3)
    result["Physical Wellness Score"] = physical_score
    social_score = round((social({key: data[key] for key in personal_keys}))*100/7,3)
    result["Social Wellness Score"] = social_score

    emp_satisfaction_keys = ['Age_Group', 'PerfScoreID', 'SpecialProjectsCount', 'DaysLateLast30', 'Absences', 'Salary', 'EngagementSurvey', 'Gender', 'PercentSalaryHike', 'PerformanceRating', 'YearsAtCompany', 'YearsInCurrentRole', 'YearsSinceLastPromotion', 'YearsWithCurrManager', 'JobSatisfaction', 'StockOptionLevel', 'TrainingTimesLastYear', 'JobLevel', 'OverTime', 'NumCompaniesWorked']
    emp_satisfaction_score = round(emp_satisfaction({key: data[key] for key in emp_satisfaction_keys})*100/5,3)
    result["Employee Satisfaction"] = emp_satisfaction_score
    
    env_satisfaction_keys = ['Age_Group', 'FromDiversityJobFairID', 'CitizenDesc', 'HispanicLatino', 'RaceDesc', 'Gender', 'Attrition', 'BusinessTravel', 'DistanceFromHome', 'JobInvolvement']
    env_satisfaction_score = round(env_satisfaction({key: data[key] for key in env_satisfaction_keys})*100/4,3)
    result["Environment Satisfaction"] = env_satisfaction_score

    work_life_balance_keys = ['TODO_COMPLETED', 'LOST_VACATION', 'TIME_FOR_PASSION', 'FLOW', 'Age_Group', 'Gender']
    work_life_balance_score = round(work_life_balance({key: data[key] for key in work_life_balance_keys})*100/4,3)
    result["Work Life Balance"] = work_life_balance_score
    
    workplace_score = round(workplace(emp_satisfaction_score, env_satisfaction_score, work_life_balance_score),3)
    result["Workplace Wellness Score"] = workplace_score

    subjective_keys = ['LIVE_VISION', 'ACHIEVEMENT', 'SUFFICIENT_INCOME', 'PERSONAL_AWARDS']
    subjective_score = round(subjective({key: data[key] for key in subjective_keys}),3)
    result["Subjective Wellness Score"] = subjective_score

    if personal_score == 0 or workplace_score == 0 or subjective_score == 0:
        gm = (math.log(personal_score+1) + math.log(workplace_score+1) + math.log(subjective_score+1)) / 3
        gm = math.pow(10,gm) - 1
        am = (personal_score + workplace_score + subjective_score) / 3
        final_score = round(gm**2/am,3)
    
    else:
        final_score = round(statistics.harmonic_mean([personal_score, workplace_score, subjective_score]),3)
    result["Wellness score"] = final_score


    wellness_programs_list = wellness_programs(result)
    result["Wellness Programs List"] = wellness_programs_list

    return result