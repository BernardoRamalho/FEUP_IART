import sys
import copy
import heuristics


def generate_possible_gamestates(gamestate):
    possible_gamestates = []
    possible_positions = gamestate.generate_valid_moves()

    for i in gamestate.players[gamestate.player_turn - 1].pieces.keys():
        if i in possible_positions.keys():
            for j in possible_positions[i]:
                new_game_state = copy.deepcopy(gamestate)

                new_game_state.move_piece(new_game_state.players[new_game_state.player_turn - 1].pieces[i], j)

                possible_gamestates.append(new_game_state)

    return possible_gamestates


class Minimax:

    def value_gamestate(self, gamestate):

        opponent = gamestate.player_turn % 2

        if gamestate.check_end_game():
            if gamestate.get_who_wins() == gamestate.player_turn:
                return sys.maxsize
            else:
                return -sys.maxsize + 1

        else:
            return heuristics.value_my_pieces(gamestate, gamestate.player_turn - 1, opponent) + \
                   heuristics.value_opponents_pieces(gamestate, gamestate.player_turn - 1, opponent)

