from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from config.database import Base


class Department(Base):
    __tablename__ = "department"

    id = Column(Integer, primary_key=True, index=True)
    department = Column(String)
    # hired_employee = relationship("HiredEmployee", back_populates="department")


# Department.hired_employees = relationship("HiredEmployees", order_by = HiredEmployees.id, back_populates = "department")