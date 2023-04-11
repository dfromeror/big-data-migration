from fastapi import Depends, FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from db import get_db, engine
import models as models
import schemas as schemas
from repositories import HiredEmployeeRepo, DepartmentRepo, JobRepo
from sqlalchemy.orm import Session
import uvicorn
from typing import List,Optional
from fastapi.encoders import jsonable_encoder

app = FastAPI(title="Sample FastAPI Application",
    description="Sample FastAPI Application with Swagger and Sqlalchemy",
    version="1.0.0",)

models.Base.metadata.create_all(bind=engine)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    print("Transactions that don't accomplish the rules")
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "Error": "Transactions that don't accomplish the rules"}),
    )

@app.exception_handler(Exception)
def validation_exception_handler(request, err):
    base_error_message = f"Failed to execute: {request.method}: {request.url}"
    return JSONResponse(status_code=400, content={"message": f"{base_error_message}. Detail2: {err}"})

@app.post('/hired_employees', tags=["HiredEmployee"],response_model=schemas.HiredEmployee,status_code=201)
async def create_hired_employee(hired_employee_request: schemas.HiredEmployeeCreate, db: Session = Depends(get_db)):
    """
    Create an hired_employee and job it in the database
    """
    
    db_hired_employee = HiredEmployeeRepo.fetch_by_name(db, name=hired_employee_request.name)
    if db_hired_employee:
        raise HTTPException(status_code=400, detail="hired_employee already exists!")

    return await HiredEmployeeRepo.create(db=db, hired_employee=hired_employee_request)

@app.get('/hired_employees', tags=["HiredEmployee"],response_model=List[schemas.HiredEmployee])
def get_all_hired_employees(name: Optional[str] = None,db: Session = Depends(get_db)):
    """
    Get all the hired_employees jobd in database
    """
    if name:
        hired_employees =[]
        db_hired_employee = HiredEmployeeRepo.fetch_by_name(db,name)
        hired_employees.append(db_hired_employee)
        return hired_employees
    else:
        return HiredEmployeeRepo.fetch_all(db)


@app.get('/employees_hired', tags=["HiredEmployee"])
def get_all_hired_employees(name: Optional[str] = None,db: Session = Depends(get_db)):
    """
    Get all the hired_employees jobd in database
    """
    print("000000")
    hired_employees =[]
    db_hired_employee = HiredEmployeeRepo.employees_hired(db,name)
    hired_employees.append(db_hired_employee)
    return hired_employees



@app.get('/hired_employees/{hired_employee_id}', tags=["HiredEmployee"],response_model=schemas.HiredEmployee)
def get_hired_employee(hired_employee_id: int,db: Session = Depends(get_db)):
    """
    Get the hired_employee with the given ID provided by User jobd in database
    """
    db_hired_employee = HiredEmployeeRepo.fetch_by_id(db,hired_employee_id)
    if db_hired_employee is None:
        raise HTTPException(status_code=404, detail="hired_employee not found with the given ID")
    return db_hired_employee

@app.delete('/hired_employees/{hired_employee_id}', tags=["HiredEmployee"])
async def delete_hired_employee(hired_employee_id: int,db: Session = Depends(get_db)):
    """
    Delete the hired_employee with the given ID provided by User jobd in database
    """
    db_hired_employee = HiredEmployeeRepo.fetch_by_id(db,hired_employee_id)
    if db_hired_employee is None:
        raise HTTPException(status_code=404, detail="hired_employee not found with the given ID")
    await HiredEmployeeRepo.delete(db,hired_employee_id)
    return "hired_employee deleted successfully!"

@app.put('/hired_employees/{hired_employee_id}', tags=["HiredEmployee"],response_model=schemas.HiredEmployee)
async def update_hired_employee(hired_employee_id: int,hired_employee_request: schemas.HiredEmployee, db: Session = Depends(get_db)):
    """
    Update an hired_employee jobd in the database
    """
    db_hired_employee = HiredEmployeeRepo.fetch_by_id(db, hired_employee_id)
    if db_hired_employee:
        update_hired_employee_encoded = jsonable_encoder(hired_employee_request)
        db_hired_employee.name = update_hired_employee_encoded['name']
        db_hired_employee.price = update_hired_employee_encoded['price']
        db_hired_employee.description = update_hired_employee_encoded['description']
        db_hired_employee.department_id = update_hired_employee_encoded['department_id']
        return await HiredEmployeeRepo.update(db=db, hired_employee_data=db_hired_employee)
    else:
        raise HTTPException(status_code=400, detail="hired_employee not found with the given ID")
    
    
