class Character:
    def __init__(self, name: str, inteligence: int, dexterity: int, strength: int, charisma: int):
        self.name = name
        self.inteligence = inteligence
        self.dexterity = dexterity
        self.strength = strength
        self.charisma = charisma

        self.physical_health = self.dexterity + self.strength
        self.mental_health = self.inteligence + self.charisma

        self.skill_points = self.inteligence + self.strength
        self.items_points = self.dexterity + self.charisma
