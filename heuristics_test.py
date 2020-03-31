import heuristics
from piece import Piece
from collections import defaultdict
from gamestate import GameState

def test_vul_pos_left(gamestate):
    print("Testing vulnerable pos left")
    piece1 = Piece(300, 60, "h", 50)
    piece2 = Piece(180, 60, "h", 50)
    piece25 = Piece(180, 60, "v", 50)
    piece3 = Piece(420, 60, "h", 50)

    # gamestate.players[1].pieces[piece3.get_position()] = piece3
    # Test 1st Return
    print("Test 1st Return")
    gamestate.players[0].pieces = defaultdict(Piece)
    gamestate.players[1].pieces = defaultdict(Piece)

    gamestate.players[0].pieces[piece1.get_position()] = piece1  # Not Vulnerable
    gamestate.players[0].pieces[piece2.get_position()] = piece2

    print("P1: ", gamestate.players[0].pieces)
    print("P2: ", gamestate.players[1].pieces)
    print(heuristics.vuln_pos_left(gamestate, 300, 60, 0, 1))

    # Test 2nd Return
    print("Test 2nd Return")
    gamestate.players[0].pieces = defaultdict(Piece)
    gamestate.players[1].pieces = defaultdict(Piece)

    gamestate.players[0].pieces[piece3.get_position()] = piece3  # vulnerable
    piece2.evolve()
    gamestate.players[1].pieces[piece2.get_position()] = piece2

    print("P1: ", gamestate.players[0].pieces)
    print("P2: ", gamestate.players[1].pieces)
    print(heuristics.vuln_pos_left(gamestate, 300, 60, 0, 1))

    # Test 3rd Return
    print("Test 3rd Return")
    gamestate.players[0].pieces = defaultdict(Piece)
    gamestate.players[1].pieces = defaultdict(Piece)

    gamestate.players[0].pieces[piece1.get_position()] = piece1  # vulnerable
    gamestate.players[1].pieces[piece2.get_position()] = piece2

    print("P1: ", gamestate.players[0].pieces)
    print("P2: ", gamestate.players[1].pieces)
    print(heuristics.vuln_pos_left(gamestate, 300, 60, 0, 1))

    # Test 4th Return
    print("Test 4th Return")
    gamestate.players[0].pieces = defaultdict(Piece)
    gamestate.players[1].pieces = defaultdict(Piece)

    gamestate.players[0].pieces[piece1.get_position()] = piece1  # Not vulnerable
    gamestate.players[1].pieces[piece25.get_position()] = piece25

    print("P1: ", gamestate.players[0].pieces)
    print("P2: ", gamestate.players[1].pieces)
    print(heuristics.vuln_pos_left(gamestate, 300, 60, 0, 1))

    # Test Last Return
    print("Test 5th Return")
    gamestate.players[0].pieces = defaultdict(Piece)
    gamestate.players[1].pieces = defaultdict(Piece)

    gamestate.players[0].pieces[piece1.get_position()] = piece1  # Not vulnerable
    # gamestate.players[1].pieces[piece2.get_position()] = piece2

    print("P1: ", gamestate.players[0].pieces)
    print("P2: ", gamestate.players[1].pieces)
    print(heuristics.vuln_pos_left(gamestate, 300, 60, 0, 1))


