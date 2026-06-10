from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from pydantic import BaseModel


from app.database.connection import (
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



# =============================
# SCHEMAS
# =============================


class RegisterRequest(BaseModel):

    email: str

    password: str



class LoginRequest(BaseModel):

    email: str

    password: str




# =============================
# REGISTER
# =============================


@router.post("/register")
def register(

    data: RegisterRequest,

    db: Session = Depends(get_db)

):


    existing = (

        db.query(User)

        .filter(
            User.email == data.email
        )

        .first()

    )



    if existing:

        raise HTTPException(

            status_code=400,

            detail="User already exists"

        )



    new_user = User(

        email=data.email,


        hashed_password=hash_password(

            data.password

        )

    )



    db.add(
        new_user
    )


    db.commit()


    db.refresh(
        new_user
    )



    return {

        "message":
        "Registered successfully",


        "email":
        new_user.email

    }





# =============================
# LOGIN
# =============================


@router.post("/login")
def login(

    data: LoginRequest,


    db: Session = Depends(get_db)

):


    user = (

        db.query(User)

        .filter(

            User.email == data.email

        )

        .first()

    )



    if not user:


        raise HTTPException(

            status_code=401,

            detail="Invalid credentials"

        )



    if not verify_password(

        data.password,


        user.hashed_password

    ):


        raise HTTPException(

            status_code=401,

            detail="Invalid credentials"

        )




    token = create_token(

        {

            "sub":
            user.email

        }

    )



    return {


        "access_token":
        token,


        "token_type":
        "bearer",


        "user":{

            "id":
            user.id,


            "email":
            user.email

        }

    }





# =============================
# CURRENT USER
# =============================


@router.get("/me")
def get_me(

    current_user = Depends(

        get_current_user

    )

):


    return {


        "authenticated":
        True,


        "user":
        current_user

    }