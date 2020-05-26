import numpy as np
import random
import gym
import gym_pivit
import time
import json

class QLAgent:

        def __init__(self, file_path, num_episodes, max_steps, learning_rate, discount_rate, exploration_rate, max_exploration_rate, min_exploration_rate, exploration_decay_rate):
                self.file_path = file_path
                self.q_table = {}
                #if file_path != "":
                        #self.read_qtable()

                self.num_episodes = num_episodes
                self.max_steps_per_episode = 100
                self.learning_rate = 0.1
                self.discount_rate = 0.99
                self.exploration_rate = exploration_rate
                self.max_exploration_rate = max_exploration_rate
                self.min_exploration_rate = min_exploration_rate
                self.exploration_decay_rate = exploration_decay_rate

                

        def write_qtable(self):
                with open(self.file_path, 'w') as file:
                        file.write(json.dumps(self.q_table))

        def read_qtable(self):
                with open(self.file_path, 'r') as file:
                        self.q_table = json.load(file)

        def train(self, env):
                self.rewards_all_episodes = []

                for episode in range(self.num_episodes):
                        env.reset()

                        done = False
                        rewards_current_episode = 0
                        state = hash(env.state_to_string())
                        
                        for step in range(self.max_steps_per_episode):
                                #env.render() 
                                exploration_rate_threshold = random.uniform(0, 1)

                                if exploration_rate_threshold > self.exploration_rate:
                                        if state in self.q_table:
                                                action = np.argmax(self.q_table[state])
                                        else:
                                                move = env.generate_valid_moves()[0]
                                                action = env.move_to_action(move) 
                                else:
                                        move = np.random.choice(env.generate_valid_moves())
                                        action = env.move_to_action(move)                       

                                reward, done = env.step(action)
                                new_state = hash(env.state_to_string())

                                if state not in self.q_table:
                                        self.q_table[state] = {}
                                        self.q_table[state][action] = 0
                                elif action not in self.q_table[state]:
                                        self.q_table[state][action] = 0

                                if new_state not in self.q_table:
                                        self.q_table[new_state] = {}
                                        self.q_table[new_state][action] = 0

                                # Update Q-table for Q(s, a)
                                self.q_table[state][action] = self.q_table[state][action] * (1 - self.learning_rate) + \
                self.learning_rate * (reward + self.discount_rate * np.max(list(self.q_table[new_state].values())))

                                state = new_state
                                rewards_current_episode += reward

                                if done == True:
                                        break

                        self.exploration_rate = self.min_exploration_rate + (self.max_exploration_rate - self.min_exploration_rate) * np.exp(-self.exploration_decay_rate*episode)
                        
                        self.rewards_all_episodes.append(rewards_current_episode)


env = gym.make("pivit-v0")
env.setup()
# env.render()

# move = {'piece_id': 1,
#         'new_pos': (2, 2)
#         }

# action = env.move_to_action(move)
# env.step(action)

# time.sleep(4)
# env.render()

#test_str = env.state_to_string()

ql_agent = QLAgent("qtable.json", 10, 100, 0.1, 0.99, 1, 1, 0.01, 0.01)

ql_agent.train(env)

print(ql_agent.rewards_all_episode
)

ql.write_qtable()

#print(test_str)
#print(ql_agent.q_table)
#print(q_table)
