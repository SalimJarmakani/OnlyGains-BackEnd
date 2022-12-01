from sqlalchemy.orm import Session

import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password,username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_Workouts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Workout).offset(skip).limit(limit).all()


def get_Workout(db:Session,w_id:int):

    return db.query(models.Workout).filter(models.Workout.id==w_id).first()


def create_user_Workout(db: Session, Workout: schemas.WorkoutCreate, user_id: int):
    db_Workout = models.Workout(**Workout.dict(), owner_id=user_id)
    db.add(db_Workout)
    db.commit()
    db.refresh(db_Workout)
    return db_Workout

def create_excercise(db: Session, Excercise: schemas.ExcerciseCreate,w_id: int):
    db_excercise = models.Excercise(**Excercise.dict(),workout_id=w_id)
    db.add(db_excercise)
    db.commit()
    db.refresh(db_excercise)
    return db_excercise

def get_excercise(db: Session,excercise_id:int):

    return db.query(models.Excercise).filter(models.Excercise.id==excercise_id).first()

def create_post(db:Session,uid:int,wid:int,Post:schemas.PostCreate):

    db_post= models.Post(uid=uid,wid=wid,**Post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_posts(db:Session, skip: int = 0, limit: int = 100):
    return db.query(models.Post).offset(skip).limit(limit).all()

def get_post(db:Session,id:int):
    return db.query(models.Post).filter(models.Post.id==id).first()