from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
#from dotenv import load_dotenv
from contextlib import asynccontextmanager

# Load the environment variables from the .env file
#load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Executed on startup
    print("Startup")
    print("Loaded model")
    yield
    # Executed on shutdown
    print("Shutdown")

# Create a FastAPI app
app = FastAPI(
    title="My First FastAPI",
    description="This is my first FastAPI application",
    version="0.1.0",
    docs_url="/docs",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://poly-analyse.onrender.com","http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

# Define a root endpoint
@app.get("/")
async def read_root():
    return {"message": "Hello, World"}

# Import the routers
from app.routers.formation_router import formation_router
from app.routers.model_router import model_router
from app.routers.kmeans_router import kmeans_router


app.include_router(formation_router)
app.include_router(model_router)
app.include_router(kmeans_router)

if __name__ == "__main__":
    import uvicorn

    # Run the application using Uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)