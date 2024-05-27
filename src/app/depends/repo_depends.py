from src.app.repository.schedule_changed_repo import ScheduleChangedRepository
from src.app.repository.schedule_date_repo import ScheduleDateRepository
from src.app.repository.schedule_repo import ScheduleRepository


async def schedule_changed_repo():
    return ScheduleChangedRepository()


async def schedule_repo():
    return ScheduleRepository()


async def schedule_date_repo():
    return ScheduleDateRepository()
