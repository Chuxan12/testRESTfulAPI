from app.schemas.user import UserCreate
from app.models.user import User
from app.repository.user_repository import UserRepository
from app.core.security import hash_password
from fastapi import Depends

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def create_user(self, user_data: UserCreate):
        user = User(username=user_data.username, email=user_data.email, hashed_password=hash_password(user_data.password)) 
        return await self.user_repository.create(user)