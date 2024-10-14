from fastapi import APIRouter, Depends, HTTPException, Response
from app.schemas.user import UserCreate
from app.schemas.token import Token
from app.core.security import delete_cookie
from app.services.auth_service import AuthService
from app.repository.repository_factory import RepositoryFactory
from app.api.dependencies import get_repository_factory

router = APIRouter()

@router.post("/register")
async def register(user_data: UserCreate, factory: RepositoryFactory = Depends(get_repository_factory)):
    auth_service = AuthService(factory.create_user_repository())
    user = await auth_service.register(user_data)
    return user

@router.post("/login", response_model=Token)
async def login(user_data: UserCreate, response: Response, factory: RepositoryFactory = Depends(get_repository_factory)):
    auth_service = AuthService(factory.create_user_repository())
    token = await auth_service.login(user_data, response)
    return token

@router.post("/logout")
async def logout(token: str, response: Response):
    await delete_cookie(response)
    return {"msg": "Successfully logged out"}