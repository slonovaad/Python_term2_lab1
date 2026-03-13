from __future__ import annotations
from dataclasses import dataclass

from src.error_types import TaskError


@dataclass(frozen=True, slots=True)
class StdinTask:
    """Класс задачи, получаемой по вводу"""
    id: int
    payload: str
    attrs = ["payload"]

    @classmethod
    def make_task_from_dict(cls, data: dict[str, str | int]) -> StdinTask:
        """Метод, создающий объект задачи из переданного словаря
        :param data: словарь с входной информацией
        :return: объект задачи"""
        if not (isinstance(data, dict)):
            raise TaskError(f'Data in invalid: {data}')
        if 'id' not in data:
            raise TaskError(f'Task id is missing: {data}')
        try:
            task_id = int(data['id'])
        except ValueError:
            raise TaskError(f'Task id is invalid: {data}')
        if task_id < 0:
            raise TaskError(f'Task id is invalid: {data}')
        attrs = []
        for key in cls.attrs:
            if key not in data:
                raise TaskError(f'Task {key} is missing: {data}')
            attrs.append(str(data[key]))
        return StdinTask(task_id, *attrs)
