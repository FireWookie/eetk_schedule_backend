from src.app.db.models import ScheduleChangedModel
from src.app.repository.base import Repository


class ScheduleChangedRepository(Repository):
    model = ScheduleChangedModel

