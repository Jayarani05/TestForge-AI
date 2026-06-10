from datetime import datetime, timedelta
import os


from passlib.context import CryptContext


from jose import (
    JWTError,
    jwt
)


from fastapi import (
    Depends,
    HTTPException,
    status
)


from fastapi.security import (
    OAuth2PasswordBearer
)


from sqlalchemy.orm import Session


from app.database.connection import (
    get_db
)


from app.database.models import (
    User
)



# ==============================
# PASSWORD CONFIG
# ==============================

pwd_context = CryptContext(

    schemes=[
        "bcrypt"
    ],

    deprecated="auto"

)



# ==============================
# JWT CONFIG
# ==============================

SECRET_KEY = os.getenv(

    "SECRET_KEY",

    "testforge-secret-key"

)


ALGORITHM = "HS256"


ACCESS_TOKEN_EXPIRE_MINUTES = 60



oauth2_scheme = OAuth2PasswordBearer(

    tokenUrl="/api/v1/auth/login"

)




# ==============================
# PASSWORD
# ==============================

def hash_password(

    password:str

):


    password = password[:72]


    return pwd_context.hash(

        password

    )




def verify_password(

    plain_password:str,

    hashed_password:str

):


    plain_password = plain_password[:72]


    return pwd_context.verify(

        plain_password,

        hashed_password

    )





# ==============================
# CREATE JWT
# ==============================

def create_token(

    data:dict

):


    payload = data.copy()


    expire = (

        datetime.utcnow()

        +

        timedelta(

            minutes=
            ACCESS_TOKEN_EXPIRE_MINUTES

        )

    )


    payload.update(

        {

            "exp":
            expire

        }

    )


    return jwt.encode(

        payload,

        SECRET_KEY,

        algorithm=ALGORITHM

    )





def create_access_token(

    data:dict

):

    return create_token(

        data

    )





# ==============================
# VERIFY TOKEN
# ==============================

def verify_token(

    token:str

):


    try:


        payload = jwt.decode(

            token,

            SECRET_KEY,

            algorithms=[

                ALGORITHM

            ]

        )



        return payload.get(

            "sub"

        )



    except JWTError:


        return None





# ==============================
# CURRENT USER
# ==============================

def get_current_user(

    token:str = Depends(

        oauth2_scheme

    ),


    db:Session = Depends(

        get_db

    )

):


    email = verify_token(

        token

    )


    if email is None:


        raise HTTPException(

            status_code=
            status.HTTP_401_UNAUTHORIZED,


            detail=
            "Invalid token"

        )



    user = (

        db.query(User)

        .filter(

            User.email == email

        )

        .first()

    )



    if user is None:


        raise HTTPException(

            status_code=404,


            detail=
            "User not found"

        )



    return user