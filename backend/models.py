from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime

# Request/Response Models
class FilterRequest(BaseModel):
    age_min: Optional[int] = 18
    age_max: Optional[int] = 65
    genders: Optional[List[str]] = ["Male", "Female"]
    workout_types: Optional[List[str]] = []
    limit: Optional[int] = 25

class KPIFitnessScore(BaseModel):
    participant_id: int
    age: int
    gender: str
    calorie_burn_rate: float
    avg_workout_frequency: float
    protein_efficiency: float
    fitness_score: float

class KPIExerciseEffectiveness(BaseModel):
    exercise_name: str
    participant_count: int
    total_calories_burned: float
    calories_per_set: float
    avg_sets_per_session: float

class KPINutritionBody(BaseModel):
    participant_id: int
    age: int
    gender: str
    fat_percentage: float
    avg_daily_protein: float
    avg_daily_carbs: float
    avg_daily_fats: float
    avg_daily_sugar: float
    avg_daily_calories_burned: float

class KPIWorkoutPerformance(BaseModel):
    workout_type: str
    unique_participants: int
    avg_duration_hr: float
    avg_calories_burned: float
    avg_burn_efficiency: float
    avg_heart_rate_zone: float
    avg_water_intake: float

class KPILifestyleBalance(BaseModel):
    participant_id: int
    age: int
    gender: str
    nutrition_score: int
    exercise_score: int
    recovery_score: int
    lifestyle_balance_index: float

class DashboardSummary(BaseModel):
    avg_fitness_score: float
    avg_burn_rate: float
    top_exercise: str
    best_workout: str
    avg_balance_index: float
    total_participants: int
    total_exercises: int
    total_workouts: int