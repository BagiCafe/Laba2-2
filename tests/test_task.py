import pytest
from src.models.task import Task, TaskSource


class TestTask:

    def test_task_creation(self):
        task = Task(id=67, payload={"user_id": 121})
        assert task.id == 67
        assert task.payload == {"user_id": 121}

    def test_task_different_payloads(self):
        task1 = Task(id=6, payload={"user_id": 123})
        task2 = Task(id=7, payload={"user_id": 456, "count": 10})
        assert task1.id != task2.id
        assert task1.payload != task2.payload

    def test_task_creation_valid(self):
        task = Task(id=1, payload={"user_id": 123, "data": "test"})
        assert task.id == 1
        assert task.payload == {"user_id": 123, "data": "test"}
        assert isinstance(task.id, int)
        assert isinstance(task.payload, dict)

    def test_task_creation_minimal(self):
        task = Task(id=42, payload={})
        assert task.id == 42
        assert task.payload == {}

    def test_task_creation_different_types(self):
        task1 = Task(id=1, payload={"x": 1})
        task2 = Task(id=999, payload={"y": 2})
        task3 = Task(id=-5, payload={"z": 3})

        assert task1.id == 1
        assert task2.id == 999
        assert task3.id == -5

    def test_task_equality(self):
        task1 = Task(id=1, payload={"x": 1})
        task2 = Task(id=1, payload={"x": 1})
        task3 = Task(id=2, payload={"x": 1})

        assert task1 == task2
        assert task1 != task3
        assert task2 != task3

    def test_task_string_representation(self):
        task = Task(id=123, payload={"name": "test"})
        repr_str = repr(task)
        assert "Task" in repr_str
        assert "id=123" in repr_str
        assert "payload={'name': 'test'}" in repr_str or "payload={'name': 'test'}" in repr_str


class TestTaskSourceProtocol:

    def test_protocol_with_valid_class(self):

        class ValidSource:
            def get_tasks(self) -> list[Task]:
                return [Task(1, {"test": "data"})]

        assert isinstance(ValidSource(), TaskSource)

    def test_protocol_with_invalid_class(self):

        class InvalidSource:
            def wrong_method(self) -> list[Task]:
                return []

        assert not isinstance(InvalidSource(), TaskSource)

    def test_protocol_with_wrong_return_type(self):

        class WrongReturnSource:
            def get_tasks(self) -> str:  # Должен быть list[Task]
                return "not a list"

        assert isinstance(WrongReturnSource(), TaskSource)