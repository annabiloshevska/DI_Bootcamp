# #Mini-project Tic-Tac-Toe

board = [['-','-','-'],
         ['-','-','-'],
         ['-','-','-']]
# #board[0][1] = "X"

# players = ['x', 'o']
def display_board():
  print('** Tic-Tac-Toe **')
  print('*'* 17)
  print(f'*   {board[0][0]}|  {board[0][1]}  |{board[0][2]}   *')
  print('*  --+-----+--  *')
  print(f'*   {board[1][0]}|  {board[1][1]}  |{board[1][2]}   *')
  print('*  --+-----+--- *')
  print(f'*   {board[2][0]}|  {board[2][1]}  |{board[2][2]}   *')
  print('*'* 17)
  print()

def player_input(player):
  player_move_row = int(input('Enter row(1-3):'))
  player_move_column = int(input('Enter column(1-3):'))
  if 0 < player_move_row <=3 and 0 < player_move_column <=3:
    board[player_move_row - 1][player_move_column - 1] = player
  else:
    player_move_row = int(input('Enter row(1-3):'))
    player_move_column = int(input('Enter column(1-3):'))
    board[player_move_row - 1][player_move_column - 1] = player

def check_win(board, player):
  # rows
  if board[0][0] == player and board[0][1] == player and board[0][2] == player:
    return True
  elif board[1][0] == player and board[1][1] == player and board[1][2] == player:
    return True
  elif board[2][0] == player and board[2][1] == player and board[2][2] == player:
    return True
  # columns
  elif board[0][0] == player and board[1][0] == player and board[2][0] == player:
    return True
  elif board[0][1] == player and board[1][1] == player and board[2][1] == player:
    return True
  elif board[0][2] == player and board[1][2] == player and board[2][2] == player:
    return True
  # diagonals
  elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
    return True
  elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
    return True
  else:
    return False

def check_tie():
  for row in board:
    if '-' in row:
      return False
  return True

def play(): 
  players = ('x', 'o')
  player = players[0]
  
  while True:
    display_board()
    print(f'It\'s {player}\'s turn')
    player_input(player)

    if check_win(board, player) == True:
      display_board()
      print(f'{player} is the winner')
      break  
    else:
      if player == 'x':
        player = 'o'
      elif player == 'o':
        player = 'x'

    if check_tie() == True:
      display_board()
      print('It\'s a tie!')
      break

play()