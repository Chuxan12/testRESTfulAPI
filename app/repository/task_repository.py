from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.task import Task
from app.repository.base_task import TaskRepository

class SQLAlchemyTaskRepository(TaskRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, task: Task) -> Task:
        self.session.add(task)
        await self.session.commit()
        await self.session.refresh(task)
        return task

    async def get_by_id(self, task_id: int) -> Task:
        statement = select(Task).where(Task.id == task_id)
        result = await self.session.execute(statement)
        return result.scalars().first()

    async def get_all(self, user_id: int) -> list[Task]:
        statement = select(Task).where(Task.owner_id == user_id)
        result = await self.session.execute(statement)
        return result.scalars().all()

    async def update(self, task: Task) -> Task:
        await self.session.commit()
        await self.session.refresh(task)
        return task

    async def delete(self, task_id: int) -> None:
        statement = select(Task).where(Task.id == task_id)
        await self.session.execute(statement)
        await self.session.commit()