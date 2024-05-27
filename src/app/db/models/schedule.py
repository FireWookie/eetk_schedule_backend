import datetime
import uuid
from typing import Optional

from sqlalchemy import UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.app.db.db import Base
from src.app.db.models import CollegeModel
from src.app.db.models.schedule_date import ScheduleDateModel


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

    college_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey('colleges.id', ondelete='CASCADE')
    )
    college: Mapped["CollegeModel"] = relationship(
        back_populates="schedule", foreign_keys=[college_id]
    )

    schedule_date_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey('schedule_date.id', ondelete='CASCADE'),
    )
    schedule_date: Mapped["ScheduleDateModel"] = relationship(
        back_populates="schedule", foreign_keys=[schedule_date_id]
    )