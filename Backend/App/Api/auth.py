from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from pydantic import BaseModel

from sqlalchemy.orm import Session

from app.database.session import (
    get_db
)

from app.database.models import (
    User
)

from app.security.auth import (
    hash_password,
    verify_password,
    create_token,
    get_current_user
)


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)



class RegisterRequest(BaseModel):

    name: str
    email: str
    password: str



class LoginRequest(BaseModel):

    email: str
    password: str





@router.post("/register")
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db)
):

    existing = (
        db.query(User)
        .filter(
            User.email == request.email
        )
        .first()
    )


    if existing:

        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )


    hashed = hash_password(
        request.password
    )


    user = User(
        name=request.name,
        email=request.email,
        hashed_password=hashed
    )


    db.add(user)

    db.commit()

    db.refresh(user)


    return {
        "message":
        "User registered successfully"
    }







@router.post("/login")
def login(
    request: LoginRequest,
    db: Session = Depends(get_db)
):

    user = (
        db.query(User)
        .filter(
            User.email == request.email
        )
        .first()
    )


    if not user:

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )


    if not verify_password(
        request.password,
        user.hashed_password
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )


    token = create_token(
        {
            "user_id": user.id
        }
    )


    return {
        "access_token": token,
        "token_type": "Bearer"
    }







@router.get("/me")
def profile(
    current_user=Depends(get_current_user)
):

    return {

        "id":
        current_user.id,

        "name":
        current_user.name,

        "email":
        current_user.email

    }