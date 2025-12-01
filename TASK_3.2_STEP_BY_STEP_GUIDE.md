# Task 3.2: Pokemon Battle Simulator - Step-by-Step Guide

This guide will help you implement a turn-based Pokemon battle simulator using object-oriented programming (OOP).

## Overview

You should create a `Pokemon` class that encapsulates all the behaviour and data for a Pokemon, then use instances of this class to simulate battles. This approach makes your code more organised, reusable, and easier to test.

---

## Step 1: Create the Pokemon Class

Define a `Pokemon` class that will represent each Pokemon in the battle.

### What to do:
- Create a class called `Pokemon`
- Add an `__init__` method that takes a Pokemon name as a parameter
- In the constructor, fetch the Pokemon's data from the PokeAPI
- Store the Pokemon's name and stats as instance attributes

### Key points:
- Convert the name to lowercase for the API request
- Use `httpx.get()` to fetch data from `https://pokeapi.co/api/v2/pokemon/{name}`
- Check the response status code (should be 200)
- Parse the JSON response to extract base stats
- Calculate actual stats using the stat calculation formulas
- Store both `max_hp` and `current_hp` (they start equal)

---

## Step 2: Add Stat Calculation Methods

Create helper methods to calculate Pokemon stats at level 50.

### What to do:
- Add a `_calculate_stat()` method for attack, defence, and speed
- Add a `_calculate_hp()` method for HP (uses a different formula)

### Formulas:
```python
# For attack, defence, speed:
stat = int(((2 * base_stat + iv + (ev / 4)) * level / 100) + 5)

# For HP:
hp = int(((2 * base_stat + iv + (ev / 4)) * level / 100) + level + 10)
```

### Parameters (use these defaults):
- `level = 50`
- `iv = 15` (individual value)
- `ev = 85` (effort value)

**Note:** The underscore prefix (e.g. `_calculate_stat`) indicates these are "private" helper methods - they're for internal use by the class.

---

## Step 3: Implement Battle Methods

Add methods that handle battle actions.

### What to do:
- **`attack(defender)`** - Calculate damage and apply it to the defender
- **`take_damage(amount)`** - Reduce current HP by the damage amount
- **`is_fainted()`** - Return `True` if `current_hp <= 0`, otherwise `False`
- **`__str__()`** - Return a nice string representation (e.g., "Pikachu (HP: 85/120)")

### Damage calculation formula:
```python
level = 50
base_power = 60  # Standard attack power
damage = int((((2 * level * 0.4 + 2) * attacker.stats['attack'] * base_power)
             / (defender.stats['defence'] * 50)) + 2)
```

### Important:
- In `take_damage()`, ensure HP doesn't go below 0
- The `attack()` method should call `defender.take_damage(damage)`

---

## Step 4: Create the simulate_battle() Function

Write a function that orchestrates the battle between two Pokemon.

### What to do:

1. **Instantiate Pokemon objects**
   - Create two `Pokemon` instances with the given names
   - Print a loading message while fetching data

2. **Display battle start**
   - Print a clear battle header
   - Show both Pokemon's names and initial HP

3. **Determine first attacker**
   - Compare `pokemon1.stats['speed']` and `pokemon2.stats['speed']`
   - Faster Pokemon attacks first
   - If speeds are equal, Pokemon 1 goes first
   - Print who attacks first and their speed stats

4. **Battle loop**
   - Start a round counter at 1
   - While both Pokemon are still alive (`not is_fainted()`):
     - Print the round number
     - Current attacker attacks the defender
     - Print damage dealt and defender's remaining HP
     - Check if defender fainted (break if true)
     - Swap attacker and defender
     - Increment round counter

5. **Display winner**
   - Print which Pokemon won
   - Show the winner's remaining HP
   - Print a clear battle end message

---

## Step 5: Test Your Implementation

### What to check:
- ✅ Pokemon data fetches correctly
- ✅ Stats calculate properly
- ✅ Faster Pokemon attacks first
- ✅ Damage is calculated and applied
- ✅ Battle ends when one Pokemon faints
- ✅ Winner is displayed correctly

---

## Common Issues and Solutions

**Problem:** "Pokemon not found" error
- **Solution:** Make sure the name is spelled correctly and in lowercase

**Problem:** Negative HP values
- **Solution:** In `take_damage()`, ensure you set `current_hp` to 0 if it goes below 0

**Problem:** Battle never ends (infinite loop)
- **Solution:** Check that damage is being applied properly and HP is actually decreasing

**Problem:** Wrong Pokemon wins
- **Solution:** Verify your damage formula is correct and that you're swapping attacker/defender properly

---

## Why Use a Class?

Using a `Pokemon` class provides several benefits:

1. **Encapsulation** - Each Pokemon manages its own data (stats, HP, name)
2. **Reusability** - Easy to create multiple Pokemon without repeating code
3. **Clarity** - Methods like `attack()` and `is_fainted()` make the code self-documenting
4. **Maintainability** - Changes to Pokemon behaviour only need to be made in one place
5. **Extensibility** - Easy to add new features (types, abilities, moves) later

---

## Extra Optional Extensions

Once your basic battle works, you could try adding:

- **Type advantages** - Fetch Pokemon types and apply effectiveness multipliers
- **Critical hits** - Random chance (1/16) for 1.5x damage
- **Miss chance** - 10% chance attacks miss entirely
- **Multiple moves** - Let each Pokemon have different attacks
- **Status effects** - Implement poison, paralysis, burn, etc.
