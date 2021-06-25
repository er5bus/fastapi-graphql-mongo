from models.user import User
from typing import List, Optional
from graphene.relay import Node
from graphene_mongo import MongoengineObjectType
from graphene_pydantic import PydanticInputObjectType, PydanticObjectType
from pydantic import BaseModel


class UserModel(BaseModel):
    id: str
    first_name: str
    last_name: str


class UserGrapheneModel(MongoengineObjectType):
    class Meta:
        model = User


class UserGrapheneInputModel(PydanticInputObjectType):
    class Meta:
        model = UserModel
        exclude_fields = ('id', )
