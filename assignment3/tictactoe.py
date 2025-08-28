# # Amir Daniali
# https://github.com/amirdaniali
# Code The Dream King Cobra
# Week 3


# Task 6
class TictactoeException(Exception):
    def __init__(self, message, *args):
        self.message = message
        super().__init__(*args)


class Board:
    """
        Within the assignment3 folder, create a file called tictactoe.py.
        Within this file, declare a class called TictactoeException. This should inherit from the Exception class. Add an __init__ method that stores an instance variable called message and then calls the __init__ method of the superclass. This is a common way of creating a new type of exception.
        Declare also a class called Board. This should have an __init__ function that only has the self argument. It creates a list of lists, 3x3, all git containing " " as a value. This is stored in the variable self.board_array. Create instance variables self.turn, which is initialized to "X". The Board class should have a class variable called valid_moves, with the value:

       valid_moves=["upper left", "upper center", "upper right", "middle left", "center", "middle right", "lower left", "lower center", "lower right"]

        Add a __str__() method. This converts the board into a displayable string. You want it to show the current state of the game. The rows to be displayed are separated by newlines ("\n") and you also want some "|" amd "-" characters. Once you have created this method, you can display the board by doing a print(board).
        Add a move() method. This has two arguments, self and move_string. The following strings are valid in TicTacToe: "upper left", "upper center", "upper right", "middle left", "center", "middle right", "lower left", "lower center", and "lower right". When a string is passed, the move() method will check if it is one of these, and if not it will raise a TictactoeException with the message "That's not a valid move.". Then the move() method will check to see if the space is taken. If so, it will raise an exception with the message "That spot is taken." If neither is the case, the move is valid, the corresponding entry in board_array is updated with X or O, and the turn value is changed from X to O or from O to X. It also updates last_move, which might make it easier to check for a win.
        Add a whats_next() method. This will see if the game is over. If there are 3 X's or 3 O's in a row, it returns a tuple, where the first value is True and the second value is either "X has won" or "O has won". If the board is full but no one has won, it returns a tuple where the first value is True and the second value is "Cat's Game". Otherwise, it returns a tuple where the first value is False and the second value is either "X's turn" or "O's turn".
        Implement the game within the mainline code of tictactoe.py. At the start of the game, an instance of the board class is created, and then the methods of the board class are used to progress through the game. Use the input() function to prompt for each move, indicating whose turn it is. Note that you need to call board.move() within a try block, with an except block for TictactoeException. Give appropriate information to the user.
        Test your program by playing a few games.

    On assembling this program, the assignment author found that it was too time consuming to write some of the methods.  So, here are some pieces to reuse.  Please make sure you understand them.
    """

    valid_moves = [
        "upper left",
        "upper center",
        "upper right",
        "middle left",
        "center",
        "middle right",
        "lower left",
        "lower center",
        "lower right",
    ]

    def __init__(self):
        self.board_array = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
        ]
        self.last_move = " "  # used to access the last player moving
        self.total_turns = 1  # each player's turn increments this number

    def move(self, move_string):
        if move_string not in self.valid_moves:
            raise TictactoeException("That's not a valid move.")

        column = self.valid_moves.index(move_string) % 3
        row = self.valid_moves.index(move_string) // 3

        new_row = self.board_array[row]

        if new_row[column] != " ":
            raise TictactoeException("That spot is taken.")

        new_row[column] = self.turn
        self.board_array[row] = new_row
        self.next_turn()

    @property
    def turn(self):
        return ["o", "x"][self.total_turns % 2]

    def next_turn(self):
        self.last_move = ["o", "x"][self.total_turns % 2]
        self.total_turns += 1
        return ["o", "x"][self.total_turns % 2]

    def whats_next(self):
        for row in self.board_array:
            if "".join(row) in ["xxx", "ooo"]:
                return (True, row[0])

        for column in range(3):
            if (
                self.board_array[0][column]
                == self.board_array[1][column]
                == self.board_array[2][column]
                != " "
            ):
                return (True, self.board_array[0][column])

        if (
            self.board_array[0][0]
            == self.board_array[1][1]
            == self.board_array[2][2]
            != " "
        ):
            return (True, self.board_array[0][0])
        if (
            self.board_array[0][2]
            == self.board_array[1][1]
            == self.board_array[2][0]
            != " "
        ):
            return (True, self.board_array[0][2])

        board_str = "".join(move for row in self.board_array for move in row)
        if not board_str.count(" "):
            # The game has ended. Its a draw.
            return (True, "Cat's Game")
        return (False, self.turn)  # Game hasn't ended.

    def __str__(self):
        lines = []
        lines.append(
            f" {self.board_array[0][0]} | {self.board_array[0][1]} | {self.board_array[0][2]} \n"
        )
        lines.append("-----------\n")
        lines.append(
            f" {self.board_array[1][0]} | {self.board_array[1][1]} | {self.board_array[1][2]} \n"
        )
        lines.append("-----------" + "\n")

        lines.append(
            f" {self.board_array[2][0]} | {self.board_array[2][1]} | {self.board_array[2][2]} \n"
        )
        return "".join(lines)


def main():
    myboard = Board()
    whats_next = myboard.whats_next()
    print(
        "The game has been initialized. \nThe program will ask each user to specify their board placement. "
    )
    print("Current board:")
    print(myboard)

    while not whats_next[0]:
        move_string = input(
            f"It's {whats_next[1]}'s turn. Enter a valid placement or type <help> to get the list of valid positions. "
        )

        while move_string not in myboard.valid_moves:
            if move_string in ["<help>", "help", "h"]:
                print("Valid move placement strings are:")
                for move in myboard.valid_moves:
                    print(move)
            move_string = input(
                f"It's {whats_next[1]}'s turn. Enter a valid placement or type <help> to get the list of valid positions. "
            )

        try:
            myboard.move(move_string=move_string)
            print(myboard)
        except TictactoeException:
            print("Error. The Spot is taken. Enter Correct placement.")
        whats_next = myboard.whats_next()
    print("Good Game. The Game is now finished.")
    if whats_next[1] == "Cat's Game":
        print("It's a tie! The game result is a Cat's Game.")
    else:
        print("Player", whats_next[1], "has won!")


if __name__ == "__main__":
    main()
