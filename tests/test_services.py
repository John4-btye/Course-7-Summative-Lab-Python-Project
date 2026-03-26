from utils.file_handler import load_data
from services.user_service import UserService


def test_create_user_service():
    data = {"users": []}
    service = UserService(data)

    user = service.create_user("Alice", "alice@test.com")

    assert len(data["users"]) == 1
    assert data["users"][0]["name"] == "Alice"