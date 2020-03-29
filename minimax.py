import sys
import math
import copy
from piece import Piece
from gamestate import GameState
from collections import defaultdict


class Minimax:

    # Player 1 -> Max, Player 2 -> Min
    def __init__(self, gamestate):
        self.gamestate = gamestate

    def vuln_pos_left(self, check_x, check_y, player, oponent):
        pos_counter = 1
        check_x -= self.gamestate.square_side
        while check_x > self.gamestate.min_pos:
            if (check_x, check_y) in self.gamestate.players[
                player].pieces.keys(): return False  # It's being protected by another friendly piece

            if (check_x, check_y) in self.gamestate.players[oponent].pieces.keys():
                if pos_counter % 2 == 0 and self.gamestate.players[oponent].pieces[(check_x, check_y)].evolved and \
                        self.gamestate.players[oponent].pieces[(check_x, check_y)].direction == "h":
                    return True
                elif pos_counter % 2 != 0 and self.gamestate.players[oponent].pieces[
                    (check_x, check_y)].direction == "h":
                    return True
                else:
                    return False  # It's being protected by an enemy piece who cant't reach it and blocks others in that line

            check_x -= self.gamestate.square_side
            pos_counter += 1

        return False

    def vuln_pos_right(self, check_x, check_y, player, oponent):
        pos_counter = 1
        check_x += self.gamestate.square_side
        while check_x <= self.gamestate.max_pos:
            if (check_x, check_y) in self.gamestate.players[
                player].pieces.keys(): return False  # It's being protected by another friendly piece

            if (check_x, check_y) in self.gamestate.players[oponent].pieces.keys():
                if pos_counter % 2 == 0 and self.gamestate.players[oponent].pieces[(check_x, check_y)].evolved and \
                        self.gamestate.players[oponent].pieces[(check_x, check_y)].direction == "h":
                    return True
                elif pos_counter % 2 != 0 and self.gamestate.players[oponent].pieces[
                    (check_x, check_y)].direction == "h":
                    return True
                else:
                    return False  # It's being protected by an enemy piece who cant't reach it and blocks others in that line

            check_x += self.gamestate.square_side
            pos_counter += 1
        return False

    def vuln_pos_top(self, check_x, check_y, player, oponent):
        pos_counter = 1
        check_y -= self.gamestate.square_side
        while check_y >= self.gamestate.min_pos:
            if (check_x, check_y) in self.gamestate.players[
                player].pieces.keys(): return False  # It's being protected by another friendly piece

            if (check_x, check_y) in self.gamestate.players[oponent].pieces.keys():
                if pos_counter % 2 == 0 and self.gamestate.players[oponent].pieces[(check_x, check_y)].evolved and \
                        self.gamestate.players[oponent].pieces[(check_x, check_y)].direction == "v":
                    return True
                elif pos_counter % 2 != 0 and self.gamestate.players[oponent].pieces[
                    (check_x, check_y)].direction == "v":
                    return True
                else:
                    return False  # It's being protected by an enemy piece who cant't reach it and blocks others in that line

            check_y -= self.gamestate.square_side
            pos_counter += 1

        return False

    def vuln_pos_bot(self, check_x, check_y, player, oponent):
        pos_counter = 1
        check_y += self.gamestate.square_side
        while check_y < self.gamestate.max_pos:
            if (check_x, check_y) in self.gamestate.players[
                player].pieces.keys(): return False  # It's being protected by another friendly piece

            if (check_x, check_y) in self.gamestate.players[oponent].pieces.keys():
                if pos_counter % 2 == 0 and self.gamestate.players[oponent].pieces[(check_x, check_y)].evolved and \
                        self.gamestate.players[oponent].pieces[(check_x, check_y)].direction == "v":
                    return True
                elif pos_counter % 2 != 0 and self.gamestate.players[oponent].pieces[
                    (check_x, check_y)].direction == "v":
                    return True
                else:
                    return False  # It's being protected by an enemy piece who cant't reach it and blocks others in that line

            check_y += self.gamestate.square_side
            pos_counter += 1

        return False

    def vulnerable_position(self, check_x, check_y, player, opponent):
        return self.vuln_pos_left(check_x, check_y, player, opponent) or self.vuln_pos_right(check_x, check_y, player,
                                                                                             opponent) or self.vuln_pos_top(
            check_x, check_y, player, opponent) or self.vuln_pos_bot(check_x, check_y, player, opponent)

    def calc_dist_to_nearest_evol(self, check_x, check_y):
        point_0 = (self.gamestate.min_pos, self.gamestate.min_pos)
        point_1 = (self.gamestate.min_pos, self.gamestate.max_pos)
        point_2 = (self.gamestate.max_pos, self.gamestate.min_pos)
        point_3 = (self.gamestate.max_pos, self.gamestate.max_pos)

        d0 = math.floor(math.sqrt(pow(check_x - point_0[0], 2) + pow(check_y - point_0[1], 2)))
        d1 = math.floor(math.sqrt(pow(check_x - point_1[0], 2) + pow(check_y - point_1[1], 2)))
        d2 = math.floor(math.sqrt(pow(check_x - point_2[0], 2) + pow(check_y - point_2[1], 2)))
        d3 = math.floor(math.sqrt(pow(check_x - point_3[0], 2) + pow(check_y - point_3[1], 2)))

        return min([d0, d1, d2, d3])

    def value_my_pieces(self, player, opponent):
        value_counter = 0
        for piece in self.gamestate.players[player].pieces.values():
            if self.vulnerable_position(piece.get_position()[0], piece.get_position()[1], player, opponent):
                continue
            elif piece.evolved:
                value_counter += 1000
            else:
                value_counter += 100
                value_counter -= self.calc_dist_to_nearest_evol(piece.get_position()[0], piece.get_position()[1])

        return value_counter

    def value_opponents_pieces(self, player, opponent):
        value_counter = 0
        for piece in self.gamestate.players[opponent].pieces.values():
            if self.vulnerable_position(piece.get_position()[0], piece.get_position()[1], opponent, player):
                continue
            elif piece.evolved:
                value_counter -= 1000
            else:
                value_counter -= 100

        return value_counter

    def value_gamestate(self):

        opponent = self.gamestate.player_turn % 2

        if self.gamestate.check_end_game():
            if self.gamestate.get_who_wins() == self.gamestate.player_turn:
                return sys.maxsize
            else:
                return -sys.maxsize + 1

        else:
            return self.value_my_pieces(self.gamestate.player_turn - 1, opponent) + \
                   self.value_opponents_pieces(self.gamestate.player_turn - 1, opponent)

    def generate_possible_gamestates(self):
        possible_gamestates = []
        possible_positions = self.gamestate.generate_valid_moves()

        for i in self.gamestate.players[self.gamestate.player_turn - 1].pieces.keys():
            if i in possible_positions.keys():
                for j in possible_positions[i]:
                    new_game_state = copy.deepcopy(self.gamestate)

                    new_game_state.move_piece(new_game_state.players[new_game_state.player_turn - 1].pieces[i], j)

                    possible_gamestates.append(new_game_state)

        return possible_gamestates

