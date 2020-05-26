import numpy as np
import time

def move_to_action(move):

        new_pos = move['new_pos']
        pos = move['pos']
        return 64*(pos[0] * 8 + pos[1]) + (new_pos[0] * 8 + new_pos[1])


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


redMap = ['none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none'] 
blueMap = ['none', 'v', 'v', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'v', 'v']  

def isDone():
        redCount = np.count_nonzero(np.array(redMap) == 'none')
        if redCount == len(redMap): return True
        blueCount = np.count_nonzero(np.array(blueMap) == 'none')
        if blueCount == len(blueMap): return True
        for redStatus, blueStatus in zip(redMap, blueMap):
            if (redStatus != 'none' and redStatus.islower()) or (blueStatus != 'none' and blueStatus.islower()) :
                return False
        return True

print(isDone())

move = {'pos': (0, 2),
        'new_pos': (2, 2)
        }

# action = move_to_action(move)
# print(action)
# print(action_to_move(action))
# #env.player_move(action, 1)


