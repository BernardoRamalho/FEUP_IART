import math


def vuln_pos_left(gamestate, check_x, check_y, player, oponent):
    pos_counter = 1
    check_x -= gamestate.square_side
    while check_x > gamestate.min_pos:
        if (check_x, check_y) in gamestate.players[
            player].pieces.keys(): return False  # It's being protected by another friendly piece

        if (check_x, check_y) in gamestate.players[oponent].pieces.keys():
            if pos_counter % 2 == 0 and gamestate.players[oponent].pieces[(check_x, check_y)].evolved and \
                    gamestate.players[oponent].pieces[(check_x, check_y)].direction == "h":
                return True
            elif pos_counter % 2 != 0 and gamestate.players[oponent].pieces[
                (check_x, check_y)].direction == "h":
                return True
            else:
                return False  # It's being protected by an enemy piece who cant't reach it and blocks others in that line

        check_x -= gamestate.square_side
        pos_counter += 1

    return False


def vuln_pos_right(gamestate, check_x, check_y, player, oponent):
    pos_counter = 1
    check_x += gamestate.square_side
    while check_x <= gamestate.max_pos:
        if (check_x, check_y) in gamestate.players[
            player].pieces.keys(): return False  # It's being protected by another friendly piece

        if (check_x, check_y) in gamestate.players[oponent].pieces.keys():
            if pos_counter % 2 == 0 and gamestate.players[oponent].pieces[(check_x, check_y)].evolved and \
                    gamestate.players[oponent].pieces[(check_x, check_y)].direction == "h":
                return True
            elif pos_counter % 2 != 0 and gamestate.players[oponent].pieces[
                (check_x, check_y)].direction == "h":
                return True
            else:
                return False  # It's being protected by an enemy piece who cant't reach it and blocks others in that line

        check_x += gamestate.square_side
        pos_counter += 1
    return False


def vuln_pos_top(gamestate, check_x, check_y, player, oponent):
    pos_counter = 1
    check_y -= gamestate.square_side
    while check_y >= gamestate.min_pos:
        if (check_x, check_y) in gamestate.players[
            player].pieces.keys(): return False  # It's being protected by another friendly piece

        if (check_x, check_y) in gamestate.players[oponent].pieces.keys():
            if pos_counter % 2 == 0 and gamestate.players[oponent].pieces[(check_x, check_y)].evolved and \
                    gamestate.players[oponent].pieces[(check_x, check_y)].direction == "v":
                return True
            elif pos_counter % 2 != 0 and gamestate.players[oponent].pieces[
                (check_x, check_y)].direction == "v":
                return True
            else:
                return False  # It's being protected by an enemy piece who cant't reach it and blocks others in that line

        check_y -= gamestate.square_side
        pos_counter += 1

    return False


def vuln_pos_bot(gamestate, check_x, check_y, player, oponent):
    pos_counter = 1
    check_y += gamestate.square_side
    while check_y < gamestate.max_pos:
        if (check_x, check_y) in gamestate.players[
            player].pieces.keys(): return False  # It's being protected by another friendly piece

        if (check_x, check_y) in gamestate.players[oponent].pieces.keys():
            if pos_counter % 2 == 0 and gamestate.players[oponent].pieces[(check_x, check_y)].evolved and \
                    gamestate.players[oponent].pieces[(check_x, check_y)].direction == "v":
                return True
            elif pos_counter % 2 != 0 and gamestate.players[oponent].pieces[
                (check_x, check_y)].direction == "v":
                return True
            else:
                return False  # It's being protected by an enemy piece who cant't reach it and blocks others in that line

        check_y += gamestate.square_side
        pos_counter += 1

    return False


def vulnerable_position(gamestate, check_x, check_y, player, opponent):
    return vuln_pos_left(gamestate, check_x, check_y, player, opponent) or vuln_pos_right(gamestate, check_x, check_y,
                                                                                          player,
                                                                                          opponent) or vuln_pos_top(
        gamestate,
        check_x, check_y, player, opponent) or vuln_pos_bot(gamestate, check_x, check_y, player, opponent)


def calc_dist_to_nearest_evol(gamestate, check_x, check_y):
    point_0 = (gamestate.min_pos, gamestate.min_pos)
    point_1 = (gamestate.min_pos, gamestate.max_pos)
    point_2 = (gamestate.max_pos, gamestate.min_pos)
    point_3 = (gamestate.max_pos, gamestate.max_pos)

    d0 = math.floor(math.sqrt(pow(check_x - point_0[0], 2) + pow(check_y - point_0[1], 2)))
    d1 = math.floor(math.sqrt(pow(check_x - point_1[0], 2) + pow(check_y - point_1[1], 2)))
    d2 = math.floor(math.sqrt(pow(check_x - point_2[0], 2) + pow(check_y - point_2[1], 2)))
    d3 = math.floor(math.sqrt(pow(check_x - point_3[0], 2) + pow(check_y - point_3[1], 2)))

    return min([d0, d1, d2, d3])


def value_my_pieces(gamestate, player, opponent):
    value_counter = 0
    for piece in gamestate.players[player].pieces.values():
        if vulnerable_position(gamestate, piece.get_position()[0], piece.get_position()[1], player, opponent):
            continue
        elif piece.evolved:
            value_counter += 1000
        else:
            value_counter += 100
            value_counter -= calc_dist_to_nearest_evol(gamestate, piece.get_position()[0], piece.get_position()[1])

    return value_counter


def value_opponents_pieces(gamestate, player, opponent):
    value_counter = 0
    for piece in gamestate.players[opponent].pieces.values():
        if vulnerable_position(gamestate, piece.get_position()[0], piece.get_position()[1], opponent, player):
            continue
        elif piece.evolved:
            value_counter -= 1000
        else:
            value_counter -= 100
            value_counter += calc_dist_to_nearest_evol(gamestate, piece.get_position()[0], piece.get_position()[1])

    return value_counter