@app.post('/departments', tags=["Department"],response_model=schemas.Department,status_code=201)
async def create_department(department_request: schemas.DepartmentCreate, db: Session = Depends(get_db)):
    """
    Create a department and save it in the database
    """
    print("333333333")
    db_departments = DepartmentRepo.fetch_by_name(db, department=department_request.department)
    print(db_departments)
    if db_departments:
        raise HTTPException(status_code=400, detail="department already exists!")

    return await DepartmentRepo.create(db=db, department=department_request)

@app.get('/departments', tags=["Department"],response_model=List[schemas.Department])
def get_all_departments(name: Optional[str] = None,db: Session = Depends(get_db)):
    """
    Get all the departments departmentd in database
    """
    if name:
        departments =[]
        db_departments = DepartmentRepo.fetch_by_name(db,name)
        print(db_departments)
        departments.append(db_departments)
        return departments
    else:
        return DepartmentRepo.fetch_all(db)
    
@app.get('/departments/{department_id}', tags=["Department"],response_model=schemas.Department)
def get_department(department_id: int,db: Session = Depends(get_db)):
    """
    Get the department with the given ID provided by User departmentd in database
    """
    db_departments = DepartmentRepo.fetch_by_id(db,department_id)
    if db_departments is None:
        raise HTTPException(status_code=404, detail="department not found with the given ID")
    return db_departments

@app.delete('/departments/{department_id}', tags=["Department"])
async def delete_department(department_id: int,db: Session = Depends(get_db)):
    """
    Delete the hired_employee with the given ID provided by User departmentd in database
    """
    db_departments = DepartmentRepo.fetch_by_id(db,department_id)
    if db_departments is None:
        raise HTTPException(status_code=404, detail="department not found with the given ID")
    await DepartmentRepo.delete(db,department_id)
    return "department deleted successfully!"


@app.post('/jobs', tags=["Job"],response_model=schemas.Job,status_code=201)
async def create_job(job_request: schemas.JobCreate, db: Session = Depends(get_db)):
    """
    Create a Job and save it in the database
    """
    db_job = JobRepo.fetch_by_name(db, job=job_request.job)
    print(db_job)
    if db_job:
        raise HTTPException(status_code=400, detail="Job already exists!")

    return await JobRepo.create(db=db, job=job_request)

@app.get('/jobs', tags=["Job"],response_model=List[schemas.Job])
def get_all_jobs(name: Optional[str] = None,db: Session = Depends(get_db)):
    """
    Get all the Jobs jobd in database
    """
    if name:
        jobs =[]
        db_job = JobRepo.fetch_by_name(db,name)
        print(db_job)
        jobs.append(db_job)
        return jobs
    else:
        return JobRepo.fetch_all(db)
    
@app.get('/jobs/{job_id}', tags=["Job"],response_model=schemas.Job)
def get_job(job_id: int,db: Session = Depends(get_db)):
    """
    Get the Job with the given ID provided by User jobd in database
    """
    db_job = JobRepo.fetch_by_id(db,job_id)
    if db_job is None:
        raise HTTPException(status_code=404, detail="Job not found with the given ID")
    return db_job

@app.delete('/jobs/{job_id}', tags=["Job"])
async def delete_job(job_id: int,db: Session = Depends(get_db)):
    """
    Delete the Item with the given ID provided by User jobd in database
    """
    db_job = JobRepo.fetch_by_id(db,job_id)
    if db_job is None:
        raise HTTPException(status_code=404, detail="Job not found with the given ID")
    await JobRepo.delete(db,job_id)
    return "Job deleted successfully!"
    

if __name__ == "__main__":
    uvicorn.run("main:app", port=9000, reload=True)