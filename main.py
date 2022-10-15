from easyAI import TwoPlayerGame, Human_Player, AI_Player, Negamax


class Mastermind(TwoPlayerGame):

    # def getBlackPegs(target, guess):
    #     """
    #     Return result of single row comparison of guess and target pegs.

    #     B (black) - peg is in correct color code and position
    #     W (white) - peg is in correct color code, but in a wrong position
    #     _ (none)  -
    #     """
    #     pegs = []
    #     return pegs

    def __init__(self, players):
        self.players = players
        # self.password = ['R', 'G', 'B'] # TODO: will be inputed by human player
        self.password = ['R']
        self.guess = []
        self.scoreBlack = []
        self.scoreWhite = []
        self.rounds = 10
        # self.password = ['R', 'G', 'B', 'X']


    # list of 3-letter moves 
    def possible_moves(self): [combination for combination in self.password]
    def make_move(self, move):
        self.rounds -= 1
    def is_over(self):
        return (self.rounds == 0)
    def show(self):
        print("Guess: ", self.guess)

class Board():
    columns = 4

    def __init__(self):
        rows = input("Enter rows: ")


if __name__ == '__main__':
    # print(getBlackPegs(['R', 'G', 'B', 'X'], ['R', 'R', 'G', 'Y']))
    Mastermind([AI_Player(Negamax(9))])



