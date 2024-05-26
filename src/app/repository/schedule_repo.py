from src.app.db.models import ScheduleModel
from src.app.repository.base import Repository


class ScheduleRepository(Repository):
    model = ScheduleModel