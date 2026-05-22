from fastapi import FastAPI, Depends, HTTPException, status
from sqlmodel import select
from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from .database import init_db, get_session
from .models import User, Role
from .schemas import UserCreate, UserRead

from typing import List

SECRET_KEY = "CHANGE_ME_SECRET"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

app = FastAPI()

init_db()


def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def get_user_by_email(session, email: str):
    stmt = select(User).where(User.email == email)
    return session.exec(stmt).first()


def authenticate_user(session, email: str, password: str):
    user = get_user_by_email(session, email)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user


async def get_current_user(token: str = Depends(oauth2_scheme), session = Depends(get_session)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user_by_email(session, email)
    if user is None:
        raise credentials_exception
    return user


def admin_required(current_user: User = Depends(get_current_user)):
    if current_user.role != Role.admin:
        raise HTTPException(status_code=403, detail="Admin privileges required")
    return current_user


@app.post("/register", response_model=UserRead)
def register(user_in: UserCreate, session = Depends(get_session)):
    existing = get_user_by_email(session, user_in.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = User(full_name=user_in.full_name, email=user_in.email, hashed_password=get_password_hash(user_in.password), role=Role(user_in.role.value))
    session.add(user)
    session.commit()
    session.refresh(user)
    return UserRead(id=user.id, full_name=user.full_name, email=user.email, role=user.role)


@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), session = Depends(get_session)):
    user = authenticate_user(session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users", response_model=List[UserRead], dependencies=[Depends(admin_required)])
def list_users(session = Depends(get_session)):
    users = session.exec(select(User)).all()
    return [UserRead(id=u.id, full_name=u.full_name, email=u.email, role=u.role) for u in users]


@app.delete("/users/{user_id}", dependencies=[Depends(admin_required)])
def delete_user(user_id: int, session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return {"detail": "User deleted"}
