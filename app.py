from flask import Flask, render_template, jsonify, Response, json, request

import database
from Job import Job

app = Flask(__name__)



# JOBS = [
#     {
#         'id': 1,
#         'title': 'Data Analyst',
#         'location': 'Bengaluru, India',
#         'salary': 'Rs. 10,00,000'
#     },
#     {
#         'id': 2,
#         'title': 'Data Scientist',
#         'location': 'Delhi, India',
#         'salary': 'Rs. 15,00,000'
#     },
#     {
#         'id': 3,
#         'title': 'Frontend Engineer',
#         'location': 'Remote'
#     },
#     {
#         'id': 4,
#         'title': 'Backend Engineer',
#         'location': 'San Francisco, USA',
#         'salary': '$150,000'
#     }
# ]




@app.route('/')
def hello_world():  # put application's code here
    JOBS = database.load_jobs_from_db()
    return render_template('home.html', jobs = JOBS, company_name='')

@app.route('/api/jobs')
def list_jobs():  # put application's code here
    JOBS = database.load_jobs_from_db()
    return jsonify(JOBS.__str__())

@app.route("/job/<id>")
def show_job(id):
    job = database.load_job_from_db(id)

    if not job:
        return "Not Found", 404

    jobShow = Job(job[0],job[1],job[2],job[3],job[4],job[5],job[6],job[7],job[8])

    return render_template('jobpage.html', job=jobShow)



@app.route("/api/job/<id>")
def show_job_json(id):
  job = database.load_job_from_db(id)
  return jsonify(job.__str__())

@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
  data = request.form
  job = database.load_job_from_db(id)
  database.add_application_to_db(id, data)
  return render_template('application_submitted.html',application=data, job=job)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
