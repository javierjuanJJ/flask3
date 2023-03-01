from flask import Flask, render_template, jsonify

import database

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

JOBS = database.load_jobs_from_db()


@app.route('/')
def hello_world():  # put application's code here
    return render_template('home.html', jobs = JOBS, company_name='')

@app.route('/api/jobs')
def list_jobs():  # put application's code here
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
