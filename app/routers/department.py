from fastapi import APIRouter, Depends

from services.departments import DepartmentService
from schemas.departments import DepartmentBase, DepartmentCreate

from utils.service_result import handle_result

from config.database import get_db

router = APIRouter(
    prefix="/deparment",
    tags=["deparment"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=DepartmentBase)
async def create_item(item: DepartmentCreate, db: get_db = Depends()):
    result = DepartmentService(db).create_item(item)
    return handle_result(result)


""" @router.get("/item/{item_id}", response_model=FooItem)
async def get_item(item_id: int, db: get_db = Depends()):
    result = FooService(db).get_item(item_id)
    return handle_result(result) """