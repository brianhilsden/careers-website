from sqlalchemy import create_engine,text
engine = create_engine("mysql+pymysql://root:-BgbEEE646GGeEF-Fg316DAG2ff55Gce@roundhouse.proxy.rlwy.net:51741/railway?charset=utf8mb4")
""" engine = create_engine("mysql+pymysql://avnadmin:AVNS_cVN41Ne4egx4yWk35tZ@mysql-7a9d636-royalty-inc20.a.aivencloud.com:16051/defaultdb?charset=utf8mb4") """

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs=result.all()
    return jobs
  
def load_job_from_db(id):
  with engine.connect() as conn:
    result=conn.execute(text(f'(select * from jobs where id={id})'))
    rows=result.all()
    if len(rows)==0:
      return  None
    else:
      return rows
    
def add_to_database(id,app):
  with engine.connect() as conn:
    conn.execute(text("INSERT INTO applications(job_id,full_name,email,github)VALUES(:job_id,:name,:email,:github)"),{"job_id":id, "name":app['Full_name'],"email":app['Email'],"github":app['github']})
    conn.commit()
  