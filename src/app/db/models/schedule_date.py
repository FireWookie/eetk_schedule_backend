import datetime
import uuid
from typing import Optional

from sqlalchemy import UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.app.db.db import Base


class ScheduleDateModel(Base):
    __tablename__ = 'schedule_date'

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(), primary_key=True, default=uuid.uuid4
    )
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        default=datetime.datetime.now
    )
    date_start: Mapped[datetime.date]
    date_end: Mapped[datetime.date]

    schedule: Mapped[list["ScheduleModel"]] = relationship(
        back_populates="schedule_date"
    )


