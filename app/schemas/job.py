from pydantic import BaseModel
from pydantic import EmailStr

class JobBase(BaseModel):
   id: int

   class Config:
      orm_mode = True

class JobCreate(JobBase):
   job: str
