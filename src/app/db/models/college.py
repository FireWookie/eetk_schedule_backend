import uuid

from sqlalchemy import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.app.db.db import Base


class CollegeModel(Base):
    __tablename__ = 'colleges'

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(), primary_key=True, default=uuid.uuid4
    )
    name: Mapped[str]
    schedule: Mapped[list["ScheduleModel"]] = relationship(
        back_populates="college"
    )
    schedule_changes: Mapped[list["ScheduleChangedModel"]] = relationship(
        back_populates="college"
    )
