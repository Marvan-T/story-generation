import names


class Character:
    def __init__(self, role, involvement=None, name=None):
        self.name = name or names.get_full_name()
        self.role = role
        self.involvement = involvement
        self.modifier = None

    def __str__(self):
        return f"{self.name} ({self.role})"

