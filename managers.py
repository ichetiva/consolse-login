import typing

from objects import User


class UsersManager:
    users: typing.List[User] = []

    def add(self, user: User) -> User:
        self.users.append(user)
        return user

    def remove(self, email: str) -> User:
        for number, user in enumerate(self.users):
            if user.email == email:
                del self.users[number]
                return user

    def get_by_email(self, email: str) -> User:
        for number, user in enumerate(self.users):
            if user.email == email:
                return user
