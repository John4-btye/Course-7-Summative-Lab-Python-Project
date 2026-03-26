from models.user import User


def test_user_creation():
    user = User("John", "john@test.com")
    assert user.name == "John"
    assert user.email == "john@test.com"
    assert user.projects == []