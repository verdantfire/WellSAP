import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from scripts.id import data_id
from scripts.score import score

app = Flask(__name__)

results = {}

@app.route('/')
@app.route('/home')
def home():
    global results
    results = {}
    return render_template('home.html')

@app.route('/empid')
@app.route('/use_employee_id')
def empid():
    return render_template('empid.html')

@app.route('/empd', methods=['GET', 'POST'])
@app.route('/use_employee_details', methods=['GET', 'POST'])
def empd():
    return render_template('empd.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    global results
    if request.method == "POST":
        if request.form.get("employee_id") != None:
            global results
            results = data_id(int(request.form.get("employee_id")))
            #session['report_results'] = results
            
            return render_template('result.html', employee_name = results['Employee Name'], Age_Group = results['Age'], Gender = results['Gender'], wellness_score = results["Wellness score"],personal_wellness_score = results["Personal Wellness Score"],workplace_wellness_score = results["Workplace Wellness Score"],subjective_wellness_score = results["Subjective Wellness Score"],physical = results["Physical Wellness Score"],social = results["Social Wellness Score"] ,emp_satifaction = results["Employee Satisfaction"],env_satisfaction = results["Environment Satisfaction"],work_life_balance = results["Work Life Balance"])
           # return render_template('result.html', employee_name = "Lorem Ipsum", Age_Group = '69', Gender = 'AH64 Apache Longbow', wellness_score = results["Wellness score"],personal_wellness_score = results["Personal Wellness Score"],workplace_wellness_score = results["Workplace Wellness Score"],subjective_wellness_score = results["Subjective Wellness Score"],physical = results["Physical Wellness Score"],social = results["Social Wellness Score"] ,emp_satifaction = results["Employee Satisfaction"],env_satisfaction = results["Environment Satisfaction"],work_life_balance = results["Work Life Balance"])
        else:
            data = {}
            #global results
            # getting input with name = fname in HTML form
            for key, val in request.form.items():
                data[key] = val
            
            for k,v in data.items():
                try:
                    data[k] = int(float(v))
                except:
                    continue
            results = score(data)
            return render_template('result.html', employee_name = results['Employee Name'], Age_Group = results['Age'], Gender = results['Gender'], wellness_score = results["Wellness score"], personal_wellness_score = results["Personal Wellness Score"],workplace_wellness_score = results["Workplace Wellness Score"],subjective_wellness_score = results["Subjective Wellness Score"],physical = results["Physical Wellness Score"],social = results["Social Wellness Score"] ,emp_satifaction = results["Employee Satisfaction"],env_satisfaction = results["Environment Satisfaction"],work_life_balance = results["Work Life Balance"])
            #return render_template('result.html', employee_name = "Lorem Ipsum", Age_Group = '69', Gender = 'AH64 Apache Longbow', wellness_score = results["Wellness score"],personal_wellness_score = results["Personal Wellness Score"],workplace_wellness_score = results["Workplace Wellness Score"],subjective_wellness_score = results["Subjective Wellness Score"],physical = results["Physical Wellness Score"],social = results["Social Wellness Score"] ,emp_satifaction = results["Employee Satisfaction"],env_satisfaction = results["Environment Satisfaction"],work_life_balance = results["Work Life Balance"])

@app.route('/compare', methods=['GET','POST'])
def compare():
    global results
    results_avg = {"Wellness score":51.932, "Personal Wellness Score": 42.857,
            "Workplace Wellness Score": 71.539,
            "Subjective Wellness Score": 48.885,
            "Physical Wellness Score": 88.860,
            "Social Wellness Score": 97.346,
            "Employee Satisfaction": 77.814,
            "Environment Satisfaction": 69.293,
            "Work Life Balance": 68.248}

    return render_template('compare.html', employee_name = results["Employee Name"], Age_Group = results["Age"], Gender = results["Gender"], wellness_score = results["Wellness score"],personal_wellness_score = results["Personal Wellness Score"],workplace_wellness_score = results["Workplace Wellness Score"],subjective_wellness_score = results["Subjective Wellness Score"],physical = results["Physical Wellness Score"],social = results["Social Wellness Score"] ,emp_satifaction = results["Employee Satisfaction"],env_satisfaction = results["Environment Satisfaction"],work_life_balance = results["Work Life Balance"], wellness_score_avg = results_avg["Wellness score"], personal_wellness_score_avg = results_avg["Personal Wellness Score"],workplace_wellness_score_avg = results_avg["Workplace Wellness Score"],subjective_wellness_score_avg = results_avg["Subjective Wellness Score"],physical_avg = results_avg["Physical Wellness Score"],social_avg = results_avg["Social Wellness Score"] ,emp_satifaction_avg = results_avg["Employee Satisfaction"],env_satisfaction_avg = results_avg["Environment Satisfaction"],work_life_balance_avg = results_avg["Work Life Balance"])

@app.route('/about')
@app.route('/about_us')
def about():
    return render_template('about.html')
if __name__ == "__main__":
    app.run(debug=False)