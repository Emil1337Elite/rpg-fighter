class Character:
    
    def __init__(self, name, health, attack, armor):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor
        
    def __str__(self) -> str:
        return f"Name: {self.name}\nHealth: {self.health}\nAttack: {self.attack}\nArmor: {self.armor}"
    
    def get_attack(self):
        return self.attack
    
    def take_damage(self, damage):
        relative_damage = damage - self.armor
        if relative_damage > 0:
            self.health -= relative_damage
        if self.health < 0: self.health = 0

    def get_health(self):
        return self.health

    def get_name(self):
        return self.name

class Goblin:
    
    def __init__(self, health, attack, armor, id):
        self.health = health
        self.attack = attack
        self.armor = armor
        self.id = id
        
    def __str__(self) -> str:
        return f"Goblin #{self.id}\nHealth: {self.health}\nAttack: {self.attack}\nArmor: {self.armor}"


    
    def take_damage(self, damage):
        relative_damage = damage - self.armor
        if relative_damage > 0:
            self.health -= relative_damage
        if self.health < 0: self.health = 0

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack

    def get_name(self):
        return f"Goblin #{self.id}"

def save_character(char : Character):
    name, health, attack, armor = char.get_attributes()
    save_string = f"{name}/{health}/{attack}/{armor}\n"
    with open ("saved_characters.txt", "a", encoding="utf-8") as f:
        f.write(save_string)
        print(f"{name} has been successfully saved.")

def load_character():
    characters = []
    with open ("saved_characters.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            attributes = line.split("/")
            char = Character(attributes[0],
                             attributes[1],
                             attributes[2],
                             attributes[3])
            
            characters.append(char)
    return characters