from fastapi import Depends

from src.app.depends.repo_depends import schedule_repo, schedule_date_repo, schedule_changed_repo
from src.app.repository.schedule_changed_repo import ScheduleChangedRepository
from src.app.repository.schedule_date_repo import ScheduleDateRepository
from src.app.repository.schedule_repo import ScheduleRepository
from src.app.service.schedule_service import ScheduleService


async def schedule_service(
    schedule_repository: ScheduleRepository = Depends(schedule_repo),
    schedule_date_repository: ScheduleDateRepository = Depends(schedule_date_repo),
    schedule_changed_repository: ScheduleChangedRepository = Depends(schedule_changed_repo),
):
    return ScheduleService(
        schedule_repository=schedule_repository,
        schedule_changed_repository=schedule_changed_repository,
        schedule_date_repository=schedule_date_repository
    )

