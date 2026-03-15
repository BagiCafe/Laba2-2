import logging
import sys
from src.sources.generator_source import TaskSourceGenerator
from src.sources.file_source import TaskSourceFile
from src.sources.api_source import TaskSourceAPI
from src.models.task import TaskSource, Task
from src.exceptions import TaskStateError

def setup_logging() -> None:
    """Настройка логирования только в консоль."""
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] %(message)s',
        datefmt='%H:%M:%S',
        stream=sys.stdout
    )

def process_tasks(source: TaskSource, logger: logging.Logger) -> None:
    """Обработка задач из любого источника, соответствующего протоколу."""
    tasks = source.get_tasks()
    logger.info(f"Получено {len(tasks)} задач из {source.__class__.__name__}")
    for task in tasks:
        logger.info(f"  Задача {task.id}: {task.payload}")
        logger.info(f"      Описание: {task.description}")
        logger.info(f"      Приоритет: {task.priority}")
        logger.info(f"      Статус: {task.status}")
        logger.info(f"      Время создания: {task.created_at}")
        logger.info(f"      Готовность к выполнению: {task.is_ready}")
        logger.info(f"      Выполняется сейчас: {task.is_active}")
        logger.info(f"      Завершена: {task.is_completed}")
        logger.info(f"      Отменена: {task.is_failed}")

def main() -> None:
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Запуск")

    generator = TaskSourceGenerator()
    api = TaskSourceAPI()
    file = TaskSourceFile("data/tasks.json")

    sources = [generator, api, file]
    for source in sources:
        if isinstance(source, TaskSource):
            process_tasks(source, logger)
        else:
            logger.error(f"Источник {source.__class__.__name__} не соответствует протоколу")

if __name__ == "__main__":
    main()