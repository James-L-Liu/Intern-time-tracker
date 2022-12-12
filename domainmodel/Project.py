
import Task
from domainmodel.user_project_interface import People
from work_interface import Work

class Project(Work):
    id_number = 0
    def __init__(self, name: str, descrition = None):
        self.__ID = Project.id_number
        Project.id_number += 1

        self.__name: str or None = None
        if isinstance(name, str) and name.strip() != '':
            self.__name= name
        self.__description = descrition
        self.__admin : People or None = None
        self.__users = list[People]()
        self.__tasks = list()
        self.__is_done = False
        self.status : str or None = None


    @property
    def ID(self):
        string_ID = str(self.__ID)
        if len(string_ID) == 1:
            return "Prj#0000" + string_ID
        elif len(string_ID) == 2:
            return "Prj#000" + string_ID
        elif len(string_ID) == 3:
            return "Prj#00" + string_ID
        elif len(string_ID) == 4:
            return "Prj#0" + string_ID
        else:
            return "Prj#" + string_ID

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
        if isinstance(new_description, str):
            self.__description = new_description

    @property
    def admin(self):
        return self.__admin

    @admin.setter
    def admin(self, new_admin: People):
        self.__admin = None
        if (isinstance(new_admin, People) and new_admin.ID[0: 2] == 'AD'):
            self.__admin = new_admin

    @property
    def get_all_users(self):
        return self.__users

    def add_user(self, new_user: People):
        if isinstance(new_user, People) and new_user.ID[:2] == 'JK':
            self.__users.append(new_user)


    def remove_user(self, user_remove: People):
        for i in range(len(self.__users), -1, -1):
            if self.__users[i] == user_remove:
                self.__users.pop(i)
                return

    @property
    def get_all_tasks(self):
        return self.__users

    def add_task(self, new_task: Task.Task):
        if isinstance(new_task, Task.Task):
            self.__tasks.append(new_task)

    def remove_task(self, task_remove):
        for i in range(len(self.__tasks), -1, -1):
            if self.__tasks[i] == task_remove:
                self.__tasks.pop(i)
                return
    @property
    def is_done(self):
        return self.__is_done

    @is_done.setter
    def is_done(self, value: bool):
        self.__is_done = value

    def isDone(self):
        return self.__is_done

    def __repr__(self):
        return f"---Project {self.name}, ID_number = {self.ID}--"

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