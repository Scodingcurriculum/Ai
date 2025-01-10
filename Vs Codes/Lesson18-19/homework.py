import numpy as np
import random

# Define the grid environment
grid_size = 6
grid = np.zeros((grid_size, grid_size), dtype=str)
grid[:, :] = "-"  # Default grid display

# Starting, goal, and obstacle positions
agent_pos = [grid_size - 1, 0]  # Bottom-left corner
goal_pos = [0, grid_size - 1]   # Top-right corner
num_obstacles = 5
obstacle_positions = []

# Place random obstacles
for _ in range(num_obstacles):
    pos = [random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)]
    while pos == agent_pos or pos == goal_pos or pos in obstacle_positions:
        pos = [random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)]
    obstacle_positions.append(pos)

# New obstacles (Water type)
num_water_obstacles = 2
water_positions = []

for _ in range(num_water_obstacles):
    pos = [random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)]
    while pos == agent_pos or pos == goal_pos or pos in obstacle_positions or pos in water_positions:
        pos = [random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)]
    water_positions.append(pos)

# Power-ups: Shield and Extra Points
shield_position = [random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)]
extra_points_position = [random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)]

# Function to display the grid
def display_grid(agent_pos, reveal_obstacles=False):
    grid_display = grid.copy()
    if reveal_obstacles:  # Reveal obstacles only after game ends
        for obs in obstacle_positions:
            grid_display[obs[0], obs[1]] = "X"
        for water in water_positions:
            grid_display[water[0], water[1]] = "W"
    grid_display[goal_pos[0], goal_pos[1]] = "G"  # Mark goal
    grid_display[agent_pos[0], agent_pos[1]] = "A"  # Mark agent
    if agent_pos == shield_position:
        grid_display[shield_position[0], shield_position[1]] = "S"  # Mark Shield
    if agent_pos == extra_points_position:
        grid_display[extra_points_position[0], extra_points_position[1]] = "P"  # Mark Extra Points
    print("\n".join([" ".join(row) for row in grid_display]))

# Function to move the agent
def move_agent(position, move):
    new_position = position[:]
    if move == "UP" and position[0] > 0:
        new_position[0] -= 1
    elif move == "DOWN" and position[0] < grid_size - 1:
        new_position[0] += 1
    elif move == "LEFT" and position[1] > 0:
        new_position[1] -= 1
    elif move == "RIGHT" and position[1] < grid_size - 1:
        new_position[1] += 1
    else:
        print("🚫 Invalid move!")
    return new_position

# Initialize score, step count, and power-ups
score = 0
steps = 0
shield_active = False
speed_boost_active = False
shield_turns_left = 0
speed_boost_turns_left = 0

# Game Introduction
print("\nWelcome to AI Navigator: Reinforcement Edition! 🚧")
print("Guide the AI (A) to the Goal (G) while avoiding hidden Obstacles.")
print("Commands: UP, DOWN, LEFT, RIGHT\n")

# Game loop
while agent_pos != goal_pos:
    display_grid(agent_pos)  # Show grid without revealing obstacles
    move = input("\nYour Move (UP, DOWN, LEFT, RIGHT): ").strip().upper()
    new_pos = move_agent(agent_pos, move)
    steps += 1

    # Check if agent hits Water obstacle
    if new_pos in water_positions:
        score -= 20  # Penalty for hitting a Water obstacle
        print("💥 Oh no! You hit a Water obstacle. Game Over!")
        print(f"Your final score is: {score}")
        print("\nFinal Grid with Obstacles Revealed:")
        display_grid(agent_pos, reveal_obstacles=True)  # Show obstacles after game ends
        break

    # Check if agent hits a regular obstacle
    elif new_pos in obstacle_positions:
        if shield_active:
            shield_active = False  # Shield is used up after protecting the agent
            print("🛡️ Shield activated! You were protected from the obstacle!")
        else:
            score -= 10  # Penalty for hitting a regular obstacle
            print("💥 Oh no! You hit a hidden obstacle. Game Over!")
            print(f"Your final score is: {score}")
            print("\nFinal Grid with Obstacles Revealed:")
            display_grid(agent_pos, reveal_obstacles=True)  # Show obstacles after game ends
            break

    # Check if agent collects the Shield power-up
    elif new_pos == shield_position:
        shield_active = True
        print("🛡️ You collected a Shield! You are now protected from obstacles for 1 move.")
        shield_position = [-1, -1]  # Remove Shield power-up from the grid

    # Check if agent collects Extra Points power-up
    elif new_pos == extra_points_position:
        score += 5
        print("✨ You collected Extra Points! +5 points.")
        extra_points_position = [-1, -1]  # Remove Extra Points power-up from the grid

    # Check if agent reaches the goal
    elif new_pos == goal_pos:
        score += 20  # Reward for reaching the goal
        agent_pos = new_pos
        print(f"\n🎉 Congratulations! You reached the goal in {steps} steps.")
        print(f"Your final score is: {score}")
        print("\nFinal Grid with Obstacles Revealed:")
        display_grid(agent_pos, reveal_obstacles=True)  # Show obstacles after success
        break

    else:
        # Small reward for making a valid move
        if abs(new_pos[0] - goal_pos[0]) + abs(new_pos[1] - goal_pos[1]) < abs(agent_pos[0] - goal_pos[0]) + abs(agent_pos[1] - goal_pos[1]):
            score += 1  # Reward for moving closer to the goal
        else:
            score -= 1  # Penalty for moving away from the goal
        agent_pos = new_pos
        print(f"Current score: {score}")
