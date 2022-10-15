from easyAI import TwoPlayerGame, Human_Player, AI_Player, Negamax


def getBlackPegs(target, guess):
    """
    Return result of single row comparison of guess and target pegs.

    B (black) - peg is in correct color code and position
    W (white) - peg is in correct color code, but in a wrong position
    _ (none)  -
    """
    pegs = []


    return pegs


class Mastermind(TwoPlayerGame):

    def __init__(self, players):
        self.players = players
        self.password = ['R']
        self.guess = []
        # self.password = ['R', 'G', 'B', 'X']


    def possible_moves(self): return ["R", "G", "B", "Y"]
    def make_move(self, move): self.guess


class Board():
    columns = 4

    def __init__(self):
        rows = input("Enter rows: ")


if __name__ == '__main__':
    print(getBlackPegs(['R', 'G', 'B', 'X'], ['R', 'R', 'G', 'Y']))
    Mastermind()



