from flask import Flask, render_template, request
from project import StudyAdvisor

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    countries = list(StudyAdvisor.universities_data.keys())
    degrees = []
    universities = []

    if request.method == 'POST':
        country = request.form.get('country')
        degree = request.form.get('degree')

        advisor = StudyAdvisor(country)
        degrees = advisor.get_degrees()

        if degree:
            advisor.degree = degree
            universities = advisor.get_universities()

    return render_template('index.html', countries=countries, degrees=degrees, universities=universities)

if __name__ == '__main__':
    app.run(debug=True)