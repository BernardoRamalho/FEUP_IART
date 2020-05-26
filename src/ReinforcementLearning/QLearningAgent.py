import numpy as np
import gym
import gym_pivit
import time

env = gym.make("pivit-v0")


env.reset()
# env.render()


# move = {'piece_id': 1,
#         'new_pos': (2, 2)
#         }

# action = env.move_to_action(move)
# env.step(action)

# time.sleep(4)
# env.render()

test_str = env.state_to_string()
q_table = {}
#print(q_table)

#time.sleep(4)

print(test_str)
print(hash(test_str))