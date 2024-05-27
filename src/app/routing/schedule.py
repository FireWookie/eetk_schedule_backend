from typing import List

from fastapi import APIRouter, Depends

from src.app.depends.service_depends import schedule_service
from src.app.enums import Tags
from src.app.schemas.schedule import ScheduleDateInfo
from src.app.service.schedule_service import ScheduleService

schedule_router = APIRouter(
    tags=[Tags.SCHEDULE],
    prefix="/schedule"
)


@schedule_router.get(
    path="/period",
    response_model=List[ScheduleDateInfo]
)
async def get_schedule(
    service: ScheduleService = Depends(schedule_service)
):
    """Получение периода доступного расписания"""
    return await service.get_schedule_date()
