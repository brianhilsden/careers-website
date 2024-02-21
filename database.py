import os
from sqlalchemy import create_engine,text
from dotenv import load_dotenv,find_dotenv
dotenv_path=find_dotenv()
load_dotenv(dotenv_path)
engine = create_engine(os.getenv("db_connect"))
def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs=result.all()
    return jobs