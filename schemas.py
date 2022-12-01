from typing import List, Union

from pydantic import BaseModel

class PostBase(BaseModel):
    likes:int
    description:str
    image:str

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    uid: int
    wid: int

    class Config:
        orm_mode=True

class ExcerciseBase(BaseModel):

    name:str
    sets:int
    reps:int
    description:str

class ExcerciseCreate(ExcerciseBase):
    pass

class Excercise(ExcerciseBase):

    id:int
    workout_id:int

    class Config:
        orm_mode=True


class WorkoutBase(BaseModel):
    title: str
    description: Union[str, None] = None
    type: str
    
        


class WorkoutCreate(WorkoutBase):
    pass


class Workout(WorkoutBase):
    id: int
    owner_id: int
    excercises : List[Excercise]= []

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str
    username:str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    workouts: List[Workout] = []
    posts: List[Post]= []
    class Config:
        orm_mode = True

