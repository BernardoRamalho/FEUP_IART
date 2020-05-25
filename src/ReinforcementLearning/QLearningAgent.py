import numpy as np
import gym
import gym_pivit
import time

env = gym.make("pivit-v0")


env.reset()
env.render()


move = {'piece_id': 1,
        'new_pos': (2, 2)
        }

action = env.move_to_action(move)
env.step(action)

time.sleep(4)
env.render()

#num_box = tuple((env.observation_space.high + np.ones(env.observation_space.shape)).astype(int))
#q_table = np.zeros(num_box + (env.action_space.n,))

#print(q_table)

time.sleep(4)