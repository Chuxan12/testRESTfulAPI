from fastapi import APIRouter, Depends, HTTPException
from app.repository.repository_factory import RepositoryFactory
from app.schemas.task import TaskCreate, Task
from app.services.task_service import TaskService
from app.api.dependencies import get_repository_factory, get_current_user_id
from fastapi_cache.decorator import cache
from app.core.config import FASTAPI_CACHE_LIFETIME

router = APIRouter()

@router.post("/tasks", response_model=Task)
async def create_task(task_data: TaskCreate, factory: RepositoryFactory = Depends(get_repository_factory), user_id: int = Depends(get_current_user_id)):
    task_service = TaskService(factory.create_task_repository())
    task = await task_service.create_task(task_data, user_id)
    return task

@router.get("/tasks", response_model=list[Task])
@cache(expire=FASTAPI_CACHE_LIFETIME)
async def get_tasks(factory: RepositoryFactory = Depends(get_repository_factory), user_id: int = Depends(get_current_user_id)):
    task_service = TaskService(factory.create_task_repository())
    tasks = await task_service.get_user_tasks(user_id)
    return tasks

@router.get("/tasks/{task_id}", response_model=Task)
@cache(expire=FASTAPI_CACHE_LIFETIME)
async def get_task(task_id: int, factory: RepositoryFactory = Depends(get_repository_factory), user_id: int = Depends(get_current_user_id)):
    task_service = TaskService(factory.create_task_repository())
    task = await task_service.get_task_by_id(task_id)
    return task

@router.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task_data: TaskCreate, factory: RepositoryFactory = Depends(get_repository_factory)):
    task_service = TaskService(factory.create_task_repository())
    task = await task_service.update_task(task_id, task_data)
    return task

@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int, factory: RepositoryFactory = Depends(get_repository_factory)):
    task_service = TaskService(factory.create_task_repository())
    await task_service.delete_task(task_id)
    return {"detail": "Task deleted successfully"}