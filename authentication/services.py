from werkzeug.security import generate_password_hash, check_password_hash

from adapters.repository import AbstractRepository
from domainmodel.user import User


class NameNotUniqueException(Exception):
    pass

class UnknownUserException(Exception):
    pass

class AuthenticationException(Exception):
    pass

class UnknownIdException(Exception):
    pass

def add_user(user_name: str, email:str, age: int, password: str, repo: AbstractRepository):
    user = repo.get_user_by_name(user_name)
    if user is not None:
        raise NameNotUniqueException

    password_hash = generate_password_hash(password)
    print(age)
    user = User(user_name, email, age, password_hash)
    repo.add_user(user)