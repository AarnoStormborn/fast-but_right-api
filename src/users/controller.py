from uuid import UUID
from fastapi import APIRouter, status

from . import models
from . import service
from ..database.core import DbSession
from ..auth.service import CurrentUser

router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.get("/me", response_model=models.UserResponse)
def get_current_user(current_user: CurrentUser, db: DbSession):
    return service.get_user_by_id(db, current_user.get_uuid())
    

@router.put("/change-password", status_code=status.HTTP_200_OK)
async def login_for_access_token(
    password_change: models.PasswordChange,
    db: DbSession,
    current_user: CurrentUser
):
    return service.change_password(db, current_user.get_uuid(), password_change)