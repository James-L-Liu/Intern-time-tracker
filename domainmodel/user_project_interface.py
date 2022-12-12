import abc

class People(abc.ABC):
    ID = None
    @abc.abstractmethod
    def take_project(self, project):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_project(self, project):
        raise NotImplementedError

    @abc.abstractmethod
    def create_project(self, name: str):
        raise NotImplementedError

    def take_task(self, task):
        pass