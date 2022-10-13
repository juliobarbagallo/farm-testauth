from sys import prefix
from fastapi import APIRouter
from app.api.api_v1.handlers import user

router = APIRouter()

router.include_router(user.user_router, prefix='/users', tags=["users"])