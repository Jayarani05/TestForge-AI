from passlib.context import CryptContext

from jose import jwt

from datetime import (
    datetime,
    timedelta
)



SECRET_KEY = (
    "testforge-secret-key"
)


ALGORITHM = (
    "HS256"
)


pwd_context = CryptContext(

    schemes=["bcrypt"],

    deprecated="auto"

)




def hash_password(
    password
):

    return pwd_context.hash(
        password
    )




def verify_password(

    plain,

    hashed

):

    return pwd_context.verify(

        plain,

        hashed

    )





def create_token(
    data:dict
):


    payload = data.copy()


    expire = (
        datetime.utcnow()
        +
        timedelta(hours=24)
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