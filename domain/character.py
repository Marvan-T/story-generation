import names


class Character:
    def __init__(self, role, involvement=None, name=None):
        self.name = name or names.get_full_name()
        self.first_name = self.name.split()[0]
        self.role = role
        self.involvement = involvement
        self.modifier = None
        self.knowledge = []
        self.monster_escape = None
        self.status = "normal"
        self.preparation_progress = []

    def __str__(self):
        return f"{self.name} ({self.role})"

