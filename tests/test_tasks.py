from models.task import Task


def test_task_completion():
    task = Task("My Task")
    task.mark_complete()
    assert task.status == "complete"