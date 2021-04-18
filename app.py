import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from .scripts.id import data_id
# from scripts.score import score

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/empid')
def empid():
    return render_template('empid.html')

@app.route('/empd', methods=['GET', 'POST'])
def empd():
    return render_template('empd.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == "POST":
        if request.form.get("employee_id") != None:
            results = data_id(str(render_template('result.html'))
            return render_template('result.html', wellness_score = results["Wellness score"], personal_wellness_score=results["Personal Wellness Score"],workplace_wellness_score=results["Workplace Wellness Score",subjective_wellness_score=results["Subjective Wellness Score"],physical = results["Physical Wellness Score"], social = results["Social Wellness Score"] ,emp_satifaction = results["Employee Satisfaction"],env_satisfaction = results["Environment Satisfaction"],work_life_balance = results["Work Life Balance"])
        else:
            data = {}
            # getting input with name = fname in HTML form
            data["employee_name"] = request.form.get("employee_name")
             # getting input with name = lname in HTML form 
            last_name[] = request.form.get("employee_name") 
            return render_template('result.html', wellness_score="Your name is "+first_name + last_name,personal_wellness_score=last_name,workplace_wellness_score=12,subjective_wellness_score=13, sub_score_1=None, sub_score_2=None, sub_score_3=None)


if __name__ == "__main__":
    app.run(debug=True)