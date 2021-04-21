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
            print('--- original order ---')
            for key, val in request.form.items():
                data[key] = val

            results = score(data)
            #session['report_results'] = results

            return render_template('result.html', employee_name = results['Employee Name'], Age_Group = results['Age'], Gender = results['Gender'], wellness_score = results["Wellness score"], personal_wellness_score = results["Personal Wellness Score"],workplace_wellness_score = results["Workplace Wellness Score"],subjective_wellness_score = results["Subjective Wellness Score"],physical = results["Physical Wellness Score"],social = results["Social Wellness Score"] ,emp_satifaction = results["Employee Satisfaction"],env_satisfaction = results["Environment Satisfaction"],work_life_balance = results["Work Life Balance"])
            #return render_template('result.html', employee_name = "Lorem Ipsum", Age_Group = '69', Gender = 'AH64 Apache Longbow', wellness_score = results["Wellness score"],personal_wellness_score = results["Personal Wellness Score"],workplace_wellness_score = results["Workplace Wellness Score"],subjective_wellness_score = results["Subjective Wellness Score"],physical = results["Physical Wellness Score"],social = results["Social Wellness Score"] ,emp_satifaction = results["Employee Satisfaction"],env_satisfaction = results["Environment Satisfaction"],work_life_balance = results["Work Life Balance"])

@app.route('/compare', methods=['GET','POST'])
def compare():
    global results
    results_avg = {"Wellness score":51.931927366908305, "Personal Wellness Score": 42.85714285714247,
            "Workplace Wellness Score": 71.53872985658633,
            "Subjective Wellness Score": 48.88504090599943,
            "Physical Wellness Score": 88.85961065464072,
            "Social Wellness Score": 97.3460764539568,
            "Employee Satisfaction": 77.81350482315112,
            "Environment Satisfaction": 69.29260450160771,
            "Work Life Balance": 68.2475884244373}

    return render_template('compare.html', employee_name = results["Employee Name"], Age_Group = results["Age"], Gender = results["Gender"], wellness_score = results["Wellness score"],personal_wellness_score = results["Personal Wellness Score"],workplace_wellness_score = results["Workplace Wellness Score"],subjective_wellness_score = results["Subjective Wellness Score"],physical = results["Physical Wellness Score"],social = results["Social Wellness Score"] ,emp_satifaction = results["Employee Satisfaction"],env_satisfaction = results["Environment Satisfaction"],work_life_balance = results["Work Life Balance"], wellness_score_avg = results_avg["Wellness score"], personal_wellness_score_avg = results_avg["Personal Wellness Score"],workplace_wellness_score_avg = results_avg["Workplace Wellness Score"],subjective_wellness_score_avg = results_avg["Subjective Wellness Score"],physical_avg = results_avg["Physical Wellness Score"],social_avg = results_avg["Social Wellness Score"] ,emp_satifaction_avg = results_avg["Employee Satisfaction"],env_satisfaction_avg = results_avg["Environment Satisfaction"],work_life_balance_avg = results_avg["Work Life Balance"])

if __name__ == "__main__":
    app.run(debug=True)