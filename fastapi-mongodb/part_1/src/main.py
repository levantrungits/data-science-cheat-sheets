# Third party modules
from fastapi import FastAPI
# Local modules
from .api import ROUTER

app = FastAPI(
    version="0.1.0",
    title="FastAPI-MongoDB Example"
)

# Add used endpoints (and simplifying endpoint declarations)
app.include_router(ROUTER)
