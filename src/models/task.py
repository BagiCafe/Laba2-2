from dataclasses import dataclass
from typing import Protocol, runtime_checkable
from datetime import datetime
from src.exceptions import TaskStateError
from src.descriptors import IntegerValidator, StringValidator, StatusValidator


class Task:
    id = IntegerValidator("_id", min_value=1)
    priority = IntegerValidator("_priority", min_value=1, max_value=10)
    description = StringValidator("_description")
    status = StatusValidator("_status")

    def __init__(self, id: int, description: str, priority: int = 1, status: str = "created", payload: dict = None):
        self.id = id
        self.description = description
        self.priority = priority
        self.status = status
        self._created_at = datetime.now()
        self.payload = payload or {}

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @property
    def is_ready(self) -> bool:
        return self.status == "created" and len(self.description) > 0

    @property
    def is_active(self) -> bool:
        return self.status == "in_progress"

    @property
    def is_completed(self) -> bool:
        return self.status == "completed"

    @property
    def is_failed(self) -> bool:
        return self.status == "failed"

    def start(self) -> None:
        if self.status != "created":
            raise TaskStateError(f"Нельзя начать задачу со статусом '{self.status}'.")
        self.status = "in_progress"

    def cancel(self) -> None:
        if self.status == "completed":
            raise TaskStateError("Нельзя отменить завершённую задачу")
        self.status = "failed"

    def complete(self) -> None:
        if self.status != "in_progress":
            raise TaskStateError(f"Нельзя завершить задачу со статусом '{self.status}'.")
        self.status = "completed"

    def __repr__(self) -> str:
        return f"Task(id={self.id}, priority={self.priority}, status={self.status})"


@runtime_checkable
class TaskSource(Protocol):
    """Протокол источника задач. Определяет контракт, которому должны соответствовать все источники задач"""
    def get_tasks(self) -> list[Task]:
        """Получаем список задач из источника"""
        pass