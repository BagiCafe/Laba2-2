from dataclasses import dataclass
from typing import Protocol, runtime_checkable


@dataclass
class Task:
    """Модель задачи. Содержит минимально необходимую информацию для обработки"""
    id: int
    payload: dict


@runtime_checkable
class TaskSource(Protocol):
    """Протокол источника задач. Определяет контракт, которому должны соответствовать все источники задач"""
    def get_tasks(self) -> list[Task]:
        """Получаем список задач из источника"""
        pass