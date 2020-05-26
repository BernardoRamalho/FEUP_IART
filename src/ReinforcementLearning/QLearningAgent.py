import numpy as np
import random
import gym
import gym_pivit
import time
import json
import timeit

def keywithmaxval(d):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]

class QLAgent:

        def __init__(self, file_path, num_episodes, max_steps, learning_rate, discount_rate, exploration_rate, max_exploration_rate, min_exploration_rate, exploration_decay_rate):
                self.file_path = file_path
                self.q_table = {}

                if file_path != "":
                        self.read_qtable()

                self.num_episodes = num_episodes
                self.max_steps_per_episode = max_steps
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

        @staticmethod
        def move_to_action(move):
 
                new_pos = move['new_pos']
                pos = move['pos']
                return 64*(pos[0] * 8 + pos[1]) + (new_pos[0] * 8 + new_pos[1])

        @staticmethod
        def action_to_move(action):
                square = action % 64
                column = square % 8
                row = (square - column) // 8
                init_square = (action - square) // 64
                init_column = init_square % 8
                init_row = (init_square - init_column) // 8
                return {
                'pos': np.array([int(init_row), int(init_column)]),
                'new_pos': np.array([int(row), int(column)])
                }      

        def train(self, env):
                self.rewards_all_episodes = []

                for episode in range(self.num_episodes):
                        env.reset()

                        done = False
                        rewards_current_episode = 0
                        for step in range(self.max_steps_per_episode):
                                #env.render() 
                                state = env.state_to_string()
                                exploration_rate_threshold = random.uniform(0, 1)
                                if exploration_rate_threshold > self.exploration_rate:
                                        if state in self.q_table:
                                                action = int(keywithmaxval(self.q_table[state]))
                                        else:
                                                move = env.generate_valid_moves()[0]
                                                action = env.move_to_action(move) 
                                else:
                                        move = np.random.choice(env.generate_valid_moves())
                                        action = env.move_to_action(move)                       
                                
                                reward, done = env.step(action)
                                new_state = env.state_to_string()
                                action = str(action)

                                if state not in self.q_table:
                                        self.q_table[state] = {}
                                        self.q_table[state][action] = 0
                                elif action not in self.q_table[state]:
                                        self.q_table[state][action] = 0

                                new_state_mod = 0
                                if new_state in self.q_table:
                                        new_state_mod = np.max(list(self.q_table[new_state].values()))
                                
                                # Update Q-table for Q(s, a)
                                self.q_table[state][action] = self.q_table[state][action] * (1 - self.learning_rate) + \
                self.learning_rate * (reward + self.discount_rate * new_state_mod)

                                rewards_current_episode += reward

                                if done == True:
                                        break

                        self.exploration_rate = self.min_exploration_rate + (self.max_exploration_rate - self.min_exploration_rate) * np.exp(-self.exploration_decay_rate*episode)
                        
                        self.rewards_all_episodes.append(rewards_current_episode)
                        
                        print("Steps: ")
                        print(step)
                        if step < self.max_steps_per_episode - 1:
                                print(env.whoWon())

start = timeit.default_timer()
env = gym.make("pivit-v0")
env.setup()
#env.render()
#state = hash(env.state_to_string())

#move = {'pos': (0, 2),
#         'new_pos': (2, 2)
#         }

#action = env.move_to_action(move)
#print(type(action))
#env.step(action)

#time.sleep(4)
#env.render()

#test_str = env.state_to_string()

ql_agent = QLAgent("qtable.json", 10000, 250, 0.1, 0.9, 1, 1, 0.01, 0.01)

ql_agent.train(env)
stop = timeit.default_timer()
print(stop)

ql_agent.write_qtable()

#print(test_str)
#print(ql_agent.q_table)
#print(q_table)
