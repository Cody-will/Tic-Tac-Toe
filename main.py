import random


class Game:
    def __init__(self):
        self.board = (["1", "2", "3"],["4", "5", "6"],["7", "8", "9"])
        self.playercharacter = input('do you want to be X or O? ')
        self.playercharacter = self.playercharacter.upper()
        self.compcharacter = ''
        if self.playercharacter == 'X':
            self.compcharacter = 'O'
        else:
            self.compcharacter = 'X'
        for i in self.board:
            print(i)
        self.playerchoice()


    def playerchoice(self):
        choice = input("Choose a number from the board: ")
        if int(choice) not in range(1, 10):
            print("incorrect input, choose number from the board.")
            self.playerchoice()
        else:
            for i in self.board:
                if str(choice) in i:
                    if int(choice) <= 3:
                        self.board[0][(int(choice) - 1)] = self.playercharacter
                    elif int(choice) > 3 and int(choice) <= 6:
                        self.board[1][(int(choice) - 4)] = self.playercharacter
                    elif int(choice) > 6 and int(choice) <= 9:
                        self.board[2][(int(choice) - 7)] = self.playercharacter
                    for i in self.board:
                        print(i)
                    self.checkplayerwin()
                else:
                    if i == self.board[2]:
                        print("Choice not available.")
                        self.playerchoice()

    def compchoice(self):
        computerchoice = random.randint(1, 9)

        for i in self.board:
            if str(computerchoice) in i:
                print(f"Computer chose {computerchoice}.")
                if int(computerchoice) <= 3:
                    self.board[0][(int(computerchoice) - 1)] = self.compcharacter
                elif int(computerchoice) > 3 and int(computerchoice) <= 6:
                    self.board[1][(int(computerchoice) - 4)] = self.compcharacter
                elif int(computerchoice) > 6 and int(computerchoice) <= 9:
                    self.board[2][(int(computerchoice) - 7)] = self.compcharacter
                for i in self.board:
                    print(i)
                self.checkcompwin()
            else:
                if i == self.board[2]:
                    self.compchoice()

    def playerwin(self):
        print("Congratulations! You won!")
        Game()

    def compwin(self):
        print("Boooo, you lost! The computer won!")
        Game()

    def checkplayerwin(self):
        # straight across top
        if self.board[0] == [self.playercharacter, self.playercharacter,self.playercharacter]:
            self.playerwin()
        # straight through middle
        elif self.board[1] == [self.playercharacter,self.playercharacter, self.playercharacter]:
            self.playerwin()
        # straight across bottom
        elif self.board[2] == [self.playercharacter, self.playercharacter, self.playercharacter]:
            self.playerwin()
        # from top left to bottom right
        elif self.board[0][0] == self.playercharacter and self.board[1][1] == self.playercharacter and self.board[2][2] == self.playercharacter:
            self.playerwin()
        # from top to bottom middle
        elif self.board[0][1] == self.playercharacter and self.board[1][1] == self.playercharacter and self.board[2][1] == self.playercharacter:
            self.playerwin()
        # from top right to bottom left
        elif self.board[0][2] == self.playercharacter and self.board[1][1] == self.playercharacter and self.board[2][0] == self.playercharacter:
            self.playerwin()
        # top to bottom left side
        elif self.board[0][0] == self.playercharacter and self.board[1][0] == self.playercharacter and self.board[2][0] == self.playercharacter:
            self.playerwin()
        # top to bottom right side
        elif self.board[0][2] == self.playercharacter and self.board[1][2] == self.playercharacter and self.board[2][2] == self.playercharacter:
            self.playerwin()
        else:
            self.compchoice()

    def checkcompwin(self):
        # straight across top
        if self.board[0] == [self.compcharacter, self.compcharacter, self.compcharacter]:
            self.compwin()
        # straight through middle
        elif self.board[1] == [self.compcharacter, self.compcharacter, self.compcharacter]:
            self.compwin()
        # straight across bottom
        elif self.board[2] == [self.compcharacter, self.compcharacter, self.compcharacter]:
            self.compwin()
        # from top left to bottom right
        elif self.board[0][0] == self.compcharacter and self.board[1][1] == self.compcharacter and self.board[2][2] == self.compcharacter:
            self.compwin()
        # from top to bottom middle
        elif self.board[0][1] == self.compcharacter and self.board[1][1] == self.compcharacter and self.board[2][1] == self.playercharacter:
            self.compwin()
        # from top right to bottom left
        elif self.board[0][2] == self.compcharacter and self.board[1][1] == self.compcharacter and self.board[2][0] == self.playercharacter:
            self.compwin()
        # top to bottom left side
        elif self.board[0][0] == self.compcharacter and self.board[1][0] == self.compcharacter and self.board[2][0] == self.playercharacter:
            self.compwin()
        # top to bottom right side
        elif self.board[0][2] == self.compcharacter and self.board[1][2] == self.compcharacter and self.board[2][2] == self.playercharacter:
            self.compwin()
        else:
            self.playerchoice()


if __name__ == "__main__":
    Game()