def test_vul_pos_right(gamestate):
    print("Testing vulnerable pos right")
    piece1 = Piece(300, 60, "h", 50)
    piece2 = Piece(180, 60, "h", 50)
    piece25 = Piece(420, 60, "v", 50)
    piece3 = Piece(420, 60, "h", 50)

    # gamestate.players[1].pieces[piece3.get_position()] = piece3
    # Test 1st Return
    print("Test 1st Return")
    gamestate.players[0].pieces = defaultdict(Piece)
    gamestate.players[1].pieces = defaultdict(Piece)

    gamestate.players[0].pieces[piece1.get_position()] = piece1
    gamestate.players[0].pieces[piece2.get_position()] = piece2  # Not Vulnerable

    print("P1: ", gamestate.players[0].pieces)
    print("P2: ", gamestate.players[1].pieces)
    print(heuristics.vuln_pos_right(gamestate, 180, 60, 0, 1))

    # Test 2nd Return
    print("Test 2nd Return")
    gamestate.players[0].pieces = defaultdict(Piece)
    gamestate.players[1].pieces = defaultdict(Piece)

    gamestate.players[0].pieces[piece2.get_position()] = piece2  # vulnerable
    piece3.evolve()
    gamestate.players[1].pieces[piece3.get_position()] = piece3

    print("P1: ", gamestate.players[0].pieces)
    print("P2: ", gamestate.players[1].pieces)
    print(heuristics.vuln_pos_right(gamestate, 180, 60, 0, 1))

    # Test 3rd Return
    print("Test 3rd Return")
    gamestate.players[0].pieces = defaultdict(Piece)
    gamestate.players[1].pieces = defaultdict(Piece)

    gamestate.players[0].pieces[piece3.get_position()] = piece3  # vulnerable
    gamestate.players[1].pieces[piece1.get_position()] = piece1

    print("P1: ", gamestate.players[0].pieces)
    print("P2: ", gamestate.players[1].pieces)
    print(heuristics.vuln_pos_right(gamestate, 300, 60, 1, 0))

    # Test 4th Return
    print("Test 4th Return")
    gamestate.players[0].pieces = defaultdict(Piece)
    gamestate.players[1].pieces = defaultdict(Piece)

    gamestate.players[0].pieces[piece1.get_position()] = piece1  # Not vulnerable
    gamestate.players[1].pieces[piece25.get_position()] = piece25

    print("P1: ", gamestate.players[0].pieces)
    print("P2: ", gamestate.players[1].pieces)
    print(heuristics.vuln_pos_right(gamestate, 300, 60, 0, 1))

    # Test Last Return
    print("Test 5th Return")
    gamestate.players[0].pieces = defaultdict(Piece)
    gamestate.players[1].pieces = defaultdict(Piece)

    gamestate.players[0].pieces[piece1.get_position()] = piece1  # Not vulnerable
    # gamestate.players[1].pieces[piece2.get_position()] = piece2

    print("P1: ", gamestate.players[0].pieces)
    print("P2: ", gamestate.players[1].pieces)
    print(heuristics.vuln_pos_right(gamestate, 300, 60, 0, 1))


def test_vul_pos_top(gamestate):
    print("Testing vulnerable pos top")
    piece1 = Piece(60, 300, "v", 50)
    piece2 = Piece(60, 180, "v", 50)
    piece25 = Piece(60, 180, "h", 50)
    piece3 = Piece(60, 420, "v", 50)

    # gamestate.players[1].pieces[piece3.get_position()] = piece3
    # Test 1st Return
    print("Test 1st Return")
    gamestate.players[0].pieces = defaultdict(Piece)
    gamestate.players[1].pieces = defaultdict(Piece)

    gamestate.players[0].pieces[piece1.get_position()] = piece1  # Not Vulnerable
    gamestate.players[0].pieces[piece2.get_position()] = piece2

    print("P1: ", gamestate.players[0].pieces)
    print("P2: ", gamestate.players[1].pieces)
    print(heuristics.vuln_pos_top(gamestate, 60, 300, 0, 1))

    # Test 2nd Return
    print("Test 2nd Return")
    gamestate.players[0].pieces = defaultdict(Piece)
    gamestate.players[1].pieces = defaultdict(Piece)

    gamestate.players[0].pieces[piece2.get_position()] = piece2
    piece2.evolve()
    gamestate.players[1].pieces[piece3.get_position()] = piece3  # vulnerable

    print("P1: ", gamestate.players[0].pieces)
    print("P2: ", gamestate.players[1].pieces)
    print(heuristics.vuln_pos_top(gamestate, 60, 420, 1, 0))

    # Test 3rd Return
    print("Test 3rd Return")
    gamestate.players[0].pieces = defaultdict(Piece)
    gamestate.players[1].pieces = defaultdict(Piece)
    piece2.evolved = False
    gamestate.players[0].pieces[piece1.get_position()] = piece1  # vulnerable
    gamestate.players[1].pieces[piece2.get_position()] = piece2

    print("P1: ", gamestate.players[0].pieces)
    print("P2: ", gamestate.players[1].pieces)
    print(heuristics.vuln_pos_top(gamestate, 60, 300, 0, 1))

    # Test 4th Return
    print("Test 4th Return")
    gamestate.players[0].pieces = defaultdict(Piece)
    gamestate.players[1].pieces = defaultdict(Piece)

    gamestate.players[0].pieces[piece2.get_position()] = piece25
    piece25.evolve()
    gamestate.players[1].pieces[piece3.get_position()] = piece3  # Not Vulnerable

    print("P1: ", gamestate.players[0].pieces)
    print("P2: ", gamestate.players[1].pieces)
    print(heuristics.vuln_pos_top(gamestate, 60, 420, 1, 0))

    # Test Last Return
    print("Test 5th Return")
    gamestate.players[0].pieces = defaultdict(Piece)
    gamestate.players[1].pieces = defaultdict(Piece)

    gamestate.players[0].pieces[piece1.get_position()] = piece1  # Not vulnerable
    # gamestate.players[1].pieces[piece2.get_position()] = piece2

    print("P1: ", gamestate.players[0].pieces)
    print("P2: ", gamestate.players[1].pieces)
    print(heuristics.vuln_pos_top(gamestate, 300, 60, 0, 1))


