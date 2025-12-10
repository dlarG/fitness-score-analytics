from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import pandas as pd
from database import get_db

router = APIRouter(prefix="/api/filters", tags=["Filters"])

@router.get("/age-range")
async def get_age_range(db: Session = Depends(get_db)):
    """Get min and max age range"""
    query = "SELECT MIN(age) as min_age, MAX(age) as max_age FROM dim_participant"
    df = pd.read_sql_query(query, db.bind)
    return df.iloc[0].to_dict()

@router.get("/genders")
async def get_genders(db: Session = Depends(get_db)):
    """Get all unique genders"""
    query = "SELECT DISTINCT gender FROM dim_participant"
    df = pd.read_sql_query(query, db.bind)
    return df['gender'].tolist()

@router.get("/workout-types")
async def get_workout_types(db: Session = Depends(get_db)):
    """Get all workout types"""
    query = "SELECT DISTINCT workout_type FROM dim_workout"
    df = pd.read_sql_query(query, db.bind)
    return df['workout_type'].tolist()