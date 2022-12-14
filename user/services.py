import adapters.repository as repo
import adapters.services as services
from domainmodel.user import User

def get_all_users():
    return services.get_all_users(repo.repo_instance)

def get_user(user_id):
    return services.get_user(repo.repo_instance, user_id)

def add_user(name, email, age, passowrd):
    services.add_user(repo.repo_instance, name, email, age, passowrd)

def delete_user(user: User):
    services.delete_user(repo.repo_instance, user)