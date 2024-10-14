from abc import ABC, abstractmethod
from app.models.task import Task
from sqlalchemy.ext.asyncio import AsyncSession

class TaskRepository(ABC):
    @abstractmethod
    async def create(self, task: Task) -> Task:
        pass

    @abstractmethod
    async def get_by_id(self, task_id: int) -> Task:
        pass

    @abstractmethod
    async def get_all(self, user_id: int) -> list[Task]:
        pass

    @abstractmethod
    async def update(self, task: Task) -> Task:
        pass

    @abstractmethod
    async def delete(self, task_id: int) -> None:
        pass