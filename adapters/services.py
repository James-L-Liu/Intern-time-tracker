from adapters.repository import AbstractRepository
from domainmodel.user import User
from domainmodel.Task import Task

def get_all_users(repo: AbstractRepository):
    return repo.get_all_users()

def get_user(repo: AbstractRepository, user_id):
    return repo.get_user(user_id)

def add_user(repo: AbstractRepository, name, email, age, password):
    repo.add_user(User(name, email, age, password))

def delete_user(repo: AbstractRepository, user: User):
    repo.delete_user(user)

def get_all_tasks(repo: AbstractRepository):
    return repo.get_all_tasks()

def add_task(repo: AbstractRepository, name, description, time):
    task = Task(name, description)
    task.time = int(time)
    repo.add_task(task)

def get_task(repo: AbstractRepository, task_id):
    return repo.get_task(task_id)

def delete_task(repo: AbstractRepository, task: Task):
    repo.delete_task(task)