from pickle import APPEND


def wellness_programs(result):

    wellness_programs_list = []
    
    if result["Wellness score"] < 51.932:
        wellness_programs_list.append('Overall Wellness Program')
    
    if result["Personal Wellness Score"] < 42.857:
        wellness_programs_list.append('Personal Wellness Program')
    
    if result["Physical Wellness Score"] < 88.86:
        wellness_programs_list.append('Physical Wellness Program')
    
    if result["Social Wellness Score"] < 97.346:
        wellness_programs_list.append('Social Wellness Program')
    
    if result["Workplace Wellness Score"] < 71.539:
        wellness_programs_list.append('Workplace Wellness Program')
    
    if result["Employee Satisfaction"] < 77.814:
        wellness_programs_list.append('Employee Satisfaction Wellness Program')
    
    if result["Environment Satisfaction"] < 69.293:
        wellness_programs_list.append('Environment Satisfaction Wellness Program')
    
    if result["Work Life Balance"] < 68.248:
        wellness_programs_list.append('Work Life Balance Wellness Program')
    
    if result["Subjective Wellness Score"] < 48.885:
        wellness_programs_list.append('Subjective Wellness Program')

    return wellness_programs_list