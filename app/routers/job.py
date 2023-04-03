from fastapi import APIRouter, Depends

from services.job import JobService
from schemas.job import JobBase, JobCreate

from utils.service_result import handle_result

from config.database import get_db

router = APIRouter(
    prefix="/job",
    tags=["job"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=JobBase)
async def create_item(item: JobCreate, db: get_db = Depends()):
    result = JobService(db).create_item(item)
    return handle_result(result)


""" @router.get("/item/{item_id}", response_model=FooItem)
async def get_item(item_id: int, db: get_db = Depends()):
    result = FooService(db).get_item(item_id)
    return handle_result(result) """