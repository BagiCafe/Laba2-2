class TaskError(Exception):
    pass

class TaskStateError(TaskError):
    def __init__(self, message: str):
        self.message = message
        super().__init__(f"Ошибка состояния задачи: {message}")