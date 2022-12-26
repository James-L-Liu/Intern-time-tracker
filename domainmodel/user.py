from domainmodel.Admin import Admin
from domainmodel.Task import Task
from domainmodel.Project import Project
from domainmodel.user_project_interface import People

class User(People):
    ID_number = 0
    def __init__(self, name: str, email: str, age: int, password: str, admin: Admin or None = None):
        self.__name = name.strip()
        self.__email = email
        self.__age = age
        self.__admin = admin
        self.__password = password
        self.__project: Project or None = None
        self.__list_of_tasks = list[Task]()
        self.__tasks_done = list[Task]()
        self.__projects_done = list[Project]()
        self.__number_of_projects = 0
        self.__ID = User.ID_number
        User.ID_number += 1

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, newname: str):
        self.__name = None
        if type(newname) is str and newname.strip() != '':
            self.__name= newname.strip()

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, new_email: str):
        self.__email = None
        if type(new_email) is str and new_email.strip() != '':
            self.__email = new_email.strip()

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, new_age: int):
        self.__age = ''
        if isinstance(new_age, int) and new_age > 0:
            self.__age = new_age

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, new_password: str):
        if isinstance(new_password, str):
            self.__password = new_password

    @property
    def admin(self) -> Admin:
        return self.__admin

    @admin.setter
    def admin(self, new_admin: Admin or None = None):
        self.__admin = None
        if isinstance(new_admin, Admin):
            self.__admin = new_admin

    @property
    def ID(self) -> str:
        string_ID = str(self.__ID)
        if len(string_ID) == 1:
            return "JK0000" + string_ID
        elif len(string_ID) == 2:
            return "JK000" + string_ID
        elif len(string_ID) == 3:
            return "JK00" + string_ID
        elif len(string_ID) == 4:
            return "JK0" + string_ID
        else:
            return "JK" + string_ID

    @property
    def project(self) -> Project:
        return self.__project

    @project.setter
    def project(self, new_project):
        self.__project = None
        if isinstance(new_project, Project):
            self.__project = new_project
            new_project.add_user(self)

    @property
    def number_of_projects(self) -> 0 or 1:
        return self.__number_of_projects

    @number_of_projects.setter
    def number_of_projects(self, value: 0 or 1):
        self.__number_of_projects = value

    def take_project(self, project: Project):
        if self.project is None or self.get_project_done():
            self.project = project

    def delete_project(self, project=None):
        proj = self.project
        proj.remove_user(self)
        self.project = None
        self.number_of_projects = 0

    def get_project_done(self):
        if self.project.isDone():
            self.project.status = 'done'
            self.__projects_done.append(self.project)
            return True
        return False

    def create_project(self, name: str):
        if self.project is None or self.get_project_done():
            project = Project(name)
            self.project = project

    def create_task(self, name: str):
        task = Task(name)
        task.user = self
        self.__list_of_tasks.append(task)

    def get_task_done(self, task: Task):
        if task in self.__list_of_tasks and task.isDone():
            task.status = 'done'
            self.__list_of_tasks.remove(task)
            self.__tasks_done.append(task)
            return True
        return False

    def delete_task(self, task: Task):
        if task in self.__list_of_tasks:
            task.user = None
            self.__list_of_tasks.remove(task)

    def take_task(self, task: Task):
        if isinstance(task, Task):
            self.__list_of_tasks.append(task)
            task.user = self

    def __repr__(self):
        return f"<User {self.name}, ID_number = {self.ID}>"

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


