from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title':'',
        'location':'',
        'salary':'',
    },
    {
        'id': 2,
        'title':'',
        'location':'',
        'salary':'',
    },
    {
        'id': 3,
        'title':'',
        'location':'',
        'salary':'',
    },
]

@app.route('/')
def hello_world():  # put application's code here
    return render_template('home.html', jobs = JOBS, company_name='')

@app.route('/api/jobs')
def hello_world():  # put application's code here
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
