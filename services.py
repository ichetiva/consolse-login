from hashlib import sha256


def hash_password(password: str) -> str:
    return sha256(password.encode()).hexdigest()


def check_password(hashed_password: str, input_password: str) -> bool:
    return hashed_password == hash_password(input_password)
