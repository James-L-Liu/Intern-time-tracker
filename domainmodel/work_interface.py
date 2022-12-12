import abc

class Work(abc.ABC):
    ID = None

    @abc.abstractmethod
    def isDone(self):
        raise NotImplementedError