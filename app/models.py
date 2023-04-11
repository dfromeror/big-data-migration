from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from db import Base
    
class HiredEmployee(Base):
    __tablename__ = "hired_employees"
    
    id = Column(Integer, primary_key=True,index=True)
    name = Column(String(80), nullable=False, unique=True,index=True)
    datetime = Column(String(80), nullable=False)
    department_id = Column(Integer,ForeignKey('departments.id'),nullable=False)
    job_id = Column(Integer,ForeignKey('jobs.id'),nullable=False)
    def __repr__(self):
        return 'HiredEmployeeModel(name=%s,id=%s)' % (self.name,self.store_id)
    
class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True,index=True)
    department = Column(String(80), nullable=False, unique=True)
    hired_employees = relationship("HiredEmployee",primaryjoin="Department.id == HiredEmployee.department_id",cascade="all, delete-orphan")

    def __repr__(self):
        return 'Department(name=%s)' % self.department


class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True,index=True)
    job = Column(String(80), nullable=False, unique=True)
    hired_employees = relationship("HiredEmployee",primaryjoin="Job.id == HiredEmployee.job_id",cascade="all, delete-orphan")

    def __repr__(self):
        return 'Job(name=%s)' % self.job