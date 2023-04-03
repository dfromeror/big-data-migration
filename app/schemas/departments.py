from pydantic import BaseModel

class DepartmentBase(BaseModel):
   id: int

   class Config:
        orm_mode = True

class DepartmentCreate(DepartmentBase):
   department: str

   
