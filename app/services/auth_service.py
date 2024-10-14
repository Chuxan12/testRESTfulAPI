from app.core.security import create_access_token, verify_password, set_cookie
from app.schemas.user import UserCreate
from app.core.security import hash_password
from app.models.user import User
from fastapi import HTTPException, Response
from app.repository.base_user import UserRepository
from app.core.config import settings
from datetime import timedelta
from typing import Any

class AuthService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def register(self, user_data: UserCreate):
        user = User(username=user_data.username, email=user_data.email, hashed_password=hash_password(user_data.password)) 
        return await self.user_repository.create(user)

    async def login(self, user_data: UserCreate, response: Response):
        user = await self.user_repository.get_by_email(user_data.email)
        if not user or not verify_password(user_data.password, user.hashed_password):
            raise HTTPException(status_code=400, detail="Invalid credentials")

        # Генерация JWT
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(data={"sub": user.id}, expires_delta=access_token_expires)
        await set_cookie(response, access_token)
        return {"access_token": access_token, "token_type": "bearer"}