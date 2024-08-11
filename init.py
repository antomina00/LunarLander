import gymnasium as gym
import random
import numpy as np
import pygame
import matplotlib.pyplot as plt

env = gym.make(
    "LunarLander-v2",
    continuous = False,
    gravity = -10.0,
    enable_wind= False,
    wind_power= 15.0,
    turbulence_power= 1.5,
    render_mode = 'human')

# Initialize the environment
state = env.reset()

# Initialize the time step
time = 0

# Indicate presence of wind
# wind = True

# Define the actions: 2 for up, 3 for right, and 1 for left
actions = [2, 3, 1]
action_index = 0

# Define engine power (this is an assumed value for demonstration purposes)
engine_power = 1

# # Define possible wind directions
# wind_directions = ['up', 'down', 'left', 'right']

# # Initialize wind direction and strength
# wind_direction = random.choice(wind_directions) if wind else "none"
# wind_strength = random.uniform(0, 5) if wind else 0

# print(f"Wind direction: {wind_direction}, Wind strength: {wind_strength}")

# # Introduce random forces (solar winds) based on wind direction and strength
# if wind_direction == 'up':
#     wind_force = np.array([0, wind_strength])
# elif wind_direction == 'down':
#     wind_force = np.array([0, -wind_strength])
# elif wind_direction == 'left':
#     wind_force = np.array([-wind_strength, 0])
# elif wind_direction == 'right':
#     wind_force = np.array([wind_strength, 0])

# Initialize Pygame
pygame.init()
font = pygame.font.SysFont(None, 24)

# Function to display text on the Pygame window
def display_text(screen, text, x, y):
    img = font.render(text, True, (255, 255, 255))
    screen.blit(img, (x, y))

# Get the Pygame display surface
screen = pygame.display.set_mode((600, 400))

force_x = []
force_y = []
timestep = []

for n in range(1000):  # Run for 1000 timesteps or until the episode ends
    time += 1
    timestep.append(n)
    env.render()  # Render the environment to visualize it

    if random.random() < 0.9:
        action = actions[action_index]  # Take the action in the specified order
        print("Taking action", action)
    else:
        action = env.action_space.sample()  # Take a random action
        print("Taking random action", action)
    action_index = (action_index + 1) % len(actions)  # Update the action index

    # Apply the action
    state, reward, done, info, *_ = env.step(action)
    print("State before", state)

    # if wind:
    #     print("Wind force", wind_force)
    #     state[2] += wind_force[0]  # Apply random force to the x position
    #     state[3] += wind_force[1]  # Apply random force to the y position
    #     print("State after", state)

    # # Display wind information on the Pygame window
    # display_text(screen, f"Wind direction: {wind_direction}", 10, 10)
    # display_text(screen, f"Wind strength: {wind_strength:.2f}", 10, 40)
    # pygame.display.flip()  # Update the display

    force_x.append(state[2])
    force_y.append(state[3])

    if done:
        print("Episode finished after {} timesteps".format(n + 1))
        break

env.close()  # Close the environment when done
pygame.quit()  # Quit Pygame

# Plot the x and y force of the lander  
plt.plot(timestep, force_x, label='Force X')
plt.plot(timestep, force_y, label='Force Y')
plt.xlabel('Timestep')
plt.ylabel('Force')
plt.legend()
plt.show()

