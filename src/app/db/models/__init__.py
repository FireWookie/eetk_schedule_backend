__all__ = [
    "ScheduleModel",
    "Base",
    "ScheduleChangedModel",
    "CollegeModel",
    "ScheduleDateModel"
]


from src.app.db.db import Base
from src.app.db.models.college import CollegeModel
from src.app.db.models.schedule_change import ScheduleChangedModel
from src.app.db.models.schedule_date import ScheduleDateModel
from src.app.db.models.schedule import ScheduleModel