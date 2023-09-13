from fastapi import FastAPI, Query
import uvicorn

from routes.person import router as PersonRouter


app = FastAPI()

app.include_router(PersonRouter, tags=['Person'], prefix='/api')