def test_vul_pos_bot(gamestate):
    print("Testing vulnerable pos bot")
    piece1 = Piece(60, 300, "v", 50)
    piece2 = Piece(60, 180, "v", 50)
    piece25 = Piece(60, 420, "h", 50)
    piece3 = Piece(60, 420, "v", 50)

    # gamestate.players[1].pieces[piece3.get_position()] = piece3
    # Test 1st Return
    print("Test 1st Return")
    gamestate.players[0].pieces = defaultdict(Piece)
    gamestate.players[1].pieces = defaultdict(Piece)

    gamestate.players[0].pieces[piece1.get_position()] = piece1
    gamestate.players[0].pieces[piece2.get_position()] = piece2  # Not Vulnerable

    print("P1: ", gamestate.players[0].pieces)
    print("P2: ", gamestate.players[1].pieces)
    print(heuristics.vuln_pos_bot(gamestate, 60, 180, 0, 1))

    # Test 2nd Return
    print("Test 2nd Return")
    gamestate.players[0].pieces = defaultdict(Piece)
    gamestate.players[1].pieces = defaultdict(Piece)

    gamestate.players[0].pieces[piece2.get_position()] = piece2  # vulnerable
    piece3.evolve()
    gamestate.players[1].pieces[piece3.get_position()] = piece3

    print("P1: ", gamestate.players[0].pieces)
    print("P2: ", gamestate.players[1].pieces)
    print(heuristics.vuln_pos_bot(gamestate, 60, 180, 0, 1))

    # Test 3rd Return
    print("Test 3rd Return")
    gamestate.players[0].pieces = defaultdict(Piece)
    gamestate.players[1].pieces = defaultdict(Piece)

    gamestate.players[0].pieces[piece3.get_position()] = piece3  # vulnerable
    gamestate.players[1].pieces[piece1.get_position()] = piece1

    print("P1: ", gamestate.players[0].pieces)
    print("P2: ", gamestate.players[1].pieces)
    print(heuristics.vuln_pos_bot(gamestate, 60, 300, 1, 0))

    # Test 4th Return
    print("Test 4th Return")
    gamestate.players[0].pieces = defaultdict(Piece)
    gamestate.players[1].pieces = defaultdict(Piece)

    gamestate.players[0].pieces[piece1.get_position()] = piece1  # Not vulnerable
    gamestate.players[1].pieces[piece25.get_position()] = piece25

    print("P1: ", gamestate.players[0].pieces)
    print("P2: ", gamestate.players[1].pieces)
    print(heuristics.vuln_pos_bot(gamestate, 60, 300, 0, 1))

    # Test Last Return
    print("Test 5th Return")
    gamestate.players[0].pieces = defaultdict(Piece)
    gamestate.players[1].pieces = defaultdict(Piece)

    gamestate.players[0].pieces[piece1.get_position()] = piece1  # Not vulnerable
    # gamestate.players[1].pieces[piece2.get_position()] = piece2

    print("P1: ", gamestate.players[0].pieces)
    print("P2: ", gamestate.players[1].pieces)
    print(heuristics.vuln_pos_bot(gamestate, 60, 30, 0, 1))

