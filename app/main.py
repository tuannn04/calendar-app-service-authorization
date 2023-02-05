from repository.token import TokenRepository
import logging

from fastapi import FastAPI

app = FastAPI()

@app.get("/token/{accessToken}")
async def token(accessToken: str):
    repository = TokenRepository()
    return repository.getByAccessToken(accessToken)
