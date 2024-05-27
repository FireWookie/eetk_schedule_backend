import datetime
import uuid
from typing import Optional

from sqlalchemy import UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

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

    college_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey('colleges.id', ondelete='CASCADE'),
    )
    college: Mapped["CollegeModel"] = relationship(
        back_populates="schedule_changes", foreign_keys=[college_id]
    )
