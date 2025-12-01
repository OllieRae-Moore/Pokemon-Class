

# Task 3: Pokémon Battle Simulator

## Overview
This task involves building a Pokémon Battle Simulator. You will fetch Pokémon stats using the PokéAPI and simulate battles with logic based on their attributes.

**This is as much an Object-Oriented Programming task as it is an API task!** You **should use classes** to complete this task. You'll apply the OOP concepts you learned in Session 2 (Task 2: Team class) to design a more complex system.

## Worksheet Objectives
- **API Integration**: Fetch and parse data from the PokéAPI.
- **Object-Oriented Programming**: Design and implement a `Pokemon` class to model Pokémon and their behaviours.
- **Encapsulation**: Store Pokémon data (stats, HP) as instance attributes and manipulate them through methods.
- **Methods**: Implement behaviours like `attack()`, `take_damage()`, and `is_fainted()` as class methods.
- **Stat Calculations**: Apply Pokémon stat formulas and damage calculations.
- **Game Logic**: Implement turn-based battle simulation with proper state management.
- **Stretch Goal**: Add randomness for unpredictability (critical hits, misses).

## Exercises

**Note on Progression:** Task 3.1 can use functions to warm up with API calls and stat calculations. **Task 3.2 should use a `Pokemon` class** - you'll refactor the stat calculation logic into class methods.

### Exercise 3.1: Compare Pokémon Stats (Warm-up)
- **Goal**: Fetch and calculate stats for two Pokémon, then compare their attributes.
- **Approach**: Functions are acceptable for this warm-up task
- **Key Features**:
  - Use base stats (attack, defense, speed) at level 50
  - Display which Pokémon has higher stats in each category
  - This prepares you for building the `Pokemon` class in Task 3.2

### Exercise 3.2: Simulate a Turn-Based Battle (MAIN TASK)
- **Goal**: Create a `Pokemon` class and use it to simulate turn-based battles.
- **Required Class Structure**:
  - `Pokemon` class with methods: `__init__()`, `attack()`, `take_damage()`, `is_fainted()`
  - Helper methods for stat calculations (use underscore prefix: `_calculate_stat()`)
  - `__str__()` method for nice Pokemon display
- **Key Features**:
  - Fetch Pokemon data from API in `__init__()`
  - Use speed stats to determine the first attacker
  - Alternate attacks until one Pokémon's HP reaches 0
  - Display battle details and declare the winner

### Exercise 3.3: Add Random Events (Stretch Goal)
- **Goal**: Introduce randomness like critical hits or misses.
- **Key Features**:
  - Add a chance for double damage (critical hit) or no damage (miss).
  - Display events dynamically during the battle.
