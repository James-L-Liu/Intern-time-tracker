
from pathlib import Path
from datetime import date, datetime
from typing import List

from bisect import bisect, bisect_left, insort_left

from werkzeug.security import generate_password_hash

from domainmodel.user import User
from domainmodel.Admin import Admin
from domainmodel.Project import Project
from domainmodel.Task import Task

class MemoryRepository():
    def __init__(self):
        self.__users = list[User]()
        self.__projects = list[Project]()
        self.__tasks = list[Task]()
        self.__admin = None

    def add_user(self, user: User):
        self.__users.append(user)

    def get_user(self, user_id) -> User:
        user = None
        for u in self.__users:
            if u.ID == user_id:
                user = u
        return user

    def get_all_users(self) -> list[User]:
        return self.__users

    def delete_user(self, user: User):
        for element in self.__users:
            if element is user:
                self.__users.remove(element)

    def add_task(self, task: Task):
        self.__tasks.append(task)

    def get_task(self, task_id) -> Task:
        result = None
        for task in self.__tasks:
            if task.ID == task_id:
                result = task
        return result

    def get_all_tasks(self) -> list[Task]:
        return self.__tasks

    def delete_task(self, task: Task):
        for element in self.__tasks:
            if element is task:
                self.__tasks.remove(element)

    def add_project(self, project: Project):
        self.__projects.append(project)

    def get_project(self, project_id) -> Project:
        result = None
        for project in self.__projects:
            if project.ID == project_id:
                result = project
        return result

    def get_all_projects(self) -> list[Project]:
        return self.__projects