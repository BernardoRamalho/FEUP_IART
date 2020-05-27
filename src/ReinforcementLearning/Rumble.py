import gym
import gym_pivit
import json
from pathlib import Path

import numpy as np


def keywithmaxval(d):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]

def read_qtable(file_path, q_table):
    test = Path(file_path)
    if test.is_file():
        try:
            with open(file_path, 'r') as file:
                q_table = json.load(file)
        except:
            q_table = {}


QLQT = {}
read_qtable('./QLQT.json', QLQT)

SARSAQT = {}
read_qtable('./SARSAQT.json', SARSAQT)

env = gym.make("pivit-v0")

def QLvsSARSA():
    done = False
    i = 0
    env.setup()
    while not done:
        #env.render()
        state = env.state_to_string()
        #QL
        if i % 2 == 0:
            if state in QLQT:
                action = int(keywithmaxval(QLQT[state]))
            else:
                valid_moves = env.generate_valid_moves()
                action = env.move_to_action(np.random.choice(valid_moves))
			
            _, done = env.step(action)
            #SARSA
        else:
            if state in SARSAQT:
                action = int(keywithmaxval(SARSAQT[state]))
            else:
                valid_moves = env.generate_valid_moves()
                action = env.move_to_action(np.random.choice(valid_moves))

            _, done = env.step(action)
			

        if done == True:
            print(env.whoWon())
            break
        i += 1