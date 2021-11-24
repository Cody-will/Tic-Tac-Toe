import random
import time

class Game:

    def __init__(self):
        self.player = ''
        self.computer = ''
        self.board = []
        self.started = True
        self.isstarted = False
        self.play()

    def getplayer(self):
        player = input('Choose x or o: ')
        self.player = player

    def getcomputer(self):
        if self.player == 'x':
            self.computer = '0'
        else:
            self.computer = 'x'

    def createboard(self):
        for i in range(3):
            self.board.append(['_', '_', '_'])

    def printboard(self):
        for i in self.board:
            for x in i:
                print(x, end=" ")
            print()

    def addtoboard(self, choice, player):
        choice = int(choice)
        if choice <= 3:
            self.board[0][(choice - 1)] = player
        elif choice <= 6:
            self.board[1][(choice - 4)] = player
        else:
            self.board[2][(choice - 7)] = player

    def checkavailable(self, choice, player):
        check = {}
        x = None
        if player == self.player:
            x = self.player
        else:
            x = self.computer
        for i in range(1, 10):
            if i <= 3:
                check[i] = self.board[0][(i - 1)]
            elif i <= 6:
                check[i] = self.board[1][(i - 4)]
            else:
                check[i] = self.board[2][(i - 7)]
        if check[int(choice)] == '_':
            self.addtoboard(choice, x)
            return True
        else:
            return False

    def playerturn(self):
        choice = input("Choose a place on the board: ")
        if self.checkavailable(choice, self.player) is True:
            if self.checkforwin(self.player) is True:
                self.win(self.player)
            if self.checkfordraw() is True:
                self.draw()
            return True
        else:
            return False

    def computerturn(self):
        choice = random.randint(1, 9)
        if self.checkavailable(choice, self.computer) is True:
            if self.checkforwin(self.computer) is True:
                self.win(self.computer)
            if self.checkfordraw() is True:
                self.draw()
            return True
        else:
            return False

    def win(self, player):
        if player == self.player:
            print('Winner winner chicken dinner!')
        else:
            print('You lost! Computer won!')
        self.started = False

    def draw(self):
        print("Game was a draw!!")
        self.started = False

    def checkfordraw(self):
        check = {}
        count = 0
        for i in range(1, 10):
            if i <= 3:
                check[i] = self.board[0][(i - 1)]
            elif i <= 6:
                check[i] = self.board[1][(i - 4)]
            else:
                check[i] = self.board[2][(i - 7)]
        for i in range(1, 10):
            if check[i] != '_':
                count += 1
        if count == 9:
            return True
        else:
            return False

    def checkforwin(self, player):
        check = {}
        for i in range(1, 10):
            if i <= 3:
                check[i] = self.board[0][(i - 1)]
            elif i <= 6:
                check[i] = self.board[1][(i - 4)]
            else:
                check[i] = self.board[2][(i - 7)]
        for i in self.board:
            if i == [player, player, player]:
                return True
        for i in range(1,4):
            if check[i] == player:
                if check[(i + 3)] == player:
                    if check[(i + 6)] == player:
                        return True
        if check[1] == player and check[5] == player and check[9] == player:
            return True
        if check[3] == player and check[5] == player and check[7] == player:
            return True
        return False

    def start(self):
        self.createboard()
        self.getplayer()
        self.getcomputer()

    def play(self):
        while self.started:
            if self.isstarted is False:
                self.start()
                self.isstarted = True
            self.printboard()
            print('========')
            while True:
                if self.playerturn() is True:
                    break
                else:
                    print('That choice was already taken, choose again: ')
            self.printboard()
            print('========')
            time.sleep(1)
            while True:
                if self.computerturn() is True:
                    break
                else:
                    pass



if __name__ == "__main__":
    Game()