import gym
from gym import error, spaces, utils
action_space = spaces.Discrete(64*12)

print(action_space.sample())