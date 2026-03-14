import json, logging
from src.models.task import Task, TaskSource

logger = logging.getLogger(__name__)


class TaskSourceFile:
    """Источник задач из JSON-файла"""
    def __init__(self, file_name: str):
        """Инициализирует файловый источник, проверяя соответствие протоколу TaskSource при создании"""
        self.file_name = file_name
        if not isinstance(self, TaskSource):
            logger.error(f"{self.__class__.__name__} не соответствует протоколу TaskSource")
            raise TypeError(f"{self.__class__.__name__} не соответствует протоколу TaskSource")

    def get_tasks(self) -> list[Task]:
        """Читает задачи из JSON-файла. Открывает файл, загружает JSON и преобразует в список задач"""
        try:
            with open(self.file_name, "r") as f:
                data = json.load(f)
                tasks = [Task(id = i["id"], payload={"user_id": i["user_id"]}) for i in data]
            return tasks
        except Exception as e:
            logger.error(f"Ошибка при чтении файла: {e}")
            raise