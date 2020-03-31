import sys
import copy
import heuristics
import time
from gamestate import GameState
from collections import defaultdict

def generate_possible_gamestates(gamestate, player):
    possible_gamestates = []
    possible_positions = gamestate.generate_valid_moves(player)

    for i in gamestate.players[player - 1].pieces.keys():
        if i in possible_positions.keys():

            for j in possible_positions[i]:
                new_game_state = copy.deepcopy(gamestate)

                new_game_state.move_piece(new_game_state.players[player - 1].pieces[i], j)
                new_game_state.change_turn()

                possible_gamestates.append([new_game_state, [i, j]])

    return possible_gamestates


def value_gamestate(gamestate, player):
    opponent = player % 2

    if gamestate.check_end_game():
        if gamestate.get_who_wins() == gamestate.player_turn:
            return sys.maxsize
        else:
            return -sys.maxsize + 1

    else:
        val = heuristics.value_my_pieces(gamestate, player - 1, opponent) + heuristics.value_opponents_pieces(
            gamestate, player - 1, opponent)
        return val

class Minimax:
    
    saved_moves1 = [] #defaultdict(tuple)
    saved_moves2 = []#defaultdict(tuple)
    max_depth = 0

    def min_alpha_beta(self, alpha, beta, depth, gamestate):

        if depth == 0 or gamestate.check_end_game():
            return value_gamestate(gamestate, gamestate.player_turn)

        min_value = sys.maxsize

        for i in generate_possible_gamestates(gamestate, gamestate.player_turn):
            value = self.max_alpha_beta(alpha, beta, depth - 1, i[0])[0]

            if value < min_value:
                min_value = min(min_value, value)

            beta = min(beta, value)

            if beta <= alpha:
                break

        return min_value

    def max_alpha_beta(self, alpha, beta, depth, gamestate):

        if depth == 0 or gamestate.check_end_game():
            return value_gamestate(gamestate, gamestate.player_turn)

        max_value = -sys.maxsize + 1

        best_move = []

        for i in generate_possible_gamestates(gamestate, gamestate.player_turn):
            value = self.min_alpha_beta(alpha, beta, depth - 1, i[0])

            if value > max_value:
                max_value = max(max_value, value)
                best_move = i[1]

            alpha = max(alpha, value)

            if beta <= alpha:
                break

        return max_value, best_move

    def play(self, gamestate, depth):

        max_value, best_move = self.max_alpha_beta(-sys.maxsize + 1, sys.maxsize, depth, gamestate)

        return best_move

    def new_min_alpha_beta(self, alpha, beta, depth, gamestate):

        if depth == 0 or gamestate.check_end_game():
            return value_gamestate(gamestate, gamestate.player_turn)

        min_value = sys.maxsize

        possible_positions = gamestate.generate_valid_moves(gamestate.player_turn)

        for i in gamestate.players[gamestate.player_turn - 1].pieces.keys():
            if i in possible_positions.keys():

                for j in possible_positions[i]:
                    new_game_state = copy.deepcopy(gamestate)

                    new_game_state.move_piece(new_game_state.players[gamestate.player_turn - 1].pieces[i], j)
                    new_game_state.change_turn()

                    value = self.new_max_alpha_beta(alpha, beta, depth - 1, new_game_state)

                    if type(value) == tuple:
                        if value[0] < min_value:
                            min_value = min(min_value, value[0])
                            beta = min(beta, value[0])
                    elif value < min_value:
                        min_value = min(min_value, value)
                        beta = min(beta, value)

                    if beta <= alpha:
                        return min_value

        return min_value

    def new_max_alpha_beta(self, alpha, beta, depth, gamestate):

        if depth == 0 or gamestate.check_end_game():
            return value_gamestate(gamestate, gamestate.player_turn)

        max_value = -sys.maxsize + 1

        best_move = []

        possible_positions = gamestate.generate_valid_moves(gamestate.player_turn)
        for i in gamestate.players[gamestate.player_turn - 1].pieces.keys():
            if i in possible_positions.keys():

                for j in possible_positions[i]:
                    new_game_state = copy.deepcopy(gamestate)

                    new_game_state.move_piece(new_game_state.players[gamestate.player_turn - 1].pieces[i], j)
                    new_game_state.change_turn()

                    value = self.new_min_alpha_beta(alpha, beta, depth - 1, new_game_state)

                    if value > max_value:
                        max_value = max(max_value, value)
                        best_move = [i, j]

                    alpha = max(alpha, value)
                    
                    if gamestate.player_turn == 1 : self.saved_moves1.append([new_game_state, best_move])
                    else : self.saved_moves2.append([new_game_state, best_move])
                    
                    if beta <= alpha:
                        return max_value, best_move
        
        
        if depth != self.max_depth:
            if gamestate.player_turn == 1 : self.saved_moves1.append([gamestate, best_move])
            else : self.saved_moves2.append([gamestate, best_move])
        return max_value, best_move

    def play_v2(self, gamestate, depth):
        
        if depth > self.max_depth: self.max_depth = depth
        if gamestate.player_turn == 1:
            for i in range(0, len(self.saved_moves1)):
                if gamestate == self.saved_moves1[i][0]:
                    return self.saved_moves1[i][1]
        else:
            for i in range(0, len(self.saved_moves2)):
                if gamestate == self.saved_moves2[i][0]:
                    return self.saved_moves2[i][1]

        if gamestate.player_turn == 1: self.saved_moves1.clear()  
        if gamestate.player_turn == 2: self.saved_moves2.clear()     
        max_value, best_move = self.new_max_alpha_beta(-sys.maxsize + 1, sys.maxsize, depth, gamestate)


        return best_move
