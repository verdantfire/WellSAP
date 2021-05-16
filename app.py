import numpy as np
from flask import Flask, request, jsonify, render_template, flash, redirect, url_for
from werkzeug.utils import secure_filename
import pickle
import csv
from scripts.id import data_id
from scripts.score import score
from scripts.programs import wellness_programs
import pandas as pd

app = Flask(__name__)

results = {}
programs = {}

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    global results
    global programs
    results = {}
    programs = {}
    return render_template('home.html')

@app.route('/empid')
@app.route('/use_employee_id')
def empid():
    return render_template('empid.html')

@app.route('/empd', methods=['GET', 'POST'])
@app.route('/use_employee_details', methods=['GET', 'POST'])
def empd():
    return render_template('empd.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    return render_template('upload.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    global results
    global programs
    if request.method == "POST":
        if request.form.get("employee_id") != None:
            global results
            global programs

            results = data_id(int(request.form.get("employee_id")))
            #session['report_results'] = results
            programs = wellness_programs(results)
            if programs == []:
                return render_template('result.html', employee_name = results['Employee Name'], Age_Group = results['Age'], Gender = results['Gender'], wellness_score = results["Wellness score"],personal_wellness_score = results["Personal Wellness Score"],workplace_wellness_score = results["Workplace Wellness Score"],subjective_wellness_score = results["Subjective Wellness Score"],physical = results["Physical Wellness Score"],social = results["Social Wellness Score"] ,emp_satifaction = results["Employee Satisfaction"],env_satisfaction = results["Environment Satisfaction"],work_life_balance = results["Work Life Balance"], programs_count=0)

            else:  
                return render_template('result.html', employee_name = results['Employee Name'], Age_Group = results['Age'], Gender = results['Gender'], wellness_score = results["Wellness score"],personal_wellness_score = results["Personal Wellness Score"],workplace_wellness_score = results["Workplace Wellness Score"],subjective_wellness_score = results["Subjective Wellness Score"],physical = results["Physical Wellness Score"],social = results["Social Wellness Score"] ,emp_satifaction = results["Employee Satisfaction"],env_satisfaction = results["Environment Satisfaction"],work_life_balance = results["Work Life Balance"], programs_count=len(programs), program_0 = programs[0]+" and "+str(len(programs)-1)+" others")

           # return render_template('result.html', employee_name = "Lorem Ipsum", Age_Group = '69', Gender = 'AH64 Apache Longbow', wellness_score = results["Wellness score"],personal_wellness_score = results["Personal Wellness Score"],workplace_wellness_score = results["Workplace Wellness Score"],subjective_wellness_score = results["Subjective Wellness Score"],physical = results["Physical Wellness Score"],social = results["Social Wellness Score"] ,emp_satifaction = results["Employee Satisfaction"],env_satisfaction = results["Environment Satisfaction"],work_life_balance = results["Work Life Balance"])
        elif request.form.get("employee_name") != None:
            data = {}
            # global results
            # global programs
            # getting input with name = fname in HTML form
            for key, val in request.form.items():
                data[key] = val
            
            for k,v in data.items():
                try:
                    data[k] = int(float(v))
                except:
                    continue
            results = score(data)
            programs = wellness_programs(results)
            if programs == []:
                return render_template('result.html', employee_name = results['Employee Name'], Age_Group = results['Age'], Gender = results['Gender'], wellness_score = results["Wellness score"], personal_wellness_score = results["Personal Wellness Score"],workplace_wellness_score = results["Workplace Wellness Score"],subjective_wellness_score = results["Subjective Wellness Score"],physical = results["Physical Wellness Score"],social = results["Social Wellness Score"] ,emp_satifaction = results["Employee Satisfaction"],env_satisfaction = results["Environment Satisfaction"],work_life_balance = results["Work Life Balance"], programs_count=0)
            
            else:
                return render_template('result.html', employee_name = results['Employee Name'], Age_Group = results['Age'], Gender = results['Gender'], wellness_score = results["Wellness score"], personal_wellness_score = results["Personal Wellness Score"],workplace_wellness_score = results["Workplace Wellness Score"],subjective_wellness_score = results["Subjective Wellness Score"],physical = results["Physical Wellness Score"],social = results["Social Wellness Score"] ,emp_satifaction = results["Employee Satisfaction"],env_satisfaction = results["Environment Satisfaction"],work_life_balance = results["Work Life Balance"], programs_count=len(programs), program_0 = programs[0]+" and "+str(len(programs)-1)+" others")

            #return render_template('result.html', employee_name = "Lorem Ipsum", Age_Group = '69', Gender = 'AH64 Apache Longbow', wellness_score = results["Wellness score"],personal_wellness_score = results["Personal Wellness Score"],workplace_wellness_score = results["Workplace Wellness Score"],subjective_wellness_score = results["Subjective Wellness Score"],physical = results["Physical Wellness Score"],social = results["Social Wellness Score"] ,emp_satifaction = results["Employee Satisfaction"],env_satisfaction = results["Environment Satisfaction"],work_life_balance = results["Work Life Balance"])
        
        else:
            # global results
            # global programs

            csv_df = pd.read_csv(request.files.get('fileupload'))
            data = {}

            for key, val in zip(csv_df.columns.to_list(),csv_df.iloc[0].to_list()):
                data[key] = val

            for k,v in data.items():
                try:
                    data[k] = int(float(v))
                except:
                    continue
            results = score(data)
            programs = wellness_programs(results)

            if programs == []:
                return render_template('result.html', employee_name = results['Employee Name'], Age_Group = results['Age'], Gender = results['Gender'], wellness_score = results["Wellness score"], personal_wellness_score = results["Personal Wellness Score"],workplace_wellness_score = results["Workplace Wellness Score"],subjective_wellness_score = results["Subjective Wellness Score"],physical = results["Physical Wellness Score"],social = results["Social Wellness Score"] ,emp_satifaction = results["Employee Satisfaction"],env_satisfaction = results["Environment Satisfaction"],work_life_balance = results["Work Life Balance"], programs_count=0)
            
            else:
                return render_template('result.html', employee_name = results['Employee Name'], Age_Group = results['Age'], Gender = results['Gender'], wellness_score = results["Wellness score"], personal_wellness_score = results["Personal Wellness Score"],workplace_wellness_score = results["Workplace Wellness Score"],subjective_wellness_score = results["Subjective Wellness Score"],physical = results["Physical Wellness Score"],social = results["Social Wellness Score"] ,emp_satifaction = results["Employee Satisfaction"],env_satisfaction = results["Environment Satisfaction"],work_life_balance = results["Work Life Balance"], programs_count=len(programs), program_0 = programs[0]+" and "+str(len(programs)-1)+" others")
                    
@app.route('/compare', methods=['GET','POST'])
def compare():
    global results
    global programs
    results_avg = {"Wellness score":51.932, "Personal Wellness Score": 42.857,
            "Workplace Wellness Score": 71.539,
            "Subjective Wellness Score": 48.885,
            "Physical Wellness Score": 88.860,
            "Social Wellness Score": 97.346,
            "Employee Satisfaction": 77.814,
            "Environment Satisfaction": 69.293,
            "Work Life Balance": 68.248}

    return render_template('compare.html', employee_name = results["Employee Name"], Age_Group = results["Age"], Gender = results["Gender"], wellness_score = results["Wellness score"],personal_wellness_score = results["Personal Wellness Score"],workplace_wellness_score = results["Workplace Wellness Score"],subjective_wellness_score = results["Subjective Wellness Score"],physical = results["Physical Wellness Score"],social = results["Social Wellness Score"] ,emp_satifaction = results["Employee Satisfaction"],env_satisfaction = results["Environment Satisfaction"],work_life_balance = results["Work Life Balance"], wellness_score_avg = results_avg["Wellness score"], personal_wellness_score_avg = results_avg["Personal Wellness Score"],workplace_wellness_score_avg = results_avg["Workplace Wellness Score"],subjective_wellness_score_avg = results_avg["Subjective Wellness Score"],physical_avg = results_avg["Physical Wellness Score"],social_avg = results_avg["Social Wellness Score"] ,emp_satifaction_avg = results_avg["Employee Satisfaction"],env_satisfaction_avg = results_avg["Environment Satisfaction"],work_life_balance_avg = results_avg["Work Life Balance"], program_0 = str(programs[0]))

@app.route('/programs_info')
def programs_info():
    global results
    global programs

    while len(programs)!=9:
        programs.append("")

    return render_template("programs_info.html", program_0 = programs[0], program_1 = programs[1], program_2 = programs[2], program_3 = programs[3], program_4 = programs[4], program_5 = programs[5], program_6 = programs[6], program_7 = programs[7], program_8 = programs[8] )
@app.route('/about')
@app.route('/about_us')
def about():
    return render_template('about.html')
if __name__ == "__main__":
    app.run(debug=False)