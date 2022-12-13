import adapters.repository as repo
import adapters.services as services


def get_all_tasks():
    return services.get_all_tasks(repo.repo_instance)

def add_task(name, description):
    services.add_task(repo.repo_instance, name, description)