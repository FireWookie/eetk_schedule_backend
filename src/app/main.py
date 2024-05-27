import time
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request

from src.app.routing.routers import apiv1


def create_app() -> FastAPI:
    api = FastAPI(
        docs_url="/docs",
        debug=True,
        title="ЕЭТК API мобильного приложения",
    )

    origins = ["*"]

    api.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=["*"],
        allow_methods=["GET", "POST", "PUT", "DELETE"],
        allow_headers=["*"],  # need to set used headers
    )
    api.include_router(apiv1)

    return api


app = create_app()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.middleware("http")
async def signature_generator(request: Request, call_next):

    response = await call_next(request)
    return response



# @app.exception_handler(UserNotAuthorizedError)
# async def user_not_authorized_error_handler(request: Request, exc: UserNotAuthorizedError):
#     return raise_http_exception_from_custom(exc)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=800, workers=4, reload=True)