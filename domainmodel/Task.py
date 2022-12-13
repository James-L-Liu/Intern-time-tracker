from domainmodel.user_project_interface import People
from domainmodel.work_interface import Work

class Task():
    id_number = 0
    def __init__(self, name: str, description: str = None):
        self.__name: str = name
        self.__description: str or None = description
        self.__user: People or None = None
        self.__project: Work or None = None
        self.__is_done: bool = False
        self.__status: str = 'undone'
        self.__ID = Task.id_number
        Task.id_number += 1

    @property
    def ID(self) -> str:
        string_ID = str(self.__ID)
        if len(string_ID) == 1:
            return "TK#0000" + string_ID
        elif len(string_ID) == 2:
            return "TK#000" + string_ID
        elif len(string_ID) == 3:
            return "TK#00" + string_ID
        elif len(string_ID) == 4:
            return "TK#0" + string_ID
        else:
            return "TK#" + string_ID

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if (type(new_name) is str) and new_name.strip() != "":
            self.__name = new_name

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, new_description):
        if (type(new_description) is str):
            self.__description = new_description

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, new_user: People or None):
        self.__user = None
        if (isinstance(new_user, People) and new_user.ID[0: 2] == 'JK'):
            self.__user = new_user

    @property
    def is_done(self):
        return self.__is_done

    @is_done.setter
    def is_done(self, value: bool):
        self.__is_done = None
        if isinstance(value, bool):
            self.__is_done = value

    def isDone(self):
        return self.__is_done

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, new_status):
        self.__status = None
        if isinstance(new_status, str):
            self.__status = new_status

    @property
    def project(self):
        return self.__project

    @project.setter
    def project(self, proj):
        self.__project = None
        if isinstance(proj, Work) and proj.ID[: 3] == 'Prj':
            self.__project = proj

    def __repr__(self):
        return f"<Task {self.name}>"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.ID == other.ID

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return True
        return self.ID < other.ID

    def __hash__(self):
        return hash(self.ID)