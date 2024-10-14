from abc import ABC, abstractmethod
from app.models.user import User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.repository.base_user import UserRepository
from sqlalchemy.ext.asyncio import AsyncSession

class SQLAlchemyUserRepository(UserRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, user: User):
        #print(user.email,user.hashed_password,user.id,user.tasks,user.username)
        self.session.add(user)
        print(self.session)
        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def get_by_email(self, email: str) -> User:
        return await self.session.execute(
            select(User).where(User.email == email)
        ).scalars().first()