from models.project import Project


def test_project_creation():
    project = Project("Test Project", "desc", "2026-01-01")
    assert project.title == "Test Project"
    assert project.description == "desc"
    assert project.tasks == []