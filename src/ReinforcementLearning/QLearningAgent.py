import numpy as np
import random
import gym
import gym_pivit
import time
import json
import timeit
import time

from pathlib import Path

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
                self.learning_rate = learning_rate
                self.discount_rate = discount_rate
                self.exploration_rate = exploration_rate
                self.max_exploration_rate = max_exploration_rate
                self.min_exploration_rate = min_exploration_rate
                self.exploration_decay_rate = exploration_decay_rate

                

        def write_qtable(self):
                with open(self.file_path, 'w') as file:
                        file.write(json.dumps(self.q_table))

        def read_qtable(self):
            test = Path(self.file_path)
            if test.is_file():
                        try:
                                with open(self.file_path, 'r') as file:
                                        self.q_table = json.load(file)
                        except:
                                print("QTable file was empty")
                                self.q_table = {}


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
                f = open("QLresults.txt", "w")
                f.write("Num episodes: " + str(self.num_episodes) + '\n')
                f.write("Max_steps: " + str(self.max_steps_per_episode) + '\n')
                self.rewards_all_episodes = []
                rewards_current_episode = 'a'
                start_time = timeit.default_timer()
                end_time = -1
                for episode in range(self.num_episodes):
                        env.reset()
                        done = False
                        rewards_current_episode = 0
                        print(episode)
                        for step in range(self.max_steps_per_episode):
                                #env.render() 
                                state = env.state_to_string()
                                exploration_rate_threshold = random.uniform(0, 1)
                                if exploration_rate_threshold > self.exploration_rate:
                                        if state in self.q_table:
                                                action = int(keywithmaxval(self.q_table[state]))
                                        else:
                                                valid_moves = env.generate_valid_moves()
                                                if not valid_moves:
                                                        done = True
                                                        break
                                                move = np.random.choice(valid_moves)
                                                action = env.move_to_action(move) 
                                else:   
                                        valid_moves = env.generate_valid_moves()
                                        if not valid_moves:
                                                done = True
                                                break
                                        move = np.random.choice(valid_moves)
                                        action = env.move_to_action(move)                       
                                
                                reward, done = env.step(action, True)
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
                                        end_time = time.time()
                                        break

                        self.exploration_rate = self.min_exploration_rate + (self.max_exploration_rate - self.min_exploration_rate) * np.exp(-self.exploration_decay_rate*episode)
                        
                        self.rewards_all_episodes.append(rewards_current_episode)
                        
                        if step < self.max_steps_per_episode - 1:
                                print("Winner:")
                                print(env.whoWon())
                rewards_per_thousand_episodes = np.split(np.array(self.rewards_all_episodes), self.num_episodes / 100)

                end_time = timeit.default_timer()
                if end_time != -1:
                        f.write("Training Time:" + str(end_time - start_time) + '\n')
                f.write("Average reward per thousand episodes\n")

                count = 100
                for r in rewards_per_thousand_episodes:
                        f.write(str(count) + ': ' + str(sum(r/100)) + '\n')
                        count += 100
                f.close()



        def test(self, env):
                done = False
                while not done:
                        time.sleep(0.5)
                        env.render()
                        state = env.state_to_string()
                        print("turn:")
                        print(env.player_turn)
                        print(env.board)
                        if state in self.q_table:
                                print(self.q_table[state])
                                action = int(keywithmaxval(self.q_table[state]))
                        else:
                                valid_moves = env.generate_valid_moves()
                                if not valid_moves:
                                        done = True
                                        break
                                action = env.move_to_action(np.random.choice(valid_moves))
                        print("Picked:")
                        print(action)
                        reward, done = env.step(action, True)

                        if done == True:
                                end_time = time.time()
                                print("Winner:")
                                print(env.whoWon())
                                break
                

                
                        


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

ql_agent = QLAgent("qtableV2.json", 1000, 250, 0.4, 0.6, 1, 1, 0.01, 0.01)


ql_agent.train(env)
stop = timeit.default_timer()
#print(stop)

ql_agent.write_qtable()

#print(test_str)
#print(ql_agent.q_table)
#print(q_table)
