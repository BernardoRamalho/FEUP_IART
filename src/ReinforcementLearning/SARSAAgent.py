import numpy as np
import random
import gym
import gym_pivit
import time
import json
import timeit

from pathlib import Path

def keywithmaxval(d):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]

class SARSAAgent:

    def __init__(self, file_path, num_episodes, max_steps, epsilon, alpha, gamma):
            self.file_path = file_path
            self.q_table = {}

            self.read_qtable()

            self.num_episodes = num_episodes
            self.max_steps_per_episode = max_steps
            self.epsilon = epsilon
            self.alpha = alpha
            self.gamma = gamma
            

            

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

    
    #Function to choose the next action 
    def choose_action(self, state, env): 
        action=0
        if random.uniform(0, 1) >= self.epsilon:
                if state in self.q_table:
                        action = int(keywithmaxval(self.q_table[state]))
                else:   
                        valid_moves = env.generate_valid_moves()
                        move = np.random.choice(valid_moves)
                        action = env.move_to_action(move) 
        else:
                valid_moves = env.generate_valid_moves()
                move = np.random.choice(valid_moves)
                action = env.move_to_action(move)

        return action 

    #Function to learn the Q-value 
    def update(self, state, state2, reward, action, action2): 
        predict = self.q_table[state][action]

        new_state_mod = 0
        if state2 in self.q_table:
            if action2 in self.q_table[state2]:
                new_state_mod = self.q_table[state2][action2]

        target = reward + self.gamma * new_state_mod 
        self.q_table[state][action] = self.q_table[state][action] + self.alpha * (target - predict) 
    
    def train(self, env):
        vict = 0
        defe = 0
        f = open("SARSAresults.txt", "w")
        self.rewards_all_episodes = []
        f.write("Num episodes: " + str(self.num_episodes) + '\n')
        f.write("Max_steps: " + str(self.max_steps_per_episode) + '\n')
        start_time = timeit.default_timer()
        # Starting the SARSA learning 
        for episode in range(self.num_episodes): 
                env.reset()
                state1 = env.state_to_string()
                action1 = self.choose_action(state1, env) 
                #Initializing the reward   
                rewards_current_episode = 0
                print(episode)
                for step in range(self.max_steps_per_episode): 
                        #Visualizing the training 
                        #env.render() 
                        
                        #Getting the next state 
                        reward, done = env.step(action1, True) 

                        rewards_current_episode += reward

                        #If at the end of learning process 
                        if done:
                                if state1 not in self.q_table:
                                        self.q_table[state1] = {}
                                        self.q_table[state1][action1] = reward
                                elif action1 not in self.q_table[state1]:
                                        self.q_table[state1][action1] = reward
                                break

                        state2 = env.state_to_string()
                        #Choosing the next action 
                        action2 = self.choose_action(state2, env) 
                        if action2 == -1:
                                done = True
                                if state1 not in self.q_table:
                                        self.q_table[state1] = {}
                                        self.q_table[state1][action1] = -1
                                elif action1 not in self.q_table[state1]:
                                        self.q_table[state1][action1] = -1
                                break

                        if state1 not in self.q_table:
                                self.q_table[state1] = {}
                                self.q_table[state1][action1] = 0
                        elif action1 not in self.q_table[state1]:
                                self.q_table[state1][action1] = 0
                        
                        #Learning the Q-value 
                        self.update(state1, state2, reward, action1, action2) 
                
                        state1 = state2 
                        action1 = action2 

            
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

if __name__ == "__main__":
        env = gym.make("pivit-v0")
        env.setup()
        sarsa_agent = SARSAAgent("sarsaQtable.json", 10000, 220, 0.8, 0.85, 0.95)

        sarsa_agent.train(env)

        sarsa_agent.write_qtable()