from pydantic import BaseModel
from pydantic import EmailStr

class DepartmentBase(BaseModel):
   id: int

class DepartmentCreate(DepartmentBase):
   department: str
