from pydantic import BaseModel
from pydantic import EmailStr

class HiredEmployeeBase(BaseModel):
   id: int

class HiredEmployeeCreate(HiredEmployeeBase):
   name: str
   datetime: str
   datetime: str 

