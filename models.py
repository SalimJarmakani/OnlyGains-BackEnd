from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Date
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username=Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    posts=relationship("Post")
    workouts = relationship("Workout", back_populates="owner")



class Workout(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    type= Column(String)
    title = Column(String)
    excercises=relationship("Excercise")
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner= relationship("User", back_populates="workouts")

class Excercise(Base):
    __tablename__ = "excercises"
    id=Column(Integer, primary_key=True, index=True)
    name=Column(String)
    sets= Column(Integer)
    reps= Column(Integer)
    description=Column(String)
    workout_id=Column(Integer,ForeignKey("workouts.id"))


class Post(Base):
    __tablename__ = "posts"
    id=Column(Integer, primary_key=True, index=True)
    uid=Column(Integer,ForeignKey("users.id"))
    wid=Column(Integer,ForeignKey("workouts.id"))
    likes=Column(Integer)
    description=Column(Integer)
    image=Column(String)