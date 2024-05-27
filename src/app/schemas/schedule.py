from pydantic import BaseModel


class ScheduleDateInfo(BaseModel):
    date_start: str
    date_end: str
