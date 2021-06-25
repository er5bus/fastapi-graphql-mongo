from os import getenv

import graphene

from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp
from mongoengine import connect

from schemas.user import UserQuery, UserMutation


app = FastAPI()


app.add_route(
    "/graphiql", GraphQLApp(schema=graphene.Schema(query=UserQuery, mutation=UserMutation))
)

@app.on_event("startup")
async def startup_event():
    connect(host="mongodb://{}:{}@{}:27017/{}".format(getenv("DATABASE_USER"), getenv("DATABASE_PASSWORD")
                                                     , getenv("DATABASE_HOST"), getenv("DATABASE_NAME")))

@app.get("/")
def main():
    return {"status": "alive"}


@app.get("/health-check")
def health_check():
    return {"ping": "pong"}
