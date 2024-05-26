from abc import abstractmethod, ABC
from typing import Iterable

from sqlalchemy import select, UUID, delete, insert

from src.app.db.db import async_session_maker, Base


class AbstractRepository(ABC):

    @abstractmethod
    async def get_all(self) -> Iterable: ...

    @abstractmethod
    async def insert_one(self, _) -> Base: ...

    @abstractmethod
    async def delete_one_by_id(self, _) -> None: ...


class Repository(AbstractRepository):
    model = Base

    async def get_all(self) -> Iterable:
        async with async_session_maker() as session:
            query = select(self.model)
            result = await session.execute(query)
            return result.scalars().all()

    async def insert_one(self, model_dump: dict) -> model:
        async with async_session_maker() as session:
            stmt = (
                insert(self.model).values(**model_dump).returning(self.model)
            )
            result = await session.execute(stmt)
            await session.commit()
            return result.scalar_one()

    async def delete_one_by_id(self, item_id: UUID) -> None:
        async with async_session_maker() as session:
            stmt = delete(self.model).where(self.model.id == item_id)
            await session.execute(stmt)
            await session.commit()