from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from config.database import Base


class HiredEmployee(Base):
    __tablename__ = "hired_employee"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    datetime = Column(String)
    department_id = Column(Integer, ForeignKey('department.id'))
    job_id = Column(Integer, ForeignKey('job.id'))
    department = relationship("Department", back_populates = "hired_employee")
    job = relationship("Job", back_populates = "hired_employee")