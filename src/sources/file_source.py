from __future__ import annotations

import json
import os

from src.task_types.base_task import BaseTask
from src.contracts.task import Task
from src.error_types import SourceError
from src.constants.source_constants import SOURCE_FOLDER


class FileSource:
    """Класс файлового источника"""
    task_class = BaseTask
    name: str
    file_name: str
    task_count: int

    def __init__(self, name: str, file_name: str) -> None:
        self.name = name
        self.file_name = file_name
        self.task_count = 0

    @staticmethod
    def make_source_by_stdin() -> FileSource:
        """Метод, создающий новый источник по вводимым данным
        :return: итоговый источник"""
        name = input("Enter source name: ")
        file_name = input("Enter file name: ")
        file_name = os.path.join(SOURCE_FOLDER, file_name)
        return FileSource(name, file_name)

    def get_task(self) -> Task | None:
        """Метод, получающий следующую задачу из источника
        :return: задача или None, если источник пуст"""
        if not os.path.isfile(self.file_name):
            raise SourceError(f"File {self.file_name} not found")
        try:
            with open(self.file_name, 'r') as file:
                data = json.load(file)
        except (UnicodeDecodeError, json.decoder.JSONDecodeError):
            raise SourceError(f"Incorrect data in file: {self.file_name}")
        if len(data) == 0:
            return None
        if not (isinstance(data, list)):
            raise SourceError(f'Incorrect data in file: {self.file_name}')
        task = self.task_class.make_task_from_dict(data[0] | {'id': self.task_count})
        self.task_count += 1
        with open(self.file_name, 'w') as file:
            json.dump(data[1:], file)
        return task

    def get_all_tasks(self) -> list[Task] | None:
        """Метод, получающий все задачи из источника
        :return: список задач или None, если источник пуст"""
        if not os.path.isfile(self.file_name):
            raise SourceError(f"File {self.file_name} not found")
        all_tasks: list[Task] = []
        try:
            with open(self.file_name, 'r') as file:
                data = json.load(file)
        except (UnicodeDecodeError, json.decoder.JSONDecodeError):
            raise SourceError(f"Incorrect data in file: {self.file_name}")
        if len(data) == 0:
            return None
        if not (isinstance(data, list)):
            raise SourceError(f'Incorrect data in file: {self.file_name}')
        for task in data:
            all_tasks.append(self.task_class.make_task_from_dict(task | {'id': self.task_count}))
            self.task_count += 1
        with open(self.file_name, 'w') as file:
            json.dump([], file)
        return all_tasks
