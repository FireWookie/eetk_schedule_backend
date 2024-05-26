from src.app.repository.schedule_changed_repo import ScheduleChangedRepository
from src.app.repository.schedule_repo import ScheduleRepository


class ScheduleService:
    def __init__(self,
                 schedule_repository: ScheduleRepository,
                 schedule_changed_repository: ScheduleChangedRepository):
        self.schedule_repository = schedule_repository
        self.schedule_changed_repository = schedule_changed_repository
