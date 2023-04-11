
from sqlalchemy.orm import Session
from sqlalchemy import func, case, text
import models
from db import engine
import decimal, datetime, json

import schemas

def alchemyencoder(obj):
    """JSON encoder function for SQLAlchemy special classes."""
    if isinstance(obj, datetime.date):
        return obj.isoformat()
    elif isinstance(obj, decimal.Decimal):
        return float(obj)


class HiredEmployeeRepo:
    
 async def create(db: Session, hired_employee: schemas.HiredEmployeeCreate):
        db_hired_employee = models.HiredEmployee(name=hired_employee.name,datetime=hired_employee.datetime,
            department_id=hired_employee.department_id, job_id=hired_employee.job_id)
        db.add(db_hired_employee)
        db.commit()
        db.refresh(db_hired_employee)
        return db_hired_employee
    
 def fetch_by_id(db: Session,_id):
     return db.query(models.HiredEmployee).filter(models.HiredEmployee.id == _id).first()
 
 def fetch_by_name(db: Session,name):
     return db.query(models.HiredEmployee).filter(models.HiredEmployee.name == name).first()
 
 def fetch_all(db: Session, skip: int = 0, limit: int = 100):
     return db.query(models.HiredEmployee).offset(skip).limit(limit).all()

 def employees_hired(db: Session,name):
    ##return db.query(models.HiredEmployee.department_id, models.HiredEmployee.job_id, func.count((models.HiredEmployee.id).label('count_id')
      ##  ).filter(models.HiredEmployee.datetime == "2021"
      ##  ).group_by(models.HiredEmployee.department_id, models.HiredEmployee.job_id
        ##).all())
    #print(db.execute(text("select * from departments")))


    # user_counts = db.query(
    #             models.HiredEmployee.job_id, models.HiredEmployee.department_id,
    #             func.count(models.HiredEmployee.job_id).label("total_counts")
    #         ).filter(

    #         ).group_by(
    #             models.HiredEmployee.job_id, models.HiredEmployee.department_id
    #         ).all()
    print("111111")
    json_response = {}
    with engine.connect() as con:
        rs = con.execute("""SELECT d.department, j.job,
                    sum(he1.Q1) AS Q1,
                    sum(he1.Q2) AS Q2,
                    sum(he1.Q3) AS Q3,
                    sum(he1.Q4) AS Q4
                    FROM (SELECT *,
                        CASE 
                            WHEN he.month_datetime < 4 THEN 1
                        END AS Q1,
                        CASE 
                            WHEN he.month_datetime > 3 and he.month_datetime < 7 THEN 1
                        END AS Q2,
                        CASE 
                            WHEN he.month_datetime > 6 and he.month_datetime < 10 THEN 1
                        END AS Q3,
                        CASE 
                            WHEN he.month_datetime > 9 THEN 1
                        END AS Q4
                    FROM 
                    (SELECT *, 
                        CAST(strftime('%m', DATE(datetime)) as int) as month_datetime 
                    FROM hired_employees) as he) as he1 inner join departments d on d.id = he1.department_id
                    inner JOIN jobs j on j.id = he1.job_id
                    GROUP BY d.department, j.job;""")
        
        json_response = json.dumps([dict(r) for r in rs], default=alchemyencoder)
        for row in rs:
            print(row)


    print(json_response)
    #user_counts = con.execute("select * from departments")
    return json_response
    #print(user_counts)
    #return db.query(models.HiredEmployee).count()
    #return user_counts




 
 async def delete(db: Session,item_id):
     db_item= db.query(models.HiredEmployee).filter_by(id=item_id).first()
     db.delete(db_item)
     db.commit()
     
     
 async def update(db: Session,item_data):
    updated_item = db.merge(item_data)
    db.commit()
    return updated_item
    
    
    
class DepartmentRepo:
    
    async def create(db: Session, department: schemas.DepartmentCreate):
            db_department = models.Department(department=department.department)
            db.add(db_department)
            db.commit()
            db.refresh(db_department)
            return db_department
        
    def fetch_by_id(db: Session,_id:int):
        return db.query(models.Department).filter(models.Department.id == _id).first()
    
    def fetch_by_name(db: Session,department:str):
        return db.query(models.Department).filter(models.Department.department == department).first()
    
    def fetch_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Department).offset(skip).limit(limit).all()
    
    async def delete(db: Session,_id:int):
        db_store= db.query(models.Department).filter_by(id=_id).first()
        db.delete(db_store)
        db.commit()
        
    async def update(db: Session,store_data):
        db.merge(store_data)
        db.commit()


class JobRepo:
    
    async def create(db: Session, job: schemas.JobCreate):
            db_job = models.Job(job=job.job)
            db.add(db_job)
            db.commit()
            db.refresh(db_job)
            return db_job
        
    def fetch_by_id(db: Session,_id:int):
        return db.query(models.Job).filter(models.Job.id == _id).first()
    
    def fetch_by_name(db: Session,job:str):
        return db.query(models.Job).filter(models.Job.job == job).first()
    
    def fetch_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Job).offset(skip).limit(limit).all()
    
    async def delete(db: Session,_id:int):
        db_store= db.query(models.Job).filter_by(id=_id).first()
        db.delete(db_store)
        db.commit()
        
    async def update(db: Session,store_data):
        db.merge(store_data)
        db.commit()