from flask import Flask,render_template,jsonify,request
from database import load_jobs_from_db,load_job_from_db,add_to_database

app=Flask(__name__)

@app.route("/")
def hello_brian():
  jobs=load_jobs_from_db()
  return render_template('home.html',jobs=jobs,company_name="Royalty")

@app.route("/job/<id>")
def show_job(id):
  job=load_job_from_db(id)
  if not job:
    return " Not found",404
  return render_template('jobpage.html',id=job[0][0], title=job[0][1],location=job[0][2],salary=job[0][3],currency=job[0][4])

@app.route("/job/<id>/apply",methods=["post"])
def apply_to_job(id):
  data=request.form.to_dict()
  job=load_job_from_db(id)
  add_to_database(id,data)
 
  return render_template('application_submitted.html',application=data,job=job)



if __name__ == '__main__':
  app.run(debug=True)