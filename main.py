#Python
from typing import Optional
from uuid import UUID
from datetime import date, datetime

#Pydantic
from pydantic import BaseModel, EmailStr
from pydantic import Field

# FastAPI
from fastapi import FastAPI

app = FastAPI()

# Los models se colocan siempre debajo de la definicion de la aplicacion y por encima de cualquier Path Operations
# Models
#Universal Unique Identifier / clase especial de Python que permite colocar un ID unico cada vez a cada entidad que creamos en la aplicacion
class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)

class UserLogin(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64
    )

class User(UserBase):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    birth_date: Optional[date] = Field(default=None)

class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ...,
        min_length=1,
        max_length=256
    )
    create_at: datetime = Field(default=datetime.now())
    update_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)

@app.get(path="/")
def home():
    return {"Twitter API": "Working!"}