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
                vict = 0
                defe = 0
                f = open("QLResults.txt", "w")
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
                                state = env.state_to_string()
                                exploration_rate_threshold = random.uniform(0, 1)

                                #Pick Action
                                if exploration_rate_threshold > self.exploration_rate:
                                        if state in self.q_table:
                                                action = int(keywithmaxval(self.q_table[state]))
                                        else:
                                                action = env.move_to_action(np.random.choice(env.generate_valid_moves()))
                                else:
                                        action = env.move_to_action(np.random.choice(env.generate_valid_moves()))

                                reward, done = env.step(action, True)
                                #print("isDone6")
                                #print(done)
                                
                                action_string = str(action)
                                if not state in self.q_table:
                                        self.q_table[state] = {}
                                if not action_string in self.q_table[state]:
                                        self.q_table[state][action_string] = 0
                                
                                next_state_mod = 0
                                next_state = env.state_to_string()
                        
                                if next_state in self.q_table:
                                        next_state_mod = self.q_table[next_state][keywithmaxval(self.q_table[next_state])]
                                
                                #Update Q. Values
                                self.q_table[state][action_string] = self.q_table[state][action_string] * (1 - self.learning_rate) + self.learning_rate * (reward + self.discount_rate * next_state_mod)

                                rewards_current_episode += reward
                                if done == True:
                                        break
                        
                        #Exploration Rate Display
                        self.exploration_rate = self.min_exploration_rate + (self.max_exploration_rate - self.min_exploration_rate) * np.exp(-self.exploration_decay_rate*episode)
                        self.rewards_all_episodes.append(rewards_current_episode)

                        if step < self.max_steps_per_episode - 1:
                                winner = env.whoWon()
                                if winner == 1:
                                        vict += 1
                                elif winner == -1:
                                        defe += 1
                                
                rewards_per_thousand_episodes = np.split(np.array(self.rewards_all_episodes), self.num_episodes / 1000)
                end_time = timeit.default_timer()
                if end_time != -1:
                        f.write("Training Time:" + str(end_time - start_time) + '\n')
                f.write("Average reward per thousand episodes\n")

                count = 1000
                for r in rewards_per_thousand_episodes:
                        f.write(str(count) + ': ' + str(sum(r/1000)) + '\n')
                        count += 1000
                f.write("Victories:" + str(vict))
                f.write("\nDefeats:" + str(defe) + "\n")
                f.close()



        def test(self, env):
                done = False
                while not done:
                        time.sleep(1)
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

ql_agent = QLAgent("QLQT.json", 10000, 220, 0.2, 0.8, 1, 1, 0.01, 0.01)


ql_agent.train(env)
stop = timeit.default_timer()
#print(stop)

ql_agent.write_qtable()

#print(test_str)
#print(ql_agent.q_table)
#print(q_table)
