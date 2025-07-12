import random

# ───── Base Character Class ─────
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health

    def attack(self, opponent):
        damage = random.randint(int(self.attack_power * 0.8), int(self.attack_power * 1.2))
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            opponent.health = 0
            print(f"{opponent.name} has been defeated!")

    def heal(self):
        amount = random.randint(15, 30)
        self.health = min(self.max_health, self.health + amount)
        print(f"{self.name} heals for {amount}. Current health: {self.health}/{self.max_health}")

    def display_stats(self):
        print(f"{self.name} - Health: {self.health}/{self.max_health} | Attack: {self.attack_power}")


# ───── Character Subclasses ─────
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

    def special_ability(self, opponent):
        print(f"{self.name} uses Power Strike!")
        damage = self.attack_power + 20
        opponent.health -= damage
        print(f"{self.name} deals {damage} damage!")


class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

    def special_ability(self, opponent):
        print(f"{self.name} casts Fireball!")
        damage = random.randint(30, 50)
        opponent.health -= damage
        print(f"Fireball hits for {damage} damage!")


class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=20)

    def special_ability(self, opponent):
        print(f"{self.name} uses Quick Shot!")
        total_damage = 0
        for _ in range(2):
            damage = random.randint(10, 20)
            total_damage += damage
            opponent.health -= damage
        print(f"{self.name} hits twice for a total of {total_damage} damage!")


class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=22)
        self.shielded = False

    def special_ability(self, opponent):
        print(f"{self.name} activates Divine Shield! Incoming attack will be blocked.")
        self.shielded = True


# ───── Enemy Class ─────
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        regen = random.randint(5, 15)
        self.health = min(self.max_health, self.health + regen)
        print(f"{self.name} regenerates {regen} health. Current health: {self.health}/{self.max_health}")


# ───── Game Logic ─────
def create_character():
    print("Choose your character class:")
    print("1. Warrior\n2. Mage\n3. Archer\n4. Paladin")
    choice = input("Enter choice (1–4): ").strip()
    name = input("Enter your character's name: ").strip()

    match choice:
        case '1': return Warrior(name)
        case '2': return Mage(name)
        case '3': return Archer(name)
        case '4': return Paladin(name)
        case _: 
            print("Invalid choice. Defaulting to Warrior.")
            return Warrior(name)


def battle(player, wizard):
    print("\n🧙‍♂️ Battle Start! Defeat the Evil Wizard! 🧙‍♂️")
    while player.health > 0 and wizard.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack\n2. Use Special Ability\n3. Heal\n4. View Stats")
        action = input("Choose an action: ").strip()

        if action == '1':
            player.attack(wizard)
        elif action == '2':
            player.special_ability(wizard)
        elif action == '3':
            player.heal()
        elif action == '4':
            player.display_stats()
            wizard.display_stats()
            continue
        else:
            print("Invalid action. Try again.")
            continue

        if wizard.health > 0:
            print("\n--- Wizard's Turn ---")
            wizard.regenerate()
            if isinstance(player, Paladin) and player.shielded:
                print(f"{player.name} blocks the wizard's attack with Divine Shield!")
                player.shielded = False
            else:
                wizard.attack(player)

        if player.health <= 0:
            print(f"\n💀 {player.name} has been defeated by the Evil Wizard. Game Over.")
        elif wizard.health <= 0:
            print(f"\n🎉 Victory! {player.name} has defeated the Evil Wizard!")


def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)


if __name__ == "__main__":
    main()
