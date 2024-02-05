def print_board(board):
  for row in board:
      print(" | ".join(row))
      print("- " * 5)


def is_winner(board, player):
  # Check rows and columns
  for i in range(3):
      if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
          return True
  # Check diagonals
  if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
      return True
  return False


def is_board_full(board):
  return all(board[i][j] != ' ' for i in range(3) for j in range(3))


def is_valid_move(board, row, col):
  return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '


def tic_tac_toe():
  board = [[' ' for _ in range(3)] for _ in range(3)]
  current_player = 'X'

  while True:
      print_board(board)
      print(f"Player {current_player}'s turn")

      row = int(input("Enter row (0, 1, or 2): "))
      col = int(input("Enter column (0, 1, or 2): "))

      if is_valid_move(board, row, col):
          board[row][col] = current_player
          if is_winner(board, current_player):
              print_board(board)
              print(f"Player {current_player} wins!")
              break
          elif is_board_full(board):
              print_board(board)
              print("CAT! The game is a draw.")
              break
          else:
              current_player = 'O' if current_player == 'X' else 'X'
      else:
          print("Invalid move. Please try again.")

tic_tac_toe()
