# from core.entities.user import User


# class UserUseCases:
#     def __init__(self, user_repository):
#         self.user_repository = user_repository

#     def register_user(self, name: str, email: str):
#         user = User(id=None, name=name, email=email)
#         return self.user_repository.save(user)
from core.entities.user import User
from core.repositories.user_repository import UserRepository


class UserUseCases:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register_user(self, name: str, email: str) -> User:
        # Create a new user
        user = User(name=name, email=email)
        # Save it to the repository
        return self.user_repository.create(user)

    def get_user_by_id(self, user_id: int) -> User:
        return self.user_repository.read_by_id(user_id)

    def get_user_by_email(self, email: str) -> User:
        return self.user_repository.read_by_email(email)

    def get_all_users(self):
        return self.user_repository.read_all()

    def update_user(self, user: User) -> User:
        return self.user_repository.update(user)

    def delete_user(self, user_id: int) -> None:
        self.user_repository.delete(user_id)
