from app.repository.base_user import UserRepository
from app.repository.base_task import TaskRepository
from app.repository.user_repository import SQLAlchemyUserRepository
from app.repository.task_repository import SQLAlchemyTaskRepository
from app.repository.base_user import UserRepository
from sqlalchemy.ext.asyncio import AsyncSession

class RepositoryFactory:
    def __init__(self, session: AsyncSession):
        self.session = session

    def create_user_repository(self) -> UserRepository:
        return SQLAlchemyUserRepository(self.session)

    def create_task_repository(self) -> TaskRepository:
        return SQLAlchemyTaskRepository(self.session)