import datetime
import uuid
from typing import Optional

from sqlalchemy import UUID
from sqlalchemy.orm import Mapped, mapped_column

from src.app.db.db import Base


class ScheduleChangedModel(Base):
    __tablename__ = 'schedule_changed'

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(), primary_key=True, default=uuid.uuid4
    )
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        default=datetime.datetime.now
    )
    date: Mapped[datetime.date]
    lesson: Mapped[int]
    group_name: Mapped[str]
    replaced_subject: Mapped[str]
    result_subject: Mapped[str]
    audience: Mapped[str]
