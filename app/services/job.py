from schemas.job import JobCreate
from utils.app_exceptions import AppException

from services.main import AppService, AppCRUD
from models.jobs import Job
from utils.service_result import ServiceResult


""" def create_todo(db: Session, current_user: models.User, todo_data: DepartmentCreate):
   todo = models.TODO(text=todo_data.text,
                   	completed=todo_data.completed)
   todo.owner = current_user
   db.add(todo)
   db.commit()
   db.refresh(todo)
   return todo """

class JobService(AppService):


    def create_item(self, job: JobCreate) -> Job:
            job_model = Job(id = job.id, job = job.job)
            self.db.add(job_model)
            self.db.commit()
            self.db.refresh(job_model)

            if not job_model:
               return ServiceResult(AppException.FooCreateItem())
            return ServiceResult(job_model)