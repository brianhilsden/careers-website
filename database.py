import os
from dotenv import load_dotenv
from sqlalchemy import create_engine,text

load_dotenv()
engine = create_engine(os.getenv("db_connection"))
def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs=result.all()
    return jobs