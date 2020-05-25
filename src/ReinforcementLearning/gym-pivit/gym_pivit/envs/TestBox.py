import numpy as np
import time
from pivit_env import PivitEnv


env = PivitEnv()
env.setup()

env.render()
time.sleep(4)

move = {'piece_id': 1,
        'new_pos': (2, 2)
        }

action = env.move_to_action(move)
env.step(action)
#env.player_move(action, 1)

env.render()
time.sleep(4)


