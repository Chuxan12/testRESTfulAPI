from fastapi import Depends, HTTPException
from app.core.security import get_user_id_from_token
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_async_session
from app.repository.repository_factory import RepositoryFactory
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

async def get_current_user_id(token: str = Depends(oauth2_scheme)) -> int:
    return get_user_id_from_token(token)

async def get_repository_factory(session: AsyncSession = Depends(get_async_session)) -> RepositoryFactory:
    return RepositoryFactory(session)