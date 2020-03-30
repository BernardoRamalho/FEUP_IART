import sys
import copy
import heuristics


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
        return heuristics.value_my_pieces(gamestate, player - 1, opponent) + heuristics.value_opponents_pieces(gamestate, player - 1, opponent)


class Minimax:

    move_to_be_made = []

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
