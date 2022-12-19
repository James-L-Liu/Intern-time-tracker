from domainmodel.user_project_interface import People
from domainmodel.Task import Task
from domainmodel.Project import Project


class Admin(People):
    ID_number = 0
    def __init__(self, name: str, email: str, age: int):
        self.__name = name
        self.__email = email
        self.__age = age
        self.__list_of_tasks = list[Task]()
        self.__list_of_users = list[People]()
        self.__list_of_projects = list[Project]()
        self.__ID = Admin.ID_number
        Admin.ID_number += 1
        self.__time_spent = 0

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, newname: str):
        self.__name = None
        if type(newname) is str and newname.strip() != '':
            self.__name = newname.strip()

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
        if type(new_age) is int and new_age > 0:
            self.__age = new_age

    @property
    def list_of_projects(self):
        return self.__list_of_projects

    @property
    def ID(self) -> str:
        string_ID = str(self.__ID)
        if len(string_ID) == 1:
            return "AD0000" + string_ID
        elif len(string_ID) == 2:
            return "AD000" + string_ID
        elif len(string_ID) == 3:
            return "AD00" + string_ID
        elif len(string_ID) == 4:
            return "AD0" + string_ID
        else:
            return "AD" + string_ID

    def create_project(self, name: str):
        new_proj = Project(name)
        self.__list_of_projects.append(new_proj)
        new_proj.admin = self

    def take_project(self, project: Project):
        self.__list_of_projects.append(project)
        project.admin = self

    def delete_project(self, project: Project):
        if project in self.list_of_projects:
            project.admin = None
            self.list_of_projects.remove(project)

    def mark_proj_as_done(self, project: Project):
        project.is_done = True
        for user in project.get_all_users:
            user.get_project_done()

    #def assign_proj_to_user(self):
    def assign_task_to_user(self, user: People, task: Task):
        user.take_task(task)


    def __repr__(self):
        return f"<Admin {self.name}, ID_number = {self.ID}>"

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



