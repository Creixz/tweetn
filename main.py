#Python
from typing import Optional
from uuid import UUID
from datetime import date

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
    pass

class User(BaseModel):
    
    password: str = Field(
        ...,
        min_length=8
    )
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
    pass

@app.get(path="/")
def home():
    return {"Twitter API": "Working!"}