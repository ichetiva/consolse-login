import os
import sys
import typing
from getpass import getpass

from colorama import init, Fore, Style

from managers import UsersManager
from objects import User
from services import hash_password, check_password

init()


class LoginSystem:
    users: typing.List[User] = []
    users_manager: UsersManager = UsersManager()

    def __init__(self):
        self.current_user: typing.Optional[User] = None
        self.commands: typing.Dict[str, typing.Callable] = {
            "status": self.status,
            "exit": self.exit,
            "register": self.register,
            "login": self.login,
            "clear": self.clear,
        }

    def login(self):
        input_email = input("Email: ").strip()
        input_password = getpass().strip()

        if not self.users_manager.get_by_email(input_email):
            print("User with this email is not exists.")
        else:
            user = self.users_manager.get_by_email(input_email)
            if not check_password(user.password, input_password):
                print("Wrong password.")
            else:
                self.current_user = user
                print(Fore.GREEN + "Success!" + Fore.WHITE)

    def register(self):
        input_email = input("Email: ").strip()
        input_password = getpass().strip()
        input_repeat_password = getpass("Repeat Password: ").strip()

        if self.users_manager.get_by_email(input_email):
            print("User with this email now exists.")
        elif input_password != input_repeat_password:
            print("Password mismatch.")
        elif len(input_password) < 8:
            print("Length of password must be more or equal 8 symbols.")
        else:
            new_user = User(
                email=input_email,
                password=hash_password(input_password)
            )
            self.users_manager.add(new_user)

            print(f"You are {Fore.GREEN}signed up{Fore.WHITE}.")

    def status(self):
        if self.current_user:
            print(f"Status: {Fore.GREEN}authorized{Fore.WHITE}.\n"
                  f"User email: {Style.BRIGHT}{self.current_user.email}{Style.RESET_ALL}.")
        else:
            print(f"Status: {Fore.RED}unauthorized{Fore.WHITE}.")

    @staticmethod
    def exit():
        sys.exit(0)

    @staticmethod
    def clear():
        os.system("cls")

    def command_manager(self, command: str):
        try:
            self.commands[command]()
        except KeyError:
            print(f"{Fore.RED}{command}{Fore.WHITE}: command not found.")

    def run(self):
        while True:
            input_command = input("... $ ").strip()
            self.command_manager(input_command)


if __name__ == "__main__":
    login_system = LoginSystem()
    login_system.run()
