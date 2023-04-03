from schemas.departments import DepartmentCreate
from utils.app_exceptions import AppException

from services.main import AppService, AppCRUD
from models.departments import Department
from utils.service_result import ServiceResult


""" def create_todo(db: Session, current_user: models.User, todo_data: DepartmentCreate):
   todo = models.TODO(text=todo_data.text,
                   	completed=todo_data.completed)
   todo.owner = current_user
   db.add(todo)
   db.commit()
   db.refresh(todo)
   return todo """

class DepartmentService(AppService):


    def create_item(self, department: DepartmentCreate) -> Department:
            department_model = Department(id = department.id, department = department.department)
            self.db.add(department_model)
            self.db.commit()
            self.db.refresh(department_model)

            if not department_model:
               return ServiceResult(AppException.FooCreateItem())
            return ServiceResult(department_model)