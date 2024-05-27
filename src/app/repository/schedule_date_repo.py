from typing import List

from sqlalchemy import select

from src.app.db.db import async_session_maker
from src.app.db.models import ScheduleDateModel
from src.app.repository.base import Repository


class ScheduleDateRepository(Repository):
    model = ScheduleDateModel

    async def get_all(self) -> List[ScheduleDateModel]:
        async with async_session_maker() as session:
            query = select(self.model)
            result = await session.execute(query)
            return result.scalars().all()

