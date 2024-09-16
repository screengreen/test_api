from fastapi import APIRouter
from shemas import STaskAdd, STask, STaskId
from repository import TaskRepository

router = APIRouter(
    prefix='/tasks',
    tags=['таски']
)

@router.post("")
async def add_task(
    task: STaskAdd
)-> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {'ok': True, 'task_id': task_id}


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return {'data': tasks}