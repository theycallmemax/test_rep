from pydantic import BaseModel, Field

from core.entities.auth_schema import Payload, Session


class UsersReport(BaseModel):
    active_users: int = Field(..., description="Total number of active users.")


class BaseUser(BaseModel):
    payload: Payload
    session: Session
