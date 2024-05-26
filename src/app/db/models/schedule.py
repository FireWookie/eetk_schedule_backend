import datetime
import uuid
from typing import Optional

from sqlalchemy import UUID
from sqlalchemy.orm import Mapped, mapped_column

from src.app.db.db import Base


class ScheduleModel(Base):
    __tablename__ = 'schedule'

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(), primary_key=True, default=uuid.uuid4
    )
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        default=datetime.datetime.now
    )
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        onupdate=datetime.datetime.now, default=datetime.datetime.now
    )
    file_url: Mapped[str]
    date_start: Mapped[datetime.date]
    date_end: Mapped[datetime.date]
    course: Mapped[int]
