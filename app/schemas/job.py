from pydantic import BaseModel
from pydantic import EmailStr

class JobBase(BaseModel):
   id: int

class JobCreate(JobBase):
   job: str
