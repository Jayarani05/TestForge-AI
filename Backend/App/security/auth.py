from passlib.context import CryptContext

from jose import (
    jwt,
    JWTError
)

from datetime import (
    datetime,
    timedelta
)


from fastapi import (
    Depends,
    HTTPException
)


from fastapi.security import (
    OAuth2PasswordBearer
)


from sqlalchemy.orm import Session


from app.database.session import (
    get_db
)


from app.database.models import (
    User
)



# ==========================
# JWT CONFIG
# ==========================


SECRET_KEY = (
    "testforge-secret-key"
)


ALGORITHM = (
    "HS256"
)


ACCESS_TOKEN_EXPIRE_HOURS = 24



# ==========================
# PASSWORD HASHING
# ==========================


pwd_context = CryptContext(

    schemes=[
        "bcrypt"
    ],

    deprecated="auto"

)




def hash_password(
    password: str
):


    return pwd_context.hash(
        password
    )




def verify_password(

    plain_password: str,


    hashed_password: str

):


    return pwd_context.verify(

        plain_password,


        hashed_password

    )



# ==========================
# CREATE JWT TOKEN
# ==========================


def create_token(
    data: dict
):


    payload = data.copy()


    expire = (

        datetime.utcnow()

        +

        timedelta(
            hours=ACCESS_TOKEN_EXPIRE_HOURS
        )

    )


    payload.update(

        {

            "exp":

            expire

        }

    )


    token = jwt.encode(

        payload,


        SECRET_KEY,


        algorithm=ALGORITHM

    )


    return token




# ==========================
# GET CURRENT USER
# ==========================


oauth2_scheme = OAuth2PasswordBearer(

    tokenUrl="/api/v1/auth/login"

)



def get_current_user(

    token: str = Depends(
        oauth2_scheme
    ),


    db: Session = Depends(
        get_db
    )

):


    try:


        payload = jwt.decode(

            token,


            SECRET_KEY,


            algorithms=[
                ALGORITHM
            ]

        )


        user_id = payload.get(

            "user_id"

        )



        if user_id is None:


            raise HTTPException(

                status_code=401,


                detail="Invalid authentication token"

            )




    except JWTError:


        raise HTTPException(

            status_code=401,


            detail="Token expired or invalid"

        )




    user = (

        db.query(
            User
        )

        .filter(

            User.id
            ==
            user_id

        )

        .first()

    )



    if user is None:


        raise HTTPException(

            status_code=404,


            detail="User not found"

        )



    return user