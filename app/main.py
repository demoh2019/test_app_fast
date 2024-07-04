import uvicorn
from fastapi import FastAPI
from .api import router as division_router


def create_app() -> FastAPI:
    application = FastAPI()
    application.include_router(division_router)
    return application


app = create_app()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)