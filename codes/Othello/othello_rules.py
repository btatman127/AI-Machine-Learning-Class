from copy import deepcopy


def diagram_to_state(diagram):
    """Converts a list of strings into a list of lists of characters (strings of length 1.)"""
    # TODO You have to write this
    l = []
    for s in diagram:
        l.append(list(s))
    return l


INITIAL_STATE = diagram_to_state(['........',
                                  '........',
                                  '........',
                                  '...#O...',
                                  '...O#...',
                                  '........',
                                  '........',
                                  '........'])


def count_pieces(state):
    """Returns a dictionary of the counts of '#', 'O', and '.' in state."""
    # TODO You have to write this
    h, z, d = 0, 0, 0
    for i in range(len(state)):
        for c in state[i]:
            if c == '#':
                h = h + 1
            if c == 'O':
                z = z + 1
            if c == '.':
                d = d + 1
    dict_counts = {'#': h, 'O': z, '.': d}
    return dict_counts


def prettify(state):
    """
    Returns a single human-readable string representing state, including row and column indices and counts of
    each color.
    """
    # TODO You have to write this
    p = ' 01234567\n'
    for i in range(len(state)):
        p = p + str(i) + ''.join(state[i]) + str(i) + '\n'
    p = p + ' 01234567\n'
    p = p + str(count_pieces(state)) + '\n'
    return p


def opposite(color):
    """opposite('#') returns 'O'. opposite('O') returns '#'."""
    # TODO You have to write this
    if color == '#':
        return 'O'
    else:
        return '#'


def flips(state, r, c, color, dr, dc):
    """
    Returns a list of pieces that would be flipped if color played at r, c, but only searching along the line
    specified by dr and dc. For example, if dr is 1 and dc is -1, consider the line (r+1, c-1), (r+2, c-2), etc.

    :param state: The game state.
    :param r: The row of the piece to be  played.
    :param c: The column of the piece to be  played.
    :param color: The color that would play at r, c.
    :param dr: The amount to adjust r on each step along the line.
    :param dc: The amount to adjust c on each step along the line.
    :return A list of (r, c) pairs of pieces that would be flipped.
    """
    # TODO You have to write this
    l = []
    try:
        while state[r + dr][c + dc] == opposite(color):
            l.append((r + dr, c + dc))
            r = r + dr
            c = c + dc
    except:
        return []
    return l


OFFSETS = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def flips_something(state, r, c, color):
    """Returns True if color playing at r, c in state would flip something."""
    # TODO You have to write this
    for sets in OFFSETS:
        for k in range(1, 8):
            try:
                if k == 1:
                    if r + sets[0] < 0 or c + sets[1] < 0:
                        break
                    if state[r + sets[0]][c + sets[1]] != opposite(color):
                        break
                else:
                    if r + sets[0] * k < 0 or c + sets[1] * k < 0:
                        break
                    if state[r + sets[0] * k][c + sets[1] * k] == color:
                        return True
                    elif state[r + sets[0] * k][c + sets[1] * k] == '.':
                        break
            except:
                break
    return False


def legal_moves(state, color):
    """
    Returns a list of legal moves ((r, c) pairs) that color can make from state. Note that a player must flip
    something if possible; otherwise they must play the special move 'pass'.
    """
    # TODO You have to write this
    l = []
    for i in range(0, 8):
        for j in range(0, 8):
            if state[i][j] == '.':
                if flips_something(state, i, j, color):
                    l.append((i, j))
    if not l:
        return ['pass']
    return l


def successor(state, move, color):
    """
    Returns the state that would result from color playing move (which is either a pair (r, c) or 'pass'.
    Assumes move is legal.
    """
    state1 = []
    for row in state:
        state1.append(row.copy())
    if move == 'pass':
        return state
    state1[move[0]][move[1]] = color
    f = []
    for i in range(len(OFFSETS)):
        f += flips(state1, move[0], move[1], color, OFFSETS[i][0], OFFSETS[i][1])
    for c in f:
        state1[c[0]][c[1]] = color
    return state1


def score(state):
    """
    Returns the scores in state. More positive values (up to 64 for occupying the entire board) are better for '#'.
    More negative values (down to -64) are better for 'O'.
    """
    # TODO You have to write this
    h, z = 0, 0
    for i in range(0, 8):
        for j in range(0, 8):
            if state[i][j] == '#':
                h += 1
            elif state[i][j] == 'O':
                z += 1
    return h - z


def game_over(state):
    """
    Returns true if neither player can flip anything.
    """
    # TODO You have to write this
    if legal_moves(state, '#') == ['pass']:
        if legal_moves(state, 'O') == ['pass']:
            return True
    return False
