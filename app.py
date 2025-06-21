from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SECRET_KEY'] = 'iTi_Assuit_2025'

db = SQLAlchemy(app)
migrate = Migrate(app, db)



class Job(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable = False)
    company = db.Column(db.String(200), nullable = False)
    location = db.Column(db.String(200), nullable = False)
    
    def __repr__(self):
        return f"{self.title}"


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    industry = db.Column(db.String(200), nullable=False)
    employees_count = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f"{self.name}"
    
    

class JobCreationForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    company = StringField("Company", validators=[DataRequired()])
    location = StringField("Location", validators=[DataRequired()])
    submit = SubmitField("Create Job")


class CompanyCreationForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    location = StringField("Location", validators=[DataRequired()])
    industry = StringField("Industry", validators=[DataRequired()])
    employees_count = IntegerField("Employees Count", validators=[DataRequired()])
    submit = SubmitField("Create Company")


# @app.route("/", methods = ['GET']) # url
# def hello_world(): # view
#     return "Hello, Assiut!"


# @app.route('/<str: name>')
# def hello(name):
#     return f'Hello, {name}!'


@app.route('/jobs/list', methods = ['GET'])
def list_jobs():
    jobs = Job.query.all()
    return render_template('jobs_list.html', jobs = jobs)


@app.route('/jobs/<id>', methods = ['GET'])
def get_job(id):
    job = Job.query.get(id)
    return render_template('jobs_list.html', jobs = [job])
    

@app.route('/jobs/create', methods = ['GET', 'POST'])
def create_job():
    form = JobCreationForm()
    if form.validate_on_submit():
        title = form.title.data
        company = form.company.data
        location = form.location.data
        
        new_job = Job(
            title = title,
            company = company,
            location = location
        )
        
        db.session.add(new_job)
        db.session.commit()
        return redirect(url_for('list_jobs'))
        
    return render_template('create_job.html', form = form)


@app.route('/companies/list', methods=['GET'])
def list_companies():
    companies = Company.query.all()
    return render_template('companies_list.html', companies=companies)


@app.route('/companies/<id>', methods=['GET'])
def get_company(id):
    company = Company.query.get(id)
    return render_template('company_details.html', company=company)
    

@app.route('/companies/create', methods=['GET', 'POST'])
def create_company():
    form = CompanyCreationForm()
    if form.validate_on_submit():
        new_company = Company(
            name=form.name.data,
            location=form.location.data,
            industry=form.industry.data,
            employees_count=form.employees_count.data
        )
        
        db.session.add(new_company)
        db.session.commit()
        return redirect(url_for('list_companies'))
        
    return render_template('create_company.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)