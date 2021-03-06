from othello_rules import *


def evaluate(state):
    """
    Returns 1 if '#' has won, -1 if 'O' has won, and 0 if the game has ended in a draw.
    If the game is not over, returns score / 100, giving a number from -0.64 to 0.64.
    This way, search will prefer winning to merely being ahead by any amount.
    """
    # TODO You have to write this
    if game_over(state):
        if score(state) == 0:
            return 0
        else:
            return int(score(state)/abs(score(state)))
    else:
        return score(state)/100


def minimax(state, player, max_depth):
    """
    Returns the value of state with player to play. max_depth gives the search depth; if 0, returns the evaluation
    of state.
    """
    # TODO You have to write this
    if max_depth == 0:
        return evaluate(state)
    successors = (successor(state, move, player) for move in legal_moves(state, player))
    if player == '#':
        return max(minimax(s, 'O', max_depth-1) for s in successors)
    else:
        return min(minimax(s, '#', max_depth-1) for s in successors)


def best_move(state, player, max_depth):
    """Returns player's best move. max_depth, which must be at least 1, gives the search depth."""
    # TODO You have to write this
    moves = legal_moves(state, player)
    successors = (successor(state, move, player) for move in moves)
    d2 = dict()
    i = 0
    for s in successors:
        d2[i] = minimax(s, opposite(player), max_depth-1)
        i += 1
    if player == '#':
        return moves[max(d2, key=d2.get)]
    else:
        return moves[min(d2, key=d2.get)]


if __name__ == '__main__':
    game = INITIAL_STATE
    while not game_over(game):
        print('# to play')
        print(prettify(game))
        print('Thinking...')
        m = best_move(game, '#', 5)
        print(m)
        game = successor(game, m, '#')
        if not game_over(game):
            while True:
                print('O to play')
                print(prettify(game))
                m = input('Enter row and column (0-7, separated by a space) or pass: ')
                if m != 'pass':
                    m = tuple([int(n) for n in m.split()])
                print(m)
                if m in legal_moves(game, 'O'):
                    break
            game = successor(game, m, 'O')
    print(prettify(game))
    result = score(game)
    if result > 0:
        print('# wins!')
    elif result == 0:
        print('Draw.')
    else:
        print('O wins!')
