import copy
from typing import List


class TZFE:
    def __init__(self):
        self.board = [[0] * 4 for _ in range(4)]

    def __str__(self) -> str:
        s = '\nThis is the current board:\n'
        for i in range(4):
            s += str(self.board[i]) + '\n'
        s = s.rstrip('\n')
        return s

    def gen_new(self, new_nums: List[List[int]]):
        """
            generate new numbers on the board
        :param new_nums: list of [x,y,val], x is row number, y is column number, val is value
        """
        for i in new_nums:
            row = i[0] - 1
            col = i[1] - 1
            val = i[2]
            self.board[row][col] = val
        print('\nGenerate new numbers')
        print(self)

    def up(self) -> bool:
        """
            swipe up, 向上滑动, 返回值表示此操作是否可以进行
        """
        pre_board = copy.deepcopy(self.board)
        for col in range(4):
            #  do merging for each column
            num_list = []
            for i in range(4):
                if self.board[i][col] != 0:
                    num_list.append(self.board[i][col])
                    self.board[i][col] = 0
            i = 0
            while i < num_list.__len__() - 1:
                if num_list[i] == num_list[i + 1]:
                    num_list[i] *= 2
                    num_list.pop(i + 1)
                i += 1
            for i in range(num_list.__len__()):
                self.board[i][col] = num_list[i]
        if pre_board == self.board:
            return False
        else:
            return True

    def down(self) -> bool:
        """
            swipe down, 向下滑动, 返回值表示此操作是否可以进行
        """
        pre_board = copy.deepcopy(self.board)
        for col in range(4):
            #  do merging for each column
            num_list = []
            for i in range(4):
                if self.board[i][col] != 0:
                    num_list.append(self.board[i][col])
                    self.board[i][col] = 0
            i = num_list.__len__() - 1
            while i > 0:
                if num_list[i] == num_list[i - 1]:
                    num_list[i] *= 2
                    num_list.pop(i - 1)
                i -= 2
            for i in range(num_list.__len__()):
                self.board[i + 4 - num_list.__len__()][col] = num_list[i]
        if pre_board == self.board:
            return False
        else:
            return True

    def left(self):
        """
            swipe left, 向左滑动, 返回值表示此操作是否可以进行
        """
        pre_board = copy.deepcopy(self.board)
        for row in range(4):
            # do merging for each row
            num_list = []
            for i in range(4):
                if self.board[row][i] != 0:
                    num_list.append(self.board[row][i])
                    self.board[row][i] = 0
            i = 0
            while i < num_list.__len__() - 1:
                if num_list[i] == num_list[i + 1]:
                    num_list[i] *= 2
                    num_list.pop(i + 1)
                i += 1
            for i in range(num_list.__len__()):
                self.board[row][i] = num_list[i]
        if pre_board == self.board:
            return False
        else:
            return True

    def right(self):
        """
            swipe right, 向右移动, 返回值表示此操作是否可以进行
        """
        pre_board = copy.deepcopy(self.board)
        for row in range(4):
            # do merging for each row
            num_list = []
            for i in range(4):
                if self.board[row][i] != 0:
                    num_list.append(self.board[row][i])
                    self.board[row][i] = 0
            i = num_list.__len__() - 1
            while i > 0:
                if num_list[i] == num_list[i - 1]:
                    num_list[i] *= 2
                    num_list.pop(i - 1)
                i -= 2
            for i in range(num_list.__len__()):
                self.board[row][i + 4 - num_list.__len__()] = num_list[i]
        if pre_board == self.board:
            return False
        else:
            return True

    def get_total(self) -> int:
        """
            get total number of blocks, 获取方块的总数
        """
        ans = 0
        for i in range(4):
            for j in range(4):
                if self.board[i][j]:
                    ans += 1
        return ans

    def consider(self) -> str:
        """
        :return: operation to make total number of blocks lowest, 让下一步方块总数最小的操作
        """
        dictionary = dict()

        left = copy.deepcopy(self)
        if left.left():
            dictionary['l'] = left.get_total()
        else:
            dictionary['l'] = 17

        right = copy.deepcopy(self)
        if right.right():
            dictionary['r'] = right.get_total()
        else:
            dictionary['r'] = 17

        up = copy.deepcopy(self)
        if up.up():
            dictionary['u'] = up.get_total()
        else:
            dictionary['u'] = 17

        down = copy.deepcopy(self)
        if down.down():
            dictionary['d'] = down.get_total()
        else:
            dictionary['d'] = 17

        best = sorted(dictionary.items(), key=lambda x: x[1])
        if best[0][1] == 17:
            return 'dead'
        print("Consider result is " + str(best))
        return best[0][0]

    def game(self):
        while True:
            print('input the generate values, like "x1 y1 2\nx2 y2 4":\n')
            gen_list = []
            while True:
                try:
                    gen_list.append(list(map(int, input().split(" "))))
                except:
                    break
            self.gen_new(gen_list)
            op = self.consider()[0]
            if op == 'l':
                self.left()
                print(self)
            elif op == 'r':
                self.right()
                print(self)
            elif op == 'u':
                self.up()
                print(self)
            elif op == 'd':
                self.down()
                print(self)


board = TZFE()
board.game()
