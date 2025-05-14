# # from core.entities.user import User
# # from core.repositories.user_repository import UserRepository


# # class UserRepositoryImpl(UserRepository):
# #     def save(self, user):
# #         # Логика сохранения пользователя в базу данных
# #         return User(id=1, name=user.name, email=user.email)
# from typing import AbstractContextManager, Callable

# from sqlalchemy.orm import Session

# from core.entities.user import User
# from core.repositories.user_repository import UserRepository


# class UserRepositoryImpl(UserRepository):
#     def __init__(
#         self, session_factory: Callable[..., AbstractContextManager[Session]]
#     ) -> None:
#         self.session_factory = session_factory

#     def save(self, user):
#         with self.session_factory() as session:
#             db_user = User(name=user.name, email=user.email)
#             session.add(db_user)
#             session.commit()
#             session.refresh(db_user)
#             return db_user
# from typing import AbstractContextManager, Any, Callable, Dict, List, Optional
from contextlib import AbstractContextManager
from typing import Any, Callable, Dict, List, Optional

from sqlalchemy.orm import Session

from core.entities.user import User
from core.repositories.user_repository import UserRepository
from utils.date import get_now


class UserRepositoryImpl(UserRepository):
    def __init__(
        self, session_factory: Callable[..., AbstractContextManager[Session]]
    ) -> None:
        self.session_factory = session_factory

    def create(self, user: User) -> User:
        with self.session_factory() as session:
            session.add(user)
            session.commit()
            session.refresh(user)
            return user

    def read_by_id(self, user_id: int) -> Optional[User]:
        with self.session_factory() as session:
            return session.query(User).filter(User.id == user_id).first()

    def read_by_email(self, email: str) -> Optional[User]:
        with self.session_factory() as session:
            return session.query(User).filter(User.email == email).first()

    def read_all(self) -> List[User]:
        with self.session_factory() as session:
            return session.query(User).all()

    def update(self, user: User) -> User:
        with self.session_factory() as session:
            session.add(user)
            session.commit()
            session.refresh(user)
            return user

    def delete(self, user_id: int) -> None:
        with self.session_factory() as session:
            user = session.query(User).filter(User.id == user_id).first()
            if user:
                session.delete(user)
                session.commit()

    def update_last_activity(self, user_id: int) -> None:
        with self.session_factory() as session:
            user = session.query(User).filter(User.id == user_id).first()
            if user:
                user.last_activity_at = get_now()
                session.add(user)
                session.commit()

    def get_users_report(self) -> List[Dict[str, Any]]:
        with self.session_factory() as session:
            # This is a placeholder - implement according to your specific needs
            # For example, querying users with certain statistics or aggregations
            result = session.query(
                User.id, User.name, User.email, User.created_at, User.last_activity_at
            ).all()

            return [
                {
                    "id": r[0],
                    "name": r[1],
                    "email": r[2],
                    "created_at": r[3],
                    "last_activity_at": r[4],
                }
                for r in result
            ]
