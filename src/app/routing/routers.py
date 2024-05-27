from fastapi import APIRouter

from src.app.routing.schedule import schedule_router

all_routers = [
    schedule_router
]

apiv1 = APIRouter(
    prefix="/api/v1",
)

for router in all_routers:
    apiv1.include_router(router)