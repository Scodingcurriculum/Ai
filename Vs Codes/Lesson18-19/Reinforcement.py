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

# Function to display the grid
def display_grid(agent_pos, reveal_obstacles=False):
    grid_display = grid.copy()
    if reveal_obstacles:  # Reveal obstacles only after game ends
        for obs in obstacle_positions:
            grid_display[obs[0], obs[1]] = "X"
    grid_display[goal_pos[0], goal_pos[1]] = "G"  # Mark goal
    grid_display[agent_pos[0], agent_pos[1]] = "A"  # Mark agent
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

# Initialize score and step count
score = 0
steps = 0

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

    # Reinforcement logic
    if new_pos in obstacle_positions:
        score -= 10  # Penalty for hitting an obstacle
        print("💥 Oh no! You hit a hidden obstacle. Game Over!")
        print(f"Your final score is: {score}")
        print("\nFinal Grid with Obstacles Revealed:")
        display_grid(agent_pos, reveal_obstacles=True)  # Show obstacles after game ends
        break
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

