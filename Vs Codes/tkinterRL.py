import tkinter as tk
import random

# Define grid size and initial positions
grid_size = 6
agent_pos = [grid_size - 1, 0]  # Start position
goal_pos = [0, grid_size - 1]   # Goal position
num_obstacles = 5
obstacle_positions = []

# Generate random obstacles
for _ in range(num_obstacles):
    pos = [random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)]
    while pos == agent_pos or pos == goal_pos or pos in obstacle_positions:
        pos = [random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)]
    obstacle_positions.append(pos)

# Initialize score and steps
score = 0
steps = 0

# Tkinter setup
root = tk.Tk()
root.title("AI Navigator: Reinforcement Learning Game")

# Canvas for the game grid
cell_size = 80
canvas = tk.Canvas(root, width=grid_size * cell_size, height=grid_size * cell_size, bg="white")
canvas.pack()

# Draw the grid
cells = {}
for i in range(grid_size):
    for j in range(grid_size):
        x1, y1 = j * cell_size, i * cell_size
        x2, y2 = x1 + cell_size, y1 + cell_size
        cells[(i, j)] = canvas.create_rectangle(x1, y1, x2, y2, fill="lightgray", outline="black")

# Draw the goal
canvas.itemconfig(cells[tuple(goal_pos)], fill="green")

# Function to update the agent's position
def update_agent_position(old_pos, new_pos):
    global score, steps
    steps += 1

    # Check for obstacles
    if new_pos in obstacle_positions:
        canvas.itemconfig(cells[tuple(new_pos)], fill="red")
        status_label.config(text=f"💥 You hit an obstacle! Game Over! Score: {score}", fg="red")
        disable_buttons()
        reveal_obstacles()
        return

    # Check for goal
    elif new_pos == goal_pos:
        canvas.itemconfig(cells[tuple(new_pos)], fill="blue")
        status_label.config(text=f"🎉 You reached the goal in {steps} steps! Final Score: {score}", fg="green")
        disable_buttons()
        reveal_obstacles()
        return

    # Reward or penalty for valid moves
    if abs(new_pos[0] - goal_pos[0]) + abs(new_pos[1] - goal_pos[1]) < abs(old_pos[0] - goal_pos[0]) + abs(old_pos[1] - goal_pos[1]):
        score_label.config(text=f"Score: {score + 1}")
    else:
        score_label.config(text=f"Score: {score - 1}")

    # Update the agent's position
    canvas.itemconfig(cells[tuple(old_pos)], fill="lightgray")
    agent_pos[0], agent_pos[1] = new_pos
    canvas.itemconfig(cells[tuple(new_pos)], fill="blue")

# Function to reveal obstacles
def reveal_obstacles():
    for obs in obstacle_positions:
        canvas.itemconfig(cells[tuple(obs)], fill="red")

# Function to disable move buttons
def disable_buttons():
    up_button.config(state="disabled")
    down_button.config(state="disabled")
    left_button.config(state="disabled")
    right_button.config(state="disabled")

# Move functions
def move_up():
    if agent_pos[0] > 0:
        new_pos = [agent_pos[0] - 1, agent_pos[1]]
        update_agent_position(agent_pos, new_pos)

def move_down():
    if agent_pos[0] < grid_size - 1:
        new_pos = [agent_pos[0] + 1, agent_pos[1]]
        update_agent_position(agent_pos, new_pos)

def move_left():
    if agent_pos[1] > 0:
        new_pos = [agent_pos[0], agent_pos[1] - 1]
        update_agent_position(agent_pos, new_pos)

def move_right():
    if agent_pos[1] < grid_size - 1:
        new_pos = [agent_pos[0], agent_pos[1] + 1]
        update_agent_position(agent_pos, new_pos)

# UI for controls and status
controls_frame = tk.Frame(root)
controls_frame.pack()

up_button = tk.Button(controls_frame, text="↑", command=move_up, width=5, height=2)
up_button.grid(row=0, column=1)

left_button = tk.Button(controls_frame, text="←", command=move_left, width=5, height=2)
left_button.grid(row=1, column=0)

down_button = tk.Button(controls_frame, text="↓", command=move_down, width=5, height=2)
down_button.grid(row=1, column=1)

right_button = tk.Button(controls_frame, text="→", command=move_right, width=5, height=2)
right_button.grid(row=1, column=2)

# Status labels
status_frame = tk.Frame(root)
status_frame.pack()

score_label = tk.Label(status_frame, text=f"Score: {score}", font=("Arial", 14))
score_label.pack(side="left", padx=10)

status_label = tk.Label(status_frame, text="Guide the agent to the goal!", font=("Arial", 14), fg="blue")
status_label.pack(side="left", padx=10)

# Initial agent position
canvas.itemconfig(cells[tuple(agent_pos)], fill="blue")

# Start the game loop
root.mainloop()
