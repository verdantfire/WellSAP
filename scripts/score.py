import math
import statistics
import math

from .personal_score import personal
from .workplace_score import emp_satifaction
from .workplace_score import env_satisfaction
from .workplace_score import work_life_balance
from .workplace_score import workplace_score
from .subjective_score import subjective

def score(data):

    personal_keys = ['FRUITS_VEGGIES', 'DAILY_STRESS', 'BMI_RANGE', 'DONATION', 'PLACES_VISITED', 'CORE_CIRCLE', 'SUPPORTING_OTHERS', 'SOCIAL_NETWORK', 'SLEEP_HOURS', 'WEEKLY_MEDITATION', 'DAILY_SHOUTING', 'MaritalStatusID', 'Age_Group', 'Gender', 'RelationshipSatisfaction']
    personal = personal({key: data[key] for key in personal_keys}) 
    
    emp_satifaction_keys = ['Age_Group', 'FromDiversityJobFairID', 'CitizenDesc', 'HispanicLatino', 'RaceDesc', 'Gender', 'Attrition', 'BusinessTravel', 'DistanceFromHome', 'JobInvolvement']
    emp_satifaction = emp_satifaction({key: data[key] for key in emp_satifaction_keys})
    
    env_satisfaction_keys = ['Age_Group', 'PerfScoreID', 'SpecialProjectsCount', 'DaysLateLast30', 'Absences', 'Salary', 'EngagementSurvey', 'Gender', 'PercentSalaryHike', 'PerformanceRating', 'YearsAtCompany', 'YearsInCurrentRole', 'YearsSinceLastPromotion', 'YearsWithCurrManager', 'JobSatisfaction', 'StockOptionLevel', 'TrainingTimesLastYear', 'JobLevel', 'OverTime', 'NumCompaniesWorked']
    env_satisfaction = env_satisfaction({key: data[key] for key in env_satisfaction_keys})
    
    work_life_balance_keys = ['TODO_COMPLETED', 'LOST_VACATION', 'TIME_FOR_PASSION', 'FLOW', 'Age_Group', 'Gender']
    work_life_balance = work_life_balance({key: data[key] for key in work_life_balance_keys})
    
    workplace = workplace_score(emp_satifaction, env_satisfaction, work_life_balance)

    subjective_keys = ['LIVE_VISION', 'ACHIEVEMENT', 'SUFFICIENT_INCOME', 'PERSONAL_AWARDS']
    subjective = subjective({key: data[key] for key in subjective_keys})

    if personal == 0 or workplace == 0 or subjective == 0:
        personal_gm = math.log(personal+1)
        workplace_gm = math.log(workplace+1)
        subjective_gm = math.log(subjective+1)
        gm = (personal_gm + workplace_gm + subjective_gm) / 3
        gm = math.pow(10,gm) - 1
        am = (personal + workplace + subjective) / 3
        score = gm**2/am
    
    else:
        score = statistics.harmonic_mean([personal, workplace, subjective])

    return score