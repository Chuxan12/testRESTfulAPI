from app.models.task import Task
from app.schemas.task import TaskCreate
from app.repository.base_task import TaskRepository
from fastapi import APIRouter, Depends, HTTPException

class TaskService:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    async def create_task(self, task_data: TaskCreate, user_id: int) -> Task:
        task = Task(**task_data.dict(), owner_id=user_id)
        return await self.task_repository.create(task)

    async def get_user_tasks(self, user_id: int) -> list[Task]:
        return await self.task_repository.get_all(user_id)

    async def get_task_by_id(self, task_id: int) -> Task:
        task = await self.task_repository.get_by_id(task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        return task

    async def update_task(self, task_id: int, task_data: TaskCreate) -> Task:
        task = await self.task_repository.get_by_id(task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        
        for key, value in task_data.dict(exclude_unset=True).items():
            setattr(task, key, value)
        
        return await self.task_repository.update(task)

    async def delete_task(self, task_id: int) -> None:
        task = await self.task_repository.get_by_id(task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        await self.task_repository.delete(task_id)