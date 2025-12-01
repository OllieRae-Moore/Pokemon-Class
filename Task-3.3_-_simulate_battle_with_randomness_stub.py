"""
Exercise 3.3: Add Random Events to Battle (Stretch Goal - Stub)

This builds on your Task 3.2 Pokemon class.
Add randomness to make battles more unpredictable!
"""

import httpx
import random


class Pokemon:
    """
    Represents a Pokemon with stats fetched from the PokeAPI.
    Copy your implementation from Task 3.2 here.
    """

    def __init__(self, name):
        """Initialize a Pokemon by fetching its data from the API and calculating its stats."""
        # TODO: Copy your __init__ implementation from Task 3.2
        pass

    def _calculate_stat(self, base_stat, level=50, iv=15, ev=85):
        """Calculate a Pokemon's stat at a given level."""
        # TODO: Copy your _calculate_stat implementation from Task 3.2
        pass

    def _calculate_hp(self, base_stat, level=50, iv=15, ev=85):
        """Calculate a Pokemon's HP at a given level."""
        # TODO: Copy your _calculate_hp implementation from Task 3.2
        pass

    def attack(self, defender):
        """
        Attack another Pokemon with a chance of critical hit or miss.

        Args:
            defender (Pokemon): The Pokemon being attacked

        Returns:
            tuple: (damage_dealt, event_type) where event_type is "miss", "critical", or "normal"
        """
        # TODO: Generate a random number between 0 and 1
        # Hint: Use random.random()

        # TODO: Implement random events:
        # - If random < 0.05 (5% chance): MISS - deal 0 damage, return (0, "miss")
        # - Elif random < 0.15 (additional 10% chance): CRITICAL HIT - deal double damage
        #   * Calculate damage as normal but multiply by 2
        #   * Call defender.take_damage(damage)
        #   * Return (damage, "critical")
        # - Else: NORMAL HIT
        #   * Calculate and apply normal damage
        #   * Return (damage, "normal")

        pass

    def take_damage(self, amount):
        """Reduce this Pokemon's HP by the damage amount."""
        # TODO: Copy your take_damage implementation from Task 3.2
        pass

    def is_fainted(self):
        """Check if this Pokemon has fainted (HP <= 0)."""
        # TODO: Copy your is_fainted implementation from Task 3.2
        pass

    def __str__(self):
        """String representation of the Pokemon for printing."""
        # TODO: Copy your __str__ implementation from Task 3.2
        pass


def simulate_battle_with_randomness(pokemon1_name, pokemon2_name):
    """
    Simulate a turn-based battle between two Pokemon with random events.

    Args:
        pokemon1_name (str): Name of the first Pokemon
        pokemon2_name (str): Name of the second Pokemon
    """
    # TODO: Create two Pokemon objects

    # TODO: Display battle start message

    # TODO: Determine who attacks first based on speed

    # TODO: Battle loop - similar to Task 3.2 but:
    # - Call attacker.attack(defender) which now returns (damage, event_type)
    # - Display different messages based on event_type:
    #   * "miss": "{Attacker} missed the attack!"
    #   * "critical": "Critical hit! {Defender} takes {damage} damage!"
    #   * "normal": "{Defender} takes {damage} damage."

    # TODO: Display battle result
    pass


if __name__ == "__main__":
    # Test your battle simulator with randomness
    simulate_battle_with_randomness("pikachu", "bulbasaur")

    # Uncomment to test other battles:
    # simulate_battle_with_randomness("mewtwo", "ho-oh")
    # simulate_battle_with_randomness("charmander", "squirtle")


"""
Hints:
- Copy your Pokemon class from Task 3.2 as a starting point
- Use random.random() to generate a random float between 0.0 and 1.0
- Structure your probability checks like:
    if rand < 0.05:      # 5% miss
    elif rand < 0.15:    # 10% critical (0.05 to 0.15)
    else:                # 85% normal (0.15 to 1.0)
- Make attack() return a tuple: (damage, event_type)
- Update simulate_battle_with_randomness() to handle the event types
"""
