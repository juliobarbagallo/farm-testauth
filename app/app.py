from sys import prefix
from fastapi import FastAPI
from app.core.config import settings
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.models.user_model import User
from app.api.api_v1.router import router

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_v1_STR}/openapi.json"
)

# @app.get('/', tags=["test"])
# async def hello():
#     return {"msg" : "hello"}

@app.on_event("startup")
async def app_init():
    """
        init crucial app services
    """

    db_client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING).testauth

    await init_beanie(
        database=db_client,
        document_models=[
            User
        ]
    )

app.include_router(router, prefix=settings.API_v1_STR)