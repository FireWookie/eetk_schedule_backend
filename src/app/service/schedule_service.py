from typing import List

from src.app.repository.schedule_changed_repo import ScheduleChangedRepository
from src.app.repository.schedule_date_repo import ScheduleDateRepository
from src.app.repository.schedule_repo import ScheduleRepository
from src.app.schemas.schedule import ScheduleDateInfo


class ScheduleService:
    def __init__(self,
                 schedule_repository: ScheduleRepository,
                 schedule_changed_repository: ScheduleChangedRepository,
                 schedule_date_repository: ScheduleDateRepository):
        self.schedule_repository = schedule_repository
        self.schedule_changed_repository = schedule_changed_repository
        self.schedule_date_repository = schedule_date_repository

    async def get_schedule_date(self) -> List[ScheduleDateInfo]:
        schedules_date = await self.schedule_date_repository.get_all()
        schedule_list = []
        for schedule_date in schedules_date:
            schedule_list.append(
                ScheduleDateInfo(
                    date_start=schedule_date.date_start,
                    date_end=schedule_date.date_end,
                )
            )
        return schedule_list

    async def update_schedule(self):
        await self.schedule_date_repository.delete_all()
