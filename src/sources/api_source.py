import random, logging
from src.models.task import Task, TaskSource

logger = logging.getLogger(__name__)


class TaskSourceAPI:
    """Имитация источника задач из внешнего API"""
    def __init__(self):
        """Инициализирует API-источник, проверяя соответствие протоколу TaskSource при создании"""
        if not isinstance(self, TaskSource):
            logger.error(f"{self.__class__.__name__} не соответствует протоколу TaskSource")
            raise TypeError(f"{self.__class__.__name__} не соответствует протоколу TaskSource")

    def get_tasks(self) -> list[Task]:
        """Получает задачи из имитированного API"""
        return [
            Task(id=10, payload={"user_id": random.randint(100, 1001), "count": random.randint(1000,10001)}),
            Task(id=11, payload={"user_id": random.randint(100, 1001), "count": random.randint(1000,10001)}),
            Task(id=12, payload={"user_id": random.randint(100, 1001), "count": random.randint(1000,10001)}),
            Task(id=13, payload={"user_id": random.randint(100, 1001), "count": random.randint(1000,10001)})
        ]