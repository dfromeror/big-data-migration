from typing import List, Optional

from pydantic import BaseModel

class HiredEmployeeBase(BaseModel):
    name: str
    datetime : str
    department_id: int
    job_id: int

class HiredEmployeeCreate(HiredEmployeeBase):
    pass


class HiredEmployee(HiredEmployeeBase):
    id: int

    class Config:
        orm_mode = True


class DepartmentBase(BaseModel):
    department: str

class DepartmentCreate(DepartmentBase):
    pass

class Department(DepartmentBase):
    id: int
    hired_employees: List[HiredEmployee] = []

    class Config:
        orm_mode = True

class JobBase(BaseModel):
    job: str

class JobCreate(JobBase):
    pass

class Job(JobBase):
    id: int
    hired_employees: List[HiredEmployee] = []

    class Config:
        orm_mode = True