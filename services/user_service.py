from models.user import User


class UserService:
    def __init__(self, data):
        self.data = data

    def create_user(self, name, email):
        """Create and store a new user."""

        # Prevent duplicate users
        existing = self.find_user_by_name(name)
        if existing:
            raise ValueError(f"User '{name}' already exists.")

        # Generate unique ID from data
        users = self.data.get("users", [])
        new_id = max([u["id"] for u in users], default=0) + 1

        user = User(name, email)
        user.id = new_id  # override BaseModel ID

        self.data["users"].append({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "projects": []
        })

        return user

    def get_all_users(self):
        """Return all users."""
        return self.data.get("users", [])

    def find_user_by_name(self, name):
        """Find a user by name."""
        for user in self.data.get("users", []):
            if user["name"].lower() == name.lower():
                return user
        return None

    def find_user_by_id(self, user_id):
        """Find user by ID."""
        for user in self.data.get("users", []):
            if user["id"] == user_id:
                return user
        return None