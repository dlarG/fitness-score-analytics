from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Import routes
from routes import kpi_routes, filter_routes

app = FastAPI(
    title="Fitness Intelligence Dashboard API",
    description="API for Lifestyle Data Analytics Dashboard",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Test endpoint to check if backend is working
@app.get("/")
async def root():
    return {"message": "Fitness Intelligence Dashboard API", "status": "running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": "2024-12-10"}

# Simple test endpoint without database
@app.get("/test")
async def test_endpoint():
    return {"test": "Backend is responding", "data": [1, 2, 3]}

try:
    app.include_router(kpi_routes.router)
    app.include_router(filter_routes.router)
    print("✅ Routes loaded successfully")
except Exception as e:
    print(f"❌ Error loading routes: {e}")

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)