from dependency_injector.wiring import Provide, inject
from fastapi import Depends
from jose import jwt
from pydantic import ValidationError

# from config import settings
from config.settings import settings
from core.entities.auth_schema import Payload
from core.entities.user_schema import BaseUser
from infra.container import Container
from infra.exceptions.exceptions import AuthError
from infra.security.security_entity import ALGORITHM, JWTBearer
from service.user_service import UserService


@inject
def get_current_user_payload(
    token: str = Depends(JWTBearer()),
    service: UserService = Depends(Provide[Container.user_service]),
) -> Payload:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=ALGORITHM)
        token_data = Payload(**payload)
    except (jwt.JWTError, ValidationError):
        raise AuthError(detail="Could not validate credentials")
    current_user: BaseUser = service.get_user_by_id(token_data.id)
    if not current_user:
        raise AuthError(detail="User not found")
    service.update_last_activity(current_user.payload.id)
    return current_user.payload


def get_current_superuser_payload(
    current_user_payload: Payload = Depends(get_current_user_payload),
) -> Payload:
    if not current_user_payload.is_superuser:
        raise AuthError("It's not a super user")
    return current_user_payload
