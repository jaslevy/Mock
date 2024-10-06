from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .db.database import connect_db, close_db
from .api import users, products  # Import your route modules

app = FastAPI()

# CORS configuration (if needed)
origins = [
    "http://localhost:3000",  # React frontend running locally
    "https://your-frontend-domain.com",  # Deployed frontend URL
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(products.router, prefix="/products", tags=["Products"])

# Startup and Shutdown events
@app.on_event("startup")
async def startup_db():
    await connect_db()

@app.on_event("shutdown")
async def shutdown_db():
    await close_db()

# Health check endpoint
@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok"}