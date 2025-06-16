from flask import Flask, render_template

app = Flask(__name__)
jobs = [
    {
        'id': 1,
        'title': 'Software Engineer',
        'location': 'Cairo',
        'company': 'Tech Company'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Alexandria',
        'company': 'Data Corp'
    },
    {
        'id': 3,
        'title': 'Web Developer',
        'location': 'Zagazig',
        'company': 'Web Solutions'
    },
    {
        'id': 4,
        'title': 'Mobile Developer',
        'location': 'Cairo',
        'company': 'App Innovations'
    },
    {
        'id': 5,
        'title': 'DevOps Engineer',
        'location': 'Giza',
        'company': 'Cloud Services'
    }
]
companies = [
    {
        'id': 1,
        'name': 'Tech Company',
        'location': 'Cairo',
        'industry': 'Software Development',
        'employees_count': 200
    },
    {
        'id': 2,
        'name': 'Data Corp',
        'location': 'Alexandria',
        'industry': 'Data Analytics',
        'employees_count': 150
    },
    {
        'id': 3,
        'name': 'Web Solutions',
        'location': 'Zagazig',
        'industry': 'Web Development',
        'employees_count': 50
    },
    {
        'id': 4,
        'name': 'App Innovations',
        'location': 'Cairo',
        'industry': 'Mobile Development',
        'employees_count': 75
    },
    {
        'id': 5,
        'name': 'Cloud Services',
        'location': 'Giza',
        'industry': 'Cloud Computing',
        'employees_count': 120
    }
]
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/jobs/list', methods=['GET'])
def get_jobs():
    return render_template('jobs_list.html', jobs=jobs)

@app.route('/companies/list', methods=['GET'])
def get_companies():
    return render_template('companies_list.html', companies=companies)

@app.route('/jobs/<int:job_id>', methods=['GET'])
def get_job(job_id):
    job = next((job for job in jobs if job['id'] == job_id), None)
    if job:
        return render_template('job_details.html', job=job)
    return "Job not found", 404

@app.route('/companies/<int:company_id>', methods=['GET'])
def get_company(company_id):
    company = next((company for company in companies if company['id'] == company_id), None)
    if company:
        return render_template('company_details.html', company=company)
    return "Company not found", 404

if __name__ == '__main__':
    app.run(debug=True)

