from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/Workouts/", response_model=schemas.Workout)
def create_Workout_for_user(
    user_id: int, Workout: schemas.WorkoutCreate, db: Session = Depends(get_db)
):
    return crud.create_user_Workout(db=db, Workout=Workout, user_id=user_id)


@app.get("/Workouts/", response_model=List[schemas.Workout])
def read_Workouts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    Workouts = crud.get_Workouts(db, skip=skip, limit=limit)
    return Workouts

@app.get("/Workouts/{w_id}",response_model=schemas.Workout)
def get_Workout(w_id:int, db:Session=Depends(get_db)):
    Workout= crud.get_Workout(db=db,w_id=w_id)

    return Workout

@app.post("/excercises/{workout_id}",response_model=schemas.Excercise)
def create_excercise_for_workout(workout_id:int, Excercise: schemas.ExcerciseCreate, db:Session=Depends(get_db) ):

    return crud.create_excercise(db=db,Excercise=Excercise,w_id=workout_id)

@app.get("/excercises/{excercise_id}",response_model=schemas.Excercise)
def get_Excercise(excercise_id: int,db:Session=Depends(get_db)):
    return crud.get_excercise(db=db,excercise_id=excercise_id)

@app.post("/post/{user_id}/{workout_id}",response_model=schemas.Post)
def create_post_for_user(user_id:int,workout_id:int,Post:schemas.PostCreate,db:Session=Depends(get_db)):

    return crud.create_post(uid=user_id,wid=workout_id,Post=Post,db=db)

@app.get("/post/",response_model=List[schemas.Post])
def read_posts(skip:int=0,limit:int=100,db:Session=Depends(get_db)):
    Posts=crud.get_posts(db=db,skip=skip,limit=limit)
    return Posts

@app.get("/post/{id}")
def get_post(id:int,db:Session=Depends(get_db)):

    return crud.get_post(db=db,id=id)
