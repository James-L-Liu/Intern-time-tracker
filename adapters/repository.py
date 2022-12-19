import abc
from domainmodel.user import User
from domainmodel.Admin import Admin
from domainmodel.Project import Project
from domainmodel.Task import Task

repo_instance = None


class RepositoryException(Exception):

    def __init__(self, message=None):
        pass


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add_user(self, user: User):
        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self, user_id) -> User:
        raise NotImplementedError

    @abc.abstractmethod
    def get_all_users(self) -> list[User]:
        raise NotImplementedError

    @abc.abstractmethod
    def delete_user(self, user: User):
        raise NotImplementedError

    @abc.abstractmethod
    def add_task(self, task: Task):
        raise NotImplementedError

    @abc.abstractmethod
    def get_task(self, task_id) -> Task:
        raise NotImplementedError

    @abc.abstractmethod
    def get_all_tasks(self) -> list[Task]:
        raise NotImplementedError

    @abc.abstractmethod
    def delete_task(self, task: Task):
        raise NotImplementedError

    @abc.abstractmethod
    def add_project(self, project: Project):
        raise NotImplementedError

    @abc.abstractmethod
    def get_project(self, project_id) -> Project:
        raise NotImplementedError

    @abc.abstractmethod
    def get_all_projects(self) -> list[Project]:
        raise NotImplementedError



