from dotenv import load_dotenv

load_dotenv()
from sqlalchemy import create_engine, text
import os

# db_connection_string = os.environ['DB_CONNECTION_STRING']

# db_connection_string = 'mysql+pymysql://ozk1rljme961lwrti1eo:pscale_pw_WQY9rfsHJdNDJW3EyfyrGsk3hlFqN1WKT3DZXxqrP4h@ap-south.connect.psdb.cloud/flask3?charset=utf8mb4'
db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    })


# connection = MySQLdb.connect(
#   host= os.getenv("HOST"),
#   user=os.getenv("USERNAME"),
#   passwd= os.getenv("PASSWORD"),
#   db= os.getenv("DATABASE"),
#   ssl_mode = "VERIFY_IDENTITY",
#   ssl      = {
#     "ca": "/etc/ssl/cert.pem"
#   }
# )


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.all():
            print(row)
            # jobs.append(dict(row))
            jobs.append(row._mapping)
        return jobs


def load_job_from_db(id):
    with engine.connect() as conn:
        query = text("SELECT * FROM jobs WHERE id = :val")
        data = {'val': id}
        result = conn.execute(query, data)
        rows = result.all()
        if len(rows) == 0:
            return None
        else:
            return rows[0]


def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        query = text(
            "INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")
        data = {
            'job_id': job_id,
            'full_name': data['full_name'],
            'email': data['email'],
            'linkedin_url': data['linkedin_url'],
            'education': data['education'],
            'work_experience': data['work_experience'],
            'resume_url': data['resume_url']
        }
        conn.execute(query,data)
