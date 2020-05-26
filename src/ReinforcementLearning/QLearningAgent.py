import numpy as np
import gym
import gym_pivit
import time
import json

class QLAgent:

	def __init__(self, file_path):
		self.file_path = file_path
		self.q_table = {}
		if file_path != "":
			self.read_qtable()

	def write_qtable(self):
		with open(self.file_path, 'w') as file:
			file.write(json.dumps(self.q_table))

	def read_qtable(self):
		with open(self.file_path, 'r') as file:
			self.q_table = json.load(file)

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
# = {'A':65, 'B':66, 'C':67}
ql_agent = QLAgent("qtable.json")

print(ql_agent.q_table)
#print(q_table)
