from abc import ABC, abstractmethod
from app.models.user import User
from sqlalchemy.ext.asyncio import AsyncSession

class UserRepository(ABC):
    @abstractmethod
    async def create(self, user: User):
        pass

    @abstractmethod
    async def get_by_email(self, email: str) -> User:
        pass
