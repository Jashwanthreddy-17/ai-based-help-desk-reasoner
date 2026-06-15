from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from passlib.context import CryptContext
from jose import jwt
from sqlalchemy.orm import Session

from backend.database import SessionLocal
from backend.models import User

# ==========================================
# ROUTER
# ==========================================

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

# ==========================================
# JWT SETTINGS
# ==========================================

SECRET_KEY = "HELPDESK_SECRET_KEY"

ALGORITHM = "HS256"

# ==========================================
# PASSWORD HASHING
# ==========================================

pwd_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    deprecated="auto"
)
@router.get("/hash-test")
def hash_test():
    return {
        "hash": pwd_context.hash("test123")
    }
# ==========================================
# REQUEST MODELS
# ==========================================

class RegisterRequest(BaseModel):

    name: str

    email: str

    password: str

    role: str = "employee"


class LoginRequest(BaseModel):

    email: str

    password: str


# ==========================================
# DATABASE SESSION
# ==========================================

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# ==========================================
# REGISTER
# ==========================================

@router.post("/register")
def register(user: RegisterRequest):

    db: Session = SessionLocal()

    try:

        existing_user = db.query(User).filter(
            User.email == user.email
        ).first()

        if existing_user:

            raise HTTPException(
                status_code=400,
                detail="Email already exists"
            )

        hashed_password = pwd_context.hash(
            user.password
        )

        new_user = User(

            name=user.name,

            email=user.email,

            password=hashed_password,

            role=user.role
        )

        db.add(new_user)

        db.commit()

        db.refresh(new_user)

        return {

            "message":
                "User registered successfully",

            "user_id":
                new_user.id
        }

    except Exception as e:

        db.rollback()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    finally:

        db.close()


# ==========================================
# LOGIN
# ==========================================

@router.post("/login")
def login(user: LoginRequest):

    db: Session = SessionLocal()

    try:

        db_user = db.query(User).filter(
            User.email == user.email
        ).first()

        if not db_user:

            raise HTTPException(
                status_code=401,
                detail="Invalid email or password"
            )

        valid_password = pwd_context.verify(
            user.password,
            db_user.password
        )

        if not valid_password:

            raise HTTPException(
                status_code=401,
                detail="Invalid email or password"
            )

        token = jwt.encode(

            {
                "id": db_user.id,
                "email": db_user.email,
                "role": db_user.role
            },

            SECRET_KEY,

            algorithm=ALGORITHM
        )

        return {

            "message":
                "Login successful",

            "token":
                token,

            "role":
                db_user.role
        }

    finally:

        db.close()


# ==========================================
# TEST ROUTE
# ==========================================

@router.get("/test")
def test_auth():

    return {

        "status":
            "Authentication API Working"
    }