import math
import movement


def calc_dist_to_nearest_evol(gamestate, check_x, check_y):
    point_0 = (gamestate.min_pos, gamestate.min_pos)
    point_1 = (gamestate.min_pos, gamestate.max_pos)
    point_2 = (gamestate.max_pos, gamestate.min_pos)
    point_3 = (gamestate.max_pos, gamestate.max_pos)

    d0 = math.floor(math.sqrt(pow(check_x - point_0[0], 2) + pow(check_y - point_0[1], 2)))
    d1 = math.floor(math.sqrt(pow(check_x - point_1[0], 2) + pow(check_y - point_1[1], 2)))
    d2 = math.floor(math.sqrt(pow(check_x - point_2[0], 2) + pow(check_y - point_2[1], 2)))
    d3 = math.floor(math.sqrt(pow(check_x - point_3[0], 2) + pow(check_y - point_3[1], 2)))

    return min([d0, d1, d2, d3]) // 6


class Heuristics:

    def __init__(self, mode):
        if mode == '1':
            self.player_pieces_values = 10
            self.player_vulnerable_pieces_values = 5
            self.opponent_vulnerable_pieces_values = 10
            self.opponent_pieces_values = 20
            self.evolved_pieces_values = 500
        elif mode == '2':
            self.player_pieces_values = 20
            self.player_vulnerable_pieces_values = 10
            self.opponent_vulnerable_pieces_values = 5
            self.opponent_pieces_values = 10
            self.evolved_pieces_values = 500
        else:
            self.player_pieces_values = 10
            self.player_vulnerable_pieces_values = 5
            self.opponent_vulnerable_pieces_values = 5
            self.opponent_pieces_values = 10
            self.evolved_pieces_values = 500

    def vulnerable_position(self, gamestate, check_x, check_y, player, opponent):
        for piece in gamestate.players[opponent].pieces.values():
            if piece.get_position()[
                0] == check_x and piece.direction == "v":  # Share x value in common, now lets check if a path exists
                if movement.check_y_movement(piece, check_y, gamestate.square_side, gamestate.players[opponent],
                                             gamestate.players[player]):
                    return True

            elif piece.get_position()[1] == check_y and piece.direction == "h":
                if movement.check_x_movement(piece, check_x, gamestate.square_side, gamestate.players[opponent],
                                             gamestate.players[player]):
                    return True

        return False

    def value_my_pieces(self, gamestate, player, opponent):
        value_counter = 0
        for piece in gamestate.players[player].pieces.values():
            if self.vulnerable_position(gamestate, piece.get_position()[0], piece.get_position()[1], player,
                                           opponent):
                value_counter -= self.player_vulnerable_pieces_values
                value_counter -= calc_dist_to_nearest_evol(gamestate, piece.get_position()[0], piece.get_position()[1])

            elif piece.evolved:
                value_counter += self.evolved_pieces_values
            else:
                value_counter += self.player_pieces_values
                value_counter -= calc_dist_to_nearest_evol(gamestate, piece.get_position()[0], piece.get_position()[1])

        return value_counter

    def value_opponents_pieces(self, gamestate, player, opponent):
        value_counter = 0
        for piece in gamestate.players[opponent].pieces.values():
            if self.vulnerable_position(gamestate, piece.get_position()[0], piece.get_position()[1], opponent,
                                           player):
                value_counter += self.opponent_vulnerable_pieces_values
                value_counter += calc_dist_to_nearest_evol(gamestate, piece.get_position()[0], piece.get_position()[1])
            elif piece.evolved:
                value_counter -= self.evolved_pieces_values
            else:
                value_counter -= self.opponent_pieces_values
                value_counter += calc_dist_to_nearest_evol(gamestate, piece.get_position()[0], piece.get_position()[1])

        return value_counter
