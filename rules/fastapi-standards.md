---
paths:
  - "**/api/**/*.py"
  - "**/routers/**/*.py"
  - "**/app/**/*.py"
---

# Standards FastAPI

## Schemas Pydantic

```python
from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    email: EmailStr
    name: str = Field(..., min_length=2, max_length=100)

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

class UserResponse(UserBase):
    id: str
    created_at: datetime

    model_config = {"from_attributes": True}
```

## Routers

```python
from fastapi import APIRouter, Depends, HTTPException, status, Query

router = APIRouter()

@router.get("", response_model=UserListResponse)
async def list_users(
    page: int = Query(1, ge=1),
    per_page: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
):
    service = UserService(db)
    users, total = await service.list(page=page, per_page=per_page)
    return UserListResponse(data=users, total=total, page=page, per_page=per_page)

@router.post("", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user_data: UserCreate, db: AsyncSession = Depends(get_db)):
    return await UserService(db).create(user_data)
```

## Dependency Injection

```python
async def get_db() -> AsyncSession:
    async with async_session() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: AsyncSession = Depends(get_db),
):
    token = credentials.credentials
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    return await db.get(User, payload["sub"])
```

## Configuration

```python
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    database_url: str
    jwt_secret: str
    cors_origins: list[str] = ["http://localhost:3000"]

    model_config = {"env_file": ".env"}

@lru_cache
def get_settings() -> Settings:
    return Settings()
```
