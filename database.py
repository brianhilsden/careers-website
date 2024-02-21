from sqlalchemy import create_engine,text
engine = create_engine("mysql+pymysql://root:-BgbEEE646GGeEF-Fg316DAG2ff55Gce@roundhouse.proxy.rlwy.net:51741/railway?charset=utf8mb4")
def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs=result.all()
    return jobs