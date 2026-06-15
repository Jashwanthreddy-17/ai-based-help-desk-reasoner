from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.database import engine
from backend.models import Base

from backend.routes.chat import router as chat_router
from backend.routes.auth import router as auth_router
from backend.routes.tickets import router as ticket_router

# ==========================================
# APP
# ==========================================

app = FastAPI(
    title="Automated Help Desk Reasoner"
)

# ==========================================
# CORS
# ==========================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================================
# DATABASE
# ==========================================

Base.metadata.create_all(bind=engine)

# ==========================================
# ROUTES
# ==========================================

app.include_router(chat_router)
app.include_router(auth_router)
app.include_router(ticket_router)

# ==========================================
# HOME
# ==========================================

@app.get("/")
def home():

    return {
        "message":
        "Automated Help Desk Reasoner Running"
    }

# ==========================================
# HEALTH
# ==========================================

@app.get("/health")
def health():

    return {
        "backend": "ok",
        "database": "connected"
    }