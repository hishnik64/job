from typing import List

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Identity
from config.config import engine
from pydantic import BaseModel
from fastapi import FastAPI
import databases

DATABASE_URL = "postgresql+psycopg2://postgres:161322@localhost/Employees"
database = databases.Database(DATABASE_URL)
meta = MetaData()

users = Table(
    'users', meta,
    Column('id', Integer, primary_key=True, auto_increment=True),
    Column('name', String, nullable=False),
    Column('surname', String, nullable=False),
    Column('password', String, nullable=False),
    Column('phone_number', String, nullable=False),
    Column('job_title', String, nullable=False),
    # Column('role', choices=(('admin', 'Администратор'), ('user', 'Пользователь')), default='user'),
    # ChoiceType({"short": "short", "medium": "medium", "tall": "tall"})
    # Column('role', String, Enum(Choices)),
)
meta.create_all(engine)

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)


class PostIn(BaseModel):
    name: str
    surname: str
    password: str
    phone_number: str
    job_title: str


class Post(BaseModel):
    id: int
    name: str
    surname: str
    password: str
    phone_number: str
    job_title: str


app = FastAPI()

@app.on_event("startup")
async  def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get('/users/', response_model=List[Post])
async def chek_users():
    query = users.select()
    return await database.fetch_all(query)

@app.post("/users/", response_model=Post)
async def create_user(post: PostIn):
    query = users.insert().values(
        name=post.name,
        surname=post.surname,
        password=post.password,
        phone_number=post.phone_number,
        job_title=post.job_title,
    )
    last_record_id = await database.execute(query)
    return {**post.dict(), "id":last_record_id}

@app.delete("/users/{post_id}")
async def delete_post(post_id:int):
    query = users.delete().where(id==post_id)
    await database.execute(query)
    return {"detail": "Post deleted", "status_code": 204}