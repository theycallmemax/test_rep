# from fastapi import APIRouter

# from core.use_cases.user_use_cases import UserUseCases
# from infra.db.user_repository_impl import UserRepositoryImpl

# router = APIRouter()
# user_repository = UserRepositoryImpl()
# user_use_cases = UserUseCases(user_repository)


# @router.post("/users")
# def register_user(name: str, email: str):
#     return user_use_cases.register_user(name, email)
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from core.use_cases.user_use_cases import UserUseCases
from infra.container import Container

router = APIRouter()


@router.post("/users")
@inject
def register_user(
    name: str,
    email: str,
    user_use_cases: UserUseCases = Depends(Provide[Container.user_use_cases]),
):
    return user_use_cases.register_user(name, email)
