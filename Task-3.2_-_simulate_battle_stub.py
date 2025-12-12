"""
Exercise 3.2: Simulate a Turn-Based Battle (Class-Based)

In this exercise, you will create a Pokemon class and use it to simulate battles.
This demonstrates object-oriented programming principles: encapsulation, methods, and clear responsibilities.
"""
#name = Oliver Rae-Moore
#ID = 20195645300
import httpx
import random


class Pokemon:
    """
    Represents a Pokemon with stats fetched from the PokeAPI.
    """

    def __init__(self, name:str):
        """
        Initialise a Pokemon by fetching its data from the API and calculating its stats.

        Args:
            name (str): The name of the Pokemon (e.g., "pikachu")
        """
        # TODO: Store the Pokemon's name (lowercase)

        # TODO: Fetch Pokemon data from PokeAPI
        # - Create the URL: f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
        # - Make GET request
        # - Check response status code (raise error if not 200)
        # - Store the JSON data

        # TODO: Calculate and store stats
        # - Use _calculate_stat() for attack, defense, speed
        # - Use _calculate_hp() for max HP
        # - Store stats in a dictionary
        # - Set current_hp = max_hp
        self.name = name.lower()
        self.base_stats = self.fetchstats(name)
        self.hpstat = self._calculate_hp(self.base_stats['hp'])
        self.attackstat = self._calculate_stat(self.base_stats['attack'])
        self.defensestat = self._calculate_stat(self.base_stats['defense'])
        self.speedstat = self._calculate_stat(self.base_stats['speed'])
        self.currenthp = self.hpstat
    def fetchstats(self, name:str):
        url = f"https://pokeapi.co/api/v2/pokemon/{name}"
        data = httpx.get(url)
        Json = data.json()
        base_stats = {stat['stat']['name']: stat['base_stat'] for stat in Json['stats']}

        return base_stats
    

    





    def _calculate_stat(self, base_stat, level=50, iv=15, ev=85):
        """
        Calculate a Pokemon's stat at a given level.
        Helper method (note the underscore prefix).

        Args:
            base_stat (int): The base stat value from the API
            level (int): Pokemon level (default 50)
            iv (int): Individual value (default 15)
            ev (int): Effort value (default 85)

        Returns:
            int: The calculated stat
        """
        # TODO: Implement the stat calculation formula
        # Formula: int(((2 * base_stat + iv + (ev / 4)) * level / 100) + 5)
        return int(((2 * base_stat + iv + (ev / 4)) * level / 100) + 5)
        

    def _calculate_hp(self, base_stat, level=50, iv=15, ev=85):
        """
        Calculate a Pokemon's HP at a given level.
        HP uses a different formula than other stats.

        Args:
            base_stat (int): The base HP value from the API
            level (int): Pokemon level (default 50)
            iv (int): Individual value (default 15)
            ev (int): Effort value (default 85)

        Returns:
            int: The calculated HP
        """
        # TODO: Implement the HP calculation formula
        # Formula: int(((2 * base_stat + iv + (ev / 4)) * level / 100) + level + 10)
        return int(((2 * base_stat + iv + (ev / 4)) * level / 100) + level + 10)
    


    def attack(self, defender):
        """
        Attack another Pokemon, dealing damage based on stats.

        Args:
            defender (Pokemon): The Pokemon being attacked

        Returns:
            int: The amount of damage dealt
        """
        # TODO: Calculate damage using the damage formula
        # Formula: int((((2 * 50 * 0.4 + 2) * self.stats['attack'] * 60) / (defender.stats['defense'] * 50)) + 2)
        # Where 50 is level and 60 is base_power

        # TODO: Make the defender take damage
        # Call defender.take_damage(damage)

        # TODO: Return the damage amount
        damage = int((((2 * 50 * 0.4 + 2) * self.attackstat * 60) / (defender.defensestat * 50)) + 2)
        defender.take_damage(damage)
        return damage

    def take_damage(self, amount):
        """
        Reduce this Pokemon's HP by the damage amount.

        Args:
            amount (int): The damage to take
        """
        # TODO: Reduce current_hp by amount
        # Make sure HP doesn't go below 0
        if amount > self.currenthp:
            self.currenthp = 0
        else:
            self.currenthp -= amount
        

    def is_fainted(self):
        """
        Check if this Pokemon has fainted (HP <= 0).

        Returns:
            bool: True if fainted, False otherwise
        """
        # TODO: Return True if current_hp <= 0, False otherwise
        if self.currenthp <= 0:
            return True
        else:
            return False


    def __str__(self):
        """
        String representation of the Pokemon for printing.

        Returns:
            str: A nice display of the Pokemon's name and HP
        """
        # TODO: Return a string like "Pikachu (HP: 95/120)"

        return f"{self.name.capitalize()} (HP:{self.currenthp}/{self.hpstat})"


def simulate_battle(pokemon1_name:str, pokemon2_name:str):
    """
    Simulate a turn-based battle between two Pokemon.

    Args:
        pokemon1_name (str): Name of the first Pokemon
        pokemon2_name (str): Name of the second Pokemon
    """
    # TODO: Create two Pokemon objects
    pokemon1 = Pokemon(pokemon1_name)
    pokemon2 = Pokemon(pokemon2_name)
    # TODO: Display battle start message
    # Show both Pokemon names and initial HP
    print("Battle Starts!")
    print(str(pokemon1))
    print(str(pokemon2))

    
    # TODO: Determine who attacks first based on speed
    if pokemon1.speedstat > pokemon2.speedstat:
        attacker = pokemon1
        defender = pokemon2
    elif pokemon1.speedstat < pokemon2.speedstat:
        attacker = pokemon2
        defender = pokemon1
    #adding this because there might be a speed tie
    else:
        number = random.randint(1,2)
        if number == 1:
            attacker = pokemon1
            defender = pokemon2
        else:
            attacker = pokemon2
            defender = pokemon1


    # The Pokemon with higher speed goes first

    # Hint: Compare pokemon1.stats['speed'] with pokemon2.stats['speed']

    # TODO: Battle loop
    # - Keep track of round number
    # - While neither Pokemon is fainted:
    #   - Display round number
    #   - Attacker attacks defender
    #   - Display damage and remaining HP
    #   - Check if defender fainted
    #   - If not, swap attacker and defender
    #   - Increment round number
    count = 0
    while not pokemon1.is_fainted() == True and not pokemon2.is_fainted() == True:
        count += 1
        print(f"Round {count}")
        print(f"{attacker} deals {attacker.attack(defender)} damage")
        print(f"{defender.name.capitalize()} has {defender.currenthp}HP")
        if defender.is_fainted() == True:
            break
        else:
            continue
        print(f"{defender} deals {defender.attack(attacker)} damage ")
        print(f"{attacker.name.capitalize()} has {attacker.currenthp}HP")
    if pokemon1.is_fainted() == True:
        print(f"{pokemon2.name.capitalize()} wins with {pokemon2.currenthp}HP")
    else:
        print(f"{pokemon1.name.capitalize()} wins with {pokemon1.currenthp}HP")
    # TODO: Display battle result
    # Show which Pokemon won and their remaining HP
    


if __name__ == "__main__":
    # Test your battle simulator
    simulate_battle("pikachu", "bulbasaur")

    # Uncomment to test other battles:
    simulate_battle("charmander", "squirtle")
    simulate_battle("eevee", "jigglypuff")
