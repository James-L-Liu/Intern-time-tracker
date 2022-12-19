import adapters.repository as repo
import adapters.services as services
from domainmodel.Task import Task

def get_all_tasks():
    return services.get_all_tasks(repo.repo_instance)

def add_task(name, description):
    services.add_task(repo.repo_instance, name, description)

def get_task(task_id):
    return services.get_task(repo.repo_instance, task_id)

def delete_task(task: Task):
    services.delete_task(repo.repo_instance, task)