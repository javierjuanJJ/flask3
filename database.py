import MySQLdb
from dotenv import load_dotenv
load_dotenv()
from sqlalchemy import create_engine, text
import os

# db_connection_string = os.environ['DB_CONNECTION_STRING']

#db_connection_string = 'mysql+pymysql://ozk1rljme961lwrti1eo:pscale_pw_WQY9rfsHJdNDJW3EyfyrGsk3hlFqN1WKT3DZXxqrP4h@ap-south.connect.psdb.cloud/flask3?charset=utf8mb4'
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
      jobs.append(dict(row))
    return jobs


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text("SELECT * FROM jobs WHERE id = :val"),
      val=id
    )
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0])