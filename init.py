import gymnasium as gym

# Create the Lunar Lander environment
env = gym.make('LunarLander-v2', render_mode="human")

# Initialize the environment
state = env.reset()

for n in range(1000):  # Run for 1000 timesteps or until the episode ends
    env.render()  # Render the environment to visualize it

    action = env.action_space.sample()  # Take a random action
    state, reward, done, info, *_ = env.step(action)  # Apply the action

    if done:
        print("Episode finished after {} timesteps".format(n + 1))
        break

env.close()  # Close the environment when done
