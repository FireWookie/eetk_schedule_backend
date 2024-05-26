from fastapi import APIRouter

from src.app.enums import Tags

schedule_router = APIRouter(
    tags=Tags.SCHEDULE
)

