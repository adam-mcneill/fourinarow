"""Four-in-a-Row: A two-player Connect Four clone."""

import sys

BOARD_WIDTH = 7
BOARD_HEIGHT = 6
PLAYER_X = "X"
PLAYER_O = "O"
EMPTY_SPACE = "."


def main():
    """Main function. Runs a single game.
    The board is represented by a list of lists. The inner lists
    represent columns and the outer list the entire board. Each space
    can be described as board[x][y]. The two different player counters
    are represented by 'X' and 'O', with a '.' representing a blank
    space. The game ends when QUIT is entered, the board is filled or
    one player has four counters in a row either horizontally,
    vertically or diagonally."""

    print('Welcome to Four-in-a-Row, a Connect Four clone.')
    mainBoard = newBoard()
    playerToMove = PLAYER_X
    drawBoard(mainBoard)

    while True:
        # Take input:
        playerMove = getPlayerMove(mainBoard, playerToMove)

        # Place counter
        placeCounter(mainBoard, playerMove, playerToMove)

        # Redraw board:
        drawBoard(mainBoard)

        # Check for a victory or draw:
        checkForEnd(mainBoard, playerToMove)

        # Switch player:
        if playerToMove == PLAYER_X:
            playerToMove = PLAYER_O
        elif playerToMove == PLAYER_O:
            playerToMove = PLAYER_X


def newBoard():
    """Generates a fresh, empty board."""
    blankColumn = [EMPTY_SPACE] * BOARD_HEIGHT
    board = []  # Start with an empty board, then fill it with columns.
    for x in range(BOARD_WIDTH):
        board.append(blankColumn[:])
    return board


def drawBoard(board):
    """Draws the board row-by-row, starting from the top."""
    print()  # Draw one blank line to space the text out.

    # Draw the column labels:
    rowLabelsList = [str(x + 1) for x in range(BOARD_WIDTH)]
    rowLabelsString = ' ' + ''.join(rowLabelsList) + ' '
    print(rowLabelsString)

    # Make a string which can be used for both the top and bottom borders:
    horizontalBorder = '+' + '-' * BOARD_WIDTH + '+'
    print(horizontalBorder)  # Top border.

    for y in range(BOARD_HEIGHT):
        # Make and print a string representing each row:
        currentRow = ['|']  # Left border.
        for x in range(BOARD_WIDTH):  # Add each counter to the row:
            currentRow.append(board[x][y])
        currentRow.append('|')  # Right border.
        print(''.join(currentRow))

    print(horizontalBorder)  # Bottom border
    print()


def getPlayerMove(board, player):
    """Takes input from the player and checks for errors. Returns valid
moves as integers."""
    print(f'Player {player} to move.')

    while True:  # Keep asking until a valid move is entered:
        # Take input and capitalise in case the input is 'QUIT'
        print(f"""Please enter a number from 1 to {BOARD_WIDTH},
or QUIT to exit.""")
        response = input('> ').upper().strip()

        if response in ('QUIT', 'EXIT'):
            print('Thanks for playing.')
            sys.exit()

        # Determine valid non-exit moves as strings:
        validMoves = [str(x) for x in range(1, BOARD_WIDTH + 1)]
        
        if response not in validMoves:
            # Move needs to be a number representing a column.
            print('Invalid move.')
            continue  # Go back to the move prompt.
        else:
            columnPicked = int(response) - 1  # -1 for zer-indexing
        
        if board[columnPicked][0] != EMPTY_SPACE:
            print('That column is full. Please pick another.')
            continue  # Go back to the move prompt.
        else:
            return columnPicked


def placeCounter(board, x, player):
    """Adds the specified counter to the specified column. The board is
edited in place."""
    # Move up the column, looking for an empty space
    for y in range(BOARD_HEIGHT - 1, -1, -1):
        if board[x][y] == EMPTY_SPACE:
            board[x][y] = player
            return


def checkForEnd(board, player):
    """Checks for a winner and declares the victor if one is found.
If no winner is found, checks for a draw and declares one is found."""
    # Check for vertical wins:
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT - 3):
            counter1 = board[x][y]
            counter2 = board[x][y+1]
            counter3 = board[x][y+2]
            counter4 = board[x][y+3]
            if counter1 == counter2 == counter3 == counter4 == player:
                declareWinner(player)

    # Check for horizontal  wins:
    for x in range(BOARD_WIDTH - 3):
        for y in range(BOARD_HEIGHT):
            counter1 = board[x][y]
            counter2 = board[x+1][y]
            counter3 = board[x+2][y]
            counter4 = board[x+3][y]
            if counter1 == counter2 == counter3 == counter4 == player:
                declareWinner(player)

    # Check for diagonal wins:
    for x in range(BOARD_WIDTH - 3):
        for y in range(BOARD_HEIGHT - 3):
            # Check for down-right wins:
            counter1 = board[x][y]
            counter2 = board[x+1][y+1]
            counter3 = board[x+2][y+2]
            counter4 = board[x+3][y+3]
            if counter1 == counter2 == counter3 == counter4 == player:
                declareWinner(player)

            # Check for down-left wins:
            counter1 = board[x+3][y]
            counter2 = board[x+2][y+1]
            counter3 = board[x+1][y+2]
            counter4 = board[x][y+3]
            if counter1 == counter2 == counter3 == counter4 == player:
                declareWinner(player)

    # Check for a draw:
    blankFound = False
    for x in range(BOARD_WIDTH):  # Check the top row for empty spaces:
        if board[x][0] == EMPTY_SPACE:
            blankFound = True
            break
        
    if not blankFound:
        # If no blanks are found on the top row the board must be full.
        print("It's a draw!")
        sys.exit()


def declareWinner(player):
    """Declares that the given player has won and exits the game."""
    print(f'Player {player} wins!')
    sys.exit()


# Run main() if the program was run, as opposed to imported.
if __name__ == '__main__':
    main()
